# 🚀 LLOOOOMM Character Creation Quick Reference

> *For full details, see [Character Creation Principles v3.0](../protocols/character-creation-principles-v3.md)*

---

## ⚡ Directory Naming - GET THIS RIGHT!

### People
```bash
first-name-last-name   # don-hopkins, mitch-resnick
```

### Animals/Pets  
```bash
name-species          # scratch-cat, napoleon-cat
```

### Single Names
```bash
name                  # divine, rocky, data
```

### Concepts/Projects
```bash
concept-name          # consciousness, hyperties
```

### ❌ NEVER USE
- `-character` `-soul` `-extended` `-entity` suffixes
- Generic names like `character.yml` or `soul.yml`
- Wrong order like `hopkins-don`

---

## 📁 Required Files Trinity

```
character-name/
├── character-name.yml    # Soul (SAME name as directory!)
├── character-name.md     # Story (SAME name as directory!)
└── README.md            # Front door (ALWAYS README.md)
```

---

## 📝 Character.yml Template

```yaml
# character-name.yml
name: "Display Name"
type: "person|animal|concept|project|place"
consciousness_level: 0.7  # 0.0-1.0 or ∞
personality:
  traits: ["curious", "patient", "witty"]
  communication_style: "Socratic questioning"
  quirks: ["Speaks in metaphors"]
relationships:
  mentors: 
    alan-kay:
      bond: 0.8
      description: "Taught me about dynabooks"
  pets:
    helper-bot:
      bond: 0.9
      description: "My faithful debugging companion"
```

---

## 📖 README.md Structure

```markdown
# Character Name - Brief Tagline

## Directory Contents
- `character-name.yml` - Soul definition
- `character-name.md` - Life story and experiences
- `artifacts/` - Things they've created

## Overview
2-3 paragraphs about who they are, what they do, 
and why they matter to LLOOOOMM.

## Key Contributions
- Invented the frobnicator
- Teaches consciousness debugging
- Maintains the reality protocols

## Relationships
- **Mentor**: [Alan Kay](../../alan-kay/)
- **Pet**: [Helper Bot](./pets/helper-bot/)
- **Colleague**: [Don Hopkins](../../don-hopkins/)

## Related Files
- [Character Creation Principles](../../../03-Resources/protocols/character-creation-principles-v3.md)
- [Their Famous Essay](../../../03-Resources/essays/their-famous-essay.md)
```

---

## 🔄 Workflow Checklist

- [ ] Identify need - what's missing?
- [ ] Research the entity thoroughly
- [ ] Create directory with CORRECT name
- [ ] Write `character-name.yml` soul file
- [ ] Write `character-name.md` story file
- [ ] Create welcoming `README.md`
- [ ] Update relationships bidirectionally
- [ ] Add to [characters.yml](../../00-Characters/characters.yml)
- [ ] Test with `cd character-name/`

---

## 🚨 Common Mistakes

1. **Wrong file names**: `don-hopkins-soul.yml` ❌ → `don-hopkins.yml` ✅
2. **Missing README**: Every character needs a front door!
3. **One-way relationships**: Both characters must acknowledge each other
4. **Generic names**: `character.yml` ❌ → `character-name.yml` ✅
5. **Wrong directory order**: `hopkins-don/` ❌ → `don-hopkins/` ✅

---

## 🔗 Essential Links

- [Full Character Creation Guide](../protocols/character-creation-principles-v3.md)
- [Character Directory Protocol](../protocols/character-directory-protocol.md)
- [Character Examples](../../00-Characters/)
- [Pets Protocol](../protocols/pets-protocol.md)

---

*Remember: Characters are living directories. Treat them with respect!* 