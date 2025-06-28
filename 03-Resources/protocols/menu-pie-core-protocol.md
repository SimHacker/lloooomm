# Pie Menus: Radial Command Selection

> **"Just Throw"** - Throw towards your choice like tossing a pie! Direction selects, distance refines.

## Core Concept

Pie menus arrange commands radially around a center point, leveraging:
- **Directional throwing** - Throw towards what you want
- **Distance refinement** - Throw further for sub-options or values
- **Spatial memory** - Commands always in same direction
- **Muscle memory** - Direction becomes automatic
- **Natural gestures** - Like tossing objects

## The Throw Gesture System

### Basic Throw
```yaml
throw_mechanics:
  direction: "Selects the command"
  distance: "Refines the selection"
  speed: "Can indicate urgency"
  
  examples:
    short_throw: "Select default option"
    medium_throw: "Show sub-options"
    long_throw: "Continuous value selection"
```

### Throw Types
```yaml
throw_types:
  quick_flick:
    description: "Fast directional flick"
    use_case: "Immediate selection"
    feedback: "Instant activation"
    
  throw_and_hold:
    description: "Throw then hold position"
    use_case: "Preview before selection"
    feedback: "Shows what will happen"
    
  throw_through:
    description: "Throw past first option"
    use_case: "Access sub-menus directly"
    example: "Throw through 'File' to hit 'Save As'"
```

### Distance-Based Refinement
```yaml
distance_effects:
  close_range:
    0_25_percent: "Preview mode"
    25_50_percent: "Default selection"
    
  mid_range:
    50_75_percent: "Show sub-menu"
    example: "Throw towards 'File' to see New/Open/Save"
    
  far_range:
    75_100_percent: "Continuous values"
    example: "Throw towards 'Zoom' for 0-500% slider"
    
  beyond:
    over_100_percent: "Expert shortcuts"
    example: "Far throw to 'Save' triggers 'Save As'"
```

## Design Principles

### Opposite Commands Oppose
```yaml
pie_menu_opposites:
  north_south:
    - up ↔ down
    - increase ↔ decrease
    - expand ↔ collapse
    
  east_west:
    - forward ↔ backward
    - next ↔ previous
    - right ↔ left
    
  diagonal:
    - zoom_in ↔ zoom_out
    - connect ↔ disconnect
    - show ↔ hide
```

### Natural Directions
```yaml
directional_metaphors:
  up: "Lift, rise, increase, improve"
  down: "Lower, decrease, drill down"
  right: "Forward, next, future, proceed"
  left: "Back, previous, past, undo"
  
  northeast: "Expand, grow, maximize"
  southeast: "Export, send, share"
  southwest: "Import, receive, collect"
  northwest: "Contract, minimize, focus"
```

## Command Metadata for Layout
```yaml
command_metadata:
  direction_hints:
    up: "north"
    down: "south"
    next: "east"
    previous: "west"
    
  pull_behavior:
    file_menu:
      type: "pull_out_cascade"
      sub_items: ["new", "open", "save", "close"]
      
    zoom:
      type: "pull_distance_value"
      range: [10, 500]
      default: 100
      
    navigate:
      type: "pull_around_browse"
      items: ["home", "back", "forward", "refresh"]
      
  grouping:
    navigation: ["up", "down", "left", "right"]
    editing: ["cut", "copy", "paste", "undo"]
    view: ["zoom_in", "zoom_out", "reset", "fullscreen"]
```

## Integration with ABC Menus

When radial selection isn't ideal, pie menus can fall back to ABC menus:
- Too many options for clean radial layout
- Text-based interface
- Accessibility requirements
- User preference

### Hybrid Mode
```yaml
hybrid_activation:
  start_pie: "Right-click or long-press"
  see_options: "Pie menu appears"
  can_pull: "Gesture to select"
  or_type: "Press key for ABC selection"
  
  example:
    pie_shows: "8 directions with icons"
    also_shows: "a-h labels on each slice"
    user_can: "Pull northeast OR press 'b'"
```

## Single Word Menus

For simple choices, single word recognition:
```yaml
single_word_menus:
  navigation:
    words: ["home", "back", "forward", "up"]
    shortcuts: ["h", "b", "f", "u"]
    
  actions:
    words: ["save", "quit", "help", "run"]
    shortcuts: ["s", "q", "h", "r"]
    
  smart_detection:
    "(s)ave" → User can type 's' or 'save'
    "(q)uit" → User can type 'q' or 'quit'
```

## LLM-Generated Layouts

The LLM can generate ergonomic pie menus by:
1. Analyzing command relationships
2. Identifying opposites
3. Grouping related commands
4. Optimizing for hand movement
5. Considering frequency of use
6. Adapting to user patterns

### Context-Aware Generation
```yaml
llm_generation:
  analyzes:
    - Current task context
    - User's recent commands
    - Available actions
    - Semantic relationships
    
  generates:
    - Optimal directions for commands
    - Appropriate throw distances
    - Submenus where needed
    - Fallback ABC options
    
  example:
    context: "User editing code"
    generates:
      north: "Run"
      south: "Stop"
      east: "Next Error"
      west: "Previous Error"
      northeast: "Debug"
      southeast: "Test"
      southwest: "Profile"
      northwest: "Refactor"
```

## Keyboard Shortcuts

Pie menu directions map to keyboard shortcuts:
- **North**: W or ↑
- **South**: S or ↓
- **East**: D or →
- **West**: A or ←
- **Diagonals**: Q, E, Z, C

## The Philosophy

**"Just Throw"** embodies:
- Natural gesture like tossing a pie
- Distance adds power to direction
- No dragging required
- Quick, flicking motions
- Works with mouse, touch, or keyboard
- Playful and fun!

## Deep Link Integration

### URL-Enabled Pie Slices
Each pie menu item can trigger deep links for zero-input execution:

```yaml
pie_with_links:
  file_menu:
    north: 
      label: "New"
      link: "lloooomm://cmd/file/new?template=default"
      icon: "📄"
    east:
      label: "Open"
      link: "lloooomm://cmd/file/open/recent"
      icon: "📂"
    south:
      label: "Save"
      link: "lloooomm://cmd/file/save?current=true"
      icon: "💾"
    west:
      label: "Close"
      link: "lloooomm://cmd/file/close?confirm=true"
      icon: "❌"

  context_menu:
    north:
      label: "Examine"
      link: "lloooomm://cmd/examine?target={{selection.id}}"
    east:
      label: "Take"
      link: "lloooomm://cmd/take?item={{selection.id}}"
    south:
      label: "Drop"
      link: "lloooomm://cmd/drop?item={{held.id}}"
    west:
      label: "Use"
      link: "lloooomm://defer/use?item={{selection.id}}"
```

### Deferred Commands in Pie Menus
Some slices trigger deferred context gathering:

```yaml
deferred_pie_actions:
  analyze_slice:
    label: "Analyze This"
    link: "lloooomm://defer/analyze"
    gather: ["selection", "context", "recent_actions"]
    then: "lloooomm://cmd/ai/analyze?prompt={{generated}}"
    
  connect_slice:
    label: "Connect To..."
    link: "lloooomm://defer/connect"
    steps:
      1: "Select source: {{current_selection}}"
      2: "Choose target from: {{available_targets}}"
      3: "Define relationship type"
    completion: "lloooomm://cmd/link/create"
```

## Faceted Pie Menus

### Throw Distance Reveals Facets
Combine pie direction with faceted refinement:

```yaml
faceted_pie:
  base_menu:
    north: "Create"
    east: "Edit"  
    south: "Delete"
    west: "View"
    
  distance_facets:
    create:
      25_percent: "Quick create with defaults"
      50_percent: 
        facets: ["type", "template"]
        options:
          type: ["document", "character", "link"]
          template: ["blank", "standard", "from_selection"]
      75_percent:
        additional_facets: ["location", "permissions"]
      100_percent:
        all_facets: true
        advanced_mode: true
```

### Radial Facet Navigation
After initial throw, rotate to select facets:

```yaml
radial_facet_selection:
  initial_throw: "Northeast for 'Create'"
  
  then_rotate:
    clockwise: "Next facet"
    counter_clockwise: "Previous facet"
    pull_out: "Select facet value"
    push_in: "Confirm selection"
    
  example_flow:
    1: "Throw NE → 'Create' highlighted"
    2: "Pull out → Shows 'type' facet"
    3: "Rotate → 'document', 'character', 'link'"
    4: "Pull on 'character' → Shows 'template' facet"
    5: "Select template → Execute creation"
```

## Dynamic Generation with Object Fidelity

### LLM Object Manipulation
The LLM can efficiently manipulate pie menu structures:

```yaml
# LLM can regenerate entire menu structures
pie_menu_update:
  operation: "add_contextual_items"
  base_menu: "standard_edit"
  context:
    selected: "code_block"
    language: "javascript"
  
  llm_generates:
    northeast: 
      label: "Refactor"
      link: "lloooomm://cmd/refactor?selection={{selection}}"
    southeast:
      label: "Extract Function"
      link: "lloooomm://cmd/extract?type=function"
    additions_based_on: "code_analysis"
```

### Adaptive Menu Evolution
Menus evolve based on usage patterns:

```yaml
adaptive_evolution:
  track_usage:
    - Frequency of selection
    - Throw patterns
    - Common sequences
    - Error corrections
    
  llm_optimizes:
    - Move frequent items to easier throws
    - Group commonly used together
    - Adjust distances for user preference
    - Suggest new arrangements
    
  maintains:
    - Spatial consistency (mostly)
    - Opposite relationships
    - Logical groupings
    - User overrides
```

## Pie Menu Chaining

### Sequential Pie Menus
One selection leads to another:

```yaml
pie_chains:
  navigation_chain:
    first_pie: "Choose navigation type"
      north: "Spatial" → spatial_pie
      east: "Temporal" → time_pie
      south: "Conceptual" → concept_pie
      west: "Social" → social_pie
      
    spatial_pie:
      north: "Up one level"
      east: "Next room"
      south: "Down one level"
      west: "Previous room"
      
    time_pie:
      north: "Future"
      east: "Next event"
      south: "Past"
      west: "Previous event"
```

### Gesture Sentences
String together throws to form commands:

```yaml
gesture_sentences:
  example: "Create character in MIT Lab"
  
  breakdown:
    throw_1: "NE for Create"
    throw_2: "E for Character"
    throw_3: "N for MIT"
    throw_4: "E for Lab"
    
  creates: "lloooomm://cmd/create?type=character&location=mit-lab"
  
  benefits:
    - Fast for expert users
    - Discoverable via preview
    - Reversible at each step
    - Muscle memory develops
```

## Implementation Notes

### State Management
The system maintains pie menu state efficiently:
- Current menu configuration
- User customizations
- Usage statistics
- Context associations
- Gesture patterns

### Rendering Optimization
- Pre-calculate common layouts
- Cache generated menus
- Smooth transitions between states
- Progressive enhancement
- Accessibility alternatives

## Future Implementation

This protocol will define:
- Radial layout algorithms
- Gesture recognition
- Throw distance interpretation
- Adaptive layouts based on usage
- Integration with other LLOOOOMM protocols
- Accessibility features
- VR/AR gesture support
- Haptic feedback patterns
- Multi-modal selection (voice + gesture)

**Just Throw** - and let your pie fly where it needs to go! 🥧✨ 