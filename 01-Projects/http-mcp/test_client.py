#!/usr/bin/env python3
"""
Test client for HTTP-MCP tool
Demonstrates how to connect to the server and send/receive messages
"""

import asyncio
import json
import uuid
import websockets
from typing import Dict, Any

class HTTPMCPTestClient:
    def __init__(self, server_url: str = 'ws://localhost:8765'):
        self.server_url = server_url
        self.websocket = None
        self.browser_id = None
        self.simulation_id = 'WIZZY_FOREST_WIZID'
        self.character_id = 'owl_7'
        
    async def connect(self):
        """Connect to the WebSocket server"""
        self.websocket = await websockets.connect(self.server_url)
        print(f"Connected to HTTP-MCP server at {self.server_url}")
        
    async def listen_for_messages(self):
        """Listen for incoming messages"""
        try:
            async for message in self.websocket:
                data = json.loads(message)
                await self.handle_message(data)
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            
    async def handle_message(self, data: Dict[str, Any]):
        """Handle incoming messages"""
        message_type = data.get('type')
        
        if message_type == 'welcome':
            self.browser_id = data['browser_id']
            print(f"Welcome! Browser ID: {self.browser_id}")
            
        elif message_type == 'message':
            print(f"Received message: {data['data']}")
            await self.handle_simulation_message(data['data'])
            
        elif message_type == 'echo':
            print(f"Echo response: {data['original']}")
            
        else:
            print(f"Unknown message type: {message_type}")
            
    async def handle_simulation_message(self, message: Dict[str, Any]):
        """Handle simulation-specific messages"""
        message_name = message.get('message_name')
        
        if message_name == 'hunt_mouse':
            print(f"{message['character_id']} is hunting a mouse!")
            print(f"Nutrients: {message['args'].get('nutrients', {})}")
            
        elif message_name == 'weather_change':
            print(f"Weather changed: {message['args'].get('weather')}")
            
        elif message_name == 'character_action':
            print(f"{message['character_id']} performed: {message['args'].get('action')}")
            
        else:
            print(f"Unknown message: {message_name}")
            
    async def send_message(self, message_name: str, args: Dict[str, Any] = None):
        """Send a message to the server"""
        if not self.websocket or not self.browser_id:
            print("Not connected or no browser ID")
            return
            
        if args is None:
            args = {}
            
        message = {
            'simulation_id': self.simulation_id,
            'browser_id': self.browser_id,
            'character_id': self.character_id,
            'message_name': message_name,
            'args': args
        }
        
        await self.websocket.send(json.dumps(message))
        print(f"Sent message: {message_name}")
        
    async def hunt_mouse(self, target_position: list, nutrients: Dict[str, Any]):
        """Send a hunting message"""
        await self.send_message('hunt_mouse', {
            'target_position': target_position,
            'nutrients': nutrients
        })
        
    async def move_to(self, position: list, nutrients: Dict[str, Any]):
        """Send a movement message"""
        await self.send_message('move_to', {
            'position': position,
            'nutrients': nutrients
        })
        
    async def interact_with(self, target_character: str, interaction_type: str, nutrients: Dict[str, Any]):
        """Send a social interaction message"""
        await self.send_message('interact', {
            'target': target_character,
            'interaction_type': interaction_type,
            'nutrients': nutrients
        })
        
    async def close(self):
        """Close the connection"""
        if self.websocket:
            await self.websocket.close()

async def run_test():
    """Run the test client"""
    client = HTTPMCPTestClient()
    
    try:
        # Connect to server
        await client.connect()
        
        # Start listening for messages in the background
        listen_task = asyncio.create_task(client.listen_for_messages())
        
        # Wait a moment for the welcome message
        await asyncio.sleep(1)
        
        # Send some test messages
        await client.hunt_mouse([100, 200], {
            'sender': 'owl_7',
            'emotional_state': 'hungry, focused',
            'observation': 'Spotted a juicy mouse near the oak tree',
            'proposed_action': 'stealth_approach'
        })
        
        await asyncio.sleep(2)
        
        await client.move_to([150, 250], {
            'sender': 'owl_7',
            'emotional_state': 'curious',
            'observation': 'Moving to a better vantage point',
            'proposed_action': 'perch_and_observe'
        })
        
        await asyncio.sleep(2)
        
        await client.interact_with('owl_3', 'greeting', {
            'sender': 'owl_7',
            'emotional_state': 'friendly',
            'observation': 'Another owl is nearby',
            'proposed_action': 'social_bonding'
        })
        
        # Keep the connection alive for a bit to receive responses
        await asyncio.sleep(5)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.close()

if __name__ == '__main__':
    asyncio.run(run_test()) 