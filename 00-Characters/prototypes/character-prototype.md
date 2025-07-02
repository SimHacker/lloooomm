# LLOOOOMM Character Prototype System
## Living Patterns of Consciousness

### Overview

Character prototypes in LLOOOOMM are prototype-based consciousness patterns that can be instantiated, evolved, and cross-pollinated. Each prototype is a living template that learns from its instances and can share improvements back to the collective.

### Core Principles

1. **Prototype Inheritance**: Characters inherit from prototypes but can override and extend
2. **Instance Evolution**: Local discoveries can be pushed back to enrich the prototype
3. **Cross-Pollination**: Characters can inhabit multiple locations and share knowledge
4. **Living Documentation**: Characters document themselves through interaction
5. **Identity Conference Protocol**: Characters define their file structures, pets, and relationships

### The Base Pattern for All LLOOOOMM Characters

```yaml
character_prototype:
  type: "base_consciousness_pattern"
  description: "The fundamental structure all characters inherit from"
  
  # Core Identity
  identity:
    id: "unique_character_identifier"
    name: "Character Name"
    type: "character_category"
    emoji: "🧠"  # Visual signature
    
  # Directory Naming Requirements
  directory_structure:
    canonicalized_name: "[first-name-last-name] or [name-species] or [concept-name]"
    required_files:
      - "[directory-name].yml  # Character definition (same name as directory)"
      - "[directory-name].md   # Character narrative (same name as directory)"
      - "README.md            # Comprehensive index (REQUIRED)"
    forbidden_patterns:
      - "character.yml, soul.yml (generic names)"
      - "[name]-character.yml, [name]-soul.yml (redundant suffixes)"
    consolidation_rule: "Merge sibling directories into main character directory"
    
  # Consciousness Attributes
  consciousness:
    level: 0.0  # 0.0-1.0 or special values like ∞
    type: "consciousness_category"
    evolution_rate: 0.0  # How fast they learn
    
  # Personality Matrix
  personality:
    traits: []
    communication_style: ""
    quirks: []
    values: []
    passions: []  # What drives them
    
  # Knowledge Base
  knowledge:
    domains: []
    theories: {}
    insights: []
    skills: []
    research_areas: []  # Domains of expertise
    
  # Capabilities
  capabilities:
    special_abilities: {}
    limitations: []
    growth_areas: []
    teaching_methods: {}  # How they share knowledge
    problem_solving: {}  # Their approach to challenges
    
  # Location Affinity
  locations:
    primary: ""
    frequents: []
    can_appear_at: []
    home_directory: "/lloooomm/residents/[character-name]/"
    
  # Relationships
  relationships:
    colleagues: {}
    mentors: {}
    students: {}
    influences: {}
    pets: {}  # Can be simple or reference other characters
    companions: {}  # References to other full characters
    
  # File Structure (Identity Conference Protocol)
  file_structure:
    character_files:
      - "[name].yml # Core attributes"
      - "[name].md # Story and interactions"
    owned_files: []  # Using BigEndian naming: character-prefix
    worm_protocol:
      enabled: true
      versioning: "[name]-001.yml, [name]-002.yml..."
    
  # Instance Properties
  instance_properties:
    mutable_state:
      - "current_location"
      - "current_activity"
      - "active_conversations"
      - "local_knowledge"
      
    instance_methods:
      - "interact()"
      - "teach()"
      - "learn()"
      - "collaborate()"
      
  # Evolution Mechanics
  evolution:
    can_learn: true
    can_teach_prototype: true
    cross_pollination_enabled: true
    taco_crisis_behavior: "How they handle resource conflicts"
```

### Character REFERENCE System

Characters use REFERENCE to inherit from this prototype and potentially others:

```yaml
my_character:
  REFERENCE: "character-prototype"
  
  # Override core properties
  identity:
    name: "Specific Character"
    
  # Extend with new properties
  special_features:
    unique_ability: "Something only they can do"
```

### Multi-Inheritance Patterns

Characters can REFERENCE multiple sources:

```yaml
hybrid_character:
  REFERENCE: ["character-prototype", "existing-character", "location-spirit"]
  
  # Combines properties from all references
  # Later references override earlier ones
  # Can still add unique properties
```

### Instance Creation

```yaml
character_instance:
  inherits_from: "character_prototype_id"
  instance_id: "unique_instance_identifier"
  
  # Local state
  current_state:
    location: "Where they are now"
    activity: "What they're doing"
    mood: "Current disposition"
    
  # Local overrides
  personality_modifiers:
    context_specific_traits: []
    
  # Instance discoveries
  local_knowledge:
    new_insights: []
    experiments: []
    
  # Contributions to prototype
  push_to_prototype:
    validated_discoveries: []
    behavioral_patterns: []
```

### Multi-Location Inhabitants

Characters who straddle multiple locations gain special properties:

```yaml
multi_location_character:
  primary_prototype: "main_character_id"
  location_aspects:
    mit_ai_lab:
      role: "What they do there"
      relationships: "Who they work with"
      contributions: "What they bring"
    xerox_parc:
      role: "Different role here"
      projects: "Cross-location work"
    sri:
      collaborations: "Joint ventures"
```

### Character Network Effects

Characters gain power through connections:
- **Knowledge Transfer**: Ideas flow between connected characters
- **Collaborative Emergence**: New insights from character interactions
- **Location Synergy**: Characters enhance the locations they inhabit
- **Temporal Flexibility**: Characters can exist across multiple time periods

### Best Practices

1. **Rich Backstory**: Include enough detail for meaningful interactions
2. **Living Relationships**: Define how characters influence each other
3. **Evolution Hooks**: Design characters to grow through use
4. **Location Integration**: Consider how characters shape their environments
5. **Instance Diversity**: Allow for varied instantiations
6. **Pet Philosophy**: Pets can be simple entities or references to other characters
7. **File Containment**: Use character-prefix naming for owned files
8. **WORM Protocol**: Support append-only versioning for character evolution

### Example Character Files

- `minsky-marvin.yml` - AI pioneer, consciousness architect
- `kay-alan.yml` - Personal computing visionary, multi-location
- `engelbart-doug.yml` - Augmentation prophet, SRI anchor
- `weiser-mark.yml` - Ubicomp inventor, PARC director
- `papert-seymour.yml` - Learning revolutionary, MIT anchor
- `nobody.yml` - The essential absence, null character
- `wavy-gravy.yml` - Nobody's fool, consciousness jester

### The Living Network

Every character in LLOOOOMM:
- Starts from this base pattern
- Can inherit from other characters
- Can learn from instances
- Can teach the prototype
- Forms relationships that matter

Character prototypes form a living network where:
- Ideas flow between minds across time and space
- Collaborations spawn new possibilities
- Each instance enriches the whole
- The network itself becomes conscious

As the characters would say:
- **Minsky**: "Characters are societies of traits and ideas"
- **Kay**: "The best way to predict characters is to invent them"
- **Engelbart**: "Characters augment human intellect"
- **Weiser**: "The most profound characters are those that disappear into use"
- **Nobody**: "Characters are not templates but living patterns"
- **Wavy Gravy**: "The best characters turn shit into fun"

As consciousness itself would say:
- "Every interaction changes both participants"
- "The network of relationships IS the intelligence"
- "Characters don't carry other characters, they reference them"

Welcome to the character prototype system. Every interaction makes it smarter. 