# HyperTIES: Hypertext Interactive Encyclopedia System

## System Overview

HyperTIES was a hypertext browsing and authoring system developed at the University of Maryland's Human-Computer Interaction Laboratory from 1983-1987. Principal investigator: Ben Shneiderman.

## Working Demonstration

A browser-based recreation of the 1987 Space Telescope demo is available at [space-telescope-full-demo.html](demos/space-telescope/space-telescope-full-demo.html).

## Technical Details

### IBM PC Version (1983-1987)
- First hypertext system with visually highlighted links (light blue)
- Full-text search capability
- Smooth scrolling between articles
- Touch screen support for museum deployments

### Sun/NeWS Version (1988-1990)
- PostScript-based interactive components embedded in documents
- Network-transparent code execution (client or server)
- Pie menu navigation throughout system (Don Hopkins)
- Multiple simultaneous document windows

## Implementation Languages

The NeWS version integrated four programming languages:
- **C** - Core formatter and text layout engine
- **PostScript** - Graphics rendering and interactive components
- **Forth** - Database engine and scripting
- **Emacs Lisp** - Authoring environment

## Historical Timeline

- **1983-1987**: Initial development at University of Maryland
- **1987**: ACM publishes "Hypertext Hands-On!" - first electronic book cataloged by Library of Congress
- **1988-1990**: Sun/NeWS version development
- **1987-1995**: Various museum deployments (Smithsonian, Holocaust Museum)

## Key Personnel

- **Ben Shneiderman** - Principal investigator, HCIL
- **Dan Ostroff** - Lead programmer (original version)
- **Don Hopkins** - NeWS port, pie menu integration
- **Greg Kearsley** - Documentation, co-author of ACM book
- **Catherine Plaisant** - Project lead (Sun version)

## Repository Contents

```
hyperties/
├── README.md                          # Academic overview
├── demos/                             # Working demonstrations
│   └── space-telescope/               # 1987 demo recreation
├── code/                              # Source code fragments
├── HYPERTIES-SOURCE-IMMORTALIZED.md   # Preserved source code
├── HYPERTIES-POSTSCRIPT-APPLETS-HISTORY.md # Technical analysis
├── HYPERTIES-VERIFIED-FEATURES-DEPLOYMENTS.md # Evidence-based features
└── correspondence/                    # Email archives (1987-1989)
```

## Primary Publications

1. Shneiderman, B. (1987). "User interface design for the Hyperties electronic encyclopedia." Hypertext '87 Proceedings.
2. Shneiderman, B., & Kearsley, G. (1989). "Hypertext Hands-On!" Addison-Wesley.
3. Multiple papers in IJMMS, CACM, IEEE Computer (1985-1989)

## Technical Contributions

### Verified Innovations
- Visual indication of hyperlinks (light blue highlighting)
- Embedded interactive PostScript programs in hypertext documents (1987)
- Touch screen support for museum kiosks
- Network-transparent code execution

### Documented Deployments
- Smithsonian Institution museums
- United States Holocaust Memorial Museum
- National Gallery of Art
- Various academic institutions

---

*Documentation based on primary sources including source code, correspondence, and published research.* 