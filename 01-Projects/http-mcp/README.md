# HTTP-MCP Tool

A general-purpose HTTP MCP tool for serving static files and web services with browser tunneling capabilities. This tool bridges the gap between Cursor's LLM and web-based simulations, allowing for real-time bidirectional communication.

## Features

- **Static File Serving**: Serve HTML, CSS, JS, and other static files
- **WebSocket Tunneling**: Real-time communication between browser and LLM
- **Simulation Management**: Create and manage multiple simulation instances
- **Message Routing**: Route messages between browsers, characters, and simulations
- **REST API**: HTTP endpoints for external integration

## Installation

### Python Dependencies

```bash
cd 01-Projects/http-mcp
pip install -r requirements.txt
```

### Node.js Dependencies (Alternative)

```bash
cd 01-Projects/http-mcp
npm install
```

## Usage

### Starting the Server

#### Python Version
```bash
python server.py
```

#### Node.js Version
```bash
npm start
```

The server will start and listen for MCP connections via stdio, with WebSocket server on port 8765.

### MCP Tools

#### 1. serve_static
Serve static files from a directory.

```json
{
  "name": "serve_static",
  "arguments": {
    "directory": "/path/to/static/files",
    "port": 3000
  }
}
```

#### 2. create_simulation
Create a new simulation instance.

```json
{
  "name": "create_simulation",
  "arguments": {
    "simulation_id": "WIZZY_FOREST_WIZID",
    "config": {
      "max_characters": 100,
      "world_size": [1000, 1000]
    }
  }
}
```

#### 3. send_message
Send a message to a simulation.

```json
{
  "name": "send_message",
  "arguments": {
    "simulation_id": "WIZZY_FOREST_WIZID",
    "browser_id": "abc123def456",
    "character_id": "owl_7",
    "message_name": "hunt_mouse",
    "args": {
      "target_position": [100, 200],
      "nutrients": {
        "sender": "owl_7",
        "emotional_state": "hungry, focused",
        "observation": "Spotted a juicy mouse near the oak tree",
        "proposed_action": "stealth_approach"
      }
    }
  }
}
```

#### 4. get_simulation_state
Get the current state of a simulation.

```json
{
  "name": "get_simulation_state",
  "arguments": {
    "simulation_id": "WIZZY_FOREST_WIZID"
  }
}
```

## Browser Integration

### WebSocket Connection

Connect to the WebSocket server to receive real-time updates:

```javascript
const ws = new WebSocket('ws://localhost:8765');

ws.onopen = () => {
  console.log('Connected to HTTP-MCP server');
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  switch (data.type) {
    case 'welcome':
      console.log('Welcome message:', data.message);
      console.log('Browser ID:', data.browser_id);
      break;
      
    case 'message':
      console.log('New message:', data.data);
      // Handle simulation message
      break;
      
    case 'echo':
      console.log('Echo response:', data.original);
      break;
  }
};
```

### Sending Messages from Browser

Send messages to the simulation via HTTP POST:

```javascript
fetch('/api/message', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    simulation_id: 'WIZZY_FOREST_WIZID',
    browser_id: 'abc123def456',
    character_id: 'owl_7',
    message_name: 'hunt_mouse',
    args: {
      target: 'mouse_3',
      nutrients: {
        sender: 'owl_7',
        emotional_state: 'hungry, focused',
        observation: 'Spotted a juicy mouse near the oak tree'
      }
    }
  })
});
```

## Message Structure

All messages follow this structure:

```json
{
  "simulation_id": "WIZZY_FOREST_WIZID",
  "browser_id": "abc123def456",
  "character_id": "owl_7",
  "message_name": "hunt_mouse",
  "args": {
    "target_position": [100, 200],
    "nutrients": {
      "sender": "owl_7",
      "emotional_state": "hungry, focused",
      "observation": "Spotted a juicy mouse near the oak tree",
      "proposed_action": "stealth_approach",
      "request": "What's the best angle for this hunt?"
    }
  }
}
```

### Components

- **simulation_id**: Unique identifier for the simulation instance
- **browser_id**: Random hash identifying the browser/client
- **character_id**: Specific entity in the simulation (owl, mouse, world_wizzy, etc.)
- **message_name**: The action or event being communicated
- **args**: Structured data including "nutrients" (Jazz JSON) for LLM processing

## REST API Endpoints

### GET /api/simulations
List all active simulations.

### GET /api/simulation/:id
Get detailed state of a specific simulation.

### POST /api/message
Send a message to a simulation.

## Testing

### Python Test Client

Run the test client to verify the server is working:

```bash
python test_client.py
```

### Node.js Test Client

```bash
node example-client.js
```

## Integration with Forest Simulation

To integrate with the forest simulation:

1. **Serve the simulation**:
   ```json
   {
     "name": "serve_static",
     "arguments": {
       "directory": "../lloooomm",
       "port": 3000
     }
   }
   ```

2. **Create simulation instance**:
   ```json
   {
     "name": "create_simulation",
     "arguments": {
       "simulation_id": "WIZZY_FOREST_WIZID"
     }
   }
   ```

3. **Modify the simulation HTML** to include WebSocket connection and message handling.

## Development

### Python Version
```bash
python server.py
```

### Node.js Version
```bash
npm run dev
```

## Architecture

The HTTP-MCP tool consists of:

1. **MCP Server**: Handles communication with Cursor
2. **HTTP Server**: Serves static files and provides REST API
3. **WebSocket Server**: Real-time communication with browsers
4. **State Management**: Tracks simulations, browsers, and messages
5. **Message Routing**: Routes messages between components

This creates a seamless bridge between the LLM in Cursor and web-based simulations, enabling rich interactive experiences with emergent behavior.

## Configuration

### Cursor MCP Configuration

Add this to your Cursor configuration to enable the HTTP-MCP tool:

```json
{
  "mcpServers": {
    "http-mcp": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "01-Projects/http-mcp"
    }
  }
}
```

Or for Node.js version:

```json
{
  "mcpServers": {
    "http-mcp": {
      "command": "node",
      "args": ["server.js"],
      "cwd": "01-Projects/http-mcp"
    }
  }
}
``` 