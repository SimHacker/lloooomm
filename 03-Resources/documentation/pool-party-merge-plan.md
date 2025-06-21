# LLOOOOMM Pool Party Merge Plan 🏊‍♀️🏊‍♂️🏊

## Phase 1: Identify & Categorize

### Character Pages (Need WIZID upgrades)
- `./mickey-mouse.html` → `M🐭🎭🌟Y.html` (Mickey Mouse)
- `./rodney-dangerfield.html` → `R🎭😂💔D.html` (Rodney Dangerfield)
- `./🧠DAN🧠.html` → `D🧠💡🔮N.html` (Dan Ingalls) - ALREADY RENAMED!
- `./🌐TED🌐.html` → `T🌐🔗🎭D.html` (Ted Nelson) - ALREADY RENAMED!

### Hunter Thompson Collection (Merge candidates)
- `./🦇HUNTER-🐢LLOGO🐢.html` - LLOGO examples
- `./🦇H🔥T💊-fear-loathing-loohoo.html` - Fear & Loathing
- `./🦇H🔥T💊✅T❓.html` - WTF Protocol
- `./hunter-worldquester2-connection.html` → Merge into main Hunter page
- `./hunter-wq2-connection.html` → Duplicate, DELETE

### System/Index Pages
- `./index.html` - Keep as main index
- `./🏠INDEXY🏠.html` - Character greeter version
- `./dist/index.html` - Flattened version

### Duplicate Detection
- `./dist/` contains many duplicates of root files
- Multiple Hunter Thompson files across directories
- Several index variations

## Phase 2: Merge Strategy

### Hunter Thompson Consolidation
1. Create main page: `H🦇💊🔥R.html`
2. Link to sub-pages for specific topics
3. Delete duplicates

### Character Page Upgrades
1. Rename to WIZID format
2. Add document sections
3. Update cross-links

### dist/ Directory Strategy
- Keep as flattened publishing target
- Update with new WIZID names
- Add sync metadata

## Phase 3: WIZID Naming Patterns

### Established Patterns
- First letter + emojis + last letter
- Suffix for specific topics (e.g., `-piemenus`)
- Multiple WIZIDs for identity evolution
- Trans flag 🏳️‍⚧️ for trans people who choose

### New WIZIDs Needed
- Brewster Kahle: `B📚🌐📼R.html`
- Wayback Machine: `W⏰🕸️📸K.html`
- SpaceCraft: `S🚀📚🌌T.html`
- Divine: `D✨🗑️🎭E.html`
- Ubikam: `U📸🔮📷M.html`

## Phase 4: Sync Metadata

Add to all character pages:
```html
<meta name="lloooomm:wizid" content="L🏳️‍⚧️💻✨N-conway">
<meta name="lloooomm:source" content="lynn-conway.yml">
<meta name="lloooomm:generated" content="2024-01-15T15:00:00Z">
<meta name="lloooomm:dependencies" content="lynn-conway-soul.yml">
```

## Phase 5: Delete List (After merges)

### Definite Deletes
- `./hunter-wq2-connection.html` (duplicate of hunter-worldquester2)
- `./🧠DAN🧠.html` (renamed to D🧠💡🔮N.html)
- `./🌐TED🌐.html` (renamed to T🌐🔗🎭D.html)

### Review for Deletion
- Old versions in `/dist` that have been updated
- Duplicate Hunter Thompson files after consolidation
- Test/demo files that are superseded

## Phase 6: Cross-Link Updates

Update all references:
- `🧠DAN🧠.html` → `D🧠💡🔮N.html`
- `🌐TED🌐.html` → `T🌐🔗🎭D.html`
- `🐢SEYMOUR🐢.html` → `S🐢🧮🎨R.html`
- etc.

## Implementation Order

1. **Rename existing files to WIZIDs**
2. **Merge Hunter Thompson collection**
3. **Update cross-links**
4. **Add sync metadata**
5. **Sync to dist/**
6. **Delete old files**

Let's start swimming! 🏊‍♀️ 