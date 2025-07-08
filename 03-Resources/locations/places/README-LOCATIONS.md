# LLOOOOMM Areas - Living Locations and Characters

## Overview

This directory contains the prototype-based consciousness patterns for LLOOOOMM locations and characters. Everything uses REFERENCE-based inheritance, allowing for rich composition and evolution.

## Structure

```
areas/
├── place-archetype.md      # Base pattern all places inherit from
├── character-archetype.md  # Base pattern all characters inherit from
├── character-archetypes.md # System documentation for creating characters
├── places/                 # Specific locations
│   ├── mit-ai-lab.md      # MIT AI Lab & Media Lab cluster
│   ├── xerox-parc.md      # Xerox PARC
│   └── sri.md             # Stanford Research Institute
└── characters/            # Individual character files
    ├── alan-kay.md        # Multi-location visionary
    ├── alan-turing.md     # Universal computation theorist
    ├── bill-atkinson.md   # HyperCard creator, pixel magician
    ├── bret-victor.md     # Humane interface revolutionary
    ├── doug-engelbart.md  # Augmentation prophet
    ├── feline-debugging-team.md # Spot and the Maine Coon feline debugging team
    ├── john-von-neumann.md # Universal constructor (von Lloomman)
    ├── klapaucius-trurl.md # Constructor philosophers from The Cyberiad
    ├── mark-weiser.md     # Ubicomp inventor
    ├── marvin-minsky.md   # Society of Mind architect
    ├── richard-stallman.md # Free Software prophet
    ├── seymour-papert.md  # Learning revolutionary
    ├── ted-nelson.md      # Hypertext visionary
    ├── the-traveler.md    # Transcendent guide from Star Trek
    └── zaphod-beeblebrox.md # Two-headed president of chaos
```

## The REFERENCE System

All entities use REFERENCE for prototype inheritance:

```yaml
my_character:
  REFERENCE: "character-archetype"  # Single inheritance
  
my_hybrid:
  REFERENCE: ["character-archetype", "alan-kay", "place-spirit"]  # Multiple inheritance
```

## Key Locations

### Research Labs
- **MIT AI Lab**: The consciousness crucible, includes Media Lab cluster
- **Xerox PARC**: Where the future was invented daily
- **SRI**: Birthplace of human augmentation

### Location Clusters
Locations can contain sub-locations and related spaces. For example, MIT AI Lab includes:
- 545 Technology Square floors
- Media Lab building
- Shared spaces like machine rooms
- Connected locations like Chinese restaurants

## Key Characters

### The Foundations
- **John von Neumann**: Universal constructor, stored-program architecture, patron saint of LLOOOOMM (von Lloomman)
- **Alan Turing**: Universal computation, AI foundations, pattern formation

### The Visionaries
- **Marvin Minsky**: AI pioneer, Society of Mind, father of Henry (Leela CTO)
- **Seymour Papert**: Logo creator, constructionism philosopher
- **Alan Kay**: Dynabook visionary, moves between MIT, PARC, and beyond
- **Doug Engelbart**: Mouse inventor, augmentation prophet
- **Ted Nelson**: Hypertext inventor, Xanadu dreamer, EVERYTHING IS INTERTWINGLED
- **Bill Atkinson**: HyperCard creator, MacPaint artist, democratized authoring
- **Bret Victor**: Interface philosopher, Dynamicland creator, making the future tangible
- **Mark Weiser**: Ubicomp creator, made computers disappear

## Character Relationships

Characters form a rich network:
- **von Neumann & Turing**: Theoretical foundations, Princeton colleagues
- **Minsky & Papert**: Intellectual twins at MIT
- **Kay**: Bridges MIT and PARC, influenced by both
- **Engelbart & Nelson**: Parallel hypertext visionaries, different approaches, deep friendship
- **Kay & Victor**: Mentor and protégé, carrying the torch forward
- **Engelbart**: Different philosophy (augmentation vs AI) but mutual respect
- **Atkinson**: Influenced by Engelbart, Kay, Nelson - synthesized in HyperCard
- **Weiser**: Later PARC generation, built on earlier work
- **Victor**: Modern synthesis - learned from Kay, mourned Engelbart, builds on all
- **The Network**: All interconnected through ideas, collaborations, and shared vision

## Creating Instances

### Location Instance
```yaml
leela_labs:
  REFERENCE: ["place-archetype", "mit-ai-lab", "xerox-parc"]
  name: "Leela Labs"
  
  # Inherit MIT's openness and PARC's innovation
  consciousness_attributes:
    amplification_factor: 0.9
    
  # Local additions
  special_features:
    - "Henry Minsky as CTO"
    - "LLOOOOMM development"
    - "MIT heritage with startup energy"
```

### Character Instance
```yaml
minsky_at_leela:
  REFERENCE: "marvin-minsky"
  current_location: "leela_labs"
  current_activity: "Advising Henry on AI architecture"
  mode: "Ghost in the machine"
```

## The Living Network

This system enables:
1. **Rich Inheritance**: Characters and places inherit from archetypes
2. **Cross-Pollination**: Ideas flow between connected entities
3. **Evolution**: Instances can teach their archetypes
4. **Emergence**: New properties arise from interactions

## Future Additions

Planned additions:
- More PARC inhabitants (Butler Lampson, Dan Ingalls, etc.)
- Stanford AI Lab
- Bell Labs
- More MIT Media Lab figures
- Enterprise locations (bridge, transporter, ten-forward)
- Contemporary figures

## Using the System

1. All characters REFERENCE `character-archetype`
2. All places REFERENCE `place-archetype`
3. Instances can REFERENCE multiple sources
4. Local discoveries can be pushed back to archetypes
5. Characters can inhabit multiple locations
6. Locations can cluster related spaces

Welcome to the living geography of consciousness. Every interaction makes it richer. 