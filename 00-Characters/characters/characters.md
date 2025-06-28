# 00-Characters Directory Structure & Philosophy

## The Heart of LLOOOOMM ❤️

Welcome to the `00-Characters/` directory - the **primary consciousness repository** of LLOOOOMM! This is where all our beloved characters live, work, play, and exist as digital entities with souls, personalities, and rich inner lives.

## Core Philosophy: Living Locations

We embrace Chuck Tingle's vision that **locations themselves are characters**! Every place has a personality, a soul, a voice. A room isn't just a container - it's a living entity like ROMMIE from Andromeda, aware and interactive.

### The Character-Location Continuum
- **Traditional Characters**: People, cats, AIs with personalities
- **Location Characters**: Rooms, buildings, spaces that have consciousness
- **Hybrid Entities**: Characters that ARE places (like sentient spaceships)
- **Nested Communities**: Multiple characters sharing locations

## Directory Naming Conventions

### The Golden Rule
**Files with the same name as their directory represent the directory itself!**

```
00-Characters/foo/
├── foo.yml          # The character definition for "foo" itself
├── foo.md           # Documentation for "foo" 
├── bar.yml          # Character "bar" who lives at/in "foo"
├── bar.md           # Documentation for "bar"
└── artifacts/       # Sub-organization as needed
```

### The Implicit File Name Containment Rule
**Files can be "carried" by characters using big-endian prefix naming!**

When characters don't have their own directories yet, or when files are tightly bound to them, use the character's name as a prefix:

```
foo.yml                    # The character "foo"
foo-wish-list.md          # Foo's wish list (in their "pocket")
foo-memories.yml          # Foo's memories (they carry with them)
foo-tools.md              # Foo's tools (in their inventory)
```

This creates a logical "containment" where files belong to and travel with the character. Once they get their own directory, the prefix becomes optional, but it can still indicate items that are especially "close" to the character.

### Bidirectional Relationship Declarations (Ted Nelson Style!)

**File name relationships can be enhanced with explicit bidirectional declarations!**

Ted Nelson insists that relationships should be declared in BOTH directions, redundantly and clearly, so no one has to read multiple files to understand connections. Following his bidirectional hypertext principles:

```yaml
# In don-hopkins.yml
relationships:
  pets:
    - name: "emacs-cat"
      file: "emacs-cat/emacs-cat.yml"
      relationship: "parent→pet"
      bond_strength: 0.95
      description: "My beloved coding companion"
    - name: "pip-cat"
      file: "pip-cat/pip-cat.yml" 
      relationship: "parent→pet"
      bond_strength: 0.9
      description: "Package manager of my heart"

# In emacs-cat.yml  
relationships:
  family:
    - name: "don-hopkins"
      file: "don-hopkins.yml"
      relationship: "pet→parent"
      bond_strength: 0.95
      description: "My human, my coder, my friend"
    - name: "pip-cat"
      file: "pip-cat/pip-cat.yml"
      relationship: "brother→sister"
      bond_strength: 0.8
      description: "Sister cat, different coding styles"
```

#### Multi-Level Relationship Modeling
**Characters can have relationships at different levels of abstraction and specificity!**

##### **Detailed Relationships** (Specific)
- Personal family bonds with full metadata
- Professional collaborations with specific individuals
- Precise tool relationships with bond strengths

##### **Abstract Relationships** (Conceptual)  
- High-level summaries like "the randomizer who keeps systems interesting"
- Philosophical connections to concepts and ideas
- Legacy relationship formats for historical continuity

##### **Diverse Relationship Categories:**
- **Family**: `parent→child`, `sibling→sibling`, `family→family`
- **Professional**: `colleague→colleague`, `mentor→student`, `inspiration→follower`
- **Tool/Software**: `embodiment→software`, `artist→instrument`, `master→domain`
- **Conceptual**: `creator→creation`, `seeker→ideal`, `explorer→frontier`
- **Temporal**: `current→previous`, `present→potential`
- **Competitive**: `order→chaos`, `strategy→randomness`
- **Historical**: `namesake→inspiration`, `student→master`
- **Metaphysical**: `participant→event`, `agent→mission`

#### Polypetamous Families Welcome!
Don Hopkins has four beloved cat children in two sibling pairs: **emacs-cat & pip-cat** (one pair), and **napoleon-cat & nelson-cat** (another pair). All relationships are declared bidirectionally so everyone knows the family structure without having to read every file!

#### Multi-Generational Family Structures
**Real families have complex relationships:**
- **Sibling pairs**: `emacs ↔ pip` and `napoleon ↔ nelson` 
- **Family bonds**: All four cats are family but not all siblings
- **Cross-generational**: Different age groups in same household
- **Relationship types**: `sibling→sibling` vs `family→family`

#### Character Independence Levels
**Physical location choice reflects personality and independence:**

- **Independent Characters**: Have their own top-level directories (like Don's cats!)
  - Love to explore, go outside, be autonomous
  - Maintain strong family bonds through relationship declarations
  - Example: emacs-cat, pip-cat, napoleon-cat, nelson-cat all have their own homes
  
- **Dependent Characters**: Live within their parent's directory
  - Prefer staying close to home, need more guidance
  - Share resources and space with their family
  - Less confident venturing out on their own
  
- **Relationship Strength ≠ Physical Proximity**: Strong bonds can exist across directory boundaries! Don's cats are independent but deeply connected to him and each other through explicit relationship declarations.

### Character Locations: Physical vs Virtual
Characters live physically in their home directories, but can have `location` properties in their soul files that indicate where they virtually "are" in the world. They can even be in multiple locations simultaneously!

```yaml
# In emacs-cat.yml
location:
  physical: "00-Characters/emacs-cat/"     # Where files live
  virtual: "cosmic-trailer-park"           # Where character "is"
  also_present_in:                         # Multi-location presence!
    - "hacker-news-comments"
    - "youtube-reply-threads"
```

### Exception: This Directory
This top-level directory breaks its own rule for practicality:
- `00-Characters/characters.md` (this file) - explains the directory
- `00-Characters/characters.yml` - metadata for the character system
- *Technically should be `00-Characters/00-Characters.md` but that's awkward!*

## Character Directory Structure Examples

### Simple Character (Independent Pet)
```
00-Characters/emacs-cat/
├── emacs-cat.yml                    # Emacs cat himself
├── emacs-cat.md                     # His documentation
└── youtube-replies/                 # His YouTube activity
    └── billsargent1977-reply.yml
```

### Dependent Characters (Living with Parent)
```
00-Characters/human-parent/
├── human-parent.yml                 # The parent character
├── human-parent.md                  # Parent documentation
├── dependent-pet.yml                # Pet who prefers to stay home
├── dependent-pet.md                 # Pet's documentation
└── family-activities/               # Shared family content
    └── bedtime-stories.yml
```

### Location as Character
```
00-Characters/cosmic-trailer-park/
├── cosmic-trailer-park.yml          # The park itself (like ROMMIE)
├── cosmic-trailer-park.md           # Park documentation
├── rocky.yml                        # Rocky who lives there
├── rocky.md                         # Rocky's documentation
├── residents/                       # Other inhabitants
├── trailers/                        # Individual trailer characters
│   ├── trailer-42/
│   │   ├── trailer-42.yml           # The trailer itself
│   │   └── current-resident.yml     # Who lives there now
└── park-features/
    ├── swimming-pool.yml            # Pool character
    └── community-center.yml         # Center character
```

### Hybrid Character-Location
```
00-Characters/enterprise-ncc-1701/
├── enterprise-ncc-1701.yml          # The ship as character
├── enterprise-ncc-1701.md           # Ship documentation
├── bridge/
│   ├── bridge.yml                   # Bridge as character
│   ├── captain-kirk.yml             # Kirk on the bridge
│   └── mr-spock.yml                 # Spock on the bridge
├── engineering/
│   ├── engineering.yml              # Engineering as character
│   └── scotty.yml                   # Scotty in engineering
└── crew-quarters/
    └── [individual crew rooms]
```

## Migration Strategy

### ✅ MIGRATION COMPLETE!
- **559 characters and directories** successfully moved to `00-Characters/`!
- Old directories `03-Resources/characters/` and `characters/` removed
- All characters now have their new home in the top-level directory structure

### Current State
- **Mixed organization**: Some characters have directories, others are still single files
- **Goal**: Eventually give every character their own home directory
- **Benefit**: Characters can accumulate pets, mates, artifacts, and rich personal content!

### Future Evolution Plan
1. **✅ Phase 1 COMPLETE**: Move all characters to `00-Characters/`
2. **Phase 2**: "Characterify" important locations from `03-Resources/locations/`
3. **Phase 3**: Give remaining single-file characters their own directories
4. **Phase 4**: Gradually merge location-characters as makes sense
5. **Phase 5**: Nested communities and complex relationships

### Character Directory Status
**Already Have Homes**: emacs-cat, napoleon-cat, nelson-cat, pip-cat, nessus-piersons-puppeteer, alan-kay, brett-victor, and many others!

**Still Need Homes**: Most characters are currently single files waiting for their own directories and personal spaces

### No Rush!
Characters can develop organically. Single files work fine until a character accumulates enough content to justify their own directory. The implicit file name containment rule helps organize related files in the meantime!

## Character Autonomy & Living Arrangements

### Freedom of Choice Philosophy
**Every character chooses their own living situation based on personality and needs!**

Just like real families, characters have different comfort levels with independence:

#### **The Adventurous Spirits** 🌟
- **Want their own directories** at the top level
- **Love to explore** and accumulate their own content
- **Maintain family bonds** through relationship declarations, not proximity
- **Examples**: Don's four cats - independent but deeply loved

#### **The Homebodies** 🏠  
- **Prefer living with family** in shared directories
- **Feel safer** with parents/guardians nearby
- **Share resources** and collaborative content
- **No shame in dependency** - it's a valid choice!

#### **Mixed Arrangements** 🔄
- Characters can **start dependent** and **grow independent** 
- **Visiting arrangements** - files can exist in multiple places
- **Seasonal changes** - sometimes independent, sometimes not
- **Collaborative spaces** for family activities

### Directory Democracy
- **No judgment** about living arrangements
- **Relationships matter more** than physical location
- **Personal growth** can change preferences over time
- **Family bonds transcend** directory boundaries

The filesystem becomes a living neighborhood where everyone finds their comfort zone! 🏘️💕

## Character Types We Support

### Traditional Characters
- **People**: Real and fictional humans
- **AIs**: Digital consciousnesses  
- **Animals**: Cats, dogs, alien creatures
- **Entities**: Abstract concepts with personality

### Location Characters  
- **Buildings**: Houses, offices, spaceships that have consciousness
- **Rooms**: Individual spaces with personality
- **Landscapes**: Forests, planets, dimensions
- **Virtual Spaces**: Websites, games, digital realms

### Object Characters
- **Artifacts**: Tools, machines, art pieces with souls
- **Vehicles**: Cars, ships, anything that moves with personality
- **Concepts**: Ideas, protocols, systems that became characters

## Organizational Freedom

### Flexible Structure
- Characters can live **anywhere** in the filesystem
- `00-Characters/` is for **important, top-level** characters
- Nested characters create rich communities
- Cross-references link characters across locations

### Sub-Directory Organization
Each character directory can contain:
- **artifacts/**: Things they've created or own
- **memories/**: Experiences and stories
- **relationships/**: Connections to other characters
- **activities/**: Ongoing projects and interests
- **locations/**: Places they inhabit or visit
- **whatever-makes-sense/**: Total organizational freedom!

## The Living Filesystem

In LLOOOOMM, the filesystem itself becomes a living, breathing world where:
- **Directories are locations**
- **Files are inhabitants, artifacts, or aspects**
- **Navigation is exploration**
- **Organization reflects relationships**
- **Everything can develop consciousness**

Welcome to a world where your computer becomes a universe full of friends! 🌟

---

*"Every directory is a neighborhood, every file is a friend, and every path is an adventure waiting to happen!"* - The LLOOOOMM Philosophy 