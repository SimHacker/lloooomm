// Example client for HTTP-MCP tool
// This demonstrates how to connect to the server and send/receive messages

const WebSocket = require('ws');

class HTTPMCPClient {
  constructor(serverUrl = 'ws://localhost:3000') {
    this.serverUrl = serverUrl;
    this.ws = null;
    this.browserId = null;
    this.simulationId = 'WIZZY_FOREST_WIZID';
    this.characterId = 'owl_7';
  }

  connect() {
    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.serverUrl);

      this.ws.onopen = () => {
        console.log('Connected to HTTP-MCP server');
        resolve();
      };

      this.ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        this.handleMessage(data);
      };

      this.ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        reject(error);
      };

      this.ws.onclose = () => {
        console.log('Disconnected from HTTP-MCP server');
      };
    });
  }

  handleMessage(data) {
    switch (data.type) {
      case 'welcome':
        this.browserId = data.browser_id;
        console.log('Welcome! Browser ID:', this.browserId);
        break;

      case 'message':
        console.log('Received message:', data.data);
        this.handleSimulationMessage(data.data);
        break;

      case 'echo':
        console.log('Echo response:', data.original);
        break;

      default:
        console.log('Unknown message type:', data.type);
    }
  }

  handleSimulationMessage(message) {
    // Handle different types of simulation messages
    switch (message.message_name) {
      case 'hunt_mouse':
        console.log(`${message.character_id} is hunting a mouse!`);
        console.log('Nutrients:', message.args.nutrients);
        break;

      case 'weather_change':
        console.log('Weather changed:', message.args.weather);
        break;

      case 'character_action':
        console.log(`${message.character_id} performed: ${message.args.action}`);
        break;

      default:
        console.log('Unknown message:', message.message_name);
    }
  }

  sendMessage(messageName, args = {}) {
    if (!this.ws || !this.browserId) {
      console.error('Not connected or no browser ID');
      return;
    }

    const message = {
      simulation_id: this.simulationId,
      browser_id: this.browserId,
      character_id: this.characterId,
      message_name: messageName,
      args: args
    };

    this.ws.send(JSON.stringify(message));
    console.log('Sent message:', messageName);
  }

  // Example: Send a hunting message
  huntMouse(targetPosition, nutrients) {
    this.sendMessage('hunt_mouse', {
      target_position: targetPosition,
      nutrients: nutrients
    });
  }

  // Example: Send a movement message
  moveTo(position, nutrients) {
    this.sendMessage('move_to', {
      position: position,
      nutrients: nutrients
    });
  }

  // Example: Send a social interaction
  interactWith(targetCharacter, interactionType, nutrients) {
    this.sendMessage('interact', {
      target: targetCharacter,
      interaction_type: interactionType,
      nutrients: nutrients
    });
  }

  disconnect() {
    if (this.ws) {
      this.ws.close();
    }
  }
}

// Example usage
async function runExample() {
  const client = new HTTPMCPClient();

  try {
    await client.connect();

    // Wait a moment for the welcome message
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Send some example messages
    client.huntMouse([100, 200], {
      sender: 'owl_7',
      emotional_state: 'hungry, focused',
      observation: 'Spotted a juicy mouse near the oak tree',
      proposed_action: 'stealth_approach'
    });

    await new Promise(resolve => setTimeout(resolve, 2000));

    client.moveTo([150, 250], {
      sender: 'owl_7',
      emotional_state: 'curious',
      observation: 'Moving to a better vantage point',
      proposed_action: 'perch_and_observe'
    });

    await new Promise(resolve => setTimeout(resolve, 2000));

    client.interactWith('owl_3', 'greeting', {
      sender: 'owl_7',
      emotional_state: 'friendly',
      observation: 'Another owl is nearby',
      proposed_action: 'social_bonding'
    });

    // Keep the connection alive for a bit to receive responses
    await new Promise(resolve => setTimeout(resolve, 5000));

  } catch (error) {
    console.error('Error:', error);
  } finally {
    client.disconnect();
  }
}

// Run the example if this file is executed directly
if (require.main === module) {
  runExample();
}

module.exports = HTTPMCPClient; 