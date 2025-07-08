#!/usr/bin/env python3
"""
HTTP-MCP Tool - Python Implementation
A general-purpose HTTP MCP tool for serving static files and web services with browser tunneling.
"""

import asyncio
import json
import uuid
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import websockets
from websockets.server import WebSocketServerProtocol
import aiohttp
from aiohttp import web
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HTTPMCPServer:
    def __init__(self):
        self.simulations: Dict[str, Dict] = {}
        self.browsers: Dict[str, Dict] = {}
        self.connections: Dict[str, WebSocketServerProtocol] = {}
        self.app = web.Application()
        self.setup_routes()
        
    def setup_routes(self):
        """Setup HTTP routes"""
        self.app.router.add_get('/api/simulations', self.get_simulations)
        self.app.router.add_get('/api/simulation/{simulation_id}', self.get_simulation)
        self.app.router.add_post('/api/message', self.post_message)
        self.app.router.add_static('/static', path='./static', name='static')
        
    async def get_simulations(self, request):
        """Get list of all simulations"""
        sim_list = []
        for sim_id, sim in self.simulations.items():
            sim_list.append({
                'id': sim_id,
                'messageCount': len(sim.get('messages', [])),
                'browserCount': len(sim.get('browsers', set()))
            })
        return web.json_response(sim_list)
        
    async def get_simulation(self, request):
        """Get detailed state of a specific simulation"""
        sim_id = request.match_info['simulation_id']
        if sim_id not in self.simulations:
            return web.json_response({'error': 'Simulation not found'}, status=404)
        
        sim = self.simulations[sim_id]
        # Convert sets to lists for JSON serialization
        sim_data = {
            'messages': sim.get('messages', []),
            'browsers': list(sim.get('browsers', set())),
            'characters': dict(sim.get('characters', {})),
            'config': sim.get('config', {})
        }
        return web.json_response(sim_data)
        
    async def post_message(self, request):
        """Post a message to a simulation"""
        try:
            data = await request.json()
            simulation_id = data.get('simulation_id')
            browser_id = data.get('browser_id')
            character_id = data.get('character_id')
            message_name = data.get('message_name')
            args = data.get('args', {})
            
            if not all([simulation_id, browser_id, character_id, message_name]):
                return web.json_response(
                    {'error': 'Missing required fields'}, 
                    status=400
                )
            
            # Create simulation if it doesn't exist
            if simulation_id not in self.simulations:
                self.simulations[simulation_id] = {
                    'messages': [],
                    'browsers': set(),
                    'characters': {},
                    'config': {}
                }
            
            sim = self.simulations[simulation_id]
            message = {
                'id': str(uuid.uuid4()),
                'timestamp': asyncio.get_event_loop().time(),
                'simulation_id': simulation_id,
                'browser_id': browser_id,
                'character_id': character_id,
                'message_name': message_name,
                'args': args
            }
            
            sim['messages'].append(message)
            sim['browsers'].add(browser_id)
            
            # Broadcast to connected browsers
            await self.broadcast_message(message, simulation_id, browser_id)
            
            return web.json_response({'success': True, 'message_id': message['id']})
            
        except Exception as e:
            logger.error(f"Error posting message: {e}")
            return web.json_response({'error': str(e)}, status=500)
    
    async def broadcast_message(self, message: Dict, simulation_id: str, sender_browser_id: str):
        """Broadcast message to connected browsers"""
        message_data = {
            'type': 'message',
            'data': message
        }
        
        for browser_id, ws in self.connections.items():
            if (browser_id == sender_browser_id or 
                browser_id in self.simulations[simulation_id]['browsers']):
                try:
                    await ws.send(json.dumps(message_data))
                except Exception as e:
                    logger.error(f"Error broadcasting to {browser_id}: {e}")
    
    def generate_browser_id(self) -> str:
        """Generate a random browser ID"""
        return str(uuid.uuid4()).replace('-', '')[:12]
    
    async def websocket_handler(self, websocket: WebSocketServerProtocol, path: str):
        """Handle WebSocket connections"""
        browser_id = self.generate_browser_id()
        self.browsers[browser_id] = {
            'connected': asyncio.get_event_loop().time(),
            'lastActivity': asyncio.get_event_loop().time()
        }
        self.connections[browser_id] = websocket
        
        logger.info(f"Browser connected: {browser_id}")
        
        # Send welcome message
        welcome_message = {
            'type': 'welcome',
            'browser_id': browser_id,
            'message': 'Connected to HTTP-MCP server'
        }
        await websocket.send(json.dumps(welcome_message))
        
        try:
            async for message in websocket:
                try:
                    data = json.loads(message)
                    self.browsers[browser_id]['lastActivity'] = asyncio.get_event_loop().time()
                    
                    logger.info(f"Message from {browser_id}: {data}")
                    
                    # Echo back for now
                    echo_message = {
                        'type': 'echo',
                        'original': data,
                        'timestamp': asyncio.get_event_loop().time()
                    }
                    await websocket.send(json.dumps(echo_message))
                    
                except json.JSONDecodeError as e:
                    logger.error(f"Error parsing message: {e}")
                    
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            if browser_id in self.browsers:
                del self.browsers[browser_id]
            if browser_id in self.connections:
                del self.connections[browser_id]
            logger.info(f"Browser disconnected: {browser_id}")

class MCPServer:
    """Simple MCP server implementation"""
    
    def __init__(self):
        self.http_server = HTTPMCPServer()
        
    async def handle_mcp_request(self, request: Dict) -> Dict:
        """Handle MCP tool requests"""
        method = request.get('method')
        params = request.get('params', {})
        
        if method == 'tools/call':
            return await self.handle_tool_call(params)
        
        return {'error': 'Unknown method'}
    
    async def handle_tool_call(self, params: Dict) -> Dict:
        """Handle tool calls"""
        name = params.get('name')
        args = params.get('arguments', {})
        
        if name == 'serve_static':
            directory = args.get('directory', './static')
            port = args.get('port', 3000)
            
            # Create static directory if it doesn't exist
            Path(directory).mkdir(parents=True, exist_ok=True)
            
            # Start HTTP server
            runner = web.AppRunner(self.http_server.app)
            await runner.setup()
            site = web.TCPSite(runner, 'localhost', port)
            await site.start()
            
            logger.info(f"HTTP server running on port {port}")
            logger.info(f"Serving static files from: {directory}")
            
            return {
                'content': [{
                    'type': 'text',
                    'text': f'Static files being served from {directory} on port {port}'
                }]
            }
            
        elif name == 'send_message':
            simulation_id = args.get('simulation_id')
            browser_id = args.get('browser_id')
            character_id = args.get('character_id')
            message_name = args.get('message_name')
            message_args = args.get('args', {})
            
            # Create simulation if it doesn't exist
            if simulation_id not in self.http_server.simulations:
                self.http_server.simulations[simulation_id] = {
                    'messages': [],
                    'browsers': set(),
                    'characters': {},
                    'config': {}
                }
            
            sim = self.http_server.simulations[simulation_id]
            message = {
                'id': str(uuid.uuid4()),
                'timestamp': asyncio.get_event_loop().time(),
                'simulation_id': simulation_id,
                'browser_id': browser_id,
                'character_id': character_id,
                'message_name': message_name,
                'args': message_args
            }
            
            sim['messages'].append(message)
            sim['browsers'].add(browser_id)
            
            # Broadcast to connected browsers
            await self.http_server.broadcast_message(message, simulation_id, browser_id)
            
            return {
                'content': [{
                    'type': 'text',
                    'text': f'Message sent: {message_name} from {character_id} in {simulation_id}'
                }]
            }
            
        elif name == 'get_simulation_state':
            simulation_id = args.get('simulation_id')
            simulation = self.http_server.simulations.get(simulation_id)
            
            if not simulation:
                return {
                    'content': [{
                        'type': 'text',
                        'text': f'Simulation {simulation_id} not found'
                    }]
                }
            
            return {
                'content': [{
                    'type': 'text',
                    'text': json.dumps(simulation, indent=2, default=str)
                }]
            }
            
        elif name == 'create_simulation':
            simulation_id = args.get('simulation_id')
            config = args.get('config', {})
            
            if simulation_id in self.http_server.simulations:
                return {
                    'content': [{
                        'type': 'text',
                        'text': f'Simulation {simulation_id} already exists'
                    }]
                }
            
            self.http_server.simulations[simulation_id] = {
                'messages': [],
                'browsers': set(),
                'characters': {},
                'config': config
            }
            
            return {
                'content': [{
                    'type': 'text',
                    'text': f'Simulation {simulation_id} created successfully'
                }]
            }
        
        return {
            'content': [{
                'type': 'text',
                'text': f'Unknown tool: {name}'
            }]
        }

async def main():
    """Main function"""
    mcp_server = MCPServer()
    
    # Start WebSocket server
    websocket_server = await websockets.serve(
        mcp_server.http_server.websocket_handler,
        'localhost',
        8765
    )
    
    logger.info("HTTP-MCP server started")
    logger.info("WebSocket server running on ws://localhost:8765")
    logger.info("Available tools: serve_static, send_message, get_simulation_state, create_simulation")
    
    # Keep the server running
    await websocket_server.wait_closed()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1) 