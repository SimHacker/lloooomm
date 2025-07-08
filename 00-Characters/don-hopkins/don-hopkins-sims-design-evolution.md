# The Sims: Design Document Evolution
## Documentation of design changes from available sources

### Early Design Documents

#### Happy Fun Home (1996)
- Working title for what became The Sims
- Will Wright's initial concept document
- Focus on home building and decoration
- Basic needs system outlined

#### Happy Friends Home (1996)
- Revised title and expanded scope
- Added social interactions
- Introduced character customization
- Early sketches of UI layout

### Design Document Drafts

#### Draft 3 (August 7, 1998)
Don Hopkins's review comments preserved in archives:

**Romance System Issues:**
- Original code checked gender before allowing romantic interactions
- Same-gender romantic attempts triggered slap animation
- Hopkins identified this as problematic in review

**Specific Comments:**
- "The whole relationship design is Heterosexist and Monosexist"
- Proposed two-axis attraction model (0-100 for each gender)
- Suggested removing gender checks from romantic interactions

**Modal Dialog Critique:**
- "MODAL DIALOGS CAUSE MANY MORE PROBLEMS THAN THEY SOLVE"
- Advocated for undo system instead of confirmations
- Implemented in final game

#### Technical Design Elements

**UI Architecture:**
- Modular panel system
- Progressive disclosure of information
- Context-sensitive controls

**Build Mode:**
- Grid-based placement
- Rotation controls
- Wall drawing tools

### Implementation Timeline

**1996-1997: Prototyping**
- Basic simulation running
- Early UI experiments
- Core team formation

**1998: Major Design Decisions**
- Romance system redesign
- UI architecture finalized
- Tool development

**1999: Polish and Content**
- Bug fixing
- Performance optimization
- Content creation

**2000: Ship**
- February 4, 2000 release
- Post-launch patches

### Key Design Principles (from documents)

1. **Object-Driven AI**
   - Behaviors stored in objects
   - Allows expansion without recompilation

2. **Progressive Disclosure**
   - Basic controls visible
   - Advanced options available on demand

3. **No Modal Dialogs**
   - Undo instead of confirmation
   - Non-blocking property panels

4. **Inclusive Design**
   - Gender-neutral romantic interactions
   - Accessible controls

### Team Contributions

Design decisions were collaborative efforts involving:
- Will Wright (Design lead)
- Multiple programmers
- UI/UX designers
- QA testers

The final game reflected input from the entire team, with specific features often being the result of group discussions and iterations rather than individual contributions. 