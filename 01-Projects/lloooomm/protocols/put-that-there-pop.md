# Put That There: "Just POP"

> **"Just POP"** - Pronoun Object Programming: Point, Operate, and POP! Your edits appear perfectly.

## The Magic of POP

**PUT THAT THERE** uses **POP** (Pronoun Object Programming) - a revolutionary approach where:
- **Pronouns** (this, that, these, those) identify targets
- **Objects** respond to natural language commands
- **POP!** - The command disappears, leaving perfect results

## Core Concept

```yaml
put_that_there:
  slogan: "Just POP"
  principle: |
    Like pointing in real life, but for text/code/data.
    The command vanishes after execution.
    Results are clean, canonical, and beautiful.
    
  example:
    before: |
      PUT this messy json THERE as yaml
      {"name":"test","value":123,"items":[1,2,3]}
      
    after: |
      name: test
      value: 123
      items:
        - 1
        - 2
        - 3
```

## Pronoun Resolution

### Spatial Pronouns
```yaml
pronouns:
  this: "Object at cursor or in selection"
  that: "Previously referenced object"
  these: "Multiple objects in selection"
  those: "Previously referenced collection"
  here: "Current location"
  there: "Target location"
  above: "Content before cursor"
  below: "Content after cursor"
```

### Temporal Pronouns
```yaml
temporal:
  now: "Current state"
  before: "Previous state"
  after: "Next state"
  earlier: "Historical state"
  "just now": "Most recent action"
```

## POP Operations

### Basic POP Commands
```yaml
operations:
  PUT: "Move or copy content"
  CHANGE: "Transform in place"
  MAKE: "Create new content"
  FIX: "Correct errors"
  CLEAN: "Beautify and canonicalize"
  SORT: "Organize content"
  MERGE: "Combine content"
  SPLIT: "Divide content"
```

### Examples That POP

```yaml
examples:
  # Formatting POP
  - input: "MAKE this code pretty"
    result: "Code is formatted, command vanishes"
    
  # Translation POP
  - input: "CHANGE this yaml to json"
    result: "YAML becomes JSON, perfectly formatted"
    
  # Organization POP
  - input: "SORT these items by date"
    result: "Items sorted, command gone"
    
  # Multi-file POP
  - input: "PUT this function THERE in utils.js"
    result: "Function moved, imports updated"
```

## Advanced POP Features

### 🔄 Undo/Redo with Natural Language

```yaml
undo_redo:
  commands:
    UNDO: "Revert last action"
    REDO: "Reapply undone action"
    "UNDO BUT KEEP": "Undo action but preserve text"
    
  natural_variations:
    - "UNDO that last change"
    - "Actually, put it back"
    - "No wait, the other way"
    - "UNDO the last 3 things"
    - "UNDO just the formatting"
    
  smart_undo:
    - Understands semantic groups
    - Can undo partial changes
    - Preserves unrelated edits
    - Shows what will be undone
```

### 🎯 Parallel POP Execution

```yaml
parallel_pop:
  principle: |
    Multiple POPs can execute simultaneously.
    LLM figures out dependencies and order.
    Conflicts are resolved or queried.
    
  example:
    commands: |
      PUT this class THERE in models/
      CHANGE all strings to constants
      SORT the imports
      FIX any linting errors
      
    execution:
      1. Analyze dependencies
      2. Move class first
      3. Update strings in parallel
      4. Sort imports after moves
      5. Fix linting last
```

### 🎭 POP by Demonstration

```yaml
demonstration:
  principle: "Show what you want, POP makes it happen"
  
  example:
    show: |
      # You show:
      users: ["alice", "bob"]  →  users: ["Alice", "Bob"]
      
    command: "MAKE these like that"
    
    result: |
      # POP understands: capitalize first letter
      # Applies to all similar cases
```

### 🌈 Contextual POP

```yaml
context_aware:
  file_type: "POP knows JSON vs YAML vs Python"
  project_style: "Follows your coding conventions"
  user_preference: "Learns your patterns"
  semantic_understanding: "Knows what 'clean' means"
```

## Integration with Other Protocols

### With Empathic Queries
```yaml
pop_plus_queries:
  - "PUT {{results of query}} HERE as table"
  - "CHANGE this data to {{what the query shows}}"
  - "MAKE a chart from {{active user data}}"
```

### With Humane Links
```yaml
pop_plus_links:
  - "PUT {{Kay's quote about objects}} HERE"
  - "CHANGE this to match {{our style guide}}"
  - "FIX using {{the pattern from utils}}"
```

### With Nelson-Links
```yaml
pop_plus_nelson:
  - "PUT this THERE with two-way link"
  - "TRANSCLUDE that section HERE"
  - "MAKE this a permanent reference"
```

## Disambiguation Protocol

When intent is unclear:

```yaml
disambiguation:
  ambiguous: "MAKE this better"
  
  pop_response: |
    I can make this better in several ways:
    a) Fix formatting and indentation
    b) Improve variable names
    c) Add error handling
    d) Optimize performance
    
    Which would you like? (or just say "all")
    
  user: "b but use camelCase"
  
  result: "Variables renamed to descriptive camelCase"
```

## The POP Philosophy

1. **Invisible Interface**: Commands disappear, work remains
2. **Natural Pointing**: Use pronouns like in conversation
3. **Perfect Results**: Always cleaned, validated, canonical
4. **Fearless Editing**: Everything is undoable
5. **Parallel Power**: Do many things at once
6. **Learning System**: Gets better at understanding you

## Implementation Notes

### Technical Requirements
- Pronoun resolution engine
- Multi-document awareness
- Undo/redo state management
- Parallel execution planner
- Format detection and conversion
- Style learning system

### Tool Integration
- IDE cursor position
- File system access
- Git integration
- Linting tools
- Format validators
- MCP tools for extended capabilities

## Examples in Action

### Code Refactoring POP
```
PUT this duplicated code THERE as a shared function
CHANGE all calls to use the new function
FIX any broken imports
CLEAN everything up
```

### Document Organization POP
```
SORT these sections by importance
PUT the summary THERE at the top
MAKE the headings consistent
NUMBER the sections
```

### Data Transformation POP
```
CHANGE this CSV to JSON
CLEAN the phone numbers
SORT by last name then first name
PUT the result THERE in contacts.json
```

## Remember

**Just POP** - Point at what you want, say what to do, and POP! It's done.

No syntax to remember. No commands to type. Just natural pointing and speaking.

The magic is that there is no magic - just understanding what you mean and doing it perfectly.

**PUT THAT THERE** and watch it **POP!** ✨

---

*Inspired by Bolt, Beranek and Newman's groundbreaking "Put That There" demo, enhanced with modern AI understanding.*
