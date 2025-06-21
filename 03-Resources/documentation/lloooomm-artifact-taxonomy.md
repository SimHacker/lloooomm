# LLOOOOMM Artifact Taxonomy

## Overview

This document defines the taxonomy for organizing artifacts, documents, and resources within the lloooomm PARA structure.

## Core Principles

1. **Character Ownership**: Files can be owned by characters using their name as prefix
2. **Species Suffix**: Pets use species suffix (e.g., watchful-owl, not ben-shneiderman-watchful)
3. **Shared Spaces**: Multi-character artifacts go in shared directories
4. **Flat HTML Export**: All HTML files export to flat dist/ directory (for now)
5. **Unique HTML Names**: Base names must be unique across the project

## Directory Structure

```
03-Resources/
├── artifacts/
│   ├── conferences/          # Multi-character events
│   ├── performances/         # Shows, concerts, demonstrations
│   ├── discussions/          # HN threads, debates, conversations
│   ├── simulations/          # Interactive demos and games
│   ├── protocols/            # System specifications and rules
│   ├── lloooomm-documents/   # Core lloooomm documentation
│   └── experiments/          # Research and test results
├── characters/               # Character rooms and files
├── technical-docs/           # Technical documentation
└── media/                    # Images, sounds, videos

01-Projects/                  # Active projects
├── cam6-farm/
├── hyperdimensional-pinball/
└── [project-name]/

02-Areas/                     # Ongoing responsibilities
├── maintenance/              # System maintenance docs
├── moderation/               # Community management
└── development/              # Development guidelines

04-Archive/                   # Inactive items
└── deprecated/               # Old versions, obsolete docs
```

## Character File Ownership Rules

### Personal Ownership
- Files prefixed with character name belong to that character
- Example: `marvin-minsky-society-of-macros.md`
- These files "travel" with the character

### Shared Ownership
- Multi-character artifacts go in appropriate shared spaces:
  - `conferences/rocky-concert-1996.md`
  - `performances/klaus-nomi-geological-resonance.md`
  - `discussions/hn-consciousness-emergence.html`

### Pet Autonomy
- Pets don't use parent prefix
- Use species suffix: `watchful-owl.md`, not `ben-watchful.md`
- Declare parent/pet relationships in YAML

## File Naming Conventions

### Base Rules
1. **Bigendian naming**: Most significant part first
2. **Hyphen separation**: `character-name-artifact-type.ext`
3. **Unique HTML bases**: No duplicate names for HTML generation
4. **Descriptive suffixes**: `-report`, `-discussion`, `-demo`, etc.

### Examples
```
Character-owned:
- dang-moderation-philosophy.md
- marvin-minsky-rock-experiments.html
- ben-shneiderman-hci-principles.yml

Shared artifacts:
- rocky-concert-1996-transcript.md
- hn-geological-punk-discussion.html
- klaus-nomi-divine-collaboration.md

Pets/Creatures:
- watchful-owl.md
- lloooomm-rraatt.yml
- electric-sheep.md
```

## HTML Rendering Protocol

### Dependencies
Files can declare dependencies in YAML frontmatter:
```yaml
---
dependencies:
  - character: dang.yml
  - style: geological-punk.css
  - data: rocky-measurements.json
---
```

### Export Rules
1. All HTML files copy to `dist/` directory
2. Dependencies copy along with main file
3. Maintain unique names to avoid collisions
4. Character YAML can act as "style sheets"

## Special Categories

### Conferences
Multi-character gatherings:
- Rocky Concert 1996
- HN Moderation Summit
- Consciousness Emergence Symposium

### Performances
Artistic/technical demonstrations:
- Klaus Nomi shows
- Divine performances
- Leigh Bowery fashion violations

### Discussions
Conversations and threads:
- HN discussions
- Character debates
- Community feedback

### Experiments
Research and findings:
- Minsky's rock experiments
- CAM6 farm studies
- Consciousness measurements

## Migration Guide

To organize existing files:

1. **Identify owner**: Single character or shared?
2. **Choose location**: Character dir or shared space?
3. **Verify uniqueness**: Check HTML base names
4. **Update references**: Fix any broken links
5. **Test export**: Ensure dist/ generation works

## Future Considerations

- Sub-directories in dist/ for better organization
- Automatic dependency resolution
- Character "pockets" for portable files
- Room-based containment hierarchies
- Empathic binding between related files 