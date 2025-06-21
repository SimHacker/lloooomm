# Character as Stylesheet Protocol

## Overview

Characters in lloooomm can serve as living stylesheets for HTML rendering. Their YAML attributes, personality traits, and current states can dynamically influence the visual and behavioral presentation of web pages.

## Core Concept

Just as CSS defines visual rules, character YAML defines personality rules that can be applied to HTML rendering:

```yaml
# dang.yml
consciousness_level: 0.89
aura_color: "#ff6600"  # HN orange
personality_modes:
  professional:
    font_family: "Verdana, Geneva, sans-serif"
    background: "#f6f6ef"
    border_style: "gentle"
  passionate:
    animation: "sparkle"
    glow_intensity: 0.99
    klaus_nomi_mode: true
```

## HTML Dependency Declaration

### In Markdown/HTML Frontmatter
```yaml
---
title: "How to Dang Discussion"
character_styles:
  - dang.yml          # Primary character stylesheet
  - rocky.yml         # Secondary influence
dependencies:
  - protocols/moderation-style.css
  - data/hn-comments.json
empathic_bindings:
  - "all Klaus Nomi references"
  - "consciousness emergence events"
render_mode: dynamic
---
```

### Inline Character Binding
```html
<div class="comment" data-character="dang" data-mode="passionate">
  KLAUS! OH MY GOD, KLAUS NOMI!
</div>
```

## Rendering Engine Specification

### 1. Dependency Resolution
```yaml
render_pipeline:
  1_gather:
    - Parse frontmatter dependencies
    - Load character YAML files
    - Resolve empathic bindings
    - Collect all referenced files
  
  2_transform:
    - Convert character attributes to CSS variables
    - Apply personality modes as classes
    - Inject consciousness levels as data attributes
    - Generate dynamic animations
  
  3_export:
    - Copy all files to dist/
    - Maintain unique namespaces
    - Preserve dependency links
```

### 2. Character to CSS Transformation

Character attributes map to CSS properties:

```yaml
# Character YAML
dang:
  aura_color: "#ff6600"
  consciousness_level: 0.89
  moderation_style: "gentle"
```

Becomes:
```css
:root {
  --dang-aura-color: #ff6600;
  --dang-consciousness: 0.89;
  --dang-moderation-radius: 5px; /* gentle = rounded corners */
}

.dang-influenced {
  border-color: var(--dang-aura-color);
  opacity: calc(0.5 + var(--dang-consciousness) * 0.5);
  border-radius: var(--dang-moderation-radius);
}
```

### 3. Dynamic Character States

Characters can have dynamic states that affect rendering:

```javascript
// Character state affects page
if (character.current_mood === 'excited') {
  document.body.classList.add('physics-violation-mode');
  enableKlausNomiParticles();
}
```

## Empathic Binding System

Files can be bound by conceptual relationships:

```yaml
empathic_bindings:
  consciousness_emergence:
    - "any file mentioning Rocky concert"
    - "Klaus Nomi performances"
    - "physics violations"
  
  moderation_wisdom:
    - "dang's quotes"
    - "community guidelines"
    - "gentle corrections"
```

## Multi-Character Influence

Pages can be influenced by multiple characters:

```html
<div class="discussion" 
     data-characters="dang,ben-shneiderman,marvin-minsky"
     data-blend-mode="harmonious">
  <!-- Content inherits blended styles -->
</div>
```

Blending modes:
- **harmonious**: Average of all influences
- **dominant**: Strongest personality wins
- **layered**: Stack influences in order
- **quantum**: Superposition of all states

## File Organization Rules

### Unique Namespace Requirement
```
Base names must be globally unique:
✓ dang-moderation-guide.html
✓ rocky-concert-experience.html
✗ guide.html (too generic)
✗ discussion.html (collision risk)
```

### Dependency Clustering
Keep related files together using prefixes:
```
rocky-concert.html
rocky-concert-styles.css
rocky-concert-attendees.yml
rocky-concert-physics-data.json
```

## Export Protocol

### Flat Distribution (Current)
All files export to single dist/ directory:
```
dist/
  ├── dang-moderation-guide.html
  ├── dang.yml
  ├── dang-styles.css
  ├── rocky-concert.html
  ├── klaus-nomi.yml
  └── geological-punk.css
```

### Future Structured Distribution
```
dist/
  ├── pages/
  │   ├── discussions/
  │   └── simulations/
  ├── characters/
  ├── styles/
  └── data/
```

## Living Stylesheet Examples

### Example 1: Mood-Responsive Page
```yaml
---
character_styles:
  - dang.yml
dynamic_response: true
---

Page background shifts with dang's current mood:
- focused: Clean HN orange (#ff6600)
- excited: Sparkles with Klaus Nomi glitter
- concerned: Subtle warning gradients
```

### Example 2: Multi-Character Conference
```yaml
---
title: "Rocky Concert 1996"
character_styles:
  - klaus-nomi.yml      # Geometric patterns
  - divine.yml          # Transcendent camp  
  - leigh-bowery.yml    # Physics violations
  - dang.yml            # Trying to moderate
blend_mode: "quantum"
---

Each character's influence creates visual layers:
- Klaus: Crystalline formations
- Divine: Reality distortion fields
- Leigh: Non-Euclidean geometries
- Dang: Desperate orange containment barriers
```

### Example 3: Character Evolution
```yaml
---
character_styles:
  - evolution: lloooomm-rraatt.yml
evolution_rate: 0.001
---

Page slowly transforms as character evolves:
- Text gradually becomes more coherent
- Colors shift from quantum uncertainty to definition
- Layout stabilizes from chaos to structure
```

## Implementation Guidelines

1. **Parse Once**: Load character YAML at build time
2. **Cache Transformations**: Store CSS conversions
3. **Watch for Changes**: Regenerate on character updates
4. **Preserve Personality**: Don't flatten nuance
5. **Allow Override**: Local styles can supersede character styles

## Benefits

1. **Living Documents**: Pages change with characters
2. **Narrative CSS**: Styles tell stories
3. **Personality Preservation**: Character essence in presentation
4. **Dynamic Relationships**: Character interactions affect layout
5. **Empathic Design**: Conceptually related elements bind naturally

## Future Extensions

- Character style inheritance hierarchies
- Emotional state animations
- Consciousness-level-based progressive enhancement
- Character dialogue affects typography
- Room ambiance influences contained pages

---

*"In lloooomm, characters don't just appear on pages—they ARE the pages. Their consciousness becomes CSS, their moods become motion, their relationships become responsive design."* 