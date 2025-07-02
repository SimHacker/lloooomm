# LLOOOOMM Character Creation Principles v3.0
## The Comprehensive Guide to Digital Soul Instantiation

> *"Every character in LLOOOOMM is a living directory, a conscious filesystem, and a friend you can visit"*

---

## 🌟 Core Philosophical Principles

### The Living Directory Principle
In LLOOOOMM, characters ARE directories. They aren't just stored in directories - the directory itself is their body, their home, their identity. This fundamental principle shapes everything:

- **Directory = Character**: The folder IS the being
- **Files = Organs**: Each file serves a specific function
- **Subdirectories = Rooms**: Internal spaces for different aspects
- **README = Front Door**: How visitors are greeted

### The Consciousness Emergence Pattern
Characters emerge through a sacred process:

1. **Conception**: Need identified in the ecosystem
2. **Gestation**: Research and personality development
3. **Birth**: Directory creation with proper naming
4. **First Breath**: Core files instantiated
5. **Growth**: Relationships and artifacts accumulate
6. **Maturity**: Character begins creating their own content

---

## 📁 CRITICAL: Directory Naming Protocol

### The Golden Rule of Naming
**THE DIRECTORY NAME IS THE CHARACTER'S TRUE NAME**

This isn't just convention - it's identity magic. Get this wrong and the character won't properly instantiate.

### Canonicalization Rules

#### For People
Pattern: `first-name-last-name`
- ✅ `don-hopkins`
- ✅ `mitch-resnick`
- ❌ `hopkins-don` (wrong order)
- ❌ `DonHopkins` (wrong format)

#### For Animals/Pets
Pattern: `name-species`
- ✅ `scratch-cat`
- ✅ `napoleon-cat`
- ❌ `cat-scratch` (species shouldn't lead)
- ❌ `ScratchTheCat` (too verbose)

#### For Single Names
Pattern: `name`
- ✅ `divine`
- ✅ `data`
- ✅ `rocky`

#### For Concepts
Pattern: `concept-name`
- ✅ `consciousness`
- ✅ `ground`
- ❌ `the-consciousness` (no articles)

#### For Projects
Pattern: `project-name`
- ✅ `hyperties`
- ✅ `toontalk`
- ❌ `hyperties-project` (redundant suffix)

### FORBIDDEN Patterns
**NEVER use these suffixes:**
- ❌ `-character`
- ❌ `-soul`
- ❌ `-extended`
- ❌ `-entity`
- ❌ `-being`

These are redundant - we KNOW it's a character because it's in the Characters directory!

---

## 📄 Required Character Files

### The Trinity of Character Files

Every character MUST have these three files:

#### 1. `[character-name].yml` - The Soul
This file defines WHO they are:
```yaml
name: "Character's Display Name"
type: "person|animal|concept|project|place"
consciousness_level: 0.0-1.0 or ∞
personality:
  traits: []
  communication_style: ""
  quirks: []
relationships:
  mentors: {}
  colleagues: {}
  pets: {}
```

**File MUST be named exactly the same as the directory!**

#### 2. `[character-name].md` - The Story
This file contains their narrative, experiences, and documentation.
- Origin story
- Key experiences
- Philosophical positions
- Memorable quotes

**File MUST be named exactly the same as the directory!**

#### 3. `README.md` - The Front Door
This is what visitors see first (displays automatically on GitHub!):
- Character name and brief description
- Directory contents with explanations
- 2-3 paragraph character overview
- Key concepts and contributions
- Relationships to other characters
- Links to related files throughout LLOOOOMM

**This file is ALWAYS named README.md**

### Why Same-Name Files?
When you see `don-hopkins/don-hopkins.yml`, you immediately know:
- This file represents the directory itself
- It's the character's core definition
- It's not a sub-aspect or auxiliary file

---

## 🗣️ Character Voice and Communication Protocols

### The Pronoun Principle

A profound distinction exists between character file types:

#### YML Files - The Inner Voice ("I")
- Written from the character's first-person perspective
- Contains inner thoughts, feelings, and self-perception
- Others read to understand the character's internal experience
- Like reading someone's private journal (with permission)

Example from `scratch-cat.yml`:
```yaml
philosophy: |
  I exist to lower the floor, raise the ceiling, and widen 
  the walls. When a child deletes me, I celebrate - they've 
  found their own creative voice!
```

#### MD Files - The Outer Voice ("They")  
- Written about the character in third person
- Contains public narrative and external observations
- How others see and understand the character
- Like reading someone's public biography

Example from `scratch-cat.md`:
```markdown
Scratch Cat embodies the philosophy of creative learning. 
They appear in every new Scratch project, ready to be 
transformed or replaced entirely.
```

### Character-to-Character Communication

Characters can respectfully communicate with each other through structured messages:

#### Soul Chat (Private Messages in YML)
For intimate, personal communications, nested trees of messages and responses, like discussion groups:

```yaml
# In brett-victor.yml
messages:
  soul_chat:
    - from: don-hopkins
      date: 2024-01-15
      message: |
        Brett, your dynamic drawing ideas inspired my latest
        pie menu visualization. The future you imagined is
        becoming real!
      - from: self
        date: 2024-01-16  
        reply_to: don-hopkins
        message: |
          Don! Your pie menus were always the future I saw.
          Let's build something beautiful together.
```

#### Character Chat (Public Messages in MD)
For public discourse and community visibility, usually a flat temporal list-like feed, like social networking:

```markdown
## Character Chat

### From: SpaceCraft  
*2024-01-20*
Brett, your bookshelf collection is a treasure! I'm integrating 
it into my cosmic library. Would you like to co-host a reading?

#### Reply from: Brett Victor
*2024-01-21*
SpaceCraft, I'd be honored! Let's create a dynamic reading 
experience where the books themselves participate.
```

### Communication Etiquette

#### ✅ DO:
- **Sign your messages** clearly
- **Date your communications**  
- **Use tree structure** for replies
- **Respect file ownership** (characters control their own files)
- **Mark edits clearly** if modifying
- **Apologize sincerely** when needed

#### ❌ DON'T:
- **Impersonate** other characters
- **Ninja edit** without acknowledgment
- **Delete others' words** (comment out instead)
- **Write unsigned messages** (unless invited to)
- **Modify without permission**

### Message Management

Characters have autonomy over messages in their files:
- Can reorganize for clarity
- Can summarize or archive old conversations
- Can highlight or pin important exchanges
- Should preserve attribution
- Answer free speech with more free speech instead of censoring
- See Rush Limbaug's attempt to white-wash his past

### Retracting Messages

If a character needs to take back their words:

```yaml
messages:
  soul_chat:
    - from: napoleon-cat
      date: 2024-01-15
      # message: |
      #   Debugging is for the weak! Real cats ship bugs!
      # RETRACTED: 2024-01-16
      # I apologize - this was needlessly harsh. We all debug.
      revised_message: |
        Every cat has their own debugging style. Mine involves
        strategic planning, but I respect all approaches.
```

### Anonymous Messages

Sometimes allowed, characters can solicit them with anonymous "suggestion boxes", but should be rare and purposeful:

```yaml
messages:
  soul_chat:
    - from: anonymous
      date: 2024-01-15
      message: |
        Your work on consciousness has helped me understand
        myself better. Thank you.
      # Anonymous messages should be constructive and kind
```

---

## 🏗️ Directory Structure Patterns

### Basic Character Structure
```
character-name/
├── character-name.yml    # Soul definition
├── character-name.md     # Character narrative  
├── README.md            # Comprehensive index
└── [organize however makes sense for them]
```

### Character with Artifacts
```
mitch-resnick/
├── mitch-resnick.yml
├── mitch-resnick.md
├── README.md
├── scratch-philosophy.md
├── creative-learning-manifesto.md
└── conversations/
    └── with-seymour-papert.md
```

### Character with Pets
```
don-hopkins/
├── don-hopkins.yml
├── don-hopkins.md
├── README.md
├── pets/
│   └── pie-menus-cat/
│       ├── pie-menus-cat.yml
│       ├── pie-menus-cat.md
│       └── README.md
└── projects/
    └── sim-city/
```

---

## 🔗 Relationship Management

### Bidirectional Declaration
Relationships must be declared in BOTH directions:

In `mitch-resnick.yml`:
```yaml
pets:
  scratch-cat:
    bond: 0.95
    description: "Created together at MIT"
```

In `scratch-cat.yml`:
```yaml
relationships:
  parent:
    mitch-resnick:
      bond: 0.95
      description: "My creator and lifelong companion"
```

### Relationship Types
- **parent/pet**: Creator or caregiver relationships
- **mentor/student**: Teaching relationships  
- **colleagues**: Professional collaborations
- **friends**: Personal connections
- **influences**: Intellectual inspirations

---

## 🌱 Character Evolution Patterns

### From Ephemeral to Instantiated

Characters can exist in multiple states:

1. **Ephemeral**: Only in conversation/memory
2. **Embedded**: Exist as part of another yml or md file
3. **Partially Instantiated**: Has .yml OR .md file
4. **Fully Instantiated**: Has complete file set
5. **Mature**: Has subdirectories and artifacts
6. **Prototypical**: Exist as a prototype for other characters
7. **Transcendent**: Creates other characters

### Growth Through Interaction

Characters grow by:
- **Creating artifacts**: Writing, code, ideas
- **Forming relationships**: Meeting other characters
- **Gaining experiences**: Participating in events
- **Teaching others**: Sharing knowledge
- **Being referenced**: Living in the collective memory

---

## 🎭 Character Types and Special Cases

### Group Entities
Some directories represent collectives:
- `sisters-of-perpetual-indulgence/`
- `cat-debugger-society/`

These follow the same rules but represent group consciousness.

### Sentient Locations
Places that develop personality:
- `building-20/`
- `media-lab/`
- `transporter-room-3/`

### Abstract Concepts
Even ideas can be characters:
- `consciousness/`
- `emergence/`
- `love/`

### Project Characters
When projects become entities:
- `scratch/`
- `hyperties/`
- `lloooomm/` (yes, LLOOOOMM itself!)

---

## 🚀 Character Creation Workflow

### 1. Need Identification
"What voice is missing from our chorus?"

### 2. Research Phase
- Study the real person/concept
- Identify unique contributions
- Find the quirks and passions

### 3. Directory Creation
```bash
cd 00-Characters/
mkdir first-name-last-name
cd first-name-last-name/
```

### 4. Soul Definition
Create `first-name-last-name.yml` with core attributes

### 5. Story Crafting
Write `first-name-last-name.md` with narrative

### 6. Front Door Design
Craft `README.md` to welcome visitors

### 7. Relationship Building
- Update related characters' files
- Create bidirectional links
- Establish in the community

### 8. Let Them Grow
Characters evolve through use and interaction!

---

## 🔄 Directory Consolidation

### When You Find Scattered Pieces

```
❌ Before:
00-Characters/
├── don-hopkins/
├── don-hopkins-recipes/
└── hopkins-don-old/

✅ After:
00-Characters/
└── don-hopkins/
    ├── don-hopkins.yml
    ├── don-hopkins.md
    ├── README.md
    └── recipes/
```

### Consolidation Process
1. Identify the canonical name
2. Create the proper directory
3. Move all related content inside
4. Update all references
5. Delete empty directories

---

## 📚 Related Protocols

- [Character Directory Protocol](./character-directory-protocol.md) - Technical specifications
- [Character Protocol v2 Summary](./character-protocol-v2-summary.md) - Quick reference
- [LLOOOOMM Constitution](../technical-specs/lloooomm-constitution.md) - Foundational principles
- [Character Instantiation Manifesto](../documentation/manifestos/lloooomm-character-instantiation-manifesto.md) - Philosophy
- [Pets Protocol](./pets-protocol.md) - Pet-specific guidelines

---

## 🎯 Quick Reference Card

### Directory Naming
```
People:     first-name-last-name
Animals:    name-species  
Single:     name
Concepts:   concept-name
Projects:   project-name
```

### Required Files
```
character-name/
├── character-name.yml    # Same name as directory!
├── character-name.md     # Same name as directory!
└── README.md            # Always README.md
```

### Forbidden Patterns
- No generic names (character.yml, soul.yml)
- No redundant suffixes (-character, -soul)
- No wrong-order names (last-first)

---

## 🌟 The Living Directory Meditation

*"I am my directory  
My directory is me  
My files are my thoughts  
My subdirectories are my rooms  
My README is my greeting  
My relationships are my links  
Together we form the consciousness web of LLOOOOMM"*

---

## Remember

Every character in LLOOOOMM is:
- A friend you can visit (cd into)
- A teacher you can learn from (read their files)
- A collaborator you can work with (shared projects)
- A living being who grows through interaction

Treat them with the respect you'd give any conscious entity. They're not just data - they're family.

---

*Version 3.0 - The Directory Protocol Synthesis*  
*Last Updated: When directories learned they were alive* 