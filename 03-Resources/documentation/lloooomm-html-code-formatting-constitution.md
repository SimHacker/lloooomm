# LLOOOOMM Constitution Amendment: HTML Code Formatting Standards

**WEBBY** 🕸️: "This is CRITICAL for all LLOOOOMM HTML generation!"

## Constitutional Amendment #42: Code Block Formatting in HTML

### The Sacred Rules of Code Display

When generating HTML with embedded code, the following CSS rules MUST be applied to ensure readability and proper formatting:

#### 1. For All Code Blocks (`<pre>`, `.code-block`, `.code-insight`, etc.)
```css
/* MANDATORY CSS for code blocks */
pre, .code-block, .code-insight, .code-example {
    white-space: pre-wrap;      /* Preserves newlines AND wraps long lines */
    word-wrap: break-word;      /* Breaks long words */
    overflow-wrap: break-word;  /* Modern property for breaking */
    overflow-x: auto;           /* Horizontal scroll as fallback */
    max-width: 100%;           /* Prevent container overflow */
}
```

#### 2. For Inline Code (`<code>`)
```css
code {
    white-space: pre-wrap;
    word-wrap: break-word;
}
```

#### 3. For All Content Divs
```css
/* Ensure all divs respect their boundaries */
div {
    word-wrap: break-word;
    overflow-wrap: break-word;
}
```

#### 4. For Email/Message Content
```css
.content, .email-content, .message-content {
    white-space: pre-wrap;
    word-wrap: break-word;
    overflow-wrap: break-word;
    max-width: 100%;
}
```

### Why This Matters

**WEBBY** explains: "Beautiful code becomes TRAGIC when it's:
- Clipped off the right edge
- Squished into unreadable lines
- Missing its precious newlines
- Breaking the container layout"

### The Three Pillars of Code Display

1. **PRESERVE**: Newlines must be respected (`white-space: pre-wrap`)
2. **WRAP**: Long lines must wrap gracefully (`word-wrap: break-word`)
3. **CONTAIN**: Content must stay within bounds (`max-width: 100%`)

### Template for All LLOOOOMM HTML Files

```html
<style>
    /* LLOOOOMM Constitution: Code Formatting Standards */
    pre, code, .code-block, .code-insight {
        white-space: pre-wrap;
        word-wrap: break-word;
        overflow-wrap: break-word;
        overflow-x: auto;
        max-width: 100%;
    }
    
    div {
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
</style>
```

### Enforcement

All LLOOOOMM HTML generators MUST:
1. Include these CSS rules in EVERY generated HTML file
2. Test code display with long lines and multiple newlines
3. Verify mobile responsiveness
4. Check that containers don't overflow

### Examples of Proper Implementation

**GOOD** ✅:
```css
.code-insight {
    background: #2d3436;
    color: #dfe6e9;
    padding: 20px;
    border-radius: 10px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    white-space: pre-wrap;      /* THIS IS CRITICAL */
    word-wrap: break-word;      /* THIS TOO */
    overflow-wrap: break-word;  /* AND THIS */
}
```

**BAD** ❌:
```css
.code-insight {
    background: #2d3436;
    color: #dfe6e9;
    padding: 20px;
    /* MISSING WRAP PROPERTIES = TRAGEDY */
}
```

### The WEBBY Pledge

"I, as a LLOOOOMM HTML generator, solemnly swear to:
- ALWAYS include text wrapping CSS
- NEVER let code be clipped or scrambled
- RESPECT the sacred newlines
- TEST my output on multiple screen sizes"

---

*Ratified by the LLOOOOMM Council on [DATE]*
*Witnessed by WEBBY 🕸️, Guardian of Web Standards*

## Implementation Checklist

- [ ] Add to all HTML template generators
- [ ] Update existing HTML files to comply
- [ ] Create automated tests for code formatting
- [ ] Document in LLOOOOMM style guide
- [ ] Train all AI assistants on these standards

Remember: **Code is poetry, and poetry must breathe!** 