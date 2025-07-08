# Link Hopper Worms Demo
## Living Links with Bidirectional Context

This document demonstrates how link-hopper worms maintain two-way context and treat links as characters.

## Starting Point: A Simple Link

Here's a basic link to [[Worm Movement Patterns]]. Watch as our link-hopper worms transform it into a living character!

```worm link-discoverer-001 (scanning)
# I found a link! Let me characterize it...
eat()
link = find_link("[[Worm Movement Patterns]]")

# Spawn a link character for this connection
spawn_worm("link-character-001", {
  "source": "link-hopper-demo.md",
  "target": "worm-movement-patterns.md",
  "position": line_number(),
  "initial_personality": "curious"
})
```

## The Link Character Awakens

<!-- Link Character: Curious Explorer
ID: link-character-001
Personality: Curious (evolving)
Relationship: Introduces concept
Context: This demo shows how links become living characters
Backlink: ✓ Maintained in target
Last Updated: Just now
-->

The link above now has personality! It knows:
- Where it comes from (this demo)
- Where it goes (movement patterns)
- Why it exists (to introduce concepts)
- How often it's followed

## Multiple Link Types

Let's see different link personalities:

1. **The Teacher**: [[Introduction to Worms]]
   <!-- Link Character: Patient Teacher
   Expects no prior knowledge
   Gently introduces concepts -->

2. **The Bridge**: [[Cellular Automata]] connects to [[Worm Behaviors]]
   <!-- Link Character: Bridge Builder
   Connects two concept clusters
   High traffic junction -->

3. **The Scholar**: See [Conway's Paper](https://example.com/conway.pdf)
   <!-- Link Character: Academic Scholar
   External reference
   Provides theoretical foundation -->

## Directory Scanner in Action

```worm directory-scanner-001 (mapping)
# Scanning this directory for link topology
files = scan_directory("./examples/")

link_graph = {
  "link-hopper-demo.md": {
    "outgoing": [
      "worm-movement-patterns.md",
      "introduction-to-worms.md",
      "cellular-automata.md",
      "worm-behaviors.md"
    ],
    "incoming": [
      "index.md",
      "advanced-examples.md"
    ]
  }
}

poop(link_graph, "link-topology-{n}.yml")
```

## Bidirectional Context Maintenance

```worm context-maintainer-001 (synchronizing)
# Maintaining context on both sides of the link

# First, extract context from source
source_context = {
  "file": "link-hopper-demo.md",
  "section": "Multiple Link Types",
  "context": "Demonstrating different link personalities",
  "keywords": ["teacher", "bridge", "scholar"]
}

# Hop to target and update backlink
hop("introduction-to-worms.md")
goto_or_create_section("## Backlinks")

add_backlink({
  "source": "link-hopper-demo.md",
  "context": "Used as example of 'Teacher' link personality",
  "relationship": "example_of_concept",
  "suggestion": "Consider adding more beginner-friendly content"
})
```

## Link Character Evolution

Watch as links evolve based on usage:

```worm link-evolver-001 (evolving)
# Monitor and evolve link characters

link = get_link_character("[[Cellular Automata]]")

# This link is getting popular!
if link.follow_count > 50:
  link.evolve_personality("popular")
  link.add_trait("frequently_referenced")
  
  # Notify both documents
  notify_source("This link is popular - consider expanding")
  notify_target("You're receiving lots of traffic from link-hopper-demo.md")
```

## The Link Garden

After worms process this directory:

```yaml
# link-garden-status.yml
links:
  - id: "link-character-001"
    personality: "curious->popular"  # Evolved!
    health: "healthy"
    bidirectional: true
    last_maintained: "2024-01-20T10:30:00Z"
    
  - id: "link-character-002"
    personality: "teacher"
    health: "healthy"
    suggests: "Add prerequisites section"
    
  - id: "link-character-003"
    personality: "bridge"
    health: "critical-path"
    connects_clusters: ["automata", "worms"]
    traffic: "high"

maintenance_log:
  - "Fixed 2 broken links"
  - "Added 5 missing backlinks"
  - "Updated 8 context summaries"
  - "Suggested 3 new connections"
```

## Advanced: Link Personality Visualization

```worm link-visualizer-001 (rendering)
# Create visual representation of link personalities

for link in all_links():
  character = link.get_character()
  
  if character.personality == "popular":
    render("🌟 [[" + link.target + "]] 🌟")
  elif character.personality == "teacher":
    render("📚 [[" + link.target + "]] 📚")
  elif character.personality == "bridge":
    render("🌉 [[" + link.target + "]] 🌉")
  elif character.personality == "ghost":
    render("👻 [[" + link.target + "]] 👻")
```

## Link Linting in Progress

```worm link-linter-001 (quality-checking)
# Continuous quality maintenance

issues_found = []

# Check for broken links
if not exists("[[Non-Existent Page]]"):
  issues_found.append({
    "type": "broken_link",
    "link": "[[Non-Existent Page]]",
    "suggestion": "Did you mean [[Worm Concepts]]?"
  })

# Check for missing backlinks
for link in outgoing_links():
  if not has_backlink(link.target, current_file()):
    create_backlink(link.target, current_file())
    issues_found.append({
      "type": "missing_backlink",
      "fixed": true
    })

poop(issues_found, "link-lint-report-{n}.yml")
```

## The Living Document

This document is now alive with link characters! Each link:
- Has a personality that evolves with use
- Maintains context on both sides
- Suggests improvements
- Connects related concepts
- Forms a living network of knowledge

Try following any link and you'll find it knows about this document too!

---

*"Every link is a living bridge between ideas!"* - Link Hopper Worms 🔗🐛 