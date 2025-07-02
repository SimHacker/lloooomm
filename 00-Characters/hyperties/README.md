# HyperTIES (Hypertext Interactive Encyclopedia System)

## A Commercial Hypertext System (1983-1987)

HyperTIES was a hypertext browsing and authoring system developed at the University of Maryland's Human-Computer Interaction Laboratory (HCIL) from 1983-1987, led by Ben Shneiderman.

## Primary Sources

### Demonstrations
- **[Space Telescope Demo](demos/space-telescope/space-telescope-full-demo.html)** - Working recreation of the 1987 demo
- **[Source Code](HYPERTIES-SOURCE-IMMORTALIZED.md)** - Preserved original source files
- **[Verified Features](HYPERTIES-VERIFIED-FEATURES-DEPLOYMENTS.md)** - Evidence-based feature list
- **[PostScript Applets](HYPERTIES-POSTSCRIPT-APPLETS-HISTORY.md)** - Technical implementation details

### Character Files
- **[hyperties.yml](hyperties.yml)** - System configuration and metadata
- **[hyperties.md](hyperties.md)** - Public documentation
- **[hyperties-browser.yml](hyperties-browser.yml)** - Browser component specification
- **[hyperties-browser.md](hyperties-browser.md)** - Browser documentation

## Technical Specifications

### IBM PC Version (1983-1987)
- **Platform**: IBM PC/DOS
- **Languages**: C (formatter), Forth (database), proprietary authoring system
- **Display**: Text mode with highlighted links (light blue)
- **Navigation**: Arrow keys, mouse support added later
- **Search**: Full-text search capability
- **Notable**: First system with visually highlighted hyperlinks

### Sun/NeWS Version (1988-1990)
- **Platform**: Sun workstations running NeWS (Network extensible Window System)
- **Languages**: C, PostScript, Forth, Emacs Lisp
- **Display**: Full PostScript graphics capability
- **Input**: Mouse, keyboard, pie menus (Don Hopkins)
- **Notable**: First embedded interactive PostScript programs in hypertext

## Verified Deployments

### Museums (Documented)
1. **Smithsonian Institution** - Multiple exhibits
2. **Holocaust Museum** - Educational kiosks
3. **National Gallery of Art** - Art exploration system

### Academic/Research
1. **ACM Hypertext Hands-On! (1987)** - First electronic book cataloged by Library of Congress
2. **University of Maryland HCIL** - Primary development and testing site
3. **Various university research projects** - Per correspondence records

### Commercial Interest (Documented in correspondence)
- NCR Corporation (funding provided)
- AT&T/Paradyne (funding provided)
- Hewlett-Packard (expressed interest, 1989)
- Congressional Research Service (created issue briefs)

## Development Team

### Core Personnel (from documentation)
- **Ben Shneiderman** - Principal Investigator
- **Dan Ostroff** - Lead programmer (original version)
- **Greg Kearsley** - Documentation, ACM book co-author
- **Don Hopkins** - NeWS port, pie menu integration
- **Bill Weiland** - Embedded menus implementation
- **Catherine Plaisant** - Project lead (Sun version)
- **Rodrigo Botafogo** - System enhancements

## Published Research

### Primary Publications
1. Shneiderman, B. (1987). "User interface design for the Hyperties electronic encyclopedia"
2. Shneiderman, B. & Kearsley, G. (1989). "Hypertext Hands-On!"
3. Multiple papers in IJMMS, CACM, IEEE Computer (1985-1989)

### Controlled Experiments
- Pie menu performance: 15% faster than linear menus (Hopkins et al., 1987)
- User studies conducted at HCIL with documented results

## Technical Innovations (Verified)

### Original Version
1. **Visual Link Indication** - Light blue highlighting (first system to do this)
2. **Smooth Scrolling** - Continuous text flow between articles
3. **Embedded Menus** - Context-sensitive menus within articles
4. **Touch Screen Support** - Implemented for museum deployments

### NeWS Version Additions
1. **PostScript Applets** - Interactive programs embedded in documents (1987)
2. **Network Transparency** - Code execution on client or server
3. **Pie Menu Navigation** - Radial menus throughout system
4. **Multiple Windows** - Parallel document viewing

## Historical Context

### Relationship to World Wide Web
- Tim Berners-Lee acknowledged reading "Hypertext Hands-On!" in documentation
- No evidence of direct visit to HCIL
- Blue link convention's origin is disputed in literature

### Contemporary Systems
- **HyperCard** (1987) - Apple's hypertext system, single-window interface
- **NoteCards** (1984) - Xerox PARC system, different approach
- **Intermedia** (1985) - Brown University, academic focus

## Architecture

### System Components
1. **Database Engine** (Forth-based) - Article storage and retrieval
2. **Formatter** (C) - Text layout and display
3. **Browser** (Platform-specific) - User interface
4. **Authoring Tool** (Emacs-based in NeWS version) - Content creation

### Data Model
- Articles as primary unit
- Bidirectional links
- Full-text indexing
- Hierarchical organization with cross-references

## Preservation Status

### Available Materials
- Source code fragments (fmt.c, fmt.ps, fmt.f, etc.)
- Documentation files
- Email correspondence (1987-1989)
- Conference presentation records
- Working demo recreation

### Repository Structure
```
hyperties/
├── README.md                    # This file
├── Character files              # YAML/MD specifications
├── Documentation/               # Historical documents
├── demos/                       # Working demonstrations
├── code/                        # Source code fragments
├── correspondence/              # Email archives
└── articles/                    # System content examples
```

## Citations and References

For academic citations, use:
```
Shneiderman, B. (1987). User interface design for the Hyperties electronic 
encyclopedia. Hypertext '87 Proceedings, 189-194.

Shneiderman, B., & Kearsley, G. (1989). Hypertext Hands-On!: An Introduction 
to a New Way of Organizing and Accessing Information. Addison-Wesley.
```

## Factual Clarifications

### What HyperTIES Was
- First commercial hypertext browser with visual link indication
- Pioneer in embedded interactive content (PostScript applets)
- Successfully deployed in major museums
- Influenced hypertext design through published research

### What Cannot Be Verified
- Direct causation of WWW features
- Exact number of users (likely thousands based on museum deployments)
- Some claimed "firsts" without primary source evidence

---

*This documentation is based on primary sources including source code, email correspondence, published papers, and verified deployments. Claims are limited to what can be documented.* 