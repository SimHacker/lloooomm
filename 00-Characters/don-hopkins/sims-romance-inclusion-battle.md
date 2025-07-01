# The Sims Romance System: Design Review and Implementation
## Documentation of Same-Sex Relationship Support

### Background

During development of The Sims in 1998, Don Hopkins reviewed the romance system implementation and identified issues with how it handled same-sex romantic interactions.

### The Initial Implementation

The original prototype SimAntics code checked gender before allowing romantic interactions (as shown by the following pseudocode):
```cpp
if (actor.gender == target.gender && interaction.type == ROMANTIC) {
    trigger_slap();
    relationship_score -= 10;
    play_sound("slap.wav");
}
```

When two Sims of the same gender attempted romance, one would slap the other.

### Design Document Review (August 7, 1998)

Don Hopkins wrote in his review of Draft 3:

> "The whole relationship design and implementation (I've looked at the tree code) is Heterosexist and Monosexist. The code tests to see if the sex of the people trying to romantically interact is the same, and if so, the result is a somewhat violent negative interaction, clearly homophobic."

He referenced the recent SimCopter incident:
> "We are going to be expected to do better than that after the SimCopter fiasco and the lip service that Maxis publically gave in response about not being anti-gay."

### Proposed Solution

Don suggested a two-axis attraction model:
> "It would be much more realistic to model it by two numbers from 0 to 100 for each person, which was the likelihood of that person being interested in a romantic interaction with each sex."

This would allow for:
- Heterosexual orientations
- Homosexual orientations  
- Bisexual orientations
- Asexual orientations
- Various points in between

### Team Response

By Draft 5 (August 31, 1998), the design document included:

> **Same Sex and Opposite Sex relationships**
> 
> To be outlined in 9/30 Live Mode deliverable.
> 
> Currently the game only allows heterosexual romance. This will not be the only type available – it just reflects the early stages of implementation. Will is reviewing the code and will make recommendations for how to implement homosexual romance as well.

### Final Implementation

Patrick J. Barrett III was hired to implement social interactions. According to Don:
> "Patrick implemented support for same sex relationships anyway, but not by explicitly modeling sexual preference as property of The Sims personality -- just as a behavior that was possible at any time for any character."

The simpler solution was to remove gender checks entirely, making all romantic interactions available to all Sims regardless of gender.

### Result

The Sims shipped on February 4, 2000 with full same-sex relationship support. All romantic interactions were available to all gender combinations with no mechanical differences.

### Additional Context

From Don's review:
> "Anyone offended by that needs to grow up and get a life, and hopefully our game will help them in that quest. Anyone who is afraid that it might offend the sensibilities of other people (but of course not themselves) is clearly homophobic by proxy but doesn't realize it since they're projecting their homophobia onto other people."

### Documentation Sources

- The Sims Design Document Draft 3 (August 7, 1998) with Don's handwritten review
- The Sims Design Document Draft 5 (August 31, 1998)
- Don Hopkins's written accounts of the implementation
- The shipped game code

### Notes

This was one of many design decisions made during The Sims development. The game was created by a large team at Maxis, with different team members contributing to different aspects of the game's systems and features. 