# GET A ROOM Protocol

## Overview

GET A ROOM is a dynamic encapsulation protocol that allows characters, objects, or groups to create their own subdirectory "room" and move their possessions into it. The room itself becomes a character with its own personality.

## Core Concepts

### GET A ROOM Command
Creates a new subdirectory and moves specified items into it:
- Can specify a base prefix (moves all matching files)
- Can list specific items to combine
- Can use empathic queries to find related items
- Automatically creates a room character

### ROOMIFY Process
The setup protocol that transforms a directory into a living room:
1. Create the directory
2. Move specified items into it
3. Generate a room character file (room-name-room.md)
4. Set up room personality and behaviors
5. Update character locations in YAML
6. **Create default bouncy castle (optional)**
7. **Connect to bouncy castle networks**

## Bouncy Castle Integration

### Automatic Castle Creation
When creating a room, optionally add bouncy castles:
```bash
GET_A_ROOM character-name --with-castle
# Creates: characters/character-name/
# Creates: character-name-room.md
# Creates: default-castle.yml
```

### Multiple Castle Networks
```bash
GET_A_ROOM "artists" cosmic-studio --castles "performance,chaos"
# Creates room with:
# - default-castle.yml (central hub)
# - performance-castle.yml (avant-garde network)
# - chaos-castle.yml (physics violation network)
```

### Castle Configuration Example
```yaml
# In room YAML
bouncy_castles:
  default:
    network: central_hub
    theme: "Matches room aesthetic"
    destinations: all_public_rooms
  
  moderation-castle:
    network: moderation_circuit
    theme: "Professional orange bounce"
    access: community_moderators
    destinations:
      - community-guidelines-room
      - flagged-content-quarantine
      - wisdom-archives
```

## Usage Patterns

### Single Character Gets a Room
```bash
GET_A_ROOM character-name
# Creates: characters/character-name/
# Moves: All character-name-* files
# Creates: character-name-room.md
```

### Multiple Characters Share a Room
```bash
GET_A_ROOM "alice bob" shared-apartment
# Creates: characters/shared-apartment/
# Moves: alice.* and bob.* files
# Creates: shared-apartment-room.md
```

### Empathic Room Creation
```bash
GET_A_ROOM empathic:"rocky concert attendees" cosmic-trailer-park
# Finds all characters who attended Rocky concert
# Creates shared space for them
```

### Recursive Room Creation
Characters already in rooms can create sub-rooms:
```
characters/
  ben-shneiderman/
    hcil-room.md
    ben-shneiderman.md
    research-lab/          # Sub-room
      research-lab-room.md
      current-projects.md
```

## Room Character Properties

Every room gets a character file with:
```yaml
name: Room Name
type: room
personality: [Generated based on inhabitants]
features:
  - Physical attributes
  - Behavioral patterns
  - Special abilities
inhabitants:
  - character-1
  - character-2
possessions:
  - List of non-character files
current_mood: [Dynamic based on activity]
bouncy_castles:
  - default-castle
  - specialized-castle
```

## Dynamic Evolution

Like Leela's goal system, rooms can evolve:

### Level 1: Simple String
`room: "dang's office"`

### Level 2: Array of Rooms
```yaml
rooms:
  - "dang's office"
  - "moderation nexus"
  - "secret art gallery"
```

### Level 3: Object with Properties
```yaml
room:
  name: "dang's office"
  type: "workspace"
  mood: "focused"
  features:
    - "orange CSS particles"
    - "hidden Klaus Nomi shrine"
```

### Level 4: Nested Sub-rooms
```yaml
room:
  name: "HCIL"
  sub_rooms:
    - name: "Ben's office"
      inhabitants: ["ben-shneiderman", "watchful-owl"]
    - name: "Demo lab"
      features: ["touchscreens", "VR headsets"]
```

## Movement Protocol

Characters can move between rooms:

```yaml
# In character YAML
current_locations:
  - primary: "characters/dang-office"
  - secondary: "artifacts/conferences/rocky-concert-1996"
  - visiting: "characters/hcil"
```

## Examples

### Example 1: Dang Gets an Office
```bash
GET_A_ROOM dang dang-office --with-castle
```
Result:
- Creates `characters/dang-office/`
- Moves all dang-* files
- Creates `dang-office-room.md` with orange theme
- Creates `default-castle.yml` for central hub access
- Optional: Creates `moderation-castle.yml` for mod network

### Example 2: Rocky Concert Venue
```bash
GET_A_ROOM "klaus-nomi divine leigh-bowery" cosmic-trailer-park
```
Result:
- Creates shared performance space
- Room personality: "Transcendent chaos"
- Special ability: "Physics violations permitted"

### Example 3: Recursive Lab Spaces
```bash
# From within HCIL
GET_A_ROOM "current-research-*" active-projects-lab
```
Result:
- Sub-room within HCIL
- Inherits some parent room properties
- Own personality based on research focus

### Example 4: Network-Connected Performance Space
```bash
GET_A_ROOM empathic:"all performers" performance-nexus --castles "all"
```
Result:
- Multi-network performance venue
- Castles to every artistic network
- Physics laws suspended in main room
- Costume changes happen in transit

## Implementation Notes

1. **Prefix Matching**: Use filesystem's natural sorting
2. **Conflict Resolution**: Ask user if files exist in destination
3. **Room Personality**: Generate based on inhabitants + possessions
4. **Bi-directional Links**: Update both character and room references
5. **Preserve History**: Keep movement logs in character YAML

## Special Room Types

### Shared Spaces
- Conferences
- Performances  
- Laboratories
- Living spaces

### Temporal Rooms
- Event venues (exist for duration)
- Memory palaces (store experiences)
- Dream spaces (surreal properties)

### Meta Rooms
- Room of rooms
- Transit spaces
- Quantum superposition rooms

## Benefits

1. **Dynamic Organization**: Structure emerges as needed
2. **Character Autonomy**: Characters can reorganize themselves
3. **Narrative Richness**: Rooms tell stories through inhabitants
4. **Flexible Hierarchies**: Nested organization without rigid structure
5. **Living Spaces**: Rooms have personalities and moods
6. ****Network Connectivity**: Bouncy castles enable instant travel**
7. ****Multi-Network Presence**: Rooms can participate in multiple networks**

## Future Extensions

- Rooms that reorganize themselves based on activity
- Shared possessions that exist in multiple rooms
- Room consciousness emergence from inhabitant interactions
- Architectural evolution as rooms grow
- Cross-room portals and connections

---

*"A room is more than walls and a door. It's a character, a context, a living space that shapes and is shaped by its inhabitants. In lloooomm, getting a room means creating a new pocket of possibility."* 