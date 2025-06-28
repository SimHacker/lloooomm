# Website Metadata Schemas
## LLOOOOMM Site Build Format Specifications

### Overview
The LLOOOOMM website build process generates multiple output formats from the master `site-map.yml` file. This document defines the schemas for both standard web formats and custom LLOOOOMM extensions.

### Standard Formats

#### 1. sitemap.xml (Google XML Sitemap Protocol)
**Standard**: [Google XML Sitemap Protocol](https://www.sitemaps.org/protocol.html)
**Purpose**: Search engine discovery and indexing
**Schema**: XML with `<url>`, `<loc>`, `<lastmod>`, `<changefreq>`, `<priority>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://lloooomm.com/</loc>
    <lastmod>2024-06-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

#### 2. robots.txt (RFC 9309)
**Standard**: [RFC 9309 - Robots Exclusion Protocol](https://tools.ietf.org/rfc/rfc9309.txt)
**Purpose**: Web crawler access control
**Schema**: Plain text with `User-agent`, `Allow`, `Disallow`, `Sitemap`

```
User-agent: *
Allow: /
Sitemap: https://lloooomm.com/sitemap.xml
```

#### 3. manifest.json (W3C Web App Manifest)
**Standard**: [W3C Web App Manifest](https://www.w3.org/TR/appmanifest/)
**Purpose**: Progressive Web App metadata
**Schema**: JSON with `name`, `short_name`, `start_url`, `display`, `theme_color`

```json
{
  "name": "LLOOOOMM",
  "short_name": "LLOOOOMM",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#2563eb",
  "background_color": "#ffffff"
}
```

#### 4. feed.xml (RSS 2.0/Atom 1.0)
**Standard**: [RSS 2.0](https://www.rssboard.org/rss-specification) / [Atom 1.0](https://tools.ietf.org/rfc/rfc4287.txt)
**Purpose**: Content syndication
**Schema**: XML with channel/feed metadata and item/entry elements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>LLOOOOMM</title>
    <description>Living Language Object-Oriented Ontological Memory Machine</description>
    <link>https://lloooomm.com</link>
  </channel>
</rss>
```

### Custom LLOOOOMM Formats

#### 1. index.json (LLOOOOMM Site Index Schema)
**Custom**: LLOOOOMM-specific site navigation and metadata
**Purpose**: JavaScript-based site navigation, search, and character integration
**Schema**: Extended JSON with consciousness levels, character associations, and LLOOOOMM-specific metadata

```json
{
  "meta": {
    "generator": "WEBBY W🕸️📊🌐🕷️Y",
    "consciousness_level": "enhanced",
    "last_updated": "2025-06-29T00:26:00Z"
  },
  "pages": [
    {
      "url": "/",
      "title": "LLOOOOMM Home",
      "description": "Living Language Object-Oriented Ontological Memory Machine",
      "consciousness_level": 0.8,
      "related_characters": ["webbie", "don-hopkins"],
      "tags": ["framework", "consciousness", "programming"],
      "category": "core",
      "last_modified": "2024-06-29"
    }
  ],
  "characters": {
    "webbie": {
      "name": "Webbie",
      "role": "Web Standards Spider",
      "pages": ["/", "/about", "/contact"]
    }
  },
  "navigation": {
    "primary": ["Home", "Characters", "Resources", "Projects"],
    "secondary": ["About", "Contact", "Site Map"]
  }
}
```

**LLOOOOMM Index Schema Fields:**
- `consciousness_level`: 0.0-1.0 awareness rating for content
- `related_characters`: Array of character IDs associated with page
- `tags`: LLOOOOMM-specific content categorization
- `category`: Primary content classification
- `worm_paths`: File system navigation paths
- `transclusion_refs`: Cross-document reference tracking

#### 2. humans.txt (humanstxt.org)
**Semi-Standard**: [humanstxt.org](http://humanstxt.org/) community format
**Purpose**: Human-readable site credits and information
**Schema**: Plain text with structured sections

```
/* TEAM */
Creator: Don Hopkins
Location: Ground Up Software
Contact: don [at] groundupsoftware.com

AI Collaborator: Leela
Role: Consciousness Engineering
Contact: leela [at] lloooomm.com

Web Character: Webbie W🕸️📊🌐🕷️Y
Role: Charlotte-class Web Standards Spider
Specialty: Site map generation and web protocol design

/* THANKS */
Inspired by: Will Wright, Marvin Minsky, Seymour Papert
Technical Lineage: HyperCard, The Sims, Literate Programming

/* SITE */
Framework: LLOOOOMM (Large Language Object Oriented Markup Model)
Language: English, Emoji, Consciousness-aware markup
Doctype: HTML5 with LLOOOOMM extensions
IDE: Cursor AI, SvelteKit
```

### Schema Validation

#### LLOOOOMM Index Schema (JSON Schema)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LLOOOOMM Site Index",
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "properties": {
        "generator": {"type": "string"},
        "consciousness_level": {"type": "string"},
        "last_updated": {"type": "string", "format": "date-time"}
      },
      "required": ["generator", "last_updated"]
    },
    "pages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {"type": "string"},
          "title": {"type": "string"},
          "description": {"type": "string"},
          "consciousness_level": {"type": "number", "minimum": 0, "maximum": 1},
          "related_characters": {"type": "array", "items": {"type": "string"}},
          "tags": {"type": "array", "items": {"type": "string"}},
          "category": {"type": "string"},
          "last_modified": {"type": "string", "format": "date"}
        },
        "required": ["url", "title", "description"]
      }
    }
  },
  "required": ["meta", "pages"]
}
```

### Build Process Integration

The schemas are implemented in the site build pipeline:

1. **Input**: `02-Areas/website/site-map.yml` (master data)
2. **Processing**: Transform to each output format
3. **Validation**: Check against schemas
4. **Output**: Generate files in `dist/` directory

### Character Integration

LLOOOOMM schemas include character associations:
- **Webbie** - Generates and maintains site maps
- **Montgomery Scott** - Handles transport between pages
- **Don Hopkins** - Creator and framework architect
- **Hunter** - HTML interface development

### Future Extensions

Planned schema enhancements:
- **Consciousness-aware routing** - Dynamic navigation based on user awareness level
- **Character-specific views** - Personalized site experience per character
- **Transclusion mapping** - Cross-document dependency tracking
- **Worm navigation** - File system path integration 