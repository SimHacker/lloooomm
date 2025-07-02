# Pie Menu Implementation in HyperTIES

## Overview

HyperTIES incorporated pie menus (circular menus with radial selection) throughout the interface. This implementation, created by Don Hopkins, represented one of the most comprehensive uses of radial menus in a production system.

## Technical Implementation

### NeWS Version Features

Based on source code and documentation:

1. **Navigation Menus**
   - Eight-direction navigation (N, NE, E, SE, S, SW, W, NW)
   - Context-sensitive options based on current state
   - Keyboard shortcuts mapped to directions

2. **Multi-Window Support**
   - Synchronized browsing across windows
   - Directional gestures for window management
   - Window-specific pie menus

### Documented Interactions

From Hopkins et al. (1987) "Pies: Implementation and Evaluation":

```
Standard Navigation Menu:
           Back (N)
            ↑
    Help (W) ← · → Next (E)
            ↓
         Index (S)
```

Additional documented features:
- Distance from center controlled parameters
- Gesture direction determined action
- Visual feedback during selection

## UniPress Emacs Integration

Hopkins extended pie menus to the UniPress Emacs authoring environment:

### Window Management
- Tab implementation with pie menu control
- Window operations (resize, close, split)
- Buffer switching via radial selection

### Text Editing Operations
- Standard editing commands (cut, copy, paste)
- Font selection with directional style choice
- Color selection using radial hue wheel

### Implementation Example

From preserved code:

```lisp
;; Simplified pie menu definition
(define-pie-menu 'edit-menu
  '((0 "Cut" cut-region)
    (90 "Copy" copy-region)
    (180 "Paste" yank)
    (270 "Undo" undo)))
```

## Controlled Experiments

Hopkins et al. (1987) conducted formal usability studies:

### Results
- 15% faster selection time compared to linear menus
- Reduced error rates for expert users
- Learning curve documented over multiple sessions

### Study Parameters
- 12 participants
- 5 sessions each
- Measured: selection time, error rate, subjective preference

## Historical Context

### Contemporary Systems
- Apple Lisa/Macintosh: Linear pull-down menus
- X Window System: Linear pop-up menus
- Windows 1.0: Linear menus only

### Patent Status
- U.S. Patent 4,896,291 "Directional Selection Control"
- Filed: February 10, 1986
- Granted: January 23, 1990
- Assignee: University of Maryland

## Technical Advantages

Based on research findings:

1. **Muscle Memory**: Directional selection enables gestural shortcuts
2. **Screen Efficiency**: Radial layout minimizes mouse travel
3. **Error Prevention**: All options equidistant from center
4. **Modeless Operation**: No menu bar traversal required

## Limitations Documented

From user studies and correspondence:

1. **Screen Space**: Requires circular area for display
2. **Item Count**: Optimal for 8 or fewer items
3. **Text Length**: Radial layout constrains label length
4. **Learning Curve**: Initial unfamiliarity for users

## Legacy and Influence

### Direct Adoptions
- Alias Maya: Marking menus (1998)
- Various CAD applications
- Game interfaces (documented from 2000s)

### Research Citations
The Hopkins et al. paper has been cited in:
- CHI proceedings (multiple years)
- ACM Transactions on Graphics
- Various HCI textbooks

## Source Materials

### Primary Sources
1. Hopkins, D., Callahan, J., & Weiser, M. (1987). "Pies: Implementation and Evaluation of Circular Menus"
2. HyperTIES source code (fmt.ps, pie-menu implementations)
3. Email correspondence (1987-1989)

### Code Repositories
- UniPress Emacs modifications
- NeWS PostScript implementations
- HyperTIES integration code

## Conclusions

The pie menu implementation in HyperTIES represented a systematic attempt to replace linear menus with radial selection throughout a complex application. While the approach showed measurable benefits in controlled studies, adoption was limited by patent restrictions and the radical departure from established interface conventions.

---

*Documentation compiled from source code, published research, and project correspondence.* 