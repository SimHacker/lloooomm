# Pie Menus Everywhere: The HyperTIES Revolution

## The Most Extensive Use of Pie Menus Ever Created

HyperTIES and UniPress Emacs didn't just use pie menus - they put pie menus EVERYWHERE, creating the most comprehensive implementation of radial interaction ever built. This wasn't just a UI choice; it was a complete interaction philosophy.

## HyperTIES Pie Menu Innovations

### Platform-Specific Features

**NeWS Version:**
- Full pie menu navigation system
- Synchronized multi-window browsing
- Directional gestures for navigation

**Windows Version:**
- **TOUCHSCREEN SUPPORT** - Yes, touchscreen in the 1980s!
- Pie menus optimized for finger input
- Direct manipulation with touch gestures

### Synchronized Multi-Window Browsing

HyperTIES pioneered synchronized browsing across multiple windows using pie menu gestures:

- **Directional Navigation**: Gesture direction determined action
  - Up: Back in history
  - Down: Show definition
  - Right: Follow link in current window
  - Left: Follow link in OTHER window
- **Multi-Window Coordination**: Windows could be linked for synchronized browsing
- **Gesture Memory**: System learned user's gesture patterns

### Navigation Pie Menus

The navigation system was incredibly sophisticated:

```
           Back
            ↑
    Help ←  ·  → Next
            ↓
         Definition
```

But it went beyond simple navigation:
- **Distance = Speed**: Pull further for faster scrolling
- **Spiral = Continuous**: Spiral gestures for continuous actions
- **Flick = Quick**: Quick flicks for instant actions

## UniPress Emacs: Pie Menus for Everything

Don Hopkins's UniPress Emacs implementation took pie menus to an unprecedented level:

### Tabbed Windows with Pie Menu Control

UniPress Emacs pioneered tabbed windows (before anyone else!):
- **Tabs on Right Edge**: Vertical tabs so many more could stack
- **Tabs as Index**: Each tab was a pie menu target
- **Pie Menu Window Management**:
  - Raise window
  - Lower window  
  - Resize (pull to size)
  - Iconify
  - Close
  - Split
  - Join

### Font Selection: The "Pull Out" Innovation

The font selection pie menu was revolutionary:

```
     Bold
      ↑
Italic ← · → Regular
      ↓
   Underline

[Pull outward to increase size]
[Live preview in center]
```

- **Direction = Style**: Choose font style by direction
- **Distance = Size**: Pull out for bigger font, push in for smaller
- **Live Feedback**: Font sample in menu center updated in real-time
- **Muscle Memory**: Users could change fonts without looking

### Color Pie Wheel

The color selection system was a work of art:

```
        Red
         ↑
  Purple ← · → Yellow
         ↓
       Blue

[Distance from center = Saturation]
[Rotation around = Hue]
[Center shows live preview]
```

This single pie menu could set:
- Text foreground color
- Text background color
- Highlight foreground color
- Highlight background color
- All with live preview!

### Complete Pie Menu Integration

Pie menus were integrated into EVERY aspect:

**Text Editing:**
- Cut/Copy/Paste
- Search/Replace
- Indent/Outdent
- Comment/Uncomment

**File Operations:**
- Open (with recent files in pie)
- Save/Save As
- Print options
- Version control

**Window Management:**
- All window operations
- Buffer switching
- View splitting
- Tab management

**Development Tools:**
- Compile
- Debug
- Run
- Profile

## The Interaction Philosophy

This wasn't just about using pie menus - it was a complete interaction philosophy:

### 1. **Directional Memory**
Users build muscle memory for directions:
- North = Back/Up/Previous
- South = Forward/Down/Next
- East = Accept/Open/Expand
- West = Cancel/Close/Contract

### 2. **Distance Encoding**
Distance from center encoded continuous values:
- Font size
- Scroll speed
- Window size
- Color saturation

### 3. **Gestural Shortcuts**
Complex gestures for power users:
- Spiral out = Zoom in
- Spiral in = Zoom out
- Figure-8 = Swap windows
- Quick flick = Instant action

### 4. **Context Everywhere**
Every object could have its own pie menu:
- Right-click on text → Text operations
- Right-click on link → Link operations
- Right-click on image → Image operations
- Right-click on window border → Window operations

## Technical Implementation

The implementation was sophisticated:

```lisp
;; UniPress Emacs pie menu definition
(define-pie-menu 'font-menu
  '((0 "Bold" (set-font-weight 'bold))
    (90 "Regular" (set-font-weight 'normal))
    (180 "Italic" (set-font-style 'italic))
    (270 "Underline" (set-font-underline t)))
  :center-preview 'font-sample
  :distance-function 'set-font-size
  :min-distance 20
  :max-distance 200)
```

## Why This Matters

The HyperTIES/UniPress Emacs pie menu system demonstrated:

1. **Complete Integration**: Pie menus weren't added on - they were fundamental
2. **Touchscreen Ready**: The Windows version worked with 1980s touchscreens
3. **Gestural Language**: Created a consistent gestural vocabulary
4. **Power + Simplicity**: Novices could click, experts could gesture
5. **Live Feedback**: Everything provided immediate visual feedback

## Legacy and Influence

This comprehensive pie menu system influenced:

- **Maya**: 3D software adopted marking menus (pie menu variant)
- **Video Games**: Radial menus became standard in gaming
- **Mobile UIs**: Gesture-based interfaces echo these concepts
- **VR/AR**: Radial menus are natural in 3D space

## The Lost Innovation

Despite being the most comprehensive pie menu system ever created, it remained largely unknown because:

1. **Platform Lock-in**: Required specific versions of HyperTIES/Emacs
2. **Ahead of Time**: Too advanced for 1980s hardware
3. **Training Required**: Users needed to learn the gestural language
4. **Patent Issues**: Pie menus were patented, limiting adoption

## Conclusion: A Vision of Fluid Interaction

HyperTIES and UniPress Emacs showed what was possible when pie menus were taken to their logical extreme:

- Every action had a direction
- Every value had a distance
- Every context had a menu
- Every gesture had meaning

It was a complete reimagining of human-computer interaction, where the interface disappeared into a fluid dance of gestures and immediate feedback. The Windows version even worked with touchscreens in the 1980s!

We're only now, 35+ years later, beginning to approach this level of gestural fluidity in modern interfaces.

---

*"We didn't just add pie menus to the interface - we made pie menus THE interface."* - Don Hopkins

*"Pull out for bigger fonts, spiral for continuous scrolling, flick for quick actions - it was like conducting an orchestra."* - The lost art of pie menu mastery 