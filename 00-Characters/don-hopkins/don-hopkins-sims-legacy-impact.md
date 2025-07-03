# Don Hopkins: Work on The Sims
## Technical Contributions and Design Document Reviews

### Role and Timeline

Don Hopkins worked as a UI programmer and tool developer on The Sims from 1996-2000 as part of the Maxis team.

### Specific Technical Contributions

#### UI Systems
- Implemented pie menus for object interaction
- Added "tilt-assist" to help players click on moving Sims
- Created build mode rotation gestures (press-and-hold to rotate)
- Worked on grid-snapping placement system

#### Development Tools
- Contributed to character animation export tools (cmxexp.cpp)
- Worked on debugging tools that shipped hidden in the game
- Created various content creation utilities

#### Code Examples
From cmxexp.cpp (character export tool):
```cpp
// Includes Walt Whitman quotes in export reports
report << "O my Body!
"
       << "I dare not desert the likes of you
"
       << "in other Sims and pixels...
";
```

### Design Document Reviews (1998)

Don reviewed early design documents and provided feedback:

#### Typo Corrections
Found and corrected "DONTROL PANEL UI" → "Control Panel UI" noting: "This appears in 17+ code modules. If we don't fix it now, we'll have inconsistent variable names forever."

#### Modal Dialog Opposition
Strongly opposed confirmation dialogs with the comment: "MODAL DIALOGS CAUSE MANY MORE PROBLEMS THAN THEY SOLVE"

#### Romance System Feedback
Identified that the game rejected same-sex romantic interactions with violence. His review stated: "The whole relationship design and implementation (I've looked at the tree code) is Heterosexist and Monosexist."

He proposed a two-axis attraction model but the final implementation by Patrick J. Barrett III was simpler - just removing gender checks entirely.

### Team Context

The Sims was developed by a team of approximately 40-50 people including:
- Will Wright (creator/lead designer)
- Eric Bowman (lead programmer)
- Patrick J. Barrett III (SimAntics visual programming)
- Jamie Doornbos (AI systems)
- Ocean Quigley (art director)
- Charles London (producer)
- Many other programmers, artists, and designers

### Implementation Details

#### Pie Menus
- Based on his earlier research (CHI 1988 paper)
- Context-sensitive options
- Maximum 8 items per menu
- Dynamic filtering based on object state

#### Build Mode
- Grid-based placement (already designed before Don joined)
- Added visual feedback for valid/invalid placement
- Rotation using mouse gestures instead of separate tools

### Post-Launch Work

After The Sims shipped, Don continued working on tools and later projects:
- Ported SimCity to Unix (became Micropolis)
- Open-sourced SimCity for OLPC
- Various pie menu implementations for other platforms

### Available Documentation

- Design document PDFs with Don's handwritten annotations
- Source code examples from The Sims tools
- CHI 1988 pie menu paper
- Various Medium posts by Don about his work

### Notes

This documentation is based on available source materials including design documents, code examples, and Don's own writings. The Sims was a collaborative effort by a large team at Maxis, with each member contributing their expertise to different systems. 