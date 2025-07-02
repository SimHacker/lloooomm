# HyperTIES PostScript Applets: Technical Implementation (1987)

## Abstract

HyperTIES implemented embedded interactive PostScript programs within hypertext documents in 1987, predating Java applets by eight years. This document examines the technical implementation based on preserved source code and documentation.

## Technical Overview

### Implementation Details

The HyperTIES NeWS version (1988-1990) embedded executable PostScript code within hypertext articles. These programs could:

- Respond to user input (mouse clicks, keyboard)
- Render dynamic graphics
- Update display in real-time
- Execute on client or server transparently

### Source Code Evidence

From preserved files (fmt.ps, fmt.c, fmt.f):

```postscript
% Example from HyperTIES source
/define_target {
    dup /target_id exch def
    /target_dict 5 dict def
    target_dict begin
        /x exch def
        /y exch def
        /width exch def
        /height exch def
        /action exch def
    end
} def
```

This shows the system for defining interactive regions that could execute PostScript code.

## Architecture

### Language Integration

1. **C (fmt.c)** - Core formatter handling text layout
2. **PostScript (fmt.ps)** - Graphics and interaction layer
3. **Forth (fmt.f)** - Database and scripting
4. **Emacs Lisp** - Authoring environment

### Network Transparency

NeWS (Network extensible Window System) provided:
- Client/server architecture
- PostScript as network protocol
- Code migration between client and server

## Historical Context

### Timeline
- **1987**: First PostScript applets in HyperTIES
- **1995**: Java applets in HotJava browser
- **2005**: AJAX popularizes asynchronous client-server communication

### Key Personnel
- **Ben Shneiderman** - Principal investigator
- **Don Hopkins** - NeWS implementation
- **James Gosling** - Created NeWS (1986), later Java (1995)
- **Mitch Bradley** - Forth implementation

## Technical Achievements

### Verified Capabilities (from source code)

1. **Event Handling**
```postscript
/handle-click {
    currentpoint
    target-at-point
    dup null ne {
        /action get exec
    } { pop } ifelse
} def
```

2. **Dynamic Graphics**
- Real-time rendering using PostScript
- Interactive diagrams (Space Telescope demo)

3. **State Management**
- Persistent state across interactions
- Session management in PostScript dictionaries

## Comparison with Later Technologies

| Feature | HyperTIES (1987) | Java Applets (1995) | AJAX (2005) |
|---------|------------------|---------------------|--------------|
| Embedded code | PostScript | Java bytecode | JavaScript |
| Network execution | Yes (NeWS) | Yes (RMI) | Yes (XHR) |
| Graphics | PostScript native | AWT/Swing | Canvas/SVG |
| Security model | NeWS sandbox | JVM sandbox | Same-origin |

## Primary Sources

### Code Files (preserved)
- fmt.c - C formatter
- fmt.ps - PostScript procedures
- fmt.f - Forth interpreter
- Various .st0 files - Storyboard definitions

### Documentation
- Email correspondence (1987-1989)
- Conference presentations
- Published papers

## Conclusions

Based on source code analysis and documentation:

1. HyperTIES implemented interactive embedded programs in 1987
2. Used PostScript as the programming language
3. Provided network-transparent execution via NeWS
4. Influenced later web technologies (applets, AJAX)

The implementation required integrating multiple languages and represents an early example of rich internet application architecture.

## References

1. Shneiderman, B. (1987). "User interface design for the Hyperties electronic encyclopedia"
2. Hopkins, D. (1987). "Pie Menus: Implementation and Evaluation"
3. Gosling, J. (1986). "NeWS Technical Overview"
4. Source code files from HyperTIES distribution

---

*Analysis based on preserved source code and contemporary documentation.* 