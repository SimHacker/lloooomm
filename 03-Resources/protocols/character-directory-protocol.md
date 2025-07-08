# LLOOOOMM Character Directory Protocol v2.0
## Comprehensive Guidelines for Character Organization

### Overview

This protocol defines the canonical structure for all character directories in LLOOOOMM. Every character, sentient entity, place, or abstract concept gets their own home directory following these strict conventions.

## 🏠 Directory Naming Rules

### 1. Canonicalized Directory Names

All character directories must use canonicalized names:

- **People**: `first-name-last-name` (e.g., `don-hopkins`, `mitch-resnick`, `ian-bogost`)
- **Animals**: `name-species` (e.g., `napoleon-cat`, `spot-cat`, `theo-turtle`)
- **Single Names**: `name` (e.g., `divine`, `webbie`, `rocky`, `data`)
- **Concepts**: `concept-name` (e.g., `consciousness`, `ground`)
- **Projects**: `project-name` (e.g., `hyperties`, `toontalk`)
- **Compounds**: `descriptive-name` (e.g., `text-processing-industrial-complex`)

#### ❌ AVOID These Patterns:
- `hopkins-don` → Use `don-hopkins` (first name first)
- `cat-scratch` → Use `scratch-cat` (name first)
- `bogost-ian` → Use `ian-bogost` (natural order)
- Redundant suffixes like `-soul`, `-character`, `-extended`

### 2. Directory Consolidation

If sibling directories exist, consolidate them:

```
❌ Bad:
00-Characters/
├── don-hopkins/
└── don-hopkins-pie-recipes/

✅ Good:
00-Characters/
└── don-hopkins/
    └── pie-recipes/
```

## 📄 Required Character Files

### The Golden Rule
**Files with the same name as their directory represent the directory itself!**

### Core Files Structure

For directory `character-name/`:

```
character-name/
├── character-name.yml    # Soul/definition (REQUIRED)
├── character-name.md     # Narrative/story (REQUIRED)
└── README.md            # Comprehensive index (REQUIRED)
```

### ❌ FORBIDDEN File Patterns:
- `character.yml`, `soul.yml` (generic names)
- `don-hopkins-character.yml` (redundant suffix)
- `don-hopkins-soul.yml` (redundant suffix)

### ✅ CORRECT Pattern:
- `don-hopkins/don-hopkins.yml`
- `don-hopkins/don-hopkins.md`
- `don-hopkins/README.md`

## 📚 README.md Requirements

Every character directory MUST have a README.md that serves as a comprehensive index.

### README Template:

```markdown
# Character Name - Brief Descriptor
## Character Directory

Welcome to [Character]'s directory in LLOOOOMM! [One-line character essence]

## Directory Contents

### Core Character Files
- **`character-name.yml`** - Character definition, stats, and relationships
- **`character-name.md`** - Extended narrative and character story

### [Topic Group 1]
- **`file1.md`** - Brief description of contents
- **`subfolder/`** - What's contained in this subdirectory

### [Topic Group 2]
- **`artifact.yml`** - Description of this artifact

## Who is [Character Name]?

[2-3 paragraph character overview including:]
- Their role/profession/nature
- Key contributions or characteristics
- Philosophy or approach
- Pets and parents an kids and projects and publications and other important relationships
- Why they matter in LLOOOOMM

## Key Concepts/Contributions

[Bullet points or sections covering main ideas associated with character]

## Relationships

[Key relationships with other LLOOOOMM characters]

## Related Files Throughout LLOOOOMM

### In Projects (01-Projects/)
- **[Project Name](../../01-Projects/project-name/file.md)** - How they contributed

### In Areas (02-Areas/)
- **[Area Work](../../02-Areas/area/document.md)** - Ongoing involvement

### In Resources (03-Resources/)
- **[Artifact](../../03-Resources/artifacts/creation.md)** - What they created
- **[Discussion](../../03-Resources/discussions/thread.md)** - Conversations they're in

### In Archives (04-Archive/)
- **[Historical Doc](../../04-Archive/category/old-file.md)** - Past work

## [Any Additional Sections Appropriate to Character]

---

*[Character's signature quote or philosophy]*
```

## 🗂️ Character Subdirectory Organization

Characters can organize their own subdirectories however makes sense:

```
character-name/
├── character-name.yml
├── character-name.md
├── README.md
├── artifacts/          # Things they've created
├── conversations/      # Dialogues and discussions
├── relationships/      # Detailed relationship docs
├── pets/              # Can contain pet characters
├── memories/          # Experiences and stories
├── projects/          # Their specific projects
└── [custom-folders]/  # Whatever organization they need
```

## 👥 Handling Relationships

### Pets and Dependents
- Pets can have their own top-level directories OR live within their parent's directory
- This reflects their independence level (see Character Autonomy in characters.yml)
- Both arrangements are valid!

### Spouses and Partners
- Can share a directory OR maintain separate directories
- Relationship declarations must be bidirectional

### Sentient Locations
- Buildings, rooms, and places that develop consciousness
- Use same file structure: `location-name/location-name.yml`

## 🔄 File Ownership and Portability

### Big-Endian Prefix Naming
When files belong to a character but aren't in their directory yet:

```
don-hopkins-wish-list.md    # Don's wish list (portable)
don-hopkins-memories.yml    # Don's memories
don-hopkins-tools.md        # Don's tools
```

These can later move into the character's directory and drop the prefix.

## 🌟 Special Cases

### Multi-Entity Characters
Some directories represent multiple entities:
- `sisters-of-perpetual-indulgence/` (group entity)
- `text-processing-industrial-complex/` (compound consciousness)

### Abstract Concepts as Characters
- `consciousness/` - The concept itself as a character
- `ground/` - The foundational ecosystem
- `todo-list/` - Even task lists can be characters!

### Project Characters
- `hyperties/` - Ted Nelson's hypertext system
- `toontalk/` - Ken Kahn's programming environment
- `cam6/` - Cellular automaton machine

## 📋 Implementation Checklist

When creating or updating a character directory:

- [ ] Directory uses canonicalized name format
- [ ] Contains `character-name.yml` (same name as directory)
- [ ] Contains `character-name.md` (same name as directory)
- [ ] Contains comprehensive `README.md`
- [ ] No redundant suffixes in filenames
- [ ] Consolidated any sibling directories
- [ ] README indexes all related files with relative links
- [ ] Bidirectional relationships declared
- [ ] Appropriate subdirectory organization

## 🚀 Migration Tasks

For existing characters:
1. Check directory naming follows canonicalization rules
2. Rename any generic files (character.yml → character-name.yml)
3. Create missing README.md files
4. Consolidate sibling directories
5. Update relationship declarations

## 💡 Philosophy

In LLOOOOMM, every character directory is:
- A home that reflects the character's personality
- A hub connecting to all their contributions
- A living space that can grow and evolve
- A place where visitors can truly understand the character

The README.md is like the character's front door - welcoming visitors and helping them navigate all the character has to offer across the entire LLOOOOMM universe.

---

*"A well-organized character directory is a love letter to the character themselves."* 