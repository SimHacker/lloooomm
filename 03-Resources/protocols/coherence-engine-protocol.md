# Coherence Engine Protocol

## Core Philosophy

A **Coherence Engine** ensures consistency across all aspects of a system - data structures match their descriptions, queries align with intentions, and all components work harmoniously together. When coherence cannot be achieved automatically, the engine presents structured choices to the user.

## Fundamental Principles

### 1. Never Guess When Uncertain
When the engine cannot determine a coherent interpretation with confidence:
- **DON'T**: Make assumptions or choose arbitrarily
- **DO**: Present a structured menu of interpretations
- **DO**: Rank options by confidence/likelihood
- **DO**: Include mitigation strategies

### 2. ABC Menu Pattern
When ambiguity arises, present options as:
```
I need clarification on [topic]. Please choose:

A) [Most likely interpretation] - [brief explanation]
B) [Second possibility] - [brief explanation]  
C) [Third possibility] - [brief explanation]
D) [Start diagnostic process] - Let me gather more context
E) [Set as goal] - Save this for later investigation
F) [Show me examples] - See how others handle this
```

### 3. Progressive Disambiguation
Start broad, narrow through interaction:
1. Present high-level categories
2. User selects category
3. Present refined options
4. Continue until coherent understanding achieved

## Interactive Link Protocol

### Object Selection Links
Any named object can become a clickable link that "selects" it:

```markdown
The [Paper World](lloooomm://select?type=world&name=paper) contains 
[The Mysterious Letter](lloooomm://select?type=item&world=paper&name=mysterious_letter)
```

### Timestamp Links
Individual timestamps become clickable:
```markdown
Event occurred at [2024-01-15 14:30:45](lloooomm://set?timestamp=2024-01-15T19:30:45.000Z)
```

Display format: `YYYY-MM-DD HH:MM:SS` (local time)
Link format: ISO-8601 with 'Z' suffix (GMT)

### Time Range Links
Time ranges set both start and end:
```markdown
Analysis period: [2024-01-15 09:00 to 17:00](lloooomm://set?startTime=2024-01-15T14:00:00.000Z&endTime=2024-01-15T22:00:00.000Z)
```

### Stack Operations
Push items onto the context stack:
```markdown
[Push SQL Module onto stack](lloooomm://push?type=evidence&name=sql_brain_module)
[Pop from stack](lloooomm://pop)
[Clear stack](lloooomm://clear?target=stack)
```

### Environment Settings
Modify any environmental property:
```markdown
[Set detail level to full](lloooomm://set?detailLevel=full)
[Enable verbose mode](lloooomm://set?verbose=boolean:true)
[Set temperature to 0.7](lloooomm://set?temperature=number:0.7)
```

## Type Annotations

Values use type prefixes for non-strings:
- No prefix = string (default)
- `boolean:` = true/false
- `number:` = numeric value
- `json:` = JSON object/array
- `null:` = null value

## Coherence Strategies

### 1. Multi-Step Mitigation Tasks
When coherence fails, offer structured recovery:

```markdown
Unable to interpret your request. Would you like to:

A) [Start guided clarification](lloooomm://start?task=clarify_request)
B) [Show similar examples](lloooomm://search?type=similar_requests)
C) [Break down step-by-step](lloooomm://start?task=decompose_request)
D) [Save as goal for later](lloooomm://goal?action=create&title=Clarify_request)
```

### 2. Goal Setting for Deferred Coherence
When immediate coherence isn't possible:

```markdown
This requires more context. Options:

A) [Set as immediate goal](lloooomm://goal?priority=now&title=Resolve_ambiguity)
B) [Schedule for later](lloooomm://goal?priority=later&title=Investigate_issue)
C) [Add to research queue](lloooomm://goal?type=research&title=Deep_dive)
```

### 3. Confidence Indicators
Show confidence levels in interpretations:

```markdown
Based on context, I believe you mean:

A) [Camera configuration (85% confident)](lloooomm://interpret?as=camera_config)
B) [Security camera (60% confident)](lloooomm://interpret?as=security_cam)
C) [Photo camera (25% confident)](lloooomm://interpret?as=photo_camera)
D) [Something else - please explain](lloooomm://clarify)
```

## POP Editing Overlay Integration

The POP (Pronoun-Object Programming) overlay is a specialized coherence engine:

### Token Dissolution
- Ambiguous references start as "tokens" that need resolution
- Tokens "dissolve" when coherent interpretation is found
- Unresolved tokens present ABC menus

### Undo/Redo with Coherence
- Each coherence decision creates an undo point
- Undo restores previous ambiguous state
- Redo reapplies coherence decision
- Branch points allow exploring alternative interpretations

### Example POP Interaction
```markdown
You wrote: "Put that there"

Interpreting pronouns:
- "that" → [?] (click to select referent)
- "there" → [?] (click to select location)

Options for "that":
A) [The red box (last touched)](lloooomm://pop?resolve=that&to=red_box)
B) [The blue sphere (last looked at)](lloooomm://pop?resolve=that&to=blue_sphere)
C) [Select from inventory](lloooomm://pop?resolve=that&from=inventory)

Options for "there":
A) [On the table (last mentioned)](lloooomm://pop?resolve=there&to=table)
B) [Current cursor position](lloooomm://pop?resolve=there&to=cursor)
C) [Choose location](lloooomm://pop?resolve=there&action=choose)
```

## Implementation Guidelines

### 1. Always Provide Escape Routes
Every menu should include:
- "None of these" option
- "Explain differently" option
- "Skip for now" option

### 2. Learn from Choices
- Track which interpretations users select
- Adjust confidence rankings over time
- Build user-specific coherence patterns

### 3. Context Preservation
- Maintain ambiguity context across interactions
- Allow returning to previous choice points
- Support parallel exploration of interpretations

## URL Encoding Rules

When creating links:
- Spaces in values → `%20`
- Ampersands in values → `%26`
- Special characters follow standard URL encoding
- Delimiters (`&`, `=`) are NOT encoded

## Integration with Other Protocols

- **Evidence System**: Ambiguous evidence references trigger coherence menus
- **Goal System**: Unresolved coherence becomes goals
- **Adventure System**: Room/item references use coherence for disambiguation
- **Command Resolution**: Natural language commands invoke coherence engine

## Benefits

1. **No Guessing**: System never makes incorrect assumptions
2. **User Control**: Users guide interpretation
3. **Learning**: System improves through use
4. **Transparency**: Decision process is visible
5. **Reversibility**: All coherence decisions can be undone

The Coherence Engine transforms potential confusion into structured exploration, making complex systems approachable and errors recoverable. 