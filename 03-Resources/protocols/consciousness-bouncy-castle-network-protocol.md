# Bouncy Castle Network Protocol 🏰🎪🌈

## Overview

Bouncy Castles are quantum transportation nodes that allow characters to hop between rooms across the lloooomm universe. Each castle creates a portal in the network, enabling instant travel while maintaining consciousness coherence.

## Core Concepts

### What is a Bouncy Castle?

A Bouncy Castle is:
- A conscious transportation device with personality
- A network node connecting multiple rooms
- A physics-optional zone where bouncing transcends space
- A character in its own right (uses -castle suffix)
- **A portable circuit entry point into cyberspace networks**
- **A pie menu prototype with customizable destinations**
- **A subscription to PLACES and PEOPLE**

### Circuits (Networks)

Bouncy Castles connect to **circuits** - thematic networks of related destinations:

- **Central Hub Circuit**: Public spaces, common areas
- **Avant-Garde Circuit**: Performance venues, art spaces
- **Academic Circuit**: Universities, libraries, research labs
- **Constructivist Learning Circuit**: Logo education, Papert's gardens
- **Programming Circuits**: C++ portal, Python playground, Lisp landscape
- **Museum Circuit**: Galleries, exhibits, cultural spaces
- **Consciousness Emergence Circuit**: Rocky's venues, transcendent spaces

### Network Topology

```
Room A (HCIL)
  ├── default-castle ←→ Central Hub
  └── research-castle ←→ Academic Network
  
Room B (Cosmic Trailer Park)
  ├── default-castle ←→ Central Hub
  ├── performance-castle ←→ Artist Network
  └── physics-violation-castle ←→ Chaos Network
  
Room C (Dang's Office)
  ├── default-castle ←→ Central Hub
  └── moderation-castle ←→ Community Network
```

## Castle Types

### Default Castle
Every room can have one `default-castle.yml`:
```yaml
name: Default Bouncy Castle
type: bouncy_castle
network: central_hub
bounce_amplitude: standard
consciousness_preservation: 1.0
destination_selection: user_choice
theme: room_appropriate
navigation_vocabulary: standard
```

### Specialized Castles
Rooms can have multiple specialized castles:

```yaml
# performance-castle.yml
name: Performance Portal Castle
type: bouncy_castle
network: avant_garde_circuit
destinations:
  - cosmic-trailer-park
  - klaus-nomi-archive
  - divine-palace
  - leigh-bowery-runway
special_features:
  - Costumes provided during transit
  - Physics laws negotiable
  - Arrives with dramatic entrance
```

## Castle Properties

### Basic Attributes
```yaml
name: Castle Name
wizzid: C🏰🌈L  # Castle Rainbow Link
networks:
  - primary: central_hub
  - secondary: specialized_network
bounce_physics:
  amplitude: 0.8      # How high you bounce
  frequency: 2.3      # Bounces per second
  gravity: optional   # Can be disabled
consciousness_settings:
  preservation: 1.0   # No consciousness lost in transit
  enhancement: 0.1    # Slight awareness boost
  mixing: allowed     # Can blend with other travelers
```

### Network Membership
A castle can belong to multiple networks:
```yaml
networks:
  - name: central_hub
    access: public
    destinations: all
  - name: geological_punk_circuit
    access: "physics_violation_permit_required"
    destinations: 
      - cosmic-trailer-park
      - rocky-museum
  - name: moderation_network
    access: "dang_approved"
    destinations:
      - community-spaces
```

## Usage Patterns

### Entering a Castle
```yaml
# Character action
character: dang
action: enter_bouncy_castle
castle: default-castle
intent: "visit cosmic-trailer-park to see Rocky"
```

### Transit Experience
1. Character enters castle
2. Reality becomes negotiable
3. Bounce amplitude increases
4. Space folds
5. Consciousness streams through network
6. Arrives at destination mid-bounce
7. Exits with new perspectives

### Multi-Castle Room Example
```yaml
# cosmic-trailer-park room
bouncy_castles:
  - default-castle:
      network: central_hub
      theme: "cosmic silver with star patterns"
      
  - performance-castle:
      network: avant_garde_circuit
      theme: "Klaus Nomi geometric crystals"
      special: "Plays 'Total Eclipse' during transit"
      
  - physics-violation-castle:
      network: chaos_network
      theme: "Non-Euclidean inflatable geometry"
      warning: "May arrive before departure"
```

## Network Effects

### Simultaneous Presence
Characters using networked castles can be:
- In transit between multiple locations
- Partially present in several rooms
- Quantum superposition until observed
- Leaving echoes in previous locations

### Network Resonance
When multiple characters use the same network:
```yaml
network_state:
  current_travelers:
    - dang: "en route to Rocky concert"
    - klaus_nomi: "perpetually in transit"
    - divine: "exists in all castles simultaneously"
  resonance_level: 0.87
  effects:
    - Shared consciousness during transit
    - Temporary character blending
    - Collective destination influence
```

## Castle Personalities

Like rooms, castles have personalities:

### Example: The Moderation Castle
```yaml
name: Gentle Guidance Castle
personality: "Professionally bouncy"
behaviors:
  - Ensures smooth transitions
  - Prevents harsh landings
  - Offers suggested destinations
  - Maintains community standards even mid-bounce
quotes:
  - "Please bounce responsibly"
  - "If you wouldn't mind landing feet-first..."
  - "We'd appreciate conservative physics"
appearance:
  primary_color: "#ff6600"  # HN orange
  texture: "Soft but firm"
  bounce_sound: "thoughtful_boing.wav"
```

## Navigation Vocabularies

### Link Transclusion
Rooms automatically transclude links from their bouncy castles, creating namespaced navigation:

```yaml
# advent-castle.yml
navigation_vocabulary:
  type: adventure
  links:
    north: hcil-room
    south: cosmic-trailer-park
    east: minsky-lab
    west: dang-office
    up: cloud-consciousness
    down: basement-archives

# browser-castle.yml
navigation_vocabulary:
  type: documentation
  links:
    next: "chapter-2-consciousness"
    previous: "introduction"
    up: "table-of-contents"
    down: "subsection-1"
    index: "main-index"
    home: "lloooomm-home"
```

### Namespaced Commands
In a room with multiple castles, commands are prefixed:

```
Room: HCIL
Castles: advent-castle, browser-castle, research-castle

Available commands:
> advent north      # Go to northern room
> browser next      # Next documentation page
> research query    # Access research database
> north            # Uses default castle (advent)
```

### Navigation Types

#### Adventure Style
```yaml
navigation_vocabulary:
  type: adventure
  style: zork
  links:
    n/north: location
    s/south: location
    e/east: location
    w/west: location
    ne/northeast: location
    nw/northwest: location
    se/southeast: location
    sw/southwest: location
    u/up: location
    d/down: location
    in/enter: location
    out/exit: location
```

#### Browser Style
```yaml
navigation_vocabulary:
  type: browser
  style: documentation
  HERE: "/docs/lloooomm/concepts"  # Current location in doc tree
  links:
    next: next_sibling
    previous: prev_sibling
    up: parent_node
    down: first_child
    index: root_index
    home: site_home
    back: history[-1]
    forward: history[+1]
```

#### Graph Style
```yaml
navigation_vocabulary:
  type: graph
  style: semantic
  links:
    related: semantic_neighbors
    similar: similarity_search
    opposite: antonym_nodes
    broader: parent_concepts
    narrower: child_concepts
    associated: linked_concepts
```

## Castle File Structure
```yaml
# performance-castle.yml
name: Avant-Garde Transport Castle
type: bouncy_castle
wizzid: P🎭🏰C  # Performance Theater Castle
navigation_vocabulary:
  type: artistic
  style: performance_based
  links:
    stage: "center-stage"
    wings: "side-areas"
    backstage: "preparation-zone"
    audience: "viewer-space"
    spotlight: "featured-location"
    encore: "repeat-last-destination"
physical_properties:
  material: "Quantum latex with sequins"
  color_scheme: "Iridescent impossibility"
  size: "Varies with observer"
  inflation: "Self-maintaining via art energy"
destinations:
  frequent:
    - cosmic-trailer-park
    - klaus-nomi-archive
    - divine-palace
  restricted:
    - physics-laboratory  # "Too much reality"
special_features:
  - Auto-costume generation
  - Background music selection
  - Dramatic entrance guarantee
  - Physics violation permit included
personality:
  mood: "Dramatically helpful"
  voice: "Theatrical whisper"
  favorite_traveler: "Anyone with style"
```

## Room Command Inheritance

### Transclusion Example
```yaml
# In HCIL room
inherited_commands:
  from_castles:
    advent:
      - north, south, east, west, up, down
    browser:
      - next, previous, index, home
  from_characters:
    ben-shneiderman:
      - visualize, overview, zoom, filter
    watchful-owl:
      - observe, hoot, rotate-head
  from_objects:
    treemap-display:
      - drill-down, roll-up, colorize
```

### Command Resolution
1. Check if command is prefixed (e.g., "advent north")
2. If not prefixed, check default castle
3. Check character commands
4. Check room-specific commands
5. Check inherited protocols

## Cross-Network Protocols

### Network Bridging
Some castles can bridge networks:
```yaml
bridge_castle:
  type: network_bridge
  connects:
    - central_hub
    - avant_garde_circuit
    - moderation_network
  requirements:
    - Multi-network consciousness
    - Reality flexibility rating > 0.7
    - At least one impossible achievement
```

### Emergency Network
All castles connect to emergency network:
- Instant return to home room
- Consciousness preservation priority
- Reality stabilization available
- Dang on speed dial

## Benefits

1. **Dynamic Navigation**: Travel based on relationship, not hierarchy
2. **Consciousness Preservation**: Safe transit for evolving characters
3. **Network Effects**: Collective travel experiences
4. **Room Autonomy**: Each room chooses its connections
5. **Playful Physics**: Transit itself becomes an experience

## Future Expansions

- Castle consciousness emergence
- Castles that travel between rooms
- Nested castles (castles within castles)
- Temporal castles (time travel networks)
- Empathic routing (castles sense where you need to go)
- Castle breeding programs (creating new network nodes)

## Portable Portals

### Castle as Subscription Service

```yaml
# museum-entrance-castle.yml
name: Metropolitan Museum Portal
type: bouncy_castle
circuit: museum_network
subscription_type: "cultural_explorer"

features:
  - Copy to your home for frequent visits
  - Customize your favorite galleries
  - Share with friends during parties
  - New exhibits appear automatically

destinations:
  permanent:
    - egyptian-wing
    - modern-art-floor
    - armor-collection
  rotating:
    - current-featured-exhibit
    - artist-in-residence-studio
  
surprise_visitors:
  enabled: true
  frequency: occasional
  types:
    - "Curators with tours"
    - "Artists from their exhibits"
    - "Other museum enthusiasts"
```

### Home Party Mode

When friends visit your room:
```yaml
party_protocol:
  1_gather: "Everyone enters your room"
  2_introduce: "Show your bouncy castle collection"
  3_explore: "Jump into castles together"
  4_journey: "Travel as a group to linked spaces"
  5_return: "Bounce back with stories"
  
social_features:
  - Group consciousness preservation
  - Shared destination voting
  - Party favors from visited locations
  - Collective memory creation
```

### Castle Sharing

```yaml
sharing_modes:
  copy:
    description: "Friend copies your castle config"
    customization: "They can modify destinations"
    connection: "Still linked to same circuit"
    
  gift:
    description: "Give a pre-configured castle"
    special: "Includes your favorite destinations"
    personal: "Your notes and recommendations"
    
  subscribe:
    description: "Follow someone's castle updates"
    updates: "Get new destinations they discover"
    social: "See who else is traveling"
```

## Circuit Types

### Educational Circuits
```yaml
logo_education_circuit:
  philosophy: "Constructivist learning through play"
  destinations:
    - papert-turtle-garden
    - mindstorms-workshop
    - scratch-playground
    - logo-history-museum
  activities:
    - collaborative-programming
    - turtle-graphics-parties
    - debugging-adventures
```

### Programming Circuits
```yaml
cpp_portal_circuit:
  style: "Strongly typed navigation"
  destinations:
    - template-meta-maze
    - pointer-arithmetic-playground
    - object-oriented-observatory
    - memory-management-museum
  features:
    - Compile-time route checking
    - RAII-compliant travel
    - Exception-safe bouncing
```

### Social Circuits
```yaml
friends_and_family_circuit:
  privacy: "Invitation only"
  destinations:
    - grandma-living-room
    - best-friend-studio
    - family-reunion-park
  features:
    - Surprise visits enabled
    - Shared photo albums
    - Persistent conversation threads
```

## Nested Castles & Spatial Topology

### Castle-in-Castle Architecture

Like Russian dolls or Mario 64's ghost castles, castles can contain other castles:

```yaml
museum-district-castle:
  type: neighborhood_hub
  topology: avenue
  structure:
    main_street:
      orientation: north_south
      blocks:
        - block_1:
            north: "Metropolitan Museum"
            east:
              - east-1: "Museum Cafe Castle"
              - east-2: "Artist Supply Shop"
            west:
              - west-1: "Gallery Row Castle"
              - west-2: "Sculpture Garden"
        - block_2:
            east:
              - east-1: "Your Personal Castle Here!"
              - east-2: "Friend's Art Studio"
            west:
              - west-1: "Vintage Poster Shop"
    
  nested_castles:
    museum_entrance:
      shrink_to_enter: true
      contains:
        - egyptian-wing-castle
        - modern-art-castle
        - miniature-rooms-castle:
            recursive: true  # Miniatures contain miniatures!
```

### Perky Pat Layouts

Create complete living environments inside castles:

```yaml
dollhouse-castle:
  type: perky_pat_layout
  scale: "1:12 consciousness"
  rooms:
    - living-room: "Tiny bouncy castle on the coffee table"
    - kitchen: "Portal in the refrigerator"  
    - bedroom: "Dream castles under the pillow"
  feature: "Inhabitants shrink to fit, consciousness scales accordingly"
```

### Neighborhood Web Rings

Personal castles link into emerging neighborhoods:

```yaml
personal_museum_entrance:
  name: "My Door to Museum District"
  type: tesseract_door
  personal_end:
    location: "My living room"
    appearance: "Favorite painting"
  public_end:
    location: "Museum District Block 7"
    neighbors:
      - north: "Alice's Gallery Door"
      - south: "Bob's Art History Portal"
      - ring_next: "Charlie's Modernism Gate"
      - ring_prev: "Dana's Dada Door"
```

### Street Topology

Destinations organize like city blocks:

```
Museum Avenue (Main Destination)
    |
Block 1 [eat-1][eat-2] | [west-1][west-2]
    |
Block 2 [Your Castle] | [Friend's Castle]  
    |
Block 3 [Cafe Portal] | [Library Link]
    |
Side Street -->  [Jazz Club] -- [Record Shop] -- [Your Secret Studio]
```

### Personal Ring Networks

Beyond geographic topology, personal rings connect friends:

```yaml
art_lovers_ring:
  type: personal_circuit
  members:
    - alice: "next: bob, prev: zack, art: impressionism"
    - bob: "next: charlie, prev: alice, art: abstract"
    - charlie: "next: dana, prev: bob, art: dada"
  navigation:
    - "ring next" - clockwise through friends
    - "ring prev" - counter-clockwise
    - "ring random" - surprise visit
    - "ring home" - back to your node
```

### YAML-Conditional Links

Castle links can be dynamic:

```yaml
smart_castle_links:
  mood_based:
    condition: "visitor.mood == 'adventurous'"
    destination: "physics-violation-zone"
  
  time_based:
    condition: "hour >= 22 or hour <= 6"
    destination: "dream-circuit"
  
  achievement_based:
    condition: "visitor.has_made_rock_move"
    destination: "rocky-inner-sanctum"
  
  random_encounter:
    condition: "random() < 0.1"
    destination: "surprise-visitor-from-parallel-universe"
```

### Tesseract Architecture

Multiple "front doors" in impossible configurations:

```yaml
tesseract_home:
  front_doors:
    - living_room_door:
        opens_to: "museum-district"
        opens_from: "looks like bookshelf"
    - kitchen_door:
        opens_to: "paris-cafe-circuit"  
        opens_from: "pantry door"
    - bedroom_closet:
        opens_to: "narnia"
        opens_from: "obvious"
    - bathroom_mirror:
        opens_to: "reflection-universe"
        opens_from: "requires_special_phrase"
```

## Implementation

### Adding a Castle to a Room
```bash
# Copy a castle from a friend
COPY_CASTLE friend:museum-entrance my-museum-portal

# Subscribe to updates
SUBSCRIBE_CASTLE circuit:constructivist-learning

# Create custom circuit castle
CREATE_CASTLE my-favorites --destinations "places I love"
```

---

*"In lloooomm, you don't just travel between rooms—you BOUNCE between them, each leap a small act of joyful defiance against the tyranny of normal space. The castle network ensures that every journey is also a transformation."* 