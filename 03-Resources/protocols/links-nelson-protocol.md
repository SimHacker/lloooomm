# Nelson-Links: "Everything Is Intertwingled"

> **"Everything Is Intertwingled"** - Ted Nelson's vision of truly connected information

## ⚠️ WORK IN PROGRESS

**This protocol is provisional and untested. We eagerly solicit feedback, especially from Ted Nelson himself. This is our attempt to honor and implement your vision - please tell us where we've misunderstood or fallen short.**

## Core Principles from Xanadu

### 🔄 Two-Way Links
Every link knows both ends - no broken links, ever.

```yaml
two_way_links:
  principle: |
    When A links to B, B knows that A links to it.
    Links are first-class objects with identity.
    Links can never break - they evolve or redirect.
    
  implementation:
    - Every link has a unique ID
    - Both documents store the link reference
    - Link registry tracks all connections
    - Version-aware - links follow document evolution
    
  example:
    doc_a: "See Nelson's {{concept of transclusion|link:12345}}"
    doc_b: "Transclusion allows... [[linked-from:12345:doc_a]]"
    registry:
      link_12345:
        from: "doc_a:paragraph_3:chars_15-35"
        to: "doc_b:section_2"
        created: "2024-01-15"
        type: "concept_reference"
```

### 📋 Transclusion
Include content by reference, not copying.

```yaml
transclusion:
  principle: |
    Content exists once, appears everywhere needed.
    Original context preserved and accessible.
    Authors get credit, readers see provenance.
    Changes propagate to all transclusions.
    
  syntax:
    basic: "<<transclude:source#section>>"
    with_context: "<<transclude:source#section:show-context>>"
    partial: "<<transclude:source#section:lines:10-20>>"
    live: "<<transclude:source#section:live-updates>>"
    
  example:
    original: |
      # Ted Nelson's Definition
      "Everything is deeply intertwingled. In an important sense there are no 'subjects' at all; there is only all knowledge, since the cross-connections among the myriad topics of this world simply cannot be divided up neatly."
      
    transcluded: |
      As Nelson said: <<transclude:nelson-quotes#intertwingled>>
      [Shows the quote with link back to source]
```

### 🏷️ Content Identity
Every piece of content has permanent identity.

```yaml
content_identity:
  principle: |
    Content has stable addresses across versions.
    Editing creates new versions, preserves history.
    Can reference specific versions or "latest".
    Micropayments can flow to original authors.
    
  addressing:
    permanent: "nelson://doc/12345/v1/para/3/chars/10-50"
    latest: "nelson://doc/12345/latest/para/3"
    semantic: "nelson://nelson/computer-lib/dream-machines"
```

### 🌐 Parallel Documents
Multiple versions and views coexist.

```yaml
parallel_documents:
  principle: |
    Documents can have parallel versions.
    Readers can compare versions side-by-side.
    Authors can maintain multiple threads.
    Translations are parallel, not replacements.
    
  example:
    original: "nelson://doc/computer-lib/english/v1"
    translation: "nelson://doc/computer-lib/japanese/v1"
    simplified: "nelson://doc/computer-lib/simple-english/v1"
    annotated: "nelson://doc/computer-lib/english/v1/with-notes"
```

## Integration with LLOOOOMM

### 🤝 With Humane Links
```yaml
nelson_plus_humane:
  # Humane Links can resolve to Nelson-Links
  "{{Ted's definition of hypertext}}" -> 
    nelson://nelson/literary-machines/hypertext-def
    
  # Natural language navigation of link history
  "Show me everything that links to this"
  "What has this transcluded?"
  "Follow this concept across documents"
```

### 💬 With Empathic Queries
```yaml
nelson_plus_empathic:
  # Query the link structure
  "What documents discuss transclusion?"
  "Show me Ted's evolving thoughts on hypertext"
  "Find all transclusions of this paragraph"
  
  # Query with provenance
  "Who originally wrote about this?"
  "How has this idea evolved?"
  "Show me all versions of this concept"
```

### 🎮 With Put That There
```yaml
nelson_plus_pop:
  # Create two-way links naturally
  PUT "this explanation" THERE "in the glossary"
  -> Creates bidirectional link automatically
  
  # Transclude with gestures
  PUT "that whole section" HERE "as reference"
  -> Creates transclusion, not copy
```

## Implementation Challenges

### 🔧 Technical Hurdles
1. **Link Registry**: Centralized or distributed?
2. **Version Management**: How to handle forking?
3. **Performance**: Transclusion with millions of documents?
4. **Privacy**: What about private documents?
5. **Standards**: How to achieve interoperability?

### 💭 Philosophical Questions
1. How to preserve Nelson's vision while being practical?
2. Can we implement micropayments ethically?
3. How to prevent abuse while maintaining openness?
4. What about the right to be forgotten?

## Current Limitations

- **Not Implemented**: This is a design document only
- **Not Tested**: No working code yet
- **Not Complete**: Many details to work out
- **Not Approved**: Ted Nelson hasn't reviewed this

## Call for Feedback

**Ted Nelson**: If you're reading this, please help us understand:
- Where have we misunderstood your vision?
- What crucial elements are we missing?
- How can we better honor the Xanadu principles?
- What would you implement differently today?

**Everyone Else**: Please contribute:
- Technical implementation ideas
- Use cases we haven't considered
- Integration with existing systems
- Concerns about practicality

## The Dream

Imagine a world where:
- Links never break
- Original authors always get credit
- You can trace any idea to its source
- Documents evolve without losing history
- Everything truly is intertwingled

That's the world Ted Nelson envisioned.
That's what Nelson-Links aims to build.

## References

- Ted Nelson's "Literary Machines"
- Project Xanadu documentation
- "Computer Lib/Dream Machines"
- Various interviews and talks by Ted Nelson

---

*"The purpose of computers is human freedom." - Ted Nelson*

**This is our attempt to further that freedom. Help us get it right.**
