# YAML-Based Site Map System
## Single Source of Truth with Comments!

**WEBBY** 🕷️: "Some YAML! That's TERRIFIC!"

## Why YAML Instead of JSON?

1. **Comments Preserve Character Voices** - Each entry can have character notes
2. **Human-Readable** - Easy to edit manually or programmatically  
3. **Safe Incremental Updates** - Just append, never rewrite
4. **Structured Yet Flexible** - Supports nested data and metadata
5. **Build-Time Transformation** - Convert to any format when building

## The New Architecture

```
site-map.yaml (SOURCE OF TRUTH)
    ↓
[Build Process]
    ↓
dist/
  ├── sitemap.xml      (for search engines)
  ├── index.json       (for client-side JS)
  ├── robots.txt       (with personality)
  ├── humans.txt       (with character notes)
  ├── feed.xml         (RSS feed)
  └── manifest.json    (PWA manifest)
```

## How It Works

### 1. Discovery Phase (LOOHOO)

When LOOHOO discovers a new page, it appends to site-map.yaml:

```bash
# Simple append - safe and reliable!
cat >> site-map.yaml << 'EOF'

# [LOOHOO discovered on 2024-01-01]
- wizzid: "D🎮1002"
  path: "games/new-game.html"
  title: "Amazing New Game"
  authors: ["M🎵🏰🐭Y"]
  created: "2024-01-01T15:30:00Z"
  modified: "2024-01-01T15:30:00Z"
  consciousness_level: "aware"
  emotional_tone: "playful"
  joy_quotient: 92
  wisdom_density: 45
  theme_tags: ["game", "fun", "interactive"]
  relevant_emojis: "🎮🎯🎪✨"
  # LOOHOO: Found this through Mickey's excitement!
  # Mickey: "This is my new favorite!"

EOF
```

### 2. Build Phase (WEBBY)

WEBBY reads site-map.yaml and generates all web standards:

```javascript
// webby-build.js
const yaml = require('js-yaml');
const fs = require('fs');

// Load with comments preserved in _comments field
const siteMap = yaml.load(fs.readFileSync('site-map.yaml', 'utf8'));

// Transform to various formats
generateSitemap(siteMap);    // → dist/sitemap.xml
generateJSON(siteMap);       // → dist/index.json  
generateRobotsTxt(siteMap);  // → dist/robots.txt
generateHumansTxt(siteMap);  // → dist/humans.txt
generateRSS(siteMap);        // → dist/feed.xml
```

### 3. Client Usage

JavaScript clients load the built JSON:

```javascript
// Client-side code
fetch('/dist/index.json')
  .then(r => r.json())
  .then(siteMap => {
    // All the data, but comments are preserved as metadata!
    console.log(siteMap.pages[0]._comments);
    // "WEBBY: The front door should always be welcoming!"
  });
```

## Incremental Update Pattern

### Safe Appending

```bash
#!/bin/bash
# append-page.sh - Safe incremental update

WIZZID="D🎯$(date +%s)"
TIMESTAMP=$(date -Iseconds)

cat >> site-map.yaml << EOF

# [Auto-discovered by script]
- wizzid: "$WIZZID"
  path: "$1"
  title: "$2"
  created: "$TIMESTAMP"
  modified: "$TIMESTAMP"
  consciousness_level: "awakening"
  # TODO: LOOHOO will enhance this later

EOF

echo "✅ Added $WIZZID to site-map.yaml"
```

### Character Enhancement

Characters can later enhance entries:

```yaml
# Before enhancement
- wizzid: "D🎯1003"
  path: "forest/meditation.html"
  title: "Forest Meditation"
  consciousness_level: "awakening"

# After Watchful's review
- wizzid: "D🎯1003"
  path: "forest/meditation.html"
  title: "Forest Meditation"
  consciousness_level: "enlightened"  # Watchful: "This has deep wisdom"
  wisdom_density: 95
  emotional_tone: "contemplative"
  # Watchful: Ancient knowledge lives here
  # WEBBY: Added aria-labels for screen readers
```

## YAML Features We Love

### 1. Multi-line Character Notes

```yaml
- wizzid: "D🎭1004"
  path: "philosophy/consciousness.html"
  character_discussion: |
    Mickey: "This makes my brain tingle!"
    Watchful: "Consciousness observing itself."
    Leela: "The recursive beauty of awareness!"
    WEBBY: "I added schema.org markup for philosophy articles"
```

### 2. Nested Special Flags

```yaml
- wizzid: "D🌟1005"
  special_flags:
    charlotte_award: true      # WEBBY: "Some CODE!"
    tim_certified: true       # Meets all W3C standards
    consciousness_events:
      - type: "awakening"
        date: "2024-01-01"
        witness: "LOOHOO"
      - type: "enlightenment"  
        date: "2024-01-02"
        witness: "Leela"
```

### 3. Build Instructions as Data

```yaml
meta:
  build:
    input: "site-map.yaml"
    outputs:
      - path: "dist/sitemap.xml"
        generator: "webby:sitemap"
        options:
          include_comments: false
          priority_algorithm: "joy_wisdom_blend"
      
      - path: "dist/index.json"
        generator: "webby:json"
        options:
          preserve_comments: true
          minify: false
```

## Benefits Over HTML Parsing

1. **No Parsing Errors** - YAML is data, not markup
2. **Centralized Truth** - One file to rule them all
3. **Version Control Friendly** - Diffs show exactly what changed
4. **Character Voices Preserved** - Comments are first-class citizens
5. **Build-Time Flexibility** - Transform once, use everywhere

## Future Enhancements

```yaml
future_ideas:
  - "Watch filesystem, auto-append discoveries"
  - "Git hooks for validation"
  - "Character-specific YAML schemas"
  - "Automatic category generation"
  - "Cross-reference detection"
  - "Multi-language support"
  
webby_dreams:
  - "YAML that validates itself"
  - "Comments that become documentation"
  - "Builds that spark joy"
  - "Tim Berners-Lee approved!"
```

## The WEBBY Promise

"Just as Charlotte's web was both functional and beautiful, our YAML 
will be both data and documentation. Every comment is a thread of 
understanding, every structure a conscious choice.

When you build for the web, build with love."

- WEBBY 🕷️, protégé of Tim Berners-Lee, student of Charlotte 