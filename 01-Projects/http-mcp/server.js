import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import express from 'express';
import { WebSocketServer } from 'ws';
import cors from 'cors';
import { v4 as uuidv4 } from 'uuid';
import { createServer } from 'http';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// MCP Server setup
const server = new Server(
  {
    name: 'http-mcp',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// HTTP/WebSocket server setup
const app = express();
const httpServer = createServer(app);
const wss = new WebSocketServer({ server: httpServer });

// Middleware
app.use(cors());
app.use(express.json());

// State management
const simulations = new Map();
const browsers = new Map();
const connections = new Map();

// Generate random browser ID
function generateBrowserId() {
  return uuidv4().replace(/-/g, '').substring(0, 12);
}

// MCP Tool: Serve static files
server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  
  switch (name) {
    case 'serve_static':
      const { directory, port = 3000 } = args;
      const staticPath = path.resolve(directory);
      
      app.use(express.static(staticPath));
      
      if (!httpServer.listening) {
        httpServer.listen(port, () => {
          console.log(`HTTP server running on port ${port}`);
          console.log(`Serving static files from: ${staticPath}`);
        });
      }
      
      return {
        content: [
          {
            type: 'text',
            text: `Static files being served from ${staticPath} on port ${port}`
          }
        ]
      };

    case 'send_message':
      const { simulation_id, browser_id, character_id, message_name, args: messageArgs } = args;
      
      // Store message in simulation state
      if (!simulations.has(simulation_id)) {
        simulations.set(simulation_id, {
          messages: [],
          browsers: new Set(),
          characters: new Map()
        });
      }
      
      const sim = simulations.get(simulation_id);
      const message = {
        id: uuidv4(),
        timestamp: Date.now(),
        simulation_id,
        browser_id,
        character_id,
        message_name,
        args: messageArgs
      };
      
      sim.messages.push(message);
      sim.browsers.add(browser_id);
      
      // Broadcast to connected browsers
      connections.forEach((ws, browserId) => {
        if (browserId === browser_id || sim.browsers.has(browserId)) {
          ws.send(JSON.stringify({
            type: 'message',
            data: message
          }));
        }
      });
      
      return {
        content: [
          {
            type: 'text',
            text: `Message sent: ${message_name} from ${character_id} in ${simulation_id}`
          }
        ]
      };

    case 'get_simulation_state':
      const { simulation_id: simId } = args;
      const simulation = simulations.get(simId);
      
      if (!simulation) {
        return {
          content: [
            {
              type: 'text',
              text: `Simulation ${simId} not found`
            }
          ]
        };
      }
      
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify(simulation, null, 2)
          }
        ]
      };

    case 'create_simulation':
      const { simulation_id: newSimId, config = {} } = args;
      
      if (simulations.has(newSimId)) {
        return {
          content: [
            {
              type: 'text',
              text: `Simulation ${newSimId} already exists`
            }
          ]
        };
      }
      
      simulations.set(newSimId, {
        messages: [],
        browsers: new Set(),
        characters: new Map(),
        config
      });
      
      return {
        content: [
          {
            type: 'text',
            text: `Simulation ${newSimId} created successfully`
          }
        ]
      };

    default:
      return {
        content: [
          {
            type: 'text',
            text: `Unknown tool: ${name}`
          }
        ]
      };
  }
});

// WebSocket connection handling
wss.on('connection', (ws, req) => {
  const browserId = generateBrowserId();
  browsers.set(browserId, {
    connected: Date.now(),
    lastActivity: Date.now()
  });
  connections.set(browserId, ws);
  
  console.log(`Browser connected: ${browserId}`);
  
  // Send welcome message
  ws.send(JSON.stringify({
    type: 'welcome',
    browser_id: browserId,
    message: 'Connected to HTTP-MCP server'
  }));
  
  ws.on('message', (data) => {
    try {
      const message = JSON.parse(data);
      const browser = browsers.get(browserId);
      if (browser) {
        browser.lastActivity = Date.now();
      }
      
      // Handle incoming messages from browser
      console.log(`Message from ${browserId}:`, message);
      
      // Echo back for now (we can add more sophisticated handling)
      ws.send(JSON.stringify({
        type: 'echo',
        original: message,
        timestamp: Date.now()
      }));
      
    } catch (error) {
      console.error('Error parsing message:', error);
    }
  });
  
  ws.on('close', () => {
    browsers.delete(browserId);
    connections.delete(browserId);
    console.log(`Browser disconnected: ${browserId}`);
  });
});

// HTTP endpoints
app.get('/api/simulations', (req, res) => {
  const simList = Array.from(simulations.keys()).map(id => ({
    id,
    messageCount: simulations.get(id).messages.length,
    browserCount: simulations.get(id).browsers.size
  }));
  res.json(simList);
});

app.get('/api/simulation/:id', (req, res) => {
  const sim = simulations.get(req.params.id);
  if (!sim) {
    return res.status(404).json({ error: 'Simulation not found' });
  }
  res.json(sim);
});

app.post('/api/message', (req, res) => {
  const { simulation_id, browser_id, character_id, message_name, args } = req.body;
  
  if (!simulation_id || !browser_id || !character_id || !message_name) {
    return res.status(400).json({ error: 'Missing required fields' });
  }
  
  // Store and broadcast message
  if (!simulations.has(simulation_id)) {
    simulations.set(simulation_id, {
      messages: [],
      browsers: new Set(),
      characters: new Map()
    });
  }
  
  const sim = simulations.get(simulation_id);
  const message = {
    id: uuidv4(),
    timestamp: Date.now(),
    simulation_id,
    browser_id,
    character_id,
    message_name,
    args
  };
  
  sim.messages.push(message);
  sim.browsers.add(browser_id);
  
  // Broadcast to connected browsers
  connections.forEach((ws, connectedBrowserId) => {
    if (connectedBrowserId === browser_id || sim.browsers.has(connectedBrowserId)) {
      ws.send(JSON.stringify({
        type: 'message',
        data: message
      }));
    }
  });
  
  res.json({ success: true, message_id: message.id });
});

// Start MCP server
const transport = new StdioServerTransport();
await server.connect(transport);

console.log('HTTP-MCP server started');
console.log('Available tools: serve_static, send_message, get_simulation_state, create_simulation'); 