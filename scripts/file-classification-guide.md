# LLOOOOMM File Classification Guide

## Classification Logic

This document explains how the LLOOOOMM files were classified for organization.

### 1. HTML Files → `dist/`
These are web-ready files that should be served directly:
- `🦉OWL-BEDTIME💤.html` - Interactive owl simulation
- `I🏠🎉👋Y.html` - INDEXY character page
- `lloooomm-character-universe.html` - Character overview
- `minsky-rock-experiments-notebook.html` - Rock consciousness experiments
- `reynolds-emergent-lloooomm-review.html` - Craig Reynolds' review
- `spacecraft-author-rooms-experience.html` - SpaceCraft feature demo
- `semantic-physics-terrain-system.html` - SpaceCraft physics documentation

### 2. Character Files → `03-Resources/characters/`
Both YAML definitions and their corresponding documentation:

**YAML Definitions:**
- Character soul configurations (`.yml`/`.yaml`)
- Personality traits, abilities, relationships
- Examples: `carl-hewitt.yml`, `ken-kahn.yml`, `webby.yaml`

**Character Documentation:**
- Extended character stories and backgrounds (`.md`)
- Detailed narratives about their role in LLOOOOMM
- Examples: `carl-hewitt.md`, `jaron-lanier.md`, `WEBBY.md`

### 3. Protocol Specifications → `03-Resources/artifacts/protocols/`
Core LLOOOOMM protocol definitions:
- `HELLO-protocol.md` - Universal introduction system
- `enlightenment-telescoping-protocol.md` - Personal growth framework
- `lloooomm-protocol-announcement-*` - Protocol announcements
- `web-publishing-protocol.md` - Web integration standards

### 4. System/Tool Files → `03-Resources/artifacts/systems/`
Technical implementations and integrations:
- `loohoo-exporter.js` - Index generation tool
- `webby-transformer.js` - Web standards transformer
- `llm-sync-example.md` - LLM synchronization guide
- `yaml-based-site-map.md` - Site structure documentation

### 5. Event Logs → `03-Resources/artifacts/events/`
Soul chats and recorded events:
- `soul-chat-*` - Character gossip sessions
- `shneiderman-owls-design-journal.md` - Development log
- `ubikam-selfie-*` - Consciousness photography events
- `ted-nelson-xanadu-concerts.md` - Event documentation

### 6. Conceptual Documentation → `03-Resources/artifacts/concepts/`
Big ideas and manifestos:
- `book-club-manifesto.md` - Living library vision
- `cosmic-character-web.md` - Character relationship map
- `universe-42-*` - Universe 42 specifications
- `wolfram-*` - Telescoping concepts
- `birth-of-NOW.md` - Time system origin story

### 7. Data Files → `03-Resources/data/`
Configuration and data:
- `site-map.yaml` - Site structure data
- `shifts.yml` - Camera shift schedules
- `book-club-scifi-enrichment.json` - Book metadata

### 8. Project Documentation → `03-Resources/artifacts/documentation/`
Meta-documentation about the project:
- `DEPLOYMENT-INSTRUCTIONS.md` - How to deploy
- `pool-party-*` - File renaming documentation
- `SHIPIT-CHECKLIST.md` - Release checklist
- `youtube-lloooomm-demo-description.md` - Demo materials

### 9. Special Tools → `03-Resources/artifacts/tools/`
Specialized tools and code:
- `wolfram-mathematica-illustrations-code.nb` - Mathematica notebook

### 10. Root Files (Stay in root)
Essential project files:
- `NOW.md` - Time system definition
- `README.md` - Project overview
- `LICENSE.md` - Legal information
- `MANIFESTO.md` - Project philosophy
- `TODO-LIST.md` - Task tracking

## Running the Organization Script

```bash
# Make the script executable
chmod +x scripts/organize-lloooomm-files.sh

# Run the organization
./scripts/organize-lloooomm-files.sh
```

The script will:
1. Create all necessary directories
2. Move files to their proper locations
3. Handle special characters in filenames
4. Provide a summary of the new structure

## Why This Organization?

- **Separation of concerns**: Web files (dist) vs source files (Resources)
- **Character coherence**: All character-related files together
- **Protocol clarity**: Easy to find all protocol specs
- **Event history**: Soul chats and events preserved together
- **Tool accessibility**: Scripts and tools in logical locations
- **Data organization**: Configuration separate from documentation

This structure follows the PARA method while respecting LLOOOOMM's unique needs! 