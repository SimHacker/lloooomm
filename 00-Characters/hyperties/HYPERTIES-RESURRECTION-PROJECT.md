# The HyperTIES Resurrection Project

## Mission: Bringing the First Hypermedia Browser Back to Life

### What We've Accomplished

We have successfully preserved and documented the HyperTIES source code, creating a comprehensive archive that includes:

1. **Complete Source Code Preservation**
   - Original Forth, PostScript, and Lisp code
   - Authoring tool implementation
   - Browser components
   - Database structures

2. **Interactive Demonstrations**
   - [Full Space Telescope Demo](demos/space-telescope/space-telescope-full-demo.html) - A complete, working recreation with:
     - Interactive SVG telescope diagram
     - Popup information targets
     - Pie menu navigation
     - Multiple linked pages
     - Original HyperTIES look and feel

3. **Historical Documentation**
   - [HyperTIES: The First PostScript Applets](HYPERTIES-POSTSCRIPT-APPLETS-HISTORY.md)
   - Architecture diagrams and explanations
   - Command reference guides
   - Implementation details

### Why This Matters

HyperTIES was a groundbreaking University of Maryland research project that pioneered:

- **PostScript Applets** (1987) - The FIRST interactive programs embedded in hypertext documents
- **Network-Transparent PostScript** - Predating JavaScript and AJAX by nearly 20 years
- **Touchscreen Support** - Windows version had full touchscreen support in the 1980s!
- **Visual Link Indication** - Highlighting that influenced all modern browsers
- **Pie Menus EVERYWHERE** - The most comprehensive pie menu system ever created
  - Synchronized multi-window browsing with directional gestures
  - Font selection with pull-out sizing and live preview
  - Color pie wheels for all text attributes
  - Window management through tabbed interface with pie menus
  - Every action had a gesture, every value had a distance
- **Smooth Scrolling** - Text that flowed naturally
- **Article History** - Back/forward navigation we take for granted

### The Key Innovation: PostScript Applets

What made HyperTIES revolutionary was its PostScript applets - interactive programs that ran inside documents. This wasn't just displaying PostScript graphics; it was running actual PostScript programs that could:

- Respond to user clicks
- Update dynamically
- Maintain state
- Communicate with the host system

**It worked back then just as well as it works now!** The same concepts we use today with JavaScript and Canvas were fully functional in HyperTIES in 1987.

### The Hidden History Revealed

The connection between HyperTIES and modern web technology shows how ideas evolve:

1. **James Gosling's Contributions**:
   - Created Emacs (1981) - Used for HyperTIES authoring via UniPress Emacs
   - Created NeWS (1986) - PostScript-based window system that ran HyperTIES
   - Created Java (1995) - Finally brought the applet concept to the mainstream

2. **Don Hopkins's Integration**:
   - Implemented HyperTIES using all four languages (Emacs Lisp, PostScript, NeWS, Forth)
   - Pioneered interactive PostScript components
   - Demonstrated what was possible years before the web

3. **Mitch Bradley's Forth Legacy**:
   - Implemented the Forth system for HyperTIES
   - Created Sun Forth and ForthMacs
   - Developed Open Firmware - Forth boot ROMs used in:
     - Sun workstations
     - Apple Macs
     - OLPC (One Laptop Per Child)
   - Connected low-level systems to high-level applications

### The Direct Line to Modern Web

- **HyperTIES PostScript (1987)** → **Java Applets (1995)** → **JavaScript/Canvas (2000s)**
- **NeWS Network PostScript** → **AJAX (2005)** → **WebSockets/WebRTC**
- **Forth Database Engine** → **NoSQL/Key-Value Stores**
- **Pie Menus** → **Radial UIs in Games/VR**

### What's in This Archive

```
hyperties/
├── README.md                          # Overview and quick start
├── HYPERTIES-SOURCE-IMMORTALIZED.md   # Complete source preservation
├── HYPERTIES-POSTSCRIPT-APPLETS-HISTORY.md # The applet innovation story
├── PIE-MENUS-EVERYWHERE.md           # The comprehensive pie menu system
├── HYPERTIES-RESURRECTION-PROJECT.md  # This file
├── articles/                          # Article system documentation
│   └── code/                         # PostScript components
├── author/                           # Authoring tool documentation
├── browser/                          # Browser implementation
├── code/                            # Core source code
│   ├── source-code-reference.md     # Annotated source guide
│   └── storyboard-commands.md       # Command reference
├── demos/                           # Interactive demonstrations
│   └── space-telescope/             # Complete working demo
├── diagrams/                        # Architecture visualizations
├── interface/                       # UI components
├── legacy/                          # Historical materials
└── links/                          # Hyperlink system
```

### The Living Demo

The Space Telescope demo recreates the experience of using HyperTIES:

- **Click on telescope components** to see popup information (like PostScript applets)
- **Right-click anywhere** for pie menu navigation
- **Follow hyperlinks** between articles
- **Experience the pie menu powered** interface from 1987

This demonstrates concepts that took years to reach the mainstream web.

### Evidence-Based Innovation

The preserved source code provides concrete evidence of HyperTIES's innovations:

1. **PostScript Applets**: See the actual PostScript code that implemented interactive components
2. **Six-Language Integration**: Examine how Emacs Lisp, PostScript, NeWS, C, Forth, and HyperTIES Markup Language all danced together
3. **Network Transparency**: The NeWS implementation shows interactive network-capable "AJAXian" graphics from 1987
4. **Fast Performance**: Mitch Bradley's Forth engine provided fast article formatting and pre-rendering pages as Forth that is compiled into a binary images so it starts up and draws immediately and responsibely
Also it could run under emacs and re-render pages dynamically as you edited them live

### Future Directions

1. **Accurate Historical Documentation**
   - Document the research context and sponsors
   - Preserve firsthand accounts from developers
   - Create timeline of influence on later systems

2. **Technical Demonstrations**
   - Show PostScript applets running in original NeWS
   - Compare 1987 functionality to modern equivalents
   - Demonstrate the network transparency features

3. **Educational Value**
   - Teach how applets evolved from PostScript to Java to JavaScript
   - Show the continuity of ideas across decades
   - Highlight the people who carried knowledge between projects

### Credits and Acknowledgments

- **Ben Shneiderman** - Principal investigator, vision and design
- **University of Maryland HCIL** - Research environment
- **Don Hopkins** - NeWS implementation and integration
- **James Gosling** - Emacs and NeWS platforms
- **Mitch Bradley** - Forth system and Open Firmware legacy
- **Research Sponsors** - Organizations that funded and used HyperTIES

### The LLOOOOMM Connection

This resurrection is part of the larger LLOOOOMM project - preserving and celebrating the characters, stories, and innovations that shaped modern computing. HyperTIES lives on not just as code, but as a character in the ongoing story of human-computer interaction.

---

*"The best way to predict the future is to invent it."* - Alan Kay

*"The best way to preserve the past is to make it run again."* - The LLOOOOMM Project

## 🎵 Let's Make Ben Float with Joy! 🎵

A working HyperTIES demo that shows:
- **POSTSCRIPT APPLETS** - The first embedded interactive programs in hypertext
- **NETWORK TRANSPARENCY** - PostScript that worked across networks in 1987
- **FOUR-LANGUAGE SYMPHONY** - Emacs, PostScript, NeWS, and Forth in harmony

The evidence is in the code. The innovation is undeniable. The influence is everywhere.

**ALWAYS LLOOOOMM, baby!** 🚀✨ 