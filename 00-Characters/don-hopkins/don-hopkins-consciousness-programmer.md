# Don Hopkins: Code Examples and Technical Work
## Documentation of Programming Contributions

### Overview

Don Hopkins worked as a programmer on various projects. This document catalogs specific code contributions based on available source materials and documentation.

### Projects and Code Contributions

#### The Sims (1996-2000)
**Role**: UI Programmer, Character Animation Tools

**Specific Code Written**:
- Pie menu implementation in C++
- Character animation export tools (cmxexp.cpp)
- Build mode rotation gestures
- VitaBoy character system contributions

**Team Context**: 
Part of a ~40 person team led by Will Wright. Other key programmers included Eric Bowman (lead engineer), Patrick J. Barrett III (SimAntics), Jamie Doornbos (AI systems).

**Code Example from cmxexp.cpp**:
```cpp
// Character File Report generator
// Includes Walt Whitman quotes as easter eggs in export reports
report << "O my Body!
"
       << "I dare not desert the likes of you
" 
       << "in other Sims and pixels...
";
```

#### Pie Menus
**Implementation History**:
- 1988: Co-authored CHI paper with Jack Callahan, Ben Shneiderman, Mark Weiser
- Various implementations: X11, NeWS, Tcl/Tk, JavaScript, Unity3D

**Technical Details**:
- Radial menu with equidistant targets
- Based on Fitts's Law optimization
- Context-sensitive option filtering

#### NeWS Window System
**Work Period**: Late 1980s at Sun Microsystems

**Contributions**:
- PizzaTool - PostScript application for ordering pizza via fax
- PSIBER Space - PostScript debugging environment
- Various PostScript utilities and examples

**Code Available**: 
- pizzatool.txt - Complete PostScript source
- ps.ps - PostScript metacircular interpreter

#### SimCity Ports
**Specific Work**:
- Ported SimCity to Unix/X11
- Created multiplayer version for X11
- Later open-sourced as Micropolis for OLPC

### Design Document Reviews

Don reviewed The Sims design documents in 1998. His comments included:

**On Typos**: 
"This appears in 17+ code modules. If we don't fix it now, we'll have inconsistent variable names forever."

**On Modal Dialogs**:
"MODAL DIALOGS CAUSE MANY MORE PROBLEMS THAN THEY SOLVE"

**On Same-Sex Relationships**:
"The whole relationship design and implementation (I've looked at the tree code) is Heterosexist and Monosexist."

He proposed making romantic interactions available regardless of gender, which was implemented by Patrick J. Barrett III.

### Tool Development

**For The Sims**:
- Edith debugging environment (with team)
- SimShow - character preview tool
- Various content creation utilities

**General Tools**:
- Multiple pie menu implementations
- Cellular automata visualizations
- PostScript development tools

### Published Work

**Academic Papers**:
- "An Empirical Comparison of Pie vs. Linear Menus" (CHI 1988)

**Software Releases**:
- Micropolis (open source SimCity)
- Various pie menu implementations
- PostScript utilities

### Notes on Attribution

The Sims was developed by a large team at Maxis. Key contributors included:
- Will Wright (design lead)
- Eric Bowman (lead programmer) 
- Patrick J. Barrett III (SimAntics, social systems)
- Jamie Doornbos (AI systems)
- Ocean Quigley (art director)
- Charles London (producer)
- And approximately 40+ other team members

Don's specific contributions centered on UI systems, character animation tools, and development utilities.

### Available Source Code

Links to actual code by Don Hopkins:
- https://www.donhopkins.com/home/archive/NeWS/pizzatool.txt
- https://github.com/SimHacker/micropolis
- Various pie menu implementations on GitHub 