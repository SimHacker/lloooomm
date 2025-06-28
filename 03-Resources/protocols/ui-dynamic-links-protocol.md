# Dynamic UI Links Protocol

## Overview

The Dynamic UI Links system transforms static text into an interactive, explorable interface where every meaningful reference becomes a clickable gateway to action.

## Core Link Types

### 1. Object Selection Links
Make any named object clickable to "select" or focus on it:

```markdown
The [Constitution Document](lloooomm://select?type=document&name=constitution) defines
how [Room Alpha](lloooomm://select?type=room&name=alpha) connects to 
[The Magic Portal](lloooomm://select?type=item&name=magic_portal)
```

### 2. Timestamp Links
**EVERY timestamp must be a clickable link!**

Format rules:
- **Display**: `YYYY-MM-DD HH:MM:SS` (user's local time, no 'T' or 'Z')
- **Link href**: ISO-8601 with 'Z' suffix (GMT/UTC)
- **Action**: Sets the current timestamp context

Example:
```markdown
Event occurred at [2024-01-15 14:30:45](lloooomm://set?timestamp=2024-01-15T19:30:45.000Z)
```

### 3. Time Range Links
**EVERY time range must be clickable and set BOTH start and end!**

Format rules:
- **Display**: `YYYY-MM-DD HH:MM to YYYY-MM-DD HH:MM` (local time)
- **Link href**: Both times in ISO-8601 GMT format
- **Action**: Sets both startTime and endTime

Example:
```markdown
Analysis period: [2024-01-15 09:00 to 17:00](lloooomm://set?startTime=2024-01-15T14:00:00.000Z&endTime=2024-01-15T22:00:00.000Z)
```

### 4. Stack Operation Links
Manage the context stack:

```markdown
[Push current context](lloooomm://push?context=current)
[Pop to previous](lloooomm://pop)
[Push "SQL Patterns" onto stack](lloooomm://push?type=evidence&name=sql_patterns)
[Clear stack](lloooomm://clear?target=stack)
[Swap top two items](lloooomm://swap)
```

### 5. Prompt Injection Links
Set or append to the current prompt:

```markdown
[Analyze this data](lloooomm://prompt/Analyze the current data set)
[Add clarification](lloooomm://append/Also consider performance metrics)
[Clear prompt](lloooomm://clear?target=prompt)
```

### 6. Environment Setting Links
Modify any environmental property:

```markdown
[Set detail level to full](lloooomm://set?detailLevel=full)
[Enable verbose mode](lloooomm://set?verbose=boolean:true)
[Set confidence threshold](lloooomm://set?confidence=number:0.85)
[Configure multiple settings](lloooomm://set?mode=expert&detail=full&verbose=boolean:true)
```

## Type Annotation System

Values in URLs use type prefixes:
- **No prefix** = string (default)
- **`boolean:`** = true/false
- **`number:`** = numeric value  
- **`json:`** = JSON object/array
- **`null:`** = null value
- **`undefined:`** = undefined

Examples:
```markdown
[Enable feature](lloooomm://set?feature=boolean:true)
[Set count](lloooomm://set?count=number:42)
[Set name](lloooomm://set?name=Alice)  // string (no prefix)
[Set config](lloooomm://set?config=json:%7B%22key%22%3A%22value%22%7D)
```

## URL Encoding Rules

1. **Parameter delimiters** (`&`, `=`) are NEVER encoded
2. **Values** follow standard URL encoding:
   - Spaces → `%20`
   - Ampersands in values → `%26`
   - Special characters → URL encoded
3. **Prompt text** can contain spaces (system handles them)
4. **JSON values** must be fully URL encoded

## Formatting Guidelines

### In Tables
Make cells interactive:
```markdown
| Object | Time | Action |
|--------|------|--------|
| [Document A](lloooomm://select?name=doc_a) | [2024-01-15 10:30](lloooomm://set?timestamp=2024-01-15T15:30:00.000Z) | [View](lloooomm://action?type=view&target=doc_a) |
```

### In Lists
Every item can be clickable:
```markdown
Available actions:
- [Push context](lloooomm://push?context=current)
- [Set goal](lloooomm://goal?action=create)
- [View details](lloooomm://set?detail=full)
```

### In Prose
Natural language with embedded links:
```markdown
The [analysis](lloooomm://select?type=evidence&name=analysis_2024) 
completed at [14:30](lloooomm://set?timestamp=2024-01-15T19:30:00.000Z) 
shows that [Configuration A](lloooomm://select?type=config&name=a) 
outperforms the baseline.
```

## Special Link Patterns

### Multi-Action Links
Combine multiple operations:
```markdown
[Analyze with full detail](lloooomm://set?detail=full&action=analyze&auto=boolean:true)
```

### Conditional Links
Links that check conditions:
```markdown
[Continue if ready](lloooomm://check?condition=ready&then=continue&else=prepare)
```

### Navigation Links
Move through structures:
```markdown
[Next](lloooomm://nav?direction=next)
[Previous](lloooomm://nav?direction=prev)
[Up to parent](lloooomm://nav?direction=up)
[Jump to section](lloooomm://nav?target=section3)
```

## Best Practices

1. **Make Everything Clickable**: Any reference to an object, time, or concept should be a link
2. **Consistent Formatting**: Always follow the time display rules
3. **Clear Actions**: Link text should indicate what will happen
4. **Preserve Context**: Links should maintain or enhance current context
5. **Progressive Disclosure**: Start simple, reveal complexity through interaction

## Integration Points

- **Coherence Engine**: Ambiguous links trigger disambiguation menus
- **Evidence System**: Evidence titles become selectable links
- **Goal System**: Goals can be created/modified through links
- **Adventure System**: All rooms, items, and actions are linkable

## Benefits

1. **Discoverability**: Users see available actions
2. **Direct Manipulation**: Click instead of type
3. **Context Preservation**: Links carry state
4. **Exploration**: Every document becomes interactive
5. **Efficiency**: Complex operations in one click

The Dynamic UI Links system transforms passive reading into active exploration, making every document a living interface. 