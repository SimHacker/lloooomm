# The BREWSTER Big-Endian Naming Protocol
## A Philosophy of Natural Clustering Through Thoughtful Naming

*"Big-endian naming sorts better than little-endian."* - Central Repository Wisdom

---

## Executive Summary

Big-endian naming is a philosophy where the most significant information comes first. This creates natural clustering when files are alphabetically sorted, keeping related content together without complex organizational schemes.

## The Core Philosophy

### What is Big-Endian Naming?

In computing, "big-endian" means putting the most significant byte first. In naming, it means putting the most significant concept first:

- **Big-Endian**: `project-component-variant-version.ext`
- **Little-Endian**: `version-variant-component-project.ext`

### Why It Matters

As the Central repository beautifully states:
> "Simple naming conventions create self-documenting systems."

When you sort files alphabetically, big-endian names naturally cluster related content:
```
shneiderman-owls-forest.html
shneiderman-owls-forest.md
shneiderman-owls-forest.yml
shneiderman-owls-forest-design-journal.md
shneiderman-owls-forest-old-1.html
shneiderman-owls-forest-old-2.html
```

## The BREWSTER Rules

### 1. Most Significant First
Always lead with the broadest category:
- ✅ `lloooomm-vm-architecture.md`
- ❌ `architecture-vm-lloooomm.md`

### 2. Natural Hierarchy
Follow conceptual hierarchy from general to specific:
- ✅ `project-subsystem-component-detail.ext`
- ❌ `detail-component-subsystem-project.ext`

### 3. Shared Base Names (The Sacred Trinity)
Main files share exact base names:
```
thing.yml    # soul/data
thing.md     # character/documentation
thing.html   # presentation
```

### 4. Descriptive Suffixes for Variants
Use suffixes to indicate relationships while maintaining clustering:
```
rfk-jr.md                    # The man (no soul)
rfk-jr-brain-worm.yml       # The worm (all soul, deeply embedded)
thing-v2.html               # Version variant
thing-experiment.html       # Experimental variant
thing-old-1.html           # Backup
```

### 5. Time-Based Suffixes Go Last
When using dates or versions, put them at the end:
- ✅ `project-report-2024-12-28.md`
- ❌ `2024-12-28-project-report.md`

## Real-World Examples

### From Central's Tagging Convention:
```
builder-base-llvm18-rust183-cuda124
builder-web-pnpm-playwright
runner-huggingface-torch-cuda121
```

This enables powerful filtering:
- All builders: `builder-*`
- All web builders: `builder-web-*`
- All CUDA images: `*-cuda*`

### From LLOOOOMM Characters:
```
shneiderman-owls-forest.yml
shneiderman-owls-forest.md
shneiderman-owls-forest.html
shneiderman-owls-forest-design-journal.md
shneiderman-owls-simulation-minsky-memo.html
```

### From Workflow Naming:
```
docker-build-base.yml
docker-build-web.yml
docker-push-all.yml
terraform-apply-prod.yml
```

## The Camel Case Corollary

As noted in the goals system:
> "Camel words: camel case in 'big endian' word order, so when it's alphabetically sorted, related names are next to each other"

Example goal names:
```
bigQueryOptimize
bigQuerySyntax
bigQueryPatterns
```

## Benefits of Big-Endian Naming

1. **Natural Clustering**: Related files group together automatically
2. **Self-Documenting**: File names tell their story from general to specific
3. **Easy Filtering**: Wildcards become powerful (`project-*`, `*-test`)
4. **Cognitive Ease**: Humans scan left-to-right, important info first
5. **Future-Proof**: New variants slot in naturally without reorganization

## Common Anti-Patterns to Avoid

### Little-Endian Disease
❌ `test-unit-authentication-user.js`
✅ `user-authentication-unit-test.js`

### Random Middle Syndrome
❌ `report-final-project-q4-2024.md`
✅ `project-report-q4-2024-final.md`

### Prefix Pollution
❌ `new-new-final-FINAL-project-doc.md`
✅ `project-doc-v4-final.md`

## The Philosophy in Practice

From Micropolis save files:
> "The save file format uses big-endian (Motorola/MAC) byte ordering."

Even at the byte level, big-endian thinking prevails!

## Special Cases

### Chemical Formulas & Technical Names
Sometimes domain conventions override:
- `H2O-analysis.md` (not `water-analysis.md`)
- `RFC-1234-implementation.md` (RFC number is significant)

### Temporal Sequences
For time-series data, consider audience:
- Archival: `sensor-data-2024-12-28.csv` (sensor first)
- Daily reports: `2024-12-28-sensor-daily.csv` (date first for chronological sorting)

## BREWSTER's Wisdom

"Think of naming like addressing a letter:
- Country → City → Street → House → Apartment
- Project → Module → Component → Feature → Version

The postal service sorts by country first, not by apartment number. Your filesystem should work the same way."

## Implementation Checklist

- [ ] Lead with project/system name
- [ ] Follow with subsystem/module
- [ ] Add component/feature
- [ ] Append variants/versions
- [ ] Use consistent separators (hyphens for words, underscores for systems)
- [ ] Test by sorting - do related files cluster?

## Conclusion

Big-endian naming isn't just a convention—it's a philosophy of thoughtful organization that leverages the natural sorting mechanisms of our tools to create self-organizing systems.

As we name, so we think. As we think, so we organize. As we organize, so we understand.

---

*"In the beginning was the Word, and the Word was big-endian."* - BREWSTER, 2024 