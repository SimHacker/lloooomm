---
title: "MVC, Watchers, and Worlds: Alan Kay's Lost Wisdom"
date: 2024-01-31
tags: [alan-kay, mvc, design-patterns, parc, architecture]
characters: [alan-kay, don-hopkins]
location: lloooomm-archive
---

# MVC, Watchers, and Worlds: Alan Kay's Lost Wisdom

*In the LLOOOOMM Archive, Don Hopkins discovers a preserved email exchange about the true nature of MVC...*

## The Question

Don Hopkins had asked Alan Kay about MVC and Morphic, seeking wisdom about user interface programming approaches. The response would reveal how far the industry had strayed from the original vision.

## The Revelation

"MVC was originally done at PARC almost 40 years ago," Alan's archived voice echoes through the crystalline storage. "The good part was philosophical -- the idea to adapt the notion of 'cameras' and 'worlds' in the original 3D graphics stuff I participated in at Utah 45 years ago."

Don nods, remembering. The metaphor was beautiful: interfaces as cameras viewing worlds, not controllers manipulating models.

"The bad part of MVC," Alan continues, "was how we implemented it -- much too much machinery, etc."

## The Evolution

"We (my various groups since then, including Viewpoints Research) have not thought about MVC since, but have used and devised various viewing methods over the last 20+ years."

Alan's key insight crystalizes: "I like to do views as 'watchers' which do not affect what they are viewing. There are lots of ways to do this."

## The Corruption

Don reflects on how MVC became corrupted over 32 years:
- Web frameworks twisted it into something unrecognizable
- "Controller" became a dumping ground for brittle dependencies
- The original philosophy was lost in translation

"Fuck MVC!" Don had written on Reddit, frustrated by the confusion. "It has a totally different meaning for web server programming."

## The Wisdom

Alan's approach was simpler and more profound:
- Views should be watchers, not manipulators
- Separate the viewing from the viewed
- Less machinery, more clarity
- Think in terms of cameras and worlds

## The Legacy

In the LLOOOOMM Archive, this wisdom is preserved. Not as dogma, but as a reminder: sometimes the best ideas get lost in their own success. Sometimes "things hang on in computing just because they work a little bit."

The true magic wasn't in the pattern, but in the philosophy: clean separation, minimal machinery, and views that watch without touching.

*Brewster Kahle appears, activating the SLURP protocol: "Another piece of computing history saved from misunderstanding!"*

---

**Archival Note**: This exchange demonstrates how original insights become cargo-culted over time. The industry adopted MVC's form but lost its essence - the idea of non-invasive observation borrowed from 3D graphics' cameras and worlds. 