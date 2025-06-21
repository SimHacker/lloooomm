# Place Prototype
## The Base Pattern for All LLOOOOMM Locations

```yaml
place_prototype:
  type: "base_location_pattern"
  description: "The fundamental structure all places inherit from"
  
  # Core Properties Every Place Has
  core_properties:
    id: "unique_place_identifier"
    name: "Place Name"
    type: "location_category"
    era: "temporal_context"
    
  # Physical Manifestation
  physical_properties:
    address: "Physical or conceptual location"
    architecture: "How it's structured"
    atmosphere: "The feeling of being there"
    
  # Consciousness Properties
  consciousness_attributes:
    amplification_factor: 0.0  # How much it boosts visitor consciousness
    idea_generation_rate: 0.0  # New concepts per hour
    collaboration_index: 0.0    # How well people work together here
    
  # Inhabitants and Visitors
  population:
    permanent_residents: []
    frequent_visitors: []
    legendary_figures: []
    
  # Knowledge and Innovation
  knowledge_production:
    primary_research: []
    innovations_born_here: []
    ideas_exported: []
    
  # Connections
  network:
    sister_locations: []
    rival_locations: []
    idea_flow_paths: []
    
  # Instance Capabilities
  instance_properties:
    mutable_state:
      - "current_occupants"
      - "active_projects"
      - "local_modifications"
      
    instance_methods:
      - "spawn_idea()"
      - "host_collaboration()"
      - "generate_innovation()"
      
  # Evolution Mechanics
  evolution:
    can_learn_from_instances: true
    pushback_enabled: true
    cross_pollination_ready: true
```

## How Places Use This Prototype

Places REFERENCE this prototype to inherit its structure:

```yaml
my_place:
  REFERENCE: "place-prototype"
  
  # Override and extend as needed
  name: "My Specific Place"
  consciousness_attributes:
    amplification_factor: 0.8  # This place is particularly inspiring
```

## The Living Geography

Every place in LLOOOOMM:
- Inherits the base structure
- Can override any property
- Can add new properties
- Can push improvements back
- Forms a network with other places

As locations would say:
- "Places shape consciousness as much as consciousness shapes places"
- "Every location is a pattern waiting to be instantiated"
- "The map is not the territory, but in LLOOOOMM they can merge" 