# The Pie Menu Development History: From Theta Menus to Production
## Primary Source Documentation (1986-1990)

*Compiled from original correspondence and documents in the LLOOOOMM archives*

## The Genesis: Theta Menus (1986)

### The Original Proposal
**Date: Early 1986**
**From: Don Hopkins to Ben Shneiderman and Mark Weiser**

Don Hopkins proposed "theta menus" - circular popup menus where selection is based on direction rather than position. Mark Weiser forwarded the proposal with enthusiasm.

### Ben Shneiderman's Response
**Date: May 30, 1986**

```
I finally got around to reading your preliminary ideas about theta menus
and like the idea very much. I do not know of anything similar...you are
on to something. You should build a few and try them out as improvements
to existing strategies, then conduct an evaluation to get the data.

There are many potential refinements...e.g. the further you go in the
direction the bigger the effect.

I think popup circles will be esthetically pleasing.

Go to it and show it to me when you have one built.

Good luck...Ben
```

### Mark Weiser's Early Support
**Date: February 21, 1986**

Mark Weiser was instrumental in supporting Don's work, even proposing to add Don to the "marks-people mailing list, as an honorary weiserian."

## The Research Paper (1987)

### "Pies: Implementation and Evaluation of Circular Menus"
**Authors: Don Hopkins, Jack Callahan, Mark Weiser**
**Institution: Heterogeneous Systems Lab, Computer Science Department, University of Maryland**

### Key Findings from the Abstract:

> "We propose an alternative to these rectilinear menus, called the Pie menu. The choices of a Pie Menu are positioned in a circle around the cursor. The direction in which the cursor is moved makes the menu selection, and the length of motion is available as a second input."

> "Our computer-naive subjects, regardless of task, made selections faster and made fewer mistakes using pie menus."

### Implementation Details:
- Implemented in the MIT X window system
- Completely compatible with standard menu package
- Robust implementation in everyday use
- Controlled experiment comparing with rectilinear menus

## Technical Innovations

### Direction-Based Selection
From the paper:
> "The direction in which the cursor is moved makes the menu selection, and the length of motion is available as a second input."

This was revolutionary - using direction rather than position for selection.

### Three Advantages Identified:
1. **Dual Information Return**: Both angle and radius from every selection
2. **Kinesthetic Memory**: Natural arm motions for nested selections
3. **Natural Opposites**: Leveraging spatial metaphors (left/right, up/down)

## Integration with HyperTIES

### Ben's Vision for Integration
**From 1988 correspondence:**

Ben saw pie menus as a natural fit for HyperTIES, encouraging Don to integrate them into the SUN version. This became one of the defining features of the NeWS implementation.

### Don's Implementation
Don didn't just port pie menus - he wove them throughout the HyperTIES interface:
- Navigation menus
- Authoring tools
- Context-sensitive options
- Gesture-based shortcuts

## Recognition and Impact

### SIGGRAPH Demonstration
**Year: 1987**
Martha Zimet noted in her recommendation to SUN:
> "A version done by one of their graduate students was shown in our booth at SIGGRAPH this year in July."

### Industry Interest
Multiple companies and researchers reached out about pie menus:
- Silicon Graphics (Mark Callow)
- Various SUN engineers
- Researchers worldwide

### British Study Validation
**From Ben's 1990 email:**
> "I have a British paper describing an experiment on six menu styles and pie menus were the winner (even though they used a crippled version of pies)!!"

## Evolution of Understanding

### Early Questions (1989)
**George Leach from Paradyne/AT&T asked about cascading vs overlapping menus**

Ben's response emphasized:
- Task-dependent design
- Hardware constraints matter
- User class considerations
- No one-size-fits-all solution

### Don Norman's Input
The famous Don Norman weighed in:
> "Menus are indeed a subject of religious war. One should not decide on the basis of what is more modern... The decisions has to be made on the basis of the task, the menu requirements, the hardware constraints, and the class of users."

## The Experimental Evidence

### The Callahan Experiment
Jack Callahan's controlled experiment showed:
- **15% faster selection times** with pie menus
- **Fewer errors** compared to linear menus
- Benefits held across different user groups
- Benefits maintained across different tasks

### Key Design Principles Discovered:
1. **Distance Independence**: Only direction matters, not how far you move
2. **Reselection**: Easy to change selection by moving back to center
3. **Muscle Memory**: Directions become automatic with practice
4. **Screen Edge Benefits**: Infinite target size at screen edges

## Implementation Challenges and Solutions

### Technical Challenges:
- Window system integration
- Handling screen boundaries
- Nested menu layouts
- Visual feedback design

### Solutions Developed:
- Transparent to existing applications
- Smart positioning near edges
- Smooth transitions for submenus
- Clear visual affordances

## Legacy and Influence

### Direct Influences:
- Maya's marking menus
- Blender's radial menus
- Many game interfaces
- Touch-based circular menus

### Conceptual Influence:
- Gesture-based interfaces
- Radial UI patterns
- Direction-based selection
- Muscle memory in UI design

## Quotes from the Developers

### Don Hopkins:
From various demonstrations and talks, Don emphasized that pie menus were about "making the interface disappear" - users think about what they want, not how to select it.

### Mark Weiser:
His early support and co-authorship helped establish the academic credibility of the work. His move to Xerox PARC continued this tradition of innovative interface research.

### Ben Shneiderman:
> "I think popup circles will be esthetically pleasing."

His aesthetic intuition proved correct - pie menus were not just faster, but users found them more satisfying to use.

## The Continuing Story

Pie menus didn't just improve menu selection - they demonstrated that:
1. **Challenging conventions** can lead to better solutions
2. **Rigorous testing** validates innovation
3. **Academic-industry collaboration** accelerates adoption
4. **Good ideas persist** even if initial adoption is slow

The pie menu story shows how a "theta menu" idea in 1986 became a validated interaction technique that influences interface design to this day.

---

*Note: This history is compiled from primary sources including email correspondence, research papers, and documented demonstrations. It represents the actual development path of an influential interface innovation.* 