# Don Hopkins' Sims Design Document Reviews

## The Fight for Inclusion and Better Design

### Overview

Don Hopkins' design reviews of The Sims reveal a passionate advocate for inclusion, better AI design, and authentic human relationships in games. His comments, preserved in annotated PDFs, show how one programmer's principled stand changed gaming history.

### The Slap That Changed Gaming

In 1998, Don Hopkins was working on The Sims as the character animation and UI programmer. While testing the game, he tried to make two female Sims kiss. What happened next would spark a revolution in gaming:

> "The initial prototype implementation did not support same sex relationships, and I noticed that, when I tried to have two women kiss, the would-be-kissee slapped the kisser."

This wasn't just a missing feature - it was active punishment for players attempting same-sex romance. The game was literally programmed to be homophobic.

### Design Document Draft 3 (August 7, 1998)

Don's review of Draft 3 contains one of the most important critiques in gaming history:

#### The Problem

> "The whole relationship design and implementation (I've looked at the tree code) is Heterosexist and Monosexist. The code tests to see if the sex of the people trying to romantically interact is the same, and if so, the result is a somewhat violent negative interaction, clearly homophobic."

#### The Context

Don referenced the recent SimCopter controversy:

> "We are going to be expected to do better than that after the SimCopter fiasco and the lip service that Maxis publically gave in response about not being anti-gay."

The SimCopter incident involved programmer Jacques Servin adding "himbos" - scantily clad men who would kiss each other - as a protest against heteronormativity in games. Maxis fired him but claimed they weren't anti-gay. Don was calling out their hypocrisy.

#### The Solution

Don proposed a elegant technical solution:

> "It would be much more realistic to model it by two numbers from 0 to 100 for each person, which was the likelihood of that person being interested in a romantic interaction with each sex."

This would allow for:
- Monosexual heterosexual (the only option in the prototype)
- Monosexual homosexual 
- Bisexual
- Nonsexual ("mother theresa, presumably")
- "All shades in between (most of the rest of the world's population)"

#### The Philosophy

Don's most powerful statement came at the end:

> "It would make for a much more interesting and realistic game, partially influenced by random factors, and anyone offended by that needs to grow up and get a life, and hopefully our game will help them in that quest. Anyone who is afraid that it might offend the sensibilities of other people (but of course not themselves) is clearly homophobic by proxy but doesn't realize it since they're projecting their homophobia onto other people."

### The Team's Response

By Draft 5 (August 31, 1998), the design document included a new section:

> **Same Sex and Opposite Sex relationships**
> 
> To be outlined in 9/30 Live Mode deliverable.
> 
> Currently the game only allows heterosexual romance. This will not be the only type available – it just reflects the early stages of implementation. Will is reviewing the code and will make recommendations for how to implement homosexual romance as well.

Don's advocacy had worked - the team officially committed to inclusive relationships.

### The Implementation

The story of how same-sex relationships actually got implemented is fascinating:

1. **Will Wright** was supposed to review the code and make recommendations
2. **Patrick J. Barrett III** was hired to implement social interactions
3. Will never got back to Patrick with specific instructions
4. Patrick implemented same-sex relationships anyway!

As Don explains:

> "But Patrick implemented support for same sex relationships anyway, but not by explicitly modeling sexual preference as property of The Sims personality -- just as a behavior that was possible at any time for any character."

Instead of Don's proposed 0-100 attraction scales, Patrick made all romantic interactions available to all gender combinations. Simpler, but equally inclusive.

### Beyond Romance: Don's Other Contributions

While fighting for inclusion, Don also created:

- **The Character Animation System**: The core architecture that makes Sims move and act
- **Pie Menus**: The radial selection interface that became iconic to The Sims
- **Visual Programming Tools**: Enabling modders to extend the game
- **UI Design**: Interface elements throughout the game
- **Open Source Advocacy**: Later open-sourced SimCity as Micropolis

### The Legacy

Don Hopkins' advocacy had immediate and lasting effects:

#### Immediate Impact
- The Sims shipped with full same-sex relationship support from day one
- It became one of the first mainstream games to treat all relationships equally
- No gender checks on romantic interactions

#### Long-term Influence
- Set precedent for LGBTQ+ inclusion in gaming
- Proved inclusive games could be bestsellers
- Influenced other developers to consider diversity
- Helped normalize same-sex relationships in media

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

### The Broader Context

Don's fight for inclusion in The Sims was part of a larger pattern in his career:

- **Open Source SimCity**: Made the game freely available for education
- **OLPC Involvement**: Brought SimCity to children's laptops worldwide
- **Accessibility Focus**: Pie menus were designed for ease of use
- **Community Tools**: Empowered players to create and share

### Conclusion

Don Hopkins' design reviews of The Sims represent a pivotal moment in gaming history. A single programmer, seeing two female Sims slap each other instead of kiss, decided to fight for change. His direct, principled advocacy - backed by concrete technical proposals and unflinching moral clarity - helped transform The Sims from a game that would have violently rejected same-sex relationships into one that celebrated all forms of love equally.

His courage to speak truth to power in 1998 helped create a game that would go on to help millions of players "grow up and get a life" in the most positive sense - by seeing themselves and others represented authentically in virtual worlds.

The slap that Don witnessed became the kiss that changed gaming forever.

---

*"Anyone who is afraid that it might offend the sensibilities of other people (but of course not themselves) is clearly homophobic by proxy but doesn't realize it since they're projecting their homophobia onto other people."* - Don Hopkins, August 7, 1998 