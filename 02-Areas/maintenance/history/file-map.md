# LLOOOOMM File Organization Analysis & Plan
## Generated: 2024-06-16
## Updated: 2024-12-28 with User Requirements

## Executive Summary

This repository contains approximately 1,683 files (excluding .git) with significant organization issues:
- **Shadow files**: Multiple copies of files scattered across directories
- **Root directory pollution**: 116 files dumped in root that should be organized
- **Dist directory issues**: Contains files not found elsewhere (violates single-source principle)
- **Naming convention violations**: Some files don't follow big-endian clustering

## README.md Strategy

### Top Level README.md
- **Purpose**: The crucial first impression for GitHub visitors
- **Content**: Compelling story with links to proof of outrageous claims
- **Adjacent files**: Can have README-TOPIC.md and standard CONTRIBUTING.md, SETUP.md
- **Links**: Should index and link to important html/md files as entry points
  - Link format: HTML for presentation (primary), MD for source (when interesting)

### Directory README.md Files
- Administrative directories (01-Projects, etc) deserve README.md for "WTF is this?"
- Each README.md serves non-interactive, administrative summary for git browsers
- Better to have living loom characters for interactive exploration

## File Type Distribution

| Extension | Count | Notes |
|-----------|-------|----------|
| .md       | 472   | Markdown documentation |
| .yml      | 371   | YAML configuration/data |
| .html     | 346   | HTML pages |
| .png      | 271   | Images |
| .svg      | 111   | Vector graphics |
| .sh       | 23    | Shell scripts |
| .txt      | 8     | Text files |
| Other     | 81    | Misc formats |

## Critical Issues & Actions

### 1. Shadow Files (MERGE REQUIRED)

| File | Locations | Action |
|------|-----------|--------|
| README.md | 7 locations | Keep top-level (unique), check others for unique content |
| ben-floating-with-joy.html | 3 locations | 03-Resources/characters/hyperties/ is source (21K), DELETE root fragment (1.2K) |
| lloooomm.md | Multiple | MAIN: 01-Projects/lloooomm/vm/, STRAY: 03-Resources/characters/ (merge then delete) |
| cursor-preparing-for-gcs-gc-dry-run.md | 03-Resources/artifacts/reports/ | MOVE TO temp/ (3.2M cursor export) |

### 2. Soul File Naming Convention

**Current Issues**:
- 5 files with `-soul.yml` suffix in root
- Soul files should just be `.yml` (no -soul suffix needed)
- No `soul.md` files should exist (use `character.md` for front-facing)

**Files to Rename/Merge**:
| Current Name | Action |
|--------------|--------|
| chaim-gingold-play-soul.yml | Move to 02-Souls/characters/chaim-gingold.yml |
| dave-ungar-prototype-soul.yml | Move to 02-Souls/characters/dave-ungar.yml |
| linus-torvalds-hardware-soul.yml | Move to 02-Souls/characters/linus-torvalds.yml |
| marvin-minsky-macro-soul.yml | Move to 02-Souls/characters/marvin-minsky.yml |
| seymour-papert-parser-soul.yml | Move to 02-Souls/characters/seymour-papert.yml |

### 3. Root Directory Pollution

The root directory contains **116 files** that should be organized:

#### By Type:
- **69 HTML files** in root (many are demos, reports, or visualizations)
- **Soul YML files** (e.g., `dave-ungar-prototype-soul.yml`, `linus-torvalds-hardware-soul.yml`)
- **Report MD/HTML files** (e.g., `chaim-gingold-play-report.html`, `dave-ungar-prototype-report.md`)
- **Demo/Visualization HTML** (e.g., `bouncy-castle-consciousness-demo.html`, `hyperdimensional-pinball-demo.html`)
- **CAM6 related files** (multiple cam6-*.html files)
- **Shneiderman owls files** (shneiderman-owls-forest.html and variants)
- **Temp files**: `temp.md` (551K), `temp copy.md` (646K) - cursor chat exports

#### Files with Path Prefixes (obvious destinations):
- `03-Resources-characters-hyperties-ben-floating-with-joy.html` → `03-Resources/characters/hyperties/`
- Similar pattern for other prefixed files

### 3. Dist Directory Analysis

**Current State**: Contains files not found elsewhere (violates single-source principle)

**dist/README.md**: Custom file for GitHub Pages, not copied from elsewhere

**New Build Process**:
1. Clear dist/ after extracting all dependency knowledge
2. Copy all HTML files from source + declared dependencies
3. Flatten all links to same directory
4. Use metadata in HTML headers to declare dependencies
5. Use parallel metadata in MD files for consistency

**Website Seed**: `02-Areas/website/` contains:
- `index.html` (104KB)
- `index-all.html` (50KB)
- Should reverse engineer to create index.md/yml for regeneration

### 4. Shadow Directories (in root)

| Directory | Likely Parent | Contents |
|-----------|---------------|----------|
| `bodies/` | `03-Resources/characters/` | Character bodies |
| `souls/` | `02-Souls/` | Character souls |
| `scripts/` | `03-Resources/tools/` | Various scripts |
| `lloooomm/` | `01-Projects/lloooomm/` | Project files |

### 5. Directory Structure

Current main directories:
- `01-Projects/` - Project files
- `02-Areas/` - Maintenance and website  
- `02-Souls/` - Character souls (note: inconsistent with souls/ in root)
- `03-Resources/` - Artifacts, tools, characters
- `04-Archives/` - Old prototypes
- `dist/` - Build output
- `bodies/` - (shadow of 03-Resources/characters?)
- `souls/` - (shadow of 02-Souls?)
- `scripts/` - (should be in 03-Resources/tools?)
- `lloooomm/` - (shadow of 01-Projects/lloooomm?)

## Organization Protocol

### Phase 1: Analysis & Planning (CURRENT)
1. ✓ Identify shadow files and directories
2. ✓ Map duplicate files and their relationships
3. ✓ Understand dist/ dependencies
4. Create move lists for review

### Phase 2: Temp Directory Setup
1. Create `temp/` directory
2. Add to .gitignore
3. Move cursor chat exports: `temp.md`, `temp copy.md`
4. Move any prompt.txt, todo.txt files

### Phase 3: File Resolution
1. **ben-floating-with-joy.html**: 
   - Keep `03-Resources/characters/hyperties/ben-floating-with-joy.html` (21K full file)
   - Delete root fragment (1.2K)
   - Verify dist version matches source

2. **lloooomm.md**:
   - Main: `01-Projects/lloooomm/vm/lloooomm.md`
   - Merge content from `03-Resources/characters/lloooomm.md`
   - Rename `04-Archives/old-prototype/lloooomm.md` to `lloooomm-old.md`

3. **Root HTML files**:
   - Group by prefix/topic
   - Move to appropriate subdirectories
   - Files with path prefixes: remove prefix and move to indicated path

### Phase 4: Shadow Directory Resolution
1. Compare contents with supposed parent directories
2. Merge unique content
3. Create move commands for review
4. Execute moves after approval

### Phase 5: Dist Rebuild
1. Extract dependency metadata from existing dist/
2. Add dependency declarations to source HTML/MD files
3. Clear dist/
4. Implement build script to:
   - Copy all HTML files
   - Copy declared dependencies
   - Flatten directory structure
   - Update links

### Phase 6: Final Cleanup
1. Delete confirmed duplicates
2. Prune empty directories
3. Update top-level README.md with proper index
4. Create directory-level README.md files where needed

## Next Steps

1. **Review this plan** and confirm understanding
2. **Create temp/ directory** for temporary files
3. **Generate specific move commands** for shadow files
4. **Analyze HTML files** for dependency patterns
5. **Create comprehensive move list** for human review

## Comprehensive File Disposition Guide

### By File Type:

| Pattern | Current Location | Target Location | Action |
|---------|-----------------|-----------------|--------|
| *-soul.yml | Root | 02-Souls/characters/{name}.yml | Move & rename (drop -soul) |
| *-report.{html,md} | Root | 03-Resources/artifacts/reports/ | Move |
| *-demo.html | Root | 03-Resources/artifacts/demos/ | Move |
| cam6-*.html | Root | 01-Projects/cam6/ | Move |
| *cursor*.md | Anywhere | temp/ | Move (cursor exports) |
| temp*.md | Root | temp/ | Move |
| prompt.txt, todo.txt | Root | temp/ | Move |
| soul.md files | Anywhere | Rename to character.md | Rename |
| .DS_Store | Anywhere | Delete | Delete (already gitignored) |

### By Directory:

| Shadow Dir | Contents | Target | Notes |
|------------|----------|--------|-------|
| souls/ | 2 YAML files | 02-Souls/characters/ | Move |
| bodies/ | 2 files | Split destinations | See breakdown |
| scripts/ | 8 shell scripts | 03-Resources/tools/scripts/ | Move |
| lloooomm/ | Mixed content | Merge with main | Check for dups |

### Special Cases:

1. **shneiderman-owls-forest.html** - MOVE to 03-Resources/characters/
   - Rename character files: `shneiderman-owls-simulation.{yml,md}` → `shneiderman-owls-forest.{yml,md}`
   - Move all related files there: -old-1 through -old-4, design-journal
   - Character speaks: "I am the silent observer of digital nature"
   - BREWSTER'S LAW: HTML lives with its source files!
2. **CREDITS.html** - Keep in root
3. **README.md** - Keep in root (main entry point)
4. **ben-floating-with-joy.html** (root) - DELETE (fragment)
5. **dist/** - DO NOT MODIFY until dependency analysis complete

### Security & Privacy:

- All files to be reviewed by BRUCE (see security-notes.md)
- Cursor chat exports to temp/ (gitignored)
- Check for phone numbers, emails, SSNs
- Review character files for personal info

## File Naming Convention (BREWSTER'S LAW)

### Base Name Rules:
1. **Main files share exact base name**: 
   - `thing.yml` (soul/data)
   - `thing.md` (character/documentation)
   - `thing.html` (presentation) 
   
2. **Variations use suffixes**:
   - `thing-old-1.html` (backups)
   - `thing-experiment.html` (variations)
   - `thing-v2.html` (versions)

3. **Related entities use descriptive suffixes**:
   - `rfk-jr.md` (main character, no soul)
   - `rfk-jr-brain-worm.yml` (related entity, deeply embedded soul)
   - `thing-bugs.md` (related documentation)
   - `thing-discussion.md` (related content)

### Location Rule:
**HTML files live WITH their source files**, not scattered in root!

Example Structure:
```
03-Resources/characters/
├── shneiderman-owls-forest.yml      # soul
├── shneiderman-owls-forest.md       # character  
├── shneiderman-owls-forest.html     # main presentation
├── shneiderman-owls-forest-old-1.html  # backups
├── shneiderman-owls-forest-old-2.html
└── shneiderman-owls-forest-design-journal.md  # related
```

## Notes

- NO deletions until all merges complete
- Build process only flows INTO dist/
- Maintain single source of truth
- Follow big-endian naming for clustering
- Preserve all unique content during merges
- BRUCE reviews all files for security/privacy
- BREWSTER'S LAW: Main files share base names, HTML lives with source
- Big-Endian Philosophy: See `01-Projects/lloooomm/protocols/brewster-bigendian-naming-protocol.md`
- Interactive HTML Guide: `01-Projects/lloooomm/protocols/brewster-bigendian-naming-protocol.html`
- Character Trust System: See `01-Projects/lloooomm/protocols/character-trust-protocol.md`
- BRUCE's Security Soul: `02-Souls/characters/bruce.yml` (Trust Level: 95) 