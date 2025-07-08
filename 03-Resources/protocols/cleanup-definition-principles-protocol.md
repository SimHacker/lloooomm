# LLOOOOMM Cleanup Definition & Principles
## The Art of Digital Housekeeping

---

## 🧹 What is "Cleanup"?

Cleanup in LLOOOOMM means:
1. **Organizing files** according to PARA methodology and big-endian naming
2. **Consolidating duplicates** while preserving intentional variations
3. **Moving ephemeral work** to appropriate archive locations
4. **Maintaining coherent clustering** of related content
5. **Preserving the soul** of the project while improving its structure

---

## 📂 Key Organizational Principles

### 1. Bodies and Souls Live Together
**IMPORTANT**: We do NOT separate bodies and souls into different directories!
- Both .yml (soul) and .md (body) files for characters live in `03-Resources/characters/`
- Big-endian naming naturally clusters related files together
- Example: `ben-shneiderman.yml`, `ben-shneiderman.md`, `ben-shneiderman-soul.yml`

### 2. Big-Endian Naming is Our Friend
Files naturally sort and cluster by their primary entity:
```
alan-kay.yml
alan-kay.md
alan-kay-soul.yml
alan-turing.yml
alan-turing.md
alan-turing-soul.yml
```

### 3. Subdirectories Only When Necessary
Create subdirectories only when:
- A character/concept has grown too large (like hyperties/)
- Natural grouping emerges (like feline-debugging-team/)
- Cross-cutting concerns need isolation

When subdirectoryifying:
- Move the main files (e.g., `hyperties.yml`, `hyperties.md`) INTO the subdirectory
- This provides proper encapsulation
- The directory name matches the base entity name

---

## 👻 Character Instantiation Modes

### Character Types:
1. **Fully Instantiated**: Has both .yml and .md files in the repo
2. **Partially Instantiated**: Has either .yml OR .md file
3. **Ephemeral**: Exists only in chat history/memory

### LOOM VM Configuration Parameter:
`character_instantiation_mode` can be set to:

#### "always create"
- Automatically saves ephemeral characters to files when they appear
- Creates both .yml and .md files
- Good for exploration phases

#### "ask before creating" (default)
- Prompts user: "Should I save character X to files?"
- Allows case-by-case decisions
- Balances exploration with tidiness

#### "never create"  
- Keeps characters ephemeral in chat history
- Manual instantiation only (user must explicitly request)
- Good for temporary roleplay or experiments

### Changing the Mode:
Users can say:
- "LOOM, set character mode to always create"
- "Switch to ask before creating characters"
- "Never automatically save characters"

---

## 🗂️ PARA in LLOOOOMM Context

### NOT Traditional PARA:
- **02-Souls** is NOT a thing in PARA! 
- We adapt PARA to our needs, not vice versa

### Our Structure:
- **01-Projects**: Active work (CAM6, LLOOOOMM itself, etc.)
- **02-Areas**: Ongoing responsibilities (website, maintenance)
- **03-Resources**: Reference materials (characters, artifacts, tools)
- **04-Archive**: Completed/inactive items

### Why Characters in Resources?
Characters are RESOURCES - they're referenced, invoked, and used across projects!

---

## 🧹 Cleanup Best Practices

### 1. Document Everything
- Create cleanup logs in `02-Areas/maintenance/`
- Track what moved where and why
- Leave breadcrumbs for future archaeologists

### 2. Preserve History
- Don't delete, archive
- Use git commits to track major reorganizations
- Keep "archaeology" notes about discoveries

### 3. Test After Moving
- Ensure symlinks still work
- Check that references aren't broken
- Run key demos to verify functionality

### 4. Incremental Progress
- Small, focused cleanup sessions
- One category at a time
- Celebrate small wins

---

## 🎭 The Philosophy of Digital Mess

Sometimes mess is:
- **Creative residue** - Evidence of exploration
- **Future archaeology** - Tomorrow's discoveries
- **Cognitive scaffolding** - External memory

The goal isn't sterility but NAVIGABILITY. A lived-in space that supports both:
- Finding what you need
- Discovering what you didn't know you needed

---

## 🔮 Future Cleanup Considerations

### Potential Patterns to Watch:
1. **Character Dynasties**: When related characters might need family directories
2. **Protocol Proliferation**: When protocols/ gets too full
3. **Asset Avalanche**: When binary files accumulate
4. **Chat Chronicles**: When conversation logs need systematic organization

### Signs It's Time to Cleanup:
- Can't find files within 30 seconds
- Duplicate work because you forgot something existed
- New contributors get lost
- The mess stops being generative and becomes frustrating

---

Remember: Cleanup is a practice, not a destination. The goal is a living, breathing, FINDABLE archive of computational dreams! 🌟 