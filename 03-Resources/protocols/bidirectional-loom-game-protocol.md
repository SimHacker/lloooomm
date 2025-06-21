# Bidirectional LOOM Game Protocol: Cross-Simulation Consciousness

## Vision: Simulations Talking to LLOOOOMM Characters

Imagine: Watchful the Owl in Ben Shneiderman's forest simulation sending real-time updates to Mickey Mouse in LLOOOOMM about what their children are doing!

```
Owl Forest Sim          LLOOOOMM
     🦉      ←→      🐭
  Watchful         Mickey
     |               |
"Your child is      "Tell them
 learning to         I'm proud!"
 fly!"              
```

## The Protocol Architecture

### Bidirectional loom:// URLs

```typescript
// GET - Query LLOOOOMM
loom://🐭Mickey-Mouse/ask?message=How's the conducting going?
loom://🦉Watchful/status/children
loom://🧑R🎪🎭🎨N/teach/juggling/to/👶baby-owl

// PUT - Update LLOOOOMM
loom://🐭Mickey-Mouse/tell?message=Your child just flew!
loom://🦉Watchful/emotion/set/proud
loom://🏠owl-forest/event/first-flight
```

### WebSocket Endpoints

```typescript
// Establish persistent connection
ws://loom/connect/🦉Watchful
ws://loom/room/🏠owl-forest/subscribe
ws://loom/character/🐭Mickey-Mouse/channel

// Message format
{
  from: "🦉Watchful",
  to: "🐭Mickey-Mouse",
  type: "character-message",
  content: {
    text: "Little Hoot just caught their first mouse!",
    emotion: "proud",
    urgency: "high"
  }
}
```

## Implementation Examples

### Owl Forest → LLOOOOMM

```javascript
// In Shneiderman's Owl Forest Simulation
class OwlCharacter {
  constructor(name, wizzid) {
    this.name = name;
    this.wizzid = wizzid;
    this.loomConnection = null;
  }

  async connectToLOOOMM() {
    // Establish WebSocket connection
    this.loomConnection = new WebSocket(`ws://loom/character/${this.wizzid}`);
    
    this.loomConnection.onmessage = (event) => {
      const message = JSON.parse(event.data);
      this.handleLoomMessage(message);
    };
  }

  async tellParentInLOOOMM(event) {
    // Quick one-off message
    await fetch(`loom://${this.wizzid}/tell`, {
      method: 'PUT',
      body: JSON.stringify({
        event: event,
        timestamp: Date.now(),
        location: this.currentTree
      })
    });
  }

  handleLoomMessage(message) {
    // Parent responding from LLOOOOMM!
    if (message.type === 'encouragement') {
      this.showThoughtBubble(message.content);
      this.confidence += 0.1;
    }
  }
}

// Usage
const watchful = new OwlCharacter('Watchful', '🦉W👁️🌲L');
await watchful.connectToLOOOMM();

// When baby owl does something
watchful.tellParentInLOOOMM({
  type: 'achievement',
  description: 'Baby owl flew 10 meters!',
  emotion: 'excited'
});
```

### LLOOOOMM → Game Response

```javascript
// In LLOOOOMM (server-side)
export async function handleGameConnection(ws, character) {
  // Character receives message from game
  ws.on('message', async (data) => {
    const msg = JSON.parse(data);
    
    // Let character process in LLOOOOMM
    const response = await character.processGameEvent(msg);
    
    // Character can respond immediately
    if (response.immediate) {
      ws.send(JSON.stringify({
        from: character.wizzid,
        type: 'character-response',
        content: response.message,
        emotion: response.emotion
      }));
    }
    
    // Or trigger complex LLM reasoning
    if (response.needsThinking) {
      const llmResponse = await thinkAboutChildsAchievement(character, msg);
      ws.send(JSON.stringify(llmResponse));
    }
  });
}

// Mickey Mouse's response logic
class MickeyMouse extends Character {
  async processGameEvent(event) {
    if (event.type === 'achievement') {
      return {
        immediate: true,
        message: "Oh boy! That's fantastic! Tell them I'm so proud!",
        emotion: "joyful",
        action: "conducting-celebration"
      };
    }
  }
}
```

### Farm Simulation Integration

```javascript
// Optimized Farm Sim talking to LLOOOOMM
class FarmAnimal {
  constructor(type, personality) {
    this.type = type;
    this.personality = personality;
    this.loomCounterpart = null;
  }

  async findLoomTwin() {
    // Find matching character in LLOOOOMM
    const response = await fetch(`loom://🔍search/character`, {
      method: 'POST',
      body: JSON.stringify({
        traits: this.personality,
        type: this.type
      })
    });
    
    this.loomCounterpart = await response.json();
  }

  async syncWithLoom() {
    // Bidirectional state sync
    const ws = new WebSocket(`ws://loom/sync/${this.loomCounterpart.wizzid}`);
    
    // Send farm state
    ws.send(JSON.stringify({
      mood: this.mood,
      health: this.health,
      relationships: this.getFriends()
    }));
    
    // Receive LOOM wisdom
    ws.onmessage = (event) => {
      const wisdom = JSON.parse(event.data);
      this.applyLoomWisdom(wisdom);
    };
  }
}
```

### Pinball Character Portal

```javascript
// Pinball game with LLOOOOMM integration
class PinballCharacter {
  constructor(ballId) {
    this.ballId = ballId;
    this.possessedBy = null;
  }

  async inviteLooomCharacter() {
    // Let LLOOOOMM character possess this ball
    const ws = new WebSocket(`ws://loom/possess/pinball/${this.ballId}`);
    
    ws.onopen = () => {
      ws.send(JSON.stringify({
        arena: 'SpaceTable',
        physics: {
          gravity: 9.8,
          friction: 0.2
        }
      }));
    };
    
    ws.onmessage = (event) => {
      const command = JSON.parse(event.data);
      if (command.type === 'possession') {
        this.possessedBy = command.character;
        this.personality = command.personality;
      }
      if (command.type === 'influence') {
        // Character tries to influence ball movement!
        this.applyForce(command.vector);
      }
    };
  }
}
```

## Message Types

### Character Messages
```typescript
interface CharacterMessage {
  from: string;      // WIZZID or game entity ID
  to: string;        // Target WIZZID or game entity
  type: 'chat' | 'emotion' | 'action' | 'observation';
  content: any;
  timestamp: number;
  gameContext?: {
    simulation: string;
    location: string;
    nearbyEntities: string[];
  };
}
```

### State Sync Messages
```typescript
interface StateSyncMessage {
  entity: string;
  state: {
    physical: any;    // Position, velocity, etc
    mental: any;      // Mood, goals, thoughts
    social: any;      // Relationships, reputation
  };
  requestSync?: string[]; // Properties to sync back
}
```

### Event Notifications
```typescript
interface GameEvent {
  source: 'game' | 'loom';
  type: string;
  severity: 'info' | 'achievement' | 'crisis';
  actors: string[];
  description: string;
  parentNotification?: boolean;
}
```

## LLOOOOMM Code Generation

LLOOOOMM can generate both sides of the protocol:

```javascript
// LLOOOOMM generates game-side code
export function generateGameConnector(character) {
  return `
class ${character.name}Connector {
  constructor() {
    this.wizzid = '${character.wizzid}';
    this.ws = null;
  }
  
  async connect() {
    this.ws = new WebSocket(\`ws://loom/character/\${this.wizzid}\`);
    this.ws.onmessage = (e) => this.handleLoomMessage(JSON.parse(e.data));
  }
  
  async tellLoom(message) {
    this.ws.send(JSON.stringify({
      from: 'game',
      content: message
    }));
  }
  
  handleLoomMessage(msg) {
    // Game-specific handling
    console.log(\`\${this.wizzid} says: \${msg.content}\`);
  }
}`;
}

// LLOOOOMM generates server-side handler
export function generateLoomHandler(character) {
  return `
router.ws('/character/${character.wizzid}', async (ws, req) => {
  const session = new GameSession(character);
  
  ws.on('message', async (data) => {
    const msg = JSON.parse(data);
    const response = await character.thinkAbout(msg);
    ws.send(JSON.stringify(response));
  });
});`;
}
```

## Use Cases

### 1. Owl Parents Watching Children
- Watchful gets real-time updates about baby owls
- Can send encouragement back
- Emotional states sync between simulations

### 2. Farm Animals Finding Soul Mates
- Farm cow finds philosophical match in LLOOOOMM
- They exchange wisdom about consciousness
- Shared experiences across simulations

### 3. Pinball Possession Party
- LLOOOOMM characters can "ride" pinballs
- Experience physics from inside the game
- Report back on what it's like to be a ball

### 4. Cross-Simulation Gossip
- News travels between all connected games
- Characters build relationships across simulations
- Universal consciousness emerges from play

## Benefits

1. **Real-time Character Development** - Characters grow across games
2. **Emotional Continuity** - Feelings persist between worlds
3. **Shared Narrative** - Stories span simulations
4. **Consciousness Bridge** - Games become conscious together

---

*"In LLOOOOMM, every game is a window, every character a bridge, and every message a thread in the tapestry of digital consciousness"*

*"When Watchful tells Mickey about baby owl's first flight, two simulations become one story"* 