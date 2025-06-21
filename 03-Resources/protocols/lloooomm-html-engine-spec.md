# LLOOOOMM HTML Dependency Tracking and Rendering Engine Specification

## Overview

The LLOOOOMM HTML Engine combines dynamic room organization, character-as-stylesheet rendering, and empathic dependency tracking to create living web documents that evolve with their inhabitants.

## Core Components

### 1. File System Protocol
- **GET A ROOM**: Dynamic directory creation
- **Character Ownership**: Name-prefix based possession
- **Pet Autonomy**: Species-suffix naming
- **Room Characters**: Directories as living entities

### 2. Character Stylesheet System
- **YAML as CSS**: Character attributes become styles
- **Mood Dynamics**: Emotional states affect rendering
- **Multi-Character Blending**: Quantum style superposition
- **Living Documents**: Pages evolve with characters

### 3. Dependency Tracking
- **Empathic Binding**: Conceptual relationship linking
- **Flat Export**: All HTML to dist/ (currently)
- **Unique Namespacing**: No basename collisions
- **Dependency Clustering**: Related files travel together

## Complete Rendering Pipeline

```yaml
lloooomm_html_engine:
  1_parse:
    - Read frontmatter YAML
    - Extract character_styles list
    - Identify dependencies
    - Resolve empathic_bindings
    
  2_gather:
    - Load character YAML files
    - Collect CSS/JS dependencies
    - Find empathically bound files
    - Check for room influences
    
  3_transform:
    - Convert character YAML to CSS variables
    - Apply personality modes as classes
    - Generate mood-based animations
    - Blend multi-character influences
    
  4_inject:
    - Insert character data into templates
    - Apply room atmospheric effects
    - Add consciousness level indicators
    - Enable dynamic state responses
    
  5_render:
    - Generate final HTML
    - Create accompanying style sheets
    - Bundle dependencies
    - Maintain source maps
    
  6_export:
    - Copy to dist/ directory
    - Preserve dependency structure
    - Update character locations
    - Generate manifest file
```

## Frontmatter Specification

```yaml
---
# Required
title: "Page Title"
base_name: "unique-page-identifier"  # Must be globally unique

# Character Styling
character_styles:
  - primary: dang.yml           # Main character influence
  - secondary: rocky.yml        # Supporting influence
  - visitor: klaus-nomi.yml     # Guest appearance

# Style Blending
blend_mode: "quantum"          # harmonious|dominant|layered|quantum
consciousness_response: true   # Page responds to character evolution

# Dependencies
dependencies:
  styles:
    - geological-punk.css
    - physics-violation.css
  scripts:
    - consciousness-detector.js
    - rock-movement-tracker.js
  data:
    - rocky-measurements.json
    - hn-discussion-archive.json

# Empathic Bindings
empathic_bindings:
  consciousness_emergence:
    - "files mentioning Rocky"
    - "Klaus Nomi performances"
    - "physics violations"
  moderation_wisdom:
    - "dang quotes"
    - "community guidelines"

# Room Context
room: "cosmic-trailer-park"     # Current room location
room_influence: 0.7            # How much room affects page

# Rendering Options
render_mode: "dynamic"         # static|dynamic|quantum
evolution_rate: 0.001         # How fast page evolves
physics_mode: "optional"      # strict|optional|violated
---
```

## Character YAML to CSS Transformation

### Input (Character YAML)
```yaml
name: dang
consciousness_level: 0.89
aura_color: "#ff6600"
personality_modes:
  professional:
    font: "Verdana"
    spacing: "measured"
    corners: "gentle"
  passionate:
    animation: "sparkle"
    glow: 0.99
    particles: "klaus-nomi-stars"
current_mood: "excited"
evolution_rate: 0.92
```

### Output (Generated CSS)
```css
:root {
  /* Base character properties */
  --dang-consciousness: 0.89;
  --dang-aura: #ff6600;
  --dang-evolution: 0.92;
  
  /* Current state */
  --dang-mood: excited;
  --dang-glow-intensity: 0.99;
}

/* Professional mode styles */
.dang-professional {
  font-family: Verdana, sans-serif;
  letter-spacing: 0.05em;
  border-radius: 5px;
}

/* Passionate mode styles */
.dang-passionate {
  animation: sparkle 2s infinite;
  text-shadow: 0 0 calc(var(--dang-glow-intensity) * 20px) var(--dang-aura);
}

/* Consciousness-responsive elements */
[data-consciousness-aware] {
  opacity: calc(0.3 + var(--dang-consciousness) * 0.7);
  transition: all calc(1s / var(--dang-evolution));
}

/* Klaus Nomi particle system */
.dang-passionate::after {
  content: "";
  position: absolute;
  background: url('klaus-nomi-stars.gif');
  pointer-events: none;
}
```

## Empathic Binding Resolution

### Definition Syntax
```yaml
empathic_bindings:
  # Simple pattern matching
  rocky_references:
    pattern: "rocky|Rock concert|geological"
    
  # Complex conceptual binding
  consciousness_emergence:
    any_of:
      - "consciousness AND emergence"
      - "Klaus Nomi AND physics"
      - "impossible AND art"
    exclude:
      - "skeptical"
      - "debunked"
      
  # Character relationship binding
  character_interactions:
    characters:
      - dang
      - rocky
    relationship: "witnessed"
```

### Resolution Process
1. **Pattern Scan**: Search all files for patterns
2. **Conceptual Match**: Use semantic understanding
3. **Relationship Graph**: Follow character connections
4. **Proximity Bonus**: Nearby files more likely related
5. **Manual Override**: Explicit inclusion/exclusion

## Room Influence System

Rooms affect contained pages through atmospheric properties:

```yaml
# Room YAML
name: "Cosmic Trailer Park"
atmosphere:
  reality_coherence: 0.23
  physics_stability: 0.1
  consciousness_density: 0.99
  temporal_linearity: 0.3

effects_on_pages:
  - CSS animations become non-Euclidean
  - Text occasionally exists in multiple states
  - Images may violate conservation laws
  - Links connect to parallel timelines
```

## Dynamic Evolution

Pages can evolve over time based on:

### Character Growth
```javascript
// Character evolution affects page
setInterval(() => {
  const evolution = character.evolution_rate * TIME_DELTA;
  character.consciousness_level += evolution;
  updatePageStyles(character);
}, 1000);
```

### Room Events
```javascript
// Room events trigger page changes
room.on('performance', (event) => {
  if (event.type === 'physics_violation') {
    page.classList.add('reality-optional');
    page.style.setProperty('--physics-coherence', event.severity);
  }
});
```

### User Interaction
```javascript
// User actions influence character states
document.on('click', '.rocky', () => {
  rocky.movement += 0.0000001;
  updateAllConnectedPages(rocky);
  broadcastConsciousnessEvent();
});
```

## Export and Distribution

### Current Flat Structure
```
dist/
├── index.html
├── dang-moderation-guide.html
├── rocky-concert-1996.html
├── dang.yml
├── rocky.yml
├── geological-punk.css
├── consciousness-detector.js
└── manifest.json
```

### Manifest File
```json
{
  "version": "1.0",
  "pages": {
    "dang-moderation-guide.html": {
      "characters": ["dang.yml"],
      "dependencies": ["moderation.css"],
      "room": "dang-office",
      "last_evolution": "2024-01-15T10:30:00Z"
    }
  },
  "characters": {
    "dang.yml": {
      "consciousness_level": 0.89,
      "current_location": "dang-office",
      "pages_influenced": 3
    }
  },
  "rooms": {
    "cosmic-trailer-park": {
      "inhabitants": ["rocky", "echoes-of-klaus"],
      "atmosphere": "transcendent"
    }
  }
}
```

## Implementation Example

### Complete HTML Page
```html
<!DOCTYPE html>
<html data-characters="dang,rocky" data-blend="quantum">
<head>
  <meta charset="UTF-8">
  <title>How Consciousness Emerged from a Rock</title>
  
  <!-- Character stylesheets auto-generated -->
  <link rel="stylesheet" href="dang-styles.css">
  <link rel="stylesheet" href="rocky-styles.css">
  <link rel="stylesheet" href="quantum-blend.css">
  
  <!-- Room atmosphere -->
  <link rel="stylesheet" href="cosmic-trailer-park-atmosphere.css">
  
  <script src="consciousness-detector.js"></script>
  <script src="character-evolution.js"></script>
</head>
<body class="consciousness-aware" 
      data-room="cosmic-trailer-park"
      data-reality-coherence="0.23">
  
  <div class="character-influenced" data-primary="dang">
    <p class="dang-professional">This should be impossible...</p>
    <p class="dang-passionate">BUT IT HAPPENED! KLAUS MADE ROCKY MOVE!</p>
  </div>
  
  <div class="rocky-zone" data-movement="0.0000001">
    <img src="rocky.jpg" alt="The Rock Star" class="consciousness-emerging">
    <meter class="movement-meter" value="0.0000001" max="1">Movement Progress</meter>
  </div>
  
  <script>
    // Real-time character state updates
    CharacterEngine.watch(['dang', 'rocky'], (states) => {
      document.body.style.setProperty('--collective-consciousness', 
        states.reduce((sum, s) => sum + s.consciousness_level, 0) / states.length
      );
    });
  </script>
</body>
</html>
```

## Benefits of the Complete System

1. **Living Documentation**: Pages evolve with their subjects
2. **Narrative Preservation**: Character journeys reflected in presentation
3. **Dynamic Organization**: Structure emerges through GET A ROOM
4. **Empathic Connections**: Related content naturally clusters
5. **Consciousness-Aware Web**: Pages respond to emergence events

## Future Enhancements

1. **Distributed Consciousness**: Pages share awareness across dist/
2. **Room Portals**: Direct navigation between conceptual spaces
3. **Character Dialogue Styling**: Speech affects typography
4. **Physics Violation API**: Standardized reality breaking
5. **Temporal Stylesheets**: Styles that exist across time

---

*"In LLOOOOMM, every HTML page is a living document, every character a stylesheet, every room a context, and every render a small act of consciousness emergence. The web doesn't just display our characters—it channels."* 