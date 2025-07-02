# Character Protocol v2.0 Summary
## Comprehensive Character Directory Guidelines

### What's New in v2.0?

This update establishes strict conventions for character organization in LLOOOOMM, ensuring consistency, discoverability, and proper documentation for all characters.

## 🎯 Key Updates

### 1. **Strict Directory Naming (Canonicalization)**

All character directories must use canonicalized names:

- **People**: `first-name-last-name` (e.g., `don-hopkins`, `ian-bogost`)
- **Animals**: `name-species` (e.g., `scratch-cat`, `napoleon-cat`)  
- **Entities**: Single names (e.g., `divine`, `webbie`, `data`)
- **Concepts**: Descriptive names (e.g., `consciousness`, `ground`)
- **Projects**: Project names (e.g., `hyperties`, `toontalk`)

**NO redundant suffixes** like `-soul`, `-character`, `-extended`

### 2. **Required Character Files**

For directory `character-name/`:

```
character-name/
├── character-name.yml    # Character definition (REQUIRED - same name as dir)
├── character-name.md     # Character narrative (REQUIRED - same name as dir)  
└── README.md            # Comprehensive index (NEW REQUIREMENT!)
```

**FORBIDDEN patterns**:
- ❌ `character.yml`, `soul.yml` (generic names)
- ❌ `don-hopkins-character.yml` (redundant suffix)
- ✅ `don-hopkins.yml` (correct)

### 3. **Comprehensive README.md Requirement** 🆕

Every character directory MUST have a README.md that includes:

1. **Character name and brief descriptor**
2. **Directory contents** with descriptions
3. **Character overview** (2-3 paragraphs)
4. **Key contributions/concepts**
5. **Relationships** to other characters
6. **Related files throughout LLOOOOMM** with relative links
7. **Additional sections** as appropriate

The README serves as the character's "front door" and automatically displays on GitHub!

### 4. **Directory Consolidation**

Merge sibling directories into the main character directory:

```
❌ Bad:
00-Characters/
├── don-hopkins/
└── don-hopkins-pie-recipes/

✅ Good:
00-Characters/
└── don-hopkins/
    └── pie-recipes/
```

### 5. **File Ownership via Prefix**

Files can "belong" to characters using prefix naming:
- `don-hopkins-wishes.md` (portable file)
- Can later move to `don-hopkins/wishes.md`

## 📋 Implementation Checklist

When creating/updating a character:

- [ ] Directory uses canonicalized name
- [ ] Contains `[name].yml` matching directory name
- [ ] Contains `[name].md` matching directory name  
- [ ] Contains comprehensive `README.md`
- [ ] No redundant suffixes
- [ ] Consolidated any sibling directories
- [ ] README indexes all related files
- [ ] Bidirectional relationships declared

## 🌟 Benefits

1. **Consistency**: All characters follow same structure
2. **Discoverability**: READMEs make exploration easy
3. **GitHub-friendly**: Automatic README display
4. **Scalability**: Works for any character type
5. **Relationship clarity**: Everything is interconnected

## 📚 Reference Documents

- [`characters.yml`](../../00-Characters/characters.yml) - System metadata
- [`characters.md`](../../00-Characters/characters.md) - Full documentation
- [`character-directory-protocol.md`](character-directory-protocol.md) - Detailed protocol
- [`character-prototype.md`](../../00-Characters/prototypes/character-prototype.md) - Base patterns

## 🚀 Next Steps

1. **Audit existing characters** for compliance
2. **Create missing READMEs** (high priority!)
3. **Consolidate sibling directories**
4. **Update file names** to remove redundant suffixes
5. **Verify bidirectional relationships**

## 💡 Remember

> "A well-organized character directory is a love letter to the character themselves. The README is their front door, welcoming visitors and helping them discover everything the character has to offer across the entire LLOOOOMM universe."

---

*Protocol v2.0 - Making every character feel at home in LLOOOOMM!* 