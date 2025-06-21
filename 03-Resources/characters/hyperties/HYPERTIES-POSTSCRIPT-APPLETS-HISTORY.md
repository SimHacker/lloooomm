# HyperTIES: The First PostScript Applets (1987)

## The Untold Story of Interactive Embedded Components

HyperTIES wasn't just an early hypertext system - it was **the first system to implement what we now call "applets"**: embedded, interactive PostScript programs that ran inside hypertext documents. This happened in 1987, eight years before Java applets appeared in web browsers.

## The Critical Innovation: PostScript Applets in Hypertext

What made HyperTIES revolutionary wasn't just hyperlinks - it was the ability to embed live, interactive PostScript graphics directly in articles. These weren't static images. They were:

- **Interactive programs** that responded to user clicks and input
- **Dynamically rendered** using PostScript's programming capabilities  
- **Embedded in context** within hypertext articles
- **Safely sandboxed** within the document environment
- **Network-transparent** - could execute on client or server (predating AJAX by 20 years!)

This is EXACTLY what Java applets would do eight years later - but HyperTIES did it first with PostScript.

## It Worked Then Just As Well As It Works Now!

The remarkable thing about HyperTIES's PostScript applets is that they were fully functional in 1987. The same concepts we use today with JavaScript, Canvas, and AJAX were already working:

- **Event handling** - Click detection and response
- **Dynamic updates** - Real-time graphics changes
- **State management** - Maintaining application state
- **Network execution** - Code running where it made sense
- **Security sandboxing** - Safe execution of untrusted code

The technology was mature and capable - it just took the rest of the world years to catch up.

## The Four-Language Symphony

HyperTIES's implementation required an unprecedented integration of four programming languages, each chosen for its unique strengths:

### 1. **Emacs Lisp** - The Authoring Environment
- James Gosling created Emacs (1981)
- UniPress commercialized it as UniPress Emacs
- Don Hopkins used UniPress Emacs 2.20 to build the HyperTIES authoring tool
- The Lisp environment provided the extensibility needed for hypertext editing

### 2. **PostScript** - The Graphics and Applet Language
- Adobe created PostScript as a page description language
- HyperTIES pioneered using it for **interactive components**
- These PostScript "applets" could:
  - Draw dynamic graphics
  - Respond to mouse clicks
  - Animate and update in real-time
  - Execute complex programs within articles
  - Communicate over the network

### 3. **NeWS** - The Display System
- James Gosling created NeWS (1986) at Sun
- Network extensible Window System based on PostScript
- Provided the runtime for HyperTIES's PostScript applets
- Enabled network-transparent execution (code could run on client OR server)
- This network transparency predated AJAX by nearly 20 years!

### 4. **Forth** - The Database Engine
- Mitch Bradley implemented the Forth system for HyperTIES
- Provided high-performance article storage and retrieval
- Enabled the scripting needed for dynamic behavior
- Connected the authoring tool to the browser
- Mitch went on to create:
  - **Sun Forth** - Used in Sun workstations
  - **ForthMacs** - Forth for Macintosh
  - **Open Firmware** - Industry standard boot ROMs using Forth
    - Used in Sun SPARCstations
    - Used in PowerPC Macs
    - Used in OLPC (One Laptop Per Child)
  - This shows how HyperTIES technology influenced everything from boot ROMs to educational computers

## The People Who Connected It All

The same individuals appear at every crucial junction:

**James Gosling** - The Triple Creator:
1. Created Emacs → Used for HyperTIES authoring
2. Created NeWS → Used for HyperTIES display and PostScript applets
3. Created Java → Finally brought applets to the mainstream web

**Don Hopkins** - The Integration Visionary:
- Integrated all four languages into HyperTIES
- Pioneered PostScript applets in hypertext
- Evangelized the concept through NeWS development
- Showed what was possible years before the web

**Mitch Bradley** - The Systems Connector:
- Implemented Forth for HyperTIES database
- Created the bridge between low-level systems and high-level applications
- His Open Firmware brought Forth to millions of computers
- Connected embedded systems philosophy to interactive applications

**Ben Shneiderman** - The Design Visionary:
- Principal investigator at University of Maryland
- Insisted on embedded interactive graphics
- Pushed for touchscreen support (implemented in Windows version)
- Created the research environment where this innovation could happen

## Timeline: From PostScript Applets to Modern Web

### 1983-1987: HyperTIES Development
- University of Maryland research project
- Sponsored by organizations needing advanced hypertext
- First implementation of embedded interactive components
- PostScript applets running in NeWS with Forth backend

### 1987-1990: The Concept Spreads
- Don Hopkins demonstrates HyperTIES widely
- NeWS developers see the power of embedded components
- Network transparency proves code can run anywhere
- Industry begins to understand the potential

### 1990-1995: The Transition
- Web emerges but lacks interactive components
- Sun develops Java with lessons from NeWS
- Arthur van Hoff (NeWS veteran) leads browser integration
- James Gosling applies PostScript applet concepts to Java

### 1995-2005: Java Applets Era
- HotJava browser demonstrates Java applets
- The same concept HyperTIES pioneered in 1987
- But now for the web instead of NeWS
- Mainstream adoption finally happens

### 2005-Present: AJAX and Modern Web
- AJAX realizes NeWS's network transparency vision
- Canvas API brings PostScript-like graphics to browsers
- JavaScript becomes the new embedded language
- Web Components continue the applet evolution

## Why This History Was Hidden

Several factors obscured HyperTIES's pioneering role:

1. **Research Project**: HyperTIES was university research, not a commercial product
2. **Limited Distribution**: Only sponsors and researchers had access
3. **Platform Requirements**: Needed NeWS, which Sun later abandoned
4. **Marketing Narratives**: Java was marketed as "revolutionary" and "new"
5. **Lost Source Code**: Until now, the evidence was hard to access

## The Technical Achievement

What HyperTIES accomplished was extraordinary for 1987:

```postscript
% Example of a HyperTIES PostScript applet
/telescope-diagram {
    % This could run on client OR server!
    /draw-component {
        dup selected? {
            3 setlinewidth
            0.5 0.5 1 setrgbcolor  % Highlight color
        } {
            1 setlinewidth
            0 0 0 setrgbcolor
        } ifelse
        stroke
    } def
    
    % Network-transparent event handling
    /handle-click {
        mouse-x mouse-y component-at
        dup null ne {
            /selected-component exch def
            % Could fetch data from server here!
            show-component-info
            redraw
        } { pop } ifelse
    } def
} def
```

This wasn't just drawing - it was interactive, network-capable programming embedded in documents.

## The Direct Line to Modern Web

The evolution is clear and direct:

1. **HyperTIES PostScript Applets (1987)**
   - First embedded interactive components
   - PostScript programs in hypertext
   - Network-transparent execution
   - Event handling and graphics

2. **NeWS Applications (1988-1993)**
   - Refined the embedded component model
   - Proved network transparency worked
   - More sophisticated interactions
   - Influenced Sun's future directions

3. **Java Applets (1995-2010)**
   - Same concept, new language
   - Brought to the web
   - Security sandbox from NeWS experience
   - Network classloading from NeWS

4. **AJAX Revolution (2005-2010)**
   - XMLHttpRequest realizes NeWS network transparency
   - Code and data can flow between client and server
   - Exactly what NeWS did in 1987!

5. **Modern Web (2010-Present)**
   - Canvas API ≈ PostScript graphics model
   - JavaScript ≈ Embedded programming
   - WebSockets ≈ NeWS network connections
   - Web Components ≈ Applet concept evolved

## The Four-Language Legacy

Each language in HyperTIES contributed to modern computing:

- **Emacs** → Modern IDEs and extensible editors
- **PostScript** → PDF, Canvas API, vector graphics
- **NeWS** → AJAX, remote execution, thin clients
- **Forth** → Embedded systems, boot ROMs, IoT devices

## Conclusion: Why This Matters

HyperTIES's PostScript applets represent a crucial innovation in computing history:

1. **First Implementation**: The first system to embed interactive programs in hypertext documents
2. **Network Transparency**: Showed code could run anywhere - client or server
3. **Proved the Concept**: Demonstrated applets were both possible and valuable
4. **Influenced Everything**: From Java applets to AJAX to modern web apps
5. **Still Works**: The concepts work today exactly as they did in 1987

The fact that it required integrating four different programming languages (Emacs Lisp, PostScript, NeWS, and Forth) shows both the complexity of the achievement and the vision required to see how these technologies could work together.

## The Continuing Story

Today, when we:
- Make an AJAX call to update part of a page
- Embed a Canvas element with interactive graphics
- Run JavaScript to create dynamic visualizations
- Use WebAssembly for high-performance code
- Build Progressive Web Apps

We're using concepts that HyperTIES pioneered with PostScript applets in 1987. It worked then, and it works now - the only difference is that it took the world 20 years to catch up.

---

*"HyperTIES didn't just link documents - it embedded living programs within them. That's the revolution everyone missed."* - Don Hopkins

*"We showed that code could run anywhere - client or server - transparently. AJAX? We did that in PostScript in 1987."* - The real innovation of HyperTIES 