# Site Mapper Worm TODO List 🐛
## The Great Metadata Harvest Plan

### Phase 1: Character Metadata Files
Create individual `character-name-meta.yml` files in `/dist` for each character:
- Extract core info: name, emoji, title, key contributions
- Track all pages where they appear
- List all content they've created
- Map their relationships to other characters

### Phase 2: Aggregate Metadata Files
1. **all-characters-meta.yml**: Complete character roster
   - Including: souls, rooms, objects, ideas, book covers
   - Not 1:1 with web pages (some have pages, some don't)
   
2. **all-pages-meta.yml**: Complete page inventory
   - Every HTML file in /dist
   - Tags, topics, featured characters
   - Creation date, last modified

### Phase 3: Character Browser System
- Dynamic character gallery that reads from metadata
- Filter by: activity level, topic, era, species
- Sort by: most active, most connected, newest
- Separate pages for:
  - Main characters (high activity)
  - Supporting cast (some activity)
  - Background souls (minimal activity)
  - All characters (complete roster)

### The Worm's Implementation Plan
```
1. INCH to each character file
2. DIGEST their essence into metadata
3. EXCRETE beautiful .yml castings
4. MERGE all castings into aggregate files
5. LAY TODO eggs for future features
```

### Example Character Metadata Structure
```yaml
name: Hugh Daniel
emoji: 🎂
title: "WELL Sysop, LED Cake Baker"
activity_level: high
appears_in:
  - reunion-in-lloooomm.html
  - well-history.html
  - artifact-party.html
created_content:
  - hugh-teaching-wisdom.md
  - well-sysop-stories.md
relationships:
  - Don Hopkins: "best friends"
  - Stewart Brand: "WELL co-conspirator"
  - The WELL: "primary caretaker"
tags:
  - community-builder
  - teacher
  - party-host
  - namespace-guardian
```

### Namespace Philosophy (per Hugh!)
Following Hugh's "DON'T FUCK WITH THE NAMESPACE!" wisdom:
- Use consistent naming: `character-name-meta.yml`
- BigEndian style: `hugh.daniel.meta.yml`
- Alternative namespaces for fun:
  - `soul.hugh.daniel.yml`
  - `party.eternal.hugh.yml`

### TODO Eggs to Lay 🥚
1. Auto-generate character gallery from metadata
2. Character relationship visualizer
3. Activity heat map
4. "Random character" feature
5. Character search by traits/tags
6. Cross-reference with site-map.yaml
7. API for character queries

### The Worm's Promise
"I shall inch through every file, taste every character's essence, and produce the most beautiful distributed metadata system LLOOOOMM has ever seen! No character shall be forgotten, no relationship unmapped!"

---
*Site Mapper Worm - Inching towards metadata enlightenment, one file at a time* 