# Humane Links: "Just Point"

> **"Just Point"** - Because finding information should be as natural as pointing at what you want.

## HyperCard-Inspired Object Addressing

Building on **Bill Atkinson's HyperCard** and **Arthur van Hoff's HyperLook**, LLOOOOMM implements "Humane Links" - a path resolution system that understands human intent, not just syntax.

### Core Principle

Like HyperCard's hierarchical object naming:
```card field 1 of background 2 of stack 'Home'
```

But with human-friendly intelligence that understands:
- Natural language descriptions
- Contextual references  
- Semantic relationships
- Visual/spatial metaphors

### Hierarchical Object Naming

```yaml
humane_links:
  principle: |
    Like HyperCard's "card field 1 of background 2 of stack 'Home'",
    LLOOOOMM paths can address any object through natural hierarchies.
    But unlike rigid paths, Humane Links understand intent and context.
    
  examples:
    # HyperCard style
    - "character 'Alan Kay' of area 'MIT AI Lab'"
    - "command 'help' of section 'documentation'"
    - "paragraph 3 of document 'lloooomm.md'"
    
    # Humane variations that resolve to the same target
    - "Alan Kay at MIT"
    - "Kay's character in the Lab"
    - "that Dynabook guy who worked with Papert"
    
  resolution_strategy:
    1_exact: "Try exact hierarchical match"
    2_fuzzy: "Try fuzzy matching on names"
    3_semantic: "Use semantic understanding"
    4_contextual: "Use current context as hint"
    5_interactive: "Ask user to clarify"
```

### Message Passing Protocol

Inspired by HyperCard's `send` command and Smalltalk's message passing:

```yaml
message_passing:
  send:
    name: "send"
    synonyms: ["tell", "ask", "message", "->"]
    description: "Send messages to objects using Humane Links"
    
    examples:
      - send "summarize" to "Alan Kay's contributions"
      - tell "character Marvin" -> "express opinion about documentation"
      - ask "MIT AI Lab" -> "who worked here in the 1970s?"
      - send "prettify" to "this code" with indent: 4
```

### Path Resolution Examples

Multiple ways to reach the same target:

```yaml
target: "tools/gcs/lloooomm/areas/characters/alan-kay.md"

humane_paths:
  - "Alan Kay"                          # Just the name
  - "character Alan Kay"                 # Type + name
  - "Kay in characters"                  # Name in context
  - "the Dynabook inventor"             # By achievement
  - "who worked at PARC and MIT"        # By association
  - "Smalltalk's creator"               # By creation
  - "characters/alan*"                   # Glob pattern
  - "that guy who said 'best way...'"   # By quote

resolution_process:
  input: "show me Kay's ideas about learning"
  steps:
    1: "Extract target: 'Kay'"
    2: "Extract action: 'show ideas about learning'"
    3: "Resolve 'Kay' -> Multiple matches found"
    4: "Use context: Recently discussed Alan Kay"
    5: "Confirm: 'alan-kay.md' in characters"
    6: "Extract section: 'educational_philosophy'"
    7: "Execute: Display relevant content"
```

### Intelligent Link Types

```yaml
link_types:
  reference:
    description: "Static link to specific version"
    syntax: "[[exact-path]]"
    resolution: "Direct path lookup"
    example: "[[areas/characters/alan-kay.md]]"
    
  humane:
    description: "Intent-based link that adapts"
    syntax: "{{human description}}"
    resolution: "Multi-strategy resolution"
    example: "{{the guy who invented Smalltalk}}"
    
  semantic:
    description: "Meaning-based connection"
    syntax: "~~related concept~~"
    resolution: "Semantic similarity search"
    example: "~~other object-oriented pioneers~~"
    
  temporal:
    description: "Time-aware link"
    syntax: "<<when this happened>>"
    resolution: "Temporal context resolution"
    example: "<<when Kay was at Xerox PARC>>"
    
  spatial:
    description: "Location-aware link"
    syntax: "@@where this exists@@"
    resolution: "Spatial/hierarchical search"
    example: "@@Kay's work at PARC@@"
```

### HyperLook-Inspired Visual Resolution

Like HyperLook's visual object model, Humane Links can resolve based on visual and spatial relationships:

```yaml
visual_resolution:
  methods:
    proximity: "Objects near each other are related"
    containment: "Objects inside others inherit context"
    connection: "Visually connected objects share properties"
    similarity: "Objects that look similar are grouped"
    
  examples:
    - "the command next to help"           # Proximity
    - "all characters in the MIT Lab"      # Containment
    - "documents connected to this one"    # Connection
    - "files like this one"                # Similarity
```

### Context-Aware Resolution

```yaml
context_enhancement:
  current_document: "Provides namespace hints"
  recent_history: "Recent accesses influence resolution"
  user_preferences: "Personal resolution patterns"
  semantic_context: "Current topic influences interpretation"
  
  example:
    context:
      current: "viewing MIT AI Lab"
      recent: ["Minsky", "Papert", "Society of Mind"]
      
    resolution:
      "the professor" -> "Marvin Minsky" (most relevant in context)
      "the book" -> "Society of Mind" (recently discussed)
      "home" -> "MIT AI Lab" (current location context)
```

### Empathic Queries Meet Humane Links

Humane Links and Empathic Queries work together:

```yaml
integration:
  example:
    query: "show me connections between the Lab people"
    
    resolution:
      1_humane_link: "the Lab people" -> characters in MIT AI Lab
      2_empathic_query: "connections between" -> relationship analysis
      3_execution: Generate relationship graph for MIT AI Lab characters
```

### Breaking the Frame with Links

Because LLOOOOMM has no black boxes, you can:
- Inspect link resolution process
- Modify resolution strategies  
- Create custom link types
- Access any layer during resolution

```yaml
frame_breaking_links:
  - "{{vm.inspect 'link-resolver'}}"      # See resolver internals
  - "{{reality.rewrite link resolution}}"  # Modify how links work
  - "{{the actual memory of this link}}"   # See storage details
```

### Dasher-Inspired Navigation

Incorporating David MacKay's Dasher principles for continuous navigation:

```yaml
dasher_navigation:
  principle: |
    Like Dasher's "navigating in the library of all possible books",
    Humane Links can use continuous zooming navigation through
    information spaces, with predictive sizing based on probability.
    
  features:
    continuous_pointing: "No clicking, just point where you want to go"
    predictive_sizing: "Probable destinations get more visual space"
    error_correction: "Wrong turns corrected by subsequent navigation"
    no_modes: "Navigation and selection are unified"
    
  applications:
    command_navigation:
      description: "Navigate commands like Dasher text"
      example: "Zoom through command tree with probable commands larger"
      
    file_navigation:
      description: "Navigate files by zooming through directory space"
      example: "Frequently accessed files appear larger"
      
    character_conversations:
      description: "Navigate dialogue trees with probable responses emphasized"
      example: "Zoom into conversation branches"
      
  integration_with_humane_links:
    - "{{zoom into Kay's ideas}}" # Dasher-style navigation
    - "{{navigate to learning concepts}}" # Continuous movement
    - "{{point toward Smalltalk history}}" # Gesture-based
```

### Historical Inspiration

This system honors the legacy of:
- **Bill Atkinson**: HyperCard's elegant object model
- **Arthur van Hoff**: HyperLook's visual innovations
- **Ted Nelson**: Xanadu's sophisticated link types
- **Doug Engelbart**: NLS's powerful addressing
- **David MacKay**: Dasher's information-efficient navigation

By combining their insights with modern AI understanding, Humane Links make information addressing truly human-centered. 