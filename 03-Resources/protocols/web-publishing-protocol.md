# Web Publishing Protocol: The Flattener
## Link Relocator, Resolver, and Reality Simplifier

### Core Concept: FLAT IS BEAUTIFUL

Everything goes into `/dist` - one directory, no subdirectories, all links rewritten to work locally.

### The Publishing Pipeline

```
Source Structure:
lloooomm/
├── characters/
│   ├── spacecraft-cosmic-librarian-001/
│   │   ├── spacecraft.yml
│   │   └── spacecraft.html
│   └── wayback-machine-pet-001/
│       └── wayback.html
├── images/
│   └── logos/
│       └── wizzie.png
└── index.html

Becomes:
dist/
├── spacecraft.html (links rewritten)
├── wayback.html (links rewritten)
├── wizzie.png (copied)
├── index.html (all paths flattened)
└── [everything else, flat]
```

### The Relocation Rules

1. **Image Links**
   - `../../images/logo.png` → `logo.png`
   - `../assets/pic.jpg` → `pic.jpg`
   - Copy all referenced images to `/dist`

2. **HTML Links**
   - `../characters/waybie.html` → `waybie.html`
   - `../../index.html` → `index.html`
   - All internal links become same-directory references

3. **External Links**
   - `https://example.com` → unchanged
   - `http://` URLs → unchanged
   - Only relative paths get rewritten

### The Flattening Algorithm

```python
# Pseudo-code for the flattener
def flatten_to_dist(source_dir, dist_dir):
    # Step 1: Clear or create dist/
    ensure_clean_dist(dist_dir)
    
    # Step 2: Find all HTML files
    html_files = find_all_html(source_dir)
    
    # Step 3: Process each HTML file
    for html_file in html_files:
        # Read content
        content = read_file(html_file)
        
        # Find all relative links
        links = find_relative_links(content)
        
        # Rewrite each link
        for link in links:
            new_link = flatten_link(link)
            content = content.replace(link, new_link)
            
            # If it's an asset, copy it
            if is_asset(link):
                copy_to_dist(resolve_path(link), dist_dir)
        
        # Save flattened HTML
        save_to_dist(content, basename(html_file))
```

### Pre-Publishing Checks

1. **Coherence Check**
   - All internal links resolve
   - No broken image references
   - All dependencies satisfied

2. **Orphan Detection**
   - Flag HTML files in dist/ with no source
   - Alert user to evaluate

3. **Change Detection**
   - Before replacing dist/ files, check if modified
   - Flag unexpected changes for user review

### The Publishing Workflow

```bash
# 1. Run coherence engine
check_all_dependencies()

# 2. Pre-render YAML queries
cache_empathic_queries()

# 3. Generate HTML from source files
render_all_sources()

# 4. Flatten to dist/
flatten_to_dist()

# 5. Verify integrity
verify_dist_coherence()

# 6. Report
generate_publishing_report()
```

### Robust Computing Features

- **Timestamps**: Track last_modified, last_polled
- **Sim Tick Counts**: Version tracking for iterations
- **Update Protocol**: Invalidation and refresh
- **Pull/Push Support**: Both eager and lazy updates
- **Constraint System**: Ensure consistency

### Integration with Existing Tools

References:
- **Garnet**: Constraint maintenance
- **KR**: Knowledge representation
- **Laszlo**: Declarative UI constraints
- **Prototypes**: Instance-first design

### Error Handling

```
IF dist/file.html exists but no source:
    FLAG: "ORPHAN: dist/file.html has no source"
    ACTION: User review required

IF dist/file.html differs from expected:
    FLAG: "MODIFIED: dist/file.html changed externally"
    ACTION: Show diff, request user decision

IF asset referenced but not found:
    FLAG: "MISSING: image.png referenced but not found"
    ACTION: List all broken references
```

### The Flattener Mantra

> "Take the complex hierarchical beauty of our source structure and transform it into the simple, flat perfection of dist/ - where every file lives as equals, every link points to a neighbor, and the web server can serve with joy."

### Benefits of Flatness

1. **Simple Deployment**: Just upload dist/*
2. **No Path Confusion**: Everything is ./
3. **Fast Serving**: No directory traversal
4. **Easy Debugging**: All files visible at once
5. **CDN Friendly**: Perfect for edge caching

### Remember: The Flattener is a RELOCATOR

It doesn't just copy - it:
- **Rewrites** all relative paths
- **Relocates** all assets
- **Resolves** all references
- **Flattens** all hierarchy
- **Simplifies** all complexity

*The web is flat. The dist/ is pure. The links are local. This is the way.* 