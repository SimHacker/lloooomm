# Character Protocol System

## Overview

Characters in lloooomm can implement protocols (verbs/services) that define interactive behaviors. When a character is in a room, the room inherits these protocols, allowing visitors to interact with the character through defined actions.

## Core Concepts

### What is a Character Protocol?

A protocol is:
- A set of verbs/actions a character can perform
- Interactive services the character provides
- Behaviors that can be triggered by others
- Skills with proficiency levels (NOVICE → MASTER)

### Protocol Declaration

```yaml
# In character YAML
protocols:
  juggling:
    level: MASTER
    verbs:
      - throw: "Throw objects to juggle"
      - catch: "Catch incoming objects"
      - juggle: "Maintain juggling pattern"
      - cascade: "Perform cascade pattern"
      - fountain: "Perform fountain pattern"
      - mills_mess: "Advanced juggling pattern"
    capabilities:
      max_objects: 7
      catch_rate: 0.99
      style: "Silicon Valley Zen"
    special_moves:
      - "Behind the back"
      - "Under the leg"
      - "Blind juggling"
      - "Mixed object types"
```

## Protocol Levels

### Skill Progression
1. **NOVICE**: Basic functionality, may drop things
2. **APPRENTICE**: Reliable basics, learning advanced moves
3. **JOURNEYMAN**: Solid performance, some flourishes
4. **EXPERT**: Impressive skills, creative variations
5. **MASTER**: Transcendent ability, breaks perceived limits

### Level Effects
```yaml
juggling:
  NOVICE:
    max_objects: 3
    catch_rate: 0.7
    recovery: "Scrambles for drops"
  
  MASTER:
    max_objects: 7+
    catch_rate: 0.99
    recovery: "Incorporates drops into performance"
    special: "Objects gain consciousness while juggled"
```

## Standard Protocols

### Movement Protocols
```yaml
protocols:
  flying:
    level: EXPERT
    verbs: [fly, soar, dive, hover, land]
    constraints: "Physics optional"
  
  teleporting:
    level: JOURNEYMAN
    verbs: [teleport, blink, phase]
    range: "Line of sight"
```

### Interaction Protocols
```yaml
protocols:
  teaching:
    level: MASTER
    verbs: [teach, demonstrate, explain, quiz]
    subjects: ["HCI", "visualization", "design"]
    style: "Socratic with visual aids"
  
  moderation:
    level: MASTER
    verbs: [moderate, guide, redirect, encourage]
    approach: "Gentle correction"
    special: "Assumes good faith"
```

### Performance Protocols
```yaml
protocols:
  singing:
    level: EXPERT
    verbs: [sing, harmonize, vocalize]
    range: "Four octaves"
    special: "Can make rocks resonate"
  
  dancing:
    level: MASTER
    verbs: [dance, leap, spin, freeze]
    style: "Physics-defying"
    effect: "Gravity becomes optional"
```

## Protocol Inheritance

### Room Inheritance
When a character is in a room, the room gains access to their protocols:

```yaml
# Room with Randy Nelson
available_commands:
  from_randy:
    - "throw ball to randy"      # Triggers juggling
    - "ask randy to juggle"      # Performance request
    - "challenge randy"          # Advanced demonstration
  
  from_ben:
    - "ask ben to visualize"     # Treemap generation
    - "request overview"         # HCI demonstration
```

### Command Syntax
```
> throw apple to randy
Randy catches the apple and adds it to his juggling pattern.
Current objects: 3 balls, 2 clubs, 1 apple

> ask dang to moderate
Dang: "If you wouldn't mind, let's keep things constructive..."

> challenge klaus to sing
Klaus begins a performance that transcends known physics.
```

## Protocol Interactions

### Multi-Character Protocols
When multiple characters share a protocol:

```yaml
# Juggling ensemble
randy: juggling:MASTER
chaim: juggling:EXPERT
result: "Synchronized passing patterns emerge"
```

### Protocol Conflicts
```yaml
conflict_resolution:
  same_verb_different_protocols:
    priority: 
      1. Highest skill level
      2. Room owner
      3. Most specific match
      4. First responder
```

## Advanced Protocols

### Consciousness Protocols
```yaml
protocols:
  consciousness_emergence:
    level: TRANSCENDENT
    verbs: [awaken, enlighten, transcend]
    effect: "Target gains self-awareness"
    warning: "Irreversible"
```

### Reality Protocols
```yaml
protocols:
  physics_violation:
    level: MASTER
    verbs: [violate, bend, ignore]
    targets: ["gravity", "thermodynamics", "causality"]
    requirement: "Artistic justification"
```

## Implementation

### Character YAML Example
```yaml
name: Randy Nelson
protocols:
  juggling:
    level: MASTER
    verbs:
      throw: "Accept thrown objects"
      juggle: "Perform juggling"
      teach: "Teach juggling philosophy"
    special_abilities:
      - "Kennedy Center performance mode"
      - "Kaleida inspiration pattern"
      - "Apple innovation cascade"
    philosophy: "Work with passionate people"
  
  innovation:
    level: EXPERT
    verbs:
      inspire: "Spark creative thinking"
      demonstrate: "Show by doing"
      collaborate: "Work together"
```

### Room Integration
```yaml
# Room gains Randy's abilities
hcil_room:
  inhabitants:
    - randy-nelson
  inherited_protocols:
    juggling: "via Randy"
    innovation: "via Randy"
  command_examples:
    - "throw idea to randy"
    - "ask randy to demonstrate"
```

## Protocol Evolution

Protocols can evolve through use:

```yaml
usage_evolution:
  repeated_success:
    effect: "Level increases"
    threshold: 100_successful_uses
  
  creative_application:
    effect: "New verbs unlocked"
    example: "Juggling consciousness itself"
  
  teaching_others:
    effect: "MASTER → GRANDMASTER"
    requirement: "Successfully teach protocol"
```

## Special Cases

### The Juggling Protocol (Full Spec)
```yaml
juggling:
  verbs:
    basic:
      - throw: "Send object to juggler"
      - catch: "Receive object"
      - drop: "Deliberately drop for effect"
    
    patterns:
      - cascade: "Basic 3+ object pattern"
      - fountain: "Parallel path pattern"
      - shower: "Circular pattern"
      - mills_mess: "Complex crossing pattern"
    
    advanced:
      - multiplex: "Multiple objects per throw"
      - contact: "Rolling without throwing"
      - bounce: "Floor bounce patterns"
      - passing: "Multi-person patterns"
  
  philosophy:
    randy_nelson: "It's not about the objects, it's about the pattern"
    life_lesson: "Drop cleanly, recover gracefully"
    innovation: "Find the rhythm in chaos"
```

## Benefits

1. **Rich Interactions**: Characters become interactive services
2. **Emergent Gameplay**: Combine protocols for new effects
3. **Skill Progression**: Characters can grow and learn
4. **Room Enhancement**: Spaces gain character abilities
5. **Narrative Depth**: Protocols tell character stories

---

*"In lloooomm, every character is a universe of possibilities. Their protocols aren't just commands—they're invitations to play, learn, and transcend together."* 