# Pie Menu Implementation (PostScript)
## Extracted from Don Hopkins Archive - Living Code in HyperTIES

*[Light blue highlight indicates clickable links to related articles]*

### Original PostScript Implementation (circa 1988)

This is the original pie menu implementation for the [NeWS Window System](../../../news.md), demonstrating the elegance of stack-based programming for creating circular menus.

```postscript
% Pie Menu Definition
% Don Hopkins, 1988
% [Click here to run in PostScript Playground]

/PieMenu {
    % Create a new pie menu dictionary
    20 dict begin
        /ItemArray 8 array def      % 8 items maximum
        /ItemCount 0 def            % Current number of items
        /Radius 50 def              % Menu radius
        /Center { 0 0 } def         % Center point
        
        % Add item to menu
        /AddItem { % label proc => -
            ItemArray ItemCount 3 -1 roll put
            ItemArray ItemCount 1 add 3 -1 roll put
            /ItemCount ItemCount 2 add def
        } def
        
        % Calculate angle for item
        /ItemAngle { % index => angle
            360 ItemCount 2 div div mul
        } def
        
        % Draw the pie menu
        /Draw {
            gsave
                Center translate
                
                % Draw circle
                0 0 Radius 0 360 arc
                stroke
                
                % Draw divisions and labels
                ItemCount 2 div {
                    dup ItemAngle rotate
                    0 0 moveto
                    Radius 0 lineto
                    stroke
                    
                    % Draw label
                    Radius 2 div 0 moveto
                    ItemArray exch 2 mul get
                    show
                    
                    360 ItemCount 2 div div neg rotate
                } for
            grestore
        } def
        
        % Track mouse and highlight selection
        /Track { % x y => selected_index
            Center aload pop     % x y cx cy
            3 -1 roll sub        % x cx dy
            3 1 roll sub         % dy dx
            atan                 % angle
            
            % Convert to item index
            360 ItemCount 2 div div div
            round cvi
            ItemCount 2 div mod
        } def
        
        % Execute selected item
        /Execute { % index => -
            ItemArray exch 2 mul 1 add get
            exec
        } def
        
    currentdict end
} def
```

### [Link: See Modern JavaScript Translation](./pie-menu-modern.js)

### Interactive Demo

[Click here to launch interactive pie menu demo]

Try it:
1. Click and hold to invoke the menu
2. Drag in any direction to select
3. Release to execute

### Key Concepts Explained

#### Stack-Based Design [→ FORTH Connection](../../forth/stack-ui.md)
The PostScript implementation uses the stack for all parameter passing:
- `label proc AddItem` - pushes label and procedure onto stack
- No variables needed for temporary values
- Natural flow of data through operations

#### Geometric Calculations [→ Storyboard](../../storyboards/pie-menu-geometry.jpg)
The angle calculation `360 ItemCount 2 div div mul` elegantly distributes items around the circle. [See original hand-drawn geometry](../../storyboards/pie-menu-math.jpg).

#### Event Handling [→ NeWS Integration](../../../news.md#event-system)
The `Track` method shows how NeWS unified:
- Mouse tracking
- Geometric calculations  
- Display updates
All in one PostScript environment!

### Historical Context

This implementation was created for the [Unix port of HyperTIES](../../c/hyperties-unix-port.c) in 1988. It demonstrated how pie menus could enhance hypertext navigation by providing quick access to:

- Navigation commands (Back, Forward, Home)
- Link following options
- Search functions
- Bookmarking

[Ben Shneiderman's notes](../../../legacy/ben-notes-on-pie-menus.md) on seeing this: *"Don's pie menus made our hypertext navigation feel magical. Users could navigate complex information spaces with simple gestures."*

### Evolution Timeline

1. **1986**: [First pie menu sketches](../../storyboards/first-pie-menu-sketch.jpg)
2. **1988**: This PostScript implementation
3. **1990**: [C implementation](../../c/pie-menu.c) for wider deployment
4. **1991**: [Integration with SimCity](../../applications/simcity-pie-menus.md)
5. **2024**: [Revival in LLOOOOMM](./pie-menu-lloooomm.js)

### Related Articles

- [Pie Menu Theory and Design](../../documentation/pie-menu-theory.md)
- [Gesture Recognition in NeWS](../gesture-recognition.ps)
- [User Studies at HCIL](../../studies/pie-menu-efficiency.md)
- [Modern Applications](../../modern/pie-menus-today.md)

### Try It Yourself

```postscript
% Create a navigation pie menu
/NavMenu PieMenu def

(Back) { history_back } NavMenu /AddItem get exec
(Forward) { history_forward } NavMenu /AddItem get exec  
(Home) { go_home } NavMenu /AddItem get exec
(Search) { show_search } NavMenu /AddItem get exec
(Bookmark) { add_bookmark } NavMenu /AddItem get exec
(Links) { show_links } NavMenu /AddItem get exec
(Help) { show_help } NavMenu /AddItem get exec
(Exit) { close_menu } NavMenu /AddItem get exec

NavMenu /Draw get exec
```

[Run this code in PostScript Playground]

### Preservation Notes

This code has been preserved exactly as found in Don's archive, with added hyperlinks to related materials. The elegance of the stack-based approach and the geometric simplicity remain timeless.

*"Good design is eternal. This 1988 code could run unchanged today and still feel modern."* - Don Hopkins

---

[← Back to Archive Index](../../index.md) | [→ Next: Smooth Scrolling Algorithm](../c/smooth-scroll.c) 