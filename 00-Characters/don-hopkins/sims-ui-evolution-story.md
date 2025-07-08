# The Sims UI Development
## Documentation of User Interface Work

### UI Contributions

Don Hopkins worked on several UI systems for The Sims:

#### Pie Menus
- Implemented radial context menus for object interaction
- Based on earlier research (CHI 1988 paper)
- Added "tilt-assist" feature to slow moving Sims when cursor hovers nearby
- Maximum 8 items per menu with dynamic filtering

Technical details:
- Context-sensitive based on actor/target relationship
- Filtered by current state and capabilities
- Equidistant targets for optimal selection speed

#### Build Mode Tools
- Press-and-hold rotation gesture (no separate rotation tool)
- Visual feedback for valid/invalid placement
- Grid-snapping improvements
- Opposition to modal confirmation dialogs

From design review: "MODAL DIALOGS CAUSE MANY MORE PROBLEMS THAN THEY SOLVE"

Alternative: Undo system instead of confirmations

#### UI Panel System
Early sketch (October 2, 1996) on Happy Friends Home document showed:
- Family Gallery for character selection
- Brain panel with mood/motive display
- Expandable subpanels for details
- Progressive disclosure principle

Quote from annotation: "Make the invisible visible - but only when players want to see it"

### Design Document Feedback

#### Draft 3 (August 7, 1998)
- Corrected UI naming inconsistencies ("DONTROL PANEL" → "Control Panel")
- Opposed pulsing heart animations for romance (distracting)
- Advocated for static state indicators

#### Draft 5 (August 31, 1998)
- Handwritten notes on build mode improvements
- Sketches of tool interactions
- Feedback on error messaging

### Implementation Details

#### Rotation System
Initial versions:
- v1: 90° only (too restrictive)
- v2: 45° (still limiting)
- Final: 22.5° increments with shift for free rotation

#### Error Feedback
Original: Generic "Cannot place" messages
Improved: Specific explanations
- "Too close to wall (needs 1 tile clearance)"
- "Not enough funds (costs §500, you have §234)"
- "Door blocked by couch"

### Team Context

UI development involved multiple team members:
- Will Wright (overall design vision)
- Ocean Quigley (art direction)
- Jenny Martin (UI art)
- Various other programmers and designers

### Available Documentation

- Design document PDFs with handwritten annotations
- CHI 1988 pie menu paper
- Implementation notes
- Post-launch documentation

### Technical Patterns

#### Progressive Disclosure
- Base UI shows essential information
- Click to expand for details
- Advanced options via right-click
- Novice to expert progression

#### Visual Feedback
- Color coding: Green (good), Red (bad), Yellow (warning)
- Ghost previews during placement
- Immediate state feedback
- No modal interruptions

### Notes

The Sims UI was developed collaboratively by the Maxis team. Different team members contributed various aspects of the interface design and implementation. 