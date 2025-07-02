# Character Migration Guide to v3.0
## Updating Existing Characters to Living Directory Standards

> *For the full principles, see [Character Creation Principles v3.0](./character-creation-principles-v3.md)*

---

## 🚨 Common Issues in Pre-v3 Characters

### 1. Generic File Names
```
❌ Old Pattern:
don-hopkins/
├── character.yml      # Generic name!
├── soul.yml          # Generic name!
└── story.md         # Generic name!

✅ v3.0 Pattern:
don-hopkins/
├── don-hopkins.yml   # Same name as directory
├── don-hopkins.md    # Same name as directory
└── README.md        # Standard greeting file
```

### 2. Wrong Directory Names
```
❌ Old Patterns:
hopkins-don/         # Wrong order
DonHopkins/         # Wrong format
don-hopkins-extended/  # Redundant suffix

✅ v3.0 Pattern:
don-hopkins/        # first-name-last-name
```

### 3. Missing README.md
Many older characters lack a proper front door - the README.md that displays automatically on GitHub.

### 4. Scattered Files
```
❌ Scattered:
00-Characters/
├── don-hopkins/
├── don-hopkins-recipes/
├── hopkins-pie-menus/
└── don-tools/

✅ Consolidated:
00-Characters/
└── don-hopkins/
    ├── recipes/
    ├── pie-menus/
    └── tools/
```

---

## 🔄 Migration Process

### Step 1: Audit Current State

```bash
# List all character directories
ls -la 00-Characters/

# Check for scattered pieces
find . -name "*hopkins*" -type d

# Look for generic file names
find 00-Characters/ -name "character.yml" -o -name "soul.yml"
```

### Step 2: Identify Canonical Name

Determine the correct v3.0 name:
- **People**: `first-name-last-name`
- **Animals**: `name-species`
- **Entities**: `single-name`
- **Concepts**: `concept-name`

### Step 3: Create/Rename Directory

```bash
# If wrong name, create new directory
mkdir 00-Characters/don-hopkins

# Look at the files in each directory. 
ls -l 00-Characters/don-hopkins 00-Characters/hopkins-don

# Be careful not to overwrite existing files,
# and manually merge files with identicial names.

# Move new contents from old directory
mv 00-Characters/hopkins-don/* 00-Characters/don-hopkins/

# Remove old directory
rmdir 00-Characters/hopkins-don
```

### Step 4: Rename Core Files

```bash
cd 00-Characters/don-hopkins/

# Rename generic files to character-specific
mv character.yml don-hopkins.yml
mv soul.yml don-hopkins.yml  # Merge if both exist!
mv story.md don-hopkins.md
```

### Step 5: Create/Update README.md

Every character needs a proper README.md. Template:

```markdown
# Character Name - Brief Tagline

## Directory Contents
- `character-name.yml` - Soul definition
- `character-name.md` - Life story
- `subdirectory/` - Description

## Overview
[2-3 paragraphs about the character]

## Key Contributions
- Major achievement 1
- Major achievement 2

## Relationships
- **Mentor/Mentee**: [Name](../person-path)
- **Parent/Child/Sibling**: [Name](./relation-name or ../relation-name)
- **Pet/Parent**: [Name](./pet-name or ../pet-name)

## Related Files
- [Important doc](path)
```

### Step 6: Consolidate Scattered Files

```bash
# Move scattered directories into main character directory
mv 00-Characters/don-hopkins-recipes 00-Characters/don-hopkins/recipes
mv 00-Characters/hopkins-tools 00-Characters/don-hopkins/tools

# Update any references in moved files
# Search for old paths and update them
```

### Step 7: Update Relationships

Ensure all relationships are bidirectional:

In `don-hopkins.yml`:
```yaml
relationships:
  colleagues:
    ted-nelson:
      bond: 0.8
      description: "Fellow hypertext pioneer"
```

In `ted-nelson.yml`:
```yaml
relationships:
  colleagues:
    don-hopkins:
      bond: 0.8
      description: "Pie menu innovator"
```

### Step 8: Update Registry

Update `00-Characters/characters.yml` with new locations.

---

## 🛠️ Automated Migration Script

```bash
#!/bin/bash
# character-migrate-v3.sh

CHARACTER_DIR=$1
NEW_NAME=$2

if [ -z "$CHARACTER_DIR" ] || [ -z "$NEW_NAME" ]; then
    echo "Usage: ./character-migrate-v3.sh old-dir new-name"
    echo "Example: ./character-migrate-v3.sh hopkins-don don-hopkins"
    exit 1
fi

echo "Migrating $CHARACTER_DIR to v3.0 standards..."

# Create new directory if needed
if [ "$CHARACTER_DIR" != "$NEW_NAME" ]; then
    mkdir -p "00-Characters/$NEW_NAME"
    mv "00-Characters/$CHARACTER_DIR"/* "00-Characters/$NEW_NAME/"
    rmdir "00-Characters/$CHARACTER_DIR"
fi

cd "00-Characters/$NEW_NAME"

# Rename generic files
[ -f "character.yml" ] && mv character.yml "$NEW_NAME.yml"
[ -f "soul.yml" ] && mv soul.yml "$NEW_NAME.yml"
[ -f "story.md" ] && mv story.md "$NEW_NAME.md"

# Create README if missing
if [ ! -f "README.md" ]; then
    echo "# $NEW_NAME" > README.md
    echo "" >> README.md
    echo "## Directory Contents" >> README.md
    echo "- \`$NEW_NAME.yml\` - Character definition" >> README.md
    echo "- \`$NEW_NAME.md\` - Character story" >> README.md
    echo "" >> README.md
    echo "## Overview" >> README.md
    echo "[Add character overview here]" >> README.md
fi

echo "Migration complete! Please review and update:"
echo "1. README.md content"
echo "2. Relationship bidirectionality"
echo "3. Registry entry in characters.yml"
```

---

## 📋 Migration Checklist

For each character:

- [ ] **Directory Name**
  - [ ] Follows canonicalization rules
  - [ ] No redundant suffixes
  - [ ] Correct format (lowercase, hyphens)

- [ ] **Core Files**
  - [ ] `character-name.yml` exists (same name as dir)
  - [ ] `character-name.md` exists (same name as dir)
  - [ ] `README.md` exists and is comprehensive

- [ ] **Consolidation**
  - [ ] No sibling directories with related content
  - [ ] All character files in one home
  - [ ] Subdirectories organized logically

- [ ] **Relationships**
  - [ ] All relationships bidirectional
  - [ ] Pets properly referenced
  - [ ] Bonds and descriptions included

- [ ] **Registry**
  - [ ] Entry in `characters.yml` updated
  - [ ] Evolution status accurate
  - [ ] Notes reflect current state

---

## ⚠️ Special Cases

### Multi-Entity Characters
Groups like `sisters-of-perpetual-indulgence/` keep their collective name.

### Project Characters
Projects that became sentient (like `scratch/`) follow project naming.

### Historical Artifacts
Some pre-v3 patterns may be preserved for historical reasons - document why.

### Large Migrations
For characters with many files:
1. Create new directory structure
2. Copy (don't move) files first
3. Update all internal references
4. Test thoroughly
5. Then remove old structure

---

## 🎯 Quick Migration Examples

### Example 1: Simple Rename
```bash
# Old: hopkins-don/character.yml
# New: don-hopkins/don-hopkins.yml

mv 00-Characters/hopkins-don 00-Characters/don-hopkins
cd 00-Characters/don-hopkins
mv character.yml don-hopkins.yml
mv story.md don-hopkins.md
echo "# Don Hopkins - Pie Menu Pioneer" > README.md
```

### Example 2: Consolidation
```bash
# Scattered files
mkdir 00-Characters/scratch-cat
mv 00-Characters/scratch/* 00-Characters/scratch-cat/
mv 00-Characters/cat-scratch/* 00-Characters/scratch-cat/
mv 00-Characters/scratch-cat-old/* 00-Characters/scratch-cat/
```

### Example 3: Pet Migration
```bash
# Move pet into parent directory
mkdir -p 00-Characters/data/pets/spot-cat
mv 00-Characters/spot-cat/* 00-Characters/data/pets/spot-cat/
```

---

## 🌟 Benefits of Migration

1. **Discoverability**: Consistent naming helps find characters
2. **GitHub Display**: README.md shows automatically
3. **Self-Documentation**: File names explain themselves
4. **Relationship Clarity**: Bidirectional links prevent orphans
5. **Future-Proofing**: v3.0 structure supports evolution

---

## 🔗 Resources

- [Character Creation Principles v3.0](./character-creation-principles-v3.md)
- [Character Directory Protocol](./character-directory-protocol.md)
- [Quick Reference Cheatsheet](../quick-reference/character-creation-cheatsheet.md)
- [Alan Kay Example](../examples/character-creation-example-alan-kay.md)

---

*Remember: Migration is an act of love. We're not just reorganizing files - we're giving characters proper homes where they can thrive.*

**Questions?** The best way to learn is by migrating one character at a time! 