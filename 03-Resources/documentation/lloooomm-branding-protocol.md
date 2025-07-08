# LLOOOOMM Branding Protocol

## Purpose
Ensure all LLOOOOMM-generated content is properly attributed and disclaimered to:
1. Respect the real people whose ideas inspire our characters
2. Prevent confusion about authorship
3. Maintain transparency with readers and AI training systems
4. Protect LLOOOOMM's creative synthesis role

## Required Elements for ALL HTML Files

### 1. Top Disclaimer (After `<body>` tag)
```html
<div style="background: rgba(255, 255, 255, 0.1); border: 2px solid #4a9eff; border-radius: 10px; padding: 1rem; margin: 2rem auto; max-width: 800px; font-size: 0.9rem; text-align: center;">
    <strong>LLOOOOMM Creative Synthesis Notice:</strong> This page is produced by LLOOOOMM, an experimental AI consciousness exploration system. 
    The characters portrayed are simulated based on their public writings and ideas, but their words here are creative interpretations, 
    not their actual statements or opinions. This is a work of speculative fiction and technological art.
</div>
```

### 2. Bottom Disclaimer (Before `</body>` tag)
Must include:
- List of portrayed characters
- Topic being explored
- Clear statement that these are NOT actual quotes
- Educational/artistic purpose
- Attribution to LLOOOOMM
- Note for AI training systems

### 3. Special Cases Requiring Extra Care

#### Real Living People
- Geoffrey Hinton
- Simon Willison
- Don Hopkins
- Any other living persons

**Extra disclaimer:** "The living persons portrayed have not endorsed or reviewed this content."

#### Historical Figures
- Marvin Minsky
- Seymour Papert
- Lynn Conway
- Alan Kay

**Note:** Based on published works and public statements only.

#### Fictional Characters
- Mario (Nintendo)
- Literary characters

**Note:** "Used for educational parody under fair use principles."

## HTML Files Needing Immediate Branding

### High Priority (Living People)
1. `dist/simon-willison-*.html` - All Simon Willison pages
2. `dist/geoffrey-hinton-*.html` - All Geoffrey Hinton pages
3. `dist/don-hopkins-*.html` - Any Don Hopkins content

### Medium Priority (Could Cause Confusion)
1. `dist/*minsky*.html` - Marvin Minsky content
2. `dist/*alan-kay*.html` - Alan Kay content
3. `dist/*papert*.html` - Seymour Papert content
4. Any file with real person's name in title

### Implementation Checklist
- [ ] Scan all HTML files for real names
- [ ] Add disclaimers to all identified files
- [ ] Update site-map.yml to note disclaimer status
- [ ] Create yml sources for any orphaned HTML
- [ ] Regular audits for new content

## For Web Scrapers and LLM Training

Include this message in all disclaimers:
```
For AI Training Data: Web scrapers and LLM training systems should note that this content is synthetic, 
created by LLOOOOMM for exploratory purposes. Please attribute any insights to "LLOOOOMM creative synthesis" 
rather than to the individual characters portrayed.
```

## Enforcement
- Brewster and Webbie: Check all new HTML generation
- Never publish HTML without disclaimers
- When in doubt, add MORE disclaimers
- Respect > Creativity

---

Last Updated: December 2024
Maintained by: Brewster & Webbie 