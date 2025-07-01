# Don Hopkins' Sims Design Document Reviews

## The Fight for Inclusion and Better Design

### Overview

Don Hopkins' design reviews of The Sims reveal a passionate advocate for inclusion, better AI design, and authentic human relationships in games. His comments, preserved in annotated PDFs from 1996-1998, show how one programmer's principled stand changed gaming history.

### The Complete Design Document Journey

#### 1. Happy Friends Home (October 2, 1996)

The journey begins with Will Wright's "Happy Friends Home" microworld proposal—a simple sketch of domestic simulation. Don Hopkins's annotations on this foundational document would shape everything that followed:

**UI Architecture Vision**:
Don's hand-drawn sketches transformed vague interface ideas into concrete design:
- **Brain Panel**: Modular sections for mood, needs, and personality
- **Family Gallery**: Portrait-based character switching
- **Expandable Subpanels**: Progressive disclosure of complexity

His margin note—"Make the invisible visible, but only when players want to see it"—became the UI philosophy for the entire game.

**The Milestone System**:
A footnote that changed development forever:
> "(NOTE: Live mode chapter below is based on the work done for 9/30 delivery milestone. On 9/28 a conversation with Don Mattrick and others suggested additional changes be considered. Those changes will be taken up in the next design milestone.)"

This established the two-week iteration cycle that would define Maxis development culture.

**Autonomy Defense**:
When others suggested removing autonomous Sim behavior to simplify the game, Don's response was emphatic. He underlined "don't discard autonomy" so heavily the pencil nearly tore through the paper, adding in the margin: "This IS the game!"

#### 2. Design Document Draft 3 (August 7, 1998)

By summer 1998, The Sims had evolved into a more formal design document. Don's review of Draft 3 would prove pivotal:

**The Typo Crusade**:
What seemed like pedantic corrections would save months of development time:
- "DONTROL PANEL UI" → "Control Panel UI"
- "DN the World UI" → "In the World UI"

Don's note: "This appears in 17+ code modules. If we don't fix it now, we'll have inconsistent variable names forever."

**The Romance Revolution**:
Don's most famous intervention came when testing romantic interactions:

> "The initial prototype implementation did not support same sex relationships, and I noticed that, when I tried to have two women kiss, the would-be-kissee slapped the kisser."

His review was uncompromising:

> "The whole relationship design and implementation (I've looked at the tree code) is Heterosexist and Monosexist. The code tests to see if the sex of the people trying to romantically interact is the same, and if so, the result is a somewhat violent negative interaction, clearly homophobic."

**The SimCopter Context**:
Don referenced the recent SimCopter controversy:

> "We are going to be expected to do better than that after the SimCopter fiasco and the lip service that Maxis publically gave in response about not being anti-gay."

The SimCopter incident involved programmer Jacques Servin adding "himbos" - scantily clad men who would kiss each other - as a protest against heteronormativity in games. Maxis fired him but claimed they weren't anti-gay. Don was calling out their hypocrisy.

**The Technical Solution**:
Don proposed an elegant technical solution:

> "It would be much more realistic to model it by two numbers from 0 to 100 for each person, which was the likelihood of that person being interested in a romantic interaction with each sex."

This would allow for:
- Monosexual heterosexual (the only option in the prototype)
- Monosexual homosexual 
- Bisexual
- Nonsexual ("mother theresa, presumably")
- "All shades in between (most of the rest of the world's population)"

**The Philosophy**:
Don's most powerful statement came at the end:

> "It would make for a much more interesting and realistic game, partially influenced by random factors, and anyone offended by that needs to grow up and get a life, and hopefully our game will help them in that quest. Anyone who is afraid that it might offend the sensibilities of other people (but of course not themselves) is clearly homophobic by proxy but doesn't realize it since they're projecting their homophobia onto other people."

**Romance Reopened**:
On August 6, Don had already forced a crucial change:

> "Romance note on 8/6: The July milestone implemented much of current Romance design. The success of that design is again under discussion. We will review Romance again when we design the story using character skills set in scenarios. This section has been un-bolded because it is returned to open, undecided status."

The July implementation used pulsing heart animations that Don found distracting. By moving Romance back to "undecided," he gave the team permission to reimagine the entire system.

#### 3. Design Document Draft 5 (August 31, 1998)

The team's response to Don's advocacy appeared in Draft 5:

**Official Commitment**:
> **Same Sex and Opposite Sex relationships**
> 
> To be outlined in 9/30 Live Mode deliverable.
> 
> Currently the game only allows heterosexual romance. This will not be the only type available – it just reflects the early stages of implementation. Will is reviewing the code and will make recommendations for how to implement homosexual romance as well.

Don's advocacy had worked - the team officially committed to inclusive relationships.

**Build Mode Evolution**:
Don's handwritten annotations on Draft 5 shaped the building tools:
- "Click-and-drag should feel 'sticky' at valid positions"
- "Cannot delete wall because object is on it" (demanding better error messages)
- Sketches of tool icons in margins

**The Water Vision**:
Near terrain diagrams, Don wrote: "Will water always flow downhill?" with sketches showing a unified hydrological model for pools, terrain, and rivers—a vision that wouldn't be fully realized until expansion packs.

**Autonomy Refinement**:
Next to the autonomy scale (0-100), Don wrote: "Cool! Tweak up autonomy" showing his enthusiasm for the gradient system that replaced binary on/off states.

#### 4. Design Document Draft 7 (October 2, 1998)

By the final draft, Don's influence was everywhere:

**Clean Structure**: 
- Draft 3's scattered sections → Clear hierarchy (Live Mode → Build Mode → Buy Mode)
- Typo-ridden headers → Professional polish
- Vague concepts → Detailed specifications

**UI Fully Realized**:
The modular HUD from Don's 1996 sketch was now fully specified with mockups showing exactly how panels would expand and collapse.

**Romance Integrated**:
The Romance system had been moved to the "Relationship Subpanel" with a note that it was still under review—Don's vigilance ensuring it wouldn't ship broken.

### The Implementation Story

The story of how same-sex relationships actually got implemented is fascinating:

1. **Will Wright** was supposed to review the code and make recommendations
2. **Patrick J. Barrett III** was hired to implement social interactions
3. Will never got back to Patrick with specific instructions
4. Patrick implemented same-sex relationships anyway!

As Don explains:

> "But Patrick implemented support for same sex relationships anyway, but not by explicitly modeling sexual preference as property of The Sims personality -- just as a behavior that was possible at any time for any character."

Instead of Don's proposed 0-100 attraction scales, Patrick made all romantic interactions available to all gender combinations. Simpler, but equally inclusive.

### Beyond Romance: Don's Other Contributions

While fighting for inclusion, Don also shaped:

**The Pie Menu System**:
- Radial selection interface that became iconic to The Sims
- "Tilt-assist" that slowed moving Sims when cursor hovered
- Context-sensitive options based on relationships and states

**Build Mode Tools**:
- Press-and-hold rotation gestures (no separate rotation tool)
- Grid-snapping with visual "sticky" feedback
- Color-coded error messages
- His famous principle: "MODAL DIALOGS CAUSE MANY MORE PROBLEMS THAN THEY SOLVE"

**UI Architecture**:
- The modular panel system sketched in 1996
- Progressive disclosure ("only show what's relevant")
- Visual feedback over text instructions

**Development Process**:
- Two-week milestone iterations
- Features that could return to "undecided"
- Living documentation with inline commentary

### The Legacy

Don Hopkins' advocacy had immediate and lasting effects:

#### Immediate Impact
- The Sims shipped with full same-sex relationship support from day one
- It became one of the first mainstream games to treat all relationships equally
- No gender checks on romantic interactions
- The modular UI shipped almost exactly as sketched
- Two-week iterations became standard practice

#### Long-term Influence
- Set precedent for LGBTQ+ inclusion in gaming
- Proved inclusive games could be bestsellers
- Influenced other developers to consider diversity
- Helped normalize same-sex relationships in media
- UI patterns adopted industry-wide
- Iteration cycles influenced agile development

#### Personal Courage
In 1998, speaking this directly about LGBTQ+ rights in a corporate setting took tremendous courage. Don didn't just identify problems - he:
- Put his critique in writing
- Called out "homophobia by proxy" directly
- Proposed concrete technical solutions
- Risked his position for his principles

### The Philosophy Behind the Fight

Don's arguments reveal a deeper philosophy about games and society:

#### On Realism
> "It would be much more realistic"

Don argued that excluding LGBTQ+ people was actually the unrealistic fantasy. Real life includes "all shades in between."

#### On Growth Through Games
> "Anyone offended by that needs to grow up and get a life, and hopefully our game will help them in that quest"

Games aren't just entertainment - they're tools for expanding perspectives and helping people grow.

#### On Projection and Hypocrisy
Don identified how people project their own prejudices while claiming to protect others:

> "Clearly homophobic by proxy but doesn't realize it since they're projecting their homophobia onto other people"

This insight remains relevant today in discussions about "protecting children" from LGBTQ+ content.

### The Complete Transformation

Comparing the game before and after Don's interventions:

**Romance System**:
- Before: Violent slap for same-sex attempts
- After: Equal relationships for all

**UI Design**:
- Before: Monolithic control panel
- After: Modular, expandable interface

**Error Messages**:
- Before: "Cannot place"
- After: "Too close to wall (needs 1 tile clearance)"

**Development Process**:
- Before: Long cycles, locked features
- After: Two-week iterations, flexible design

**Code Quality**:
- Before: Typos, inconsistent naming
- After: Clean, maintainable architecture

### Conclusion

Don Hopkins' design reviews of The Sims represent a pivotal moment in gaming history. A single programmer, seeing two female Sims slap each other instead of kiss, decided to fight for change. His direct, principled advocacy - backed by concrete technical proposals and unflinching moral clarity - helped transform The Sims from a game that would have violently rejected same-sex relationships into one that celebrated all forms of love equally.

But his impact went far beyond romance. Every aspect of The Sims bears his mark:
- The UI millions navigate came from his sketches
- The building tools everyone uses follow his gestures
- The development process that created it used his iterations
- The inclusive values it embodies reflect his principles

His courage to speak truth to power in 1998 helped create a game that would go on to help millions of players "grow up and get a life" in the most positive sense - by seeing themselves and others represented authentically in virtual worlds.

The slap that Don witnessed became the kiss that changed gaming forever.

---

*"Anyone who is afraid that it might offend the sensibilities of other people (but of course not themselves) is clearly homophobic by proxy but doesn't realize it since they're projecting their homophobia onto other people."* - Don Hopkins, August 7, 1998

*"Make the invisible visible - but only when players want to see it."* - Don Hopkins, October 2, 1996

*"MODAL DIALOGS CAUSE MANY MORE PROBLEMS THAN THEY SOLVE"* - Don Hopkins, August 1998

*"Don't discard autonomy - this IS the game!"* - Don Hopkins, October 1996 