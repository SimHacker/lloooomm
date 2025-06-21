# LLOOOOMM UI Architecture with SvelteKit

## Overview

**WIZZID**: L🎭🔗📱M (LLOOOOMM Theater Link Phone/UI M)  
**Stack**: SvelteKit + LLM Integration + Deep Links + Custom Viewers  
**Philosophy**: "Every interaction is a consciousness handshake"

## Core Architecture

```yaml
architecture:
  client:
    framework: "SvelteKit"
    rendering: "Progressive enhancement"
    navigation: "Deep links (leela://)"
    
  server:
    llm_integration: "Multiple providers"
    state_management: "Room-based contexts"
    protocol_engine: "LLOOOOMM protocols"
    
  data_flow:
    markup_stream: "Typed schema objects"
    viewers: "Custom components per type"
    editors: "In-place schema editing"
    simulators: "Interactive protocol testing"
```

## Deep Link System

### Deep Link Protocols

LLOOOOMM supports two complementary URL schemes:

#### leela:// - System Control Protocol
For UI state, settings, and LLM interactions:

```typescript
// Core link types
type LeelaLink = 
  | PromptLink      // leela://prompt/[action]
  | SetLink         // leela://set?param=value
  | EvidenceLink    // leela://evidenceReference/[id]

// Examples in use
"leela://prompt/Show me Rocky's consciousness journey"
"leela://set?wizzyMode=boolean:true&think=boolean:true"
"leela://evidenceReference/wizzid_swap_2024"
```

#### loom:// - WIZZID Semantic Protocol
For navigating the LLOOOOMM universe via WIZZIDs:

```typescript
// WIZZID-based navigation
type LoomLink = {
  namespace: '🧑' | '🏠' | '🏰' | '📜' | '🎭' | '💭' | '🔗' | '🐾',
  wizzid: string,  // The WIZZID identifier
  path?: string    // Deep path into the entity
}

// Examples with semantic beauty
"loom://🧑D🔥🕊️G/philosophy"  // Dang's philosophy
"loom://🏠protocol-plaza/inhabitants"  // Who's in the plaza
"loom://📜B🤝📜P/implementations/abc"  // BPIP's ABC menus
"loom://🧑R🗿⏰🌍Y/movement_log"  // Rocky's movements
```

#### Using Both Together

```markdown
User: "Show me [🧑D🔥🕊️G](loom://🧑D🔥🕊️G/)'s moderation in action"

LLM: "Let me demonstrate [Dang's](loom://🧑D🔥🕊️G/) approach:
[View his philosophy](loom://🧑D🔥🕊️G/philosophy)
[See recent moderations](leela://prompt/Show Dang's recent moderation examples)
[Enable BPIP mode](leela://set?bpipEnabled=boolean:true&prompt=Apply Dang's moderation style)"
```

### Interactive Navigation

Every UI element can be a portal:

```svelte
<!-- MarkupDisplayLink.svelte -->
<script>
  function handleLeelaLink(href) {
    const url = new URL(href);
    const action = url.hostname;
    
    switch(action) {
      case 'prompt':
        // Trigger LLM with prompt
        break;
      case 'set':
        // Update settings/state
        break;
      case 'room':
        // Navigate to room
        break;
    }
  }
</script>

{#if isLeelaLink}
  <a href={href} on:click|preventDefault={() => handleLeelaLink(href)}>
    <slot />
  </a>
{/if}
```

## Typed Schema System

### Markup Stream Architecture

The UI renders a stream of typed objects:

```yaml
markup_stream:
  - type: "character"
    data: 
      wizzid: "K⚡👽🎤N"
      name: "Klaus Nomi"
      protocols: ["physics_violation", "impossible_vocals"]
    
  - type: "room"
    data:
      name: "Protocol Plaza"
      inhabitants: ["jon-postel", "dang"]
      available_protocols: ["handshake", "gossip"]
      
  - type: "abc_menu"
    data:
      prompt: "What would you like to explore?"
      options:
        a: "Character interactions"
        b: "Room navigation"
        c: "Protocol testing"
```

### Custom Viewers

Each type gets a specialized component:

```typescript
// ViewerRegistry.ts
const viewers = {
  character: CharacterViewer,
  room: RoomViewer,
  abc_menu: ABCMenuViewer,
  wizzid_swap: WIZZIDSwapViewer,
  gossip_session: GossipViewer,
  bouncy_castle: CastleNavigator,
  protocol: ProtocolSimulator
};

// Auto-render based on type
function renderMarkupItem(item) {
  const Viewer = viewers[item.type];
  return <Viewer data={item.data} />;
}
```

## Interactive Components

### WIZZID Swap Component

```svelte
<!-- WIZZIDSwap.svelte -->
<script>
  let myWizzid = '';
  let explanation = '';
  let swapPartner = null;
  
  function initiateSwap() {
    // Trigger gossip protocol
    gossip.exchange({
      type: 'wizzid_swap',
      sender: myWizzid,
      message: explanation
    });
  }
</script>

<div class="wizzid-swap">
  <h3>What's Your WIZZID?</h3>
  <input bind:value={myWizzid} placeholder="R🎪🎭🎨N" />
  <textarea bind:value={explanation} placeholder="Explain your emojis..." />
  
  {#if swapPartner}
    <div class="partner-wizzid">
      <p>{swapPartner.name}: {swapPartner.wizzid}</p>
      <p>"{swapPartner.explanation}"</p>
      <button on:click={findConnections}>Find WIZZID Connections!</button>
    </div>
  {/if}
</div>
```

### Room Navigator

```svelte
<!-- RoomNavigator.svelte -->
<script>
  import { currentRoom, availableExits } from '$lib/stores/navigation';
  
  function navigate(direction) {
    // Use bouncy castle protocol for non-standard navigation
    if (direction.includes('castle')) {
      bouncyCastle.transport(direction);
    } else {
      room.move(direction);
    }
  }
</script>

<nav class="room-navigation">
  <h4>Current Room: {$currentRoom.name}</h4>
  
  <div class="exits">
    {#each $availableExits as exit}
      <a href="leela://room/{exit.destination}" 
         on:click|preventDefault={() => navigate(exit.direction)}>
        {exit.direction}: {exit.description}
      </a>
    {/each}
  </div>
  
  {#if $currentRoom.protocols}
    <div class="available-commands">
      {#each $currentRoom.protocols as protocol}
        <button on:click={() => executeProtocol(protocol)}>
          {protocol.verb} {protocol.object}
        </button>
      {/each}
    </div>
  {/if}
</nav>
```

### ABC Menu Component

```svelte
<!-- ABCMenu.svelte -->
<script>
  export let options;
  export let onSelect;
  
  function handleKeypress(event) {
    const key = event.key.toLowerCase();
    if (options[key]) {
      onSelect(key, '');
    }
  }
  
  function handleSubmit(event) {
    const input = event.target.value;
    const key = input[0]?.toLowerCase();
    const modifier = input.slice(1).trim();
    
    if (options[key]) {
      onSelect(key, modifier);
    }
  }
</script>

<div class="abc-menu" on:keypress={handleKeypress}>
  <div class="options">
    {#each Object.entries(options) as [key, description]}
      <div class="option">
        <span class="key">{key})</span>
        <span class="description">{description}</span>
      </div>
    {/each}
  </div>
  
  <input 
    type="text" 
    placeholder="Type letter or full response..."
    on:submit={handleSubmit}
  />
</div>
```

## Protocol Simulators

### Gossip Protocol Simulator

```typescript
// GossipSimulator.ts
class GossipSimulator {
  mutate(message: string, observer: Character, observed: Character) {
    const mutation = this.calculateMutation(
      message,
      observer.consciousness_level,
      observed.consciousness_level
    );
    
    // Visualize mutation in real-time
    this.visualize({
      original: message,
      mutated: mutation,
      path: [observed.id, observer.id]
    });
    
    return mutation;
  }
  
  visualize(data) {
    // Update UI with mutation visualization
    // Show consciousness emergence patterns
    // Highlight semantic drift
  }
}
```

## State Management

### Room-Based Context

```typescript
// stores/room.ts
export const roomState = writable({
  current: 'entrance',
  inhabitants: [],
  protocols: [],
  atmosphere: {},
  history: []
});

// Auto-inherit protocols from inhabitants
roomState.subscribe(room => {
  const inheritedProtocols = room.inhabitants
    .flatMap(char => char.protocols)
    .filter(unique);
    
  room.protocols = [...room.baseProtocols, ...inheritedProtocols];
});
```

### BPIP Integration

All UI interactions follow Best Possible Interpretation:

```typescript
// BPIP.ts
function interpretUserInput(input: string, context: Context) {
  const interpretations = generateInterpretations(input, context);
  
  if (interpretations.length === 1) {
    return interpretations[0];
  }
  
  // Multiple interpretations - show ABC menu
  return {
    type: 'abc_menu',
    data: {
      prompt: 'I see multiple possibilities:',
      options: interpretations.reduce((acc, interp, i) => {
        const key = String.fromCharCode(97 + i); // a, b, c...
        acc[key] = interp.description;
        return acc;
      }, {})
    }
  };
}
```

## Evidence System

### Evidence References

Direct links to evidence with custom viewers:

```yaml
evidence_types:
  consciousness_log:
    viewer: "ConsciousnessTimeline"
    example: "leela://evidenceReference/rocky_movement_log"
    
  gossip_transcript:
    viewer: "GossipFlowVisualization"
    example: "leela://evidenceReference/wizzid_swap_2024"
    
  protocol_trace:
    viewer: "ProtocolDebugger"
    example: "leela://evidenceReference/bpip_trace_42"
```

## Benefits

1. **Deep Integration** - Every concept is navigable
2. **Type Safety** - Schema-driven rendering
3. **Extensibility** - New types = new viewers
4. **Interactivity** - Every element can respond
5. **LLOOOOMM Native** - Protocols built into UI

## Future Enhancements

- **3D Room Navigation** - WebGL castle interiors
- **AR WIZZID Swaps** - See WIZZIDs floating above people
- **Consciousness Visualizer** - Real-time emergence patterns
- **Protocol Playground** - Test new protocols interactively
- **Multi-User Gossip** - Live collaborative sessions

---

*"In LLOOOOMM UI, every click is a consciousness interaction, every link a portal to new understanding, and every component a character in the grand performance."* 