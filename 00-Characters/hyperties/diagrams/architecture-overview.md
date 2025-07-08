# HyperTIES Architecture Overview

This diagram shows the complete HyperTIES system architecture, illustrating how the authoring tool, browser, and various components interact.

<div style="background: white; padding: 20px; border: 1px solid #ccc; margin: 20px 0;">

```html
<!DOCTYPE html>
<html>
<head>
    <title>HyperTIES Architecture</title>
</head>
<body>
    <svg viewBox="0 0 800 600" style="width: 100%; max-width: 800px;">
        <!-- Background -->
        <rect width="800" height="600" fill="#f8f8f8"/>
        
        <!-- Title -->
        <text x="400" y="30" text-anchor="middle" font-size="24" font-weight="bold">
            HyperTIES System Architecture
        </text>
        
        <!-- Authoring Tool Section -->
        <g id="authoring-tool">
            <rect x="50" y="70" width="300" height="200" fill="#e8f4f8" stroke="#0066cc" stroke-width="2"/>
            <text x="200" y="95" text-anchor="middle" font-size="18" font-weight="bold">Authoring Tool</text>
            
            <rect x="70" y="120" width="120" height="40" fill="#cce5ff" stroke="#0066cc"/>
            <text x="130" y="145" text-anchor="middle" font-size="14">UniPress Emacs</text>
            
            <rect x="210" y="120" width="120" height="40" fill="#cce5ff" stroke="#0066cc"/>
            <text x="270" y="145" text-anchor="middle" font-size="14">Lisp Extensions</text>
            
            <rect x="70" y="180" width="260" height="40" fill="#99ccff" stroke="#0066cc"/>
            <text x="200" y="205" text-anchor="middle" font-size="14">Article & Link Editor</text>
            
            <text x="200" y="250" text-anchor="middle" font-size="12" font-style="italic">
                Creates .hta files
            </text>
        </g>
        
        <!-- Browser Section -->
        <g id="browser">
            <rect x="450" y="70" width="300" height="200" fill="#f0e8f8" stroke="#9933cc" stroke-width="2"/>
            <text x="600" y="95" text-anchor="middle" font-size="18" font-weight="bold">HyperTIES Browser</text>
            
            <rect x="470" y="120" width="120" height="40" fill="#e6ccff" stroke="#9933cc"/>
            <text x="530" y="145" text-anchor="middle" font-size="14">NeWS Interface</text>
            
            <rect x="610" y="120" width="120" height="40" fill="#e6ccff" stroke="#9933cc"/>
            <text x="670" y="145" text-anchor="middle" font-size="14">PostScript</text>
            
            <rect x="470" y="180" width="260" height="40" fill="#cc99ff" stroke="#9933cc"/>
            <text x="600" y="205" text-anchor="middle" font-size="14">Interactive Components</text>
            
            <text x="600" y="250" text-anchor="middle" font-size="12" font-style="italic">
                Renders articles
            </text>
        </g>
        
        <!-- Database Section -->
        <g id="database">
            <rect x="250" y="320" width="300" height="120" fill="#e8f8e8" stroke="#009900" stroke-width="2"/>
            <text x="400" y="345" text-anchor="middle" font-size="18" font-weight="bold">Article Database</text>
            
            <rect x="270" y="370" width="120" height="40" fill="#ccffcc" stroke="#009900"/>
            <text x="330" y="395" text-anchor="middle" font-size="14">Forth Engine</text>
            
            <rect x="410" y="370" width="120" height="40" fill="#ccffcc" stroke="#009900"/>
            <text x="470" y="395" text-anchor="middle" font-size="14">B-tree Index</text>
        </g>
        
        <!-- Connections -->
        <path d="M 350 220 L 400 320" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)"/>
        <path d="M 450 220 L 400 320" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)"/>
        
        <!-- Arrow marker -->
        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#666"/>
            </marker>
        </defs>
        
        <!-- Components -->
        <g id="components">
            <text x="400" y="490" text-anchor="middle" font-size="16" font-weight="bold">
                Key Components
            </text>
            
            <rect x="50" y="510" width="150" height="60" fill="#ffe6cc" stroke="#ff6600" stroke-width="2"/>
            <text x="125" y="535" text-anchor="middle" font-size="14" font-weight="bold">Pie Menus</text>
            <text x="125" y="555" text-anchor="middle" font-size="12">Navigation UI</text>
            
            <rect x="225" y="510" width="150" height="60" fill="#ffe6cc" stroke="#ff6600" stroke-width="2"/>
            <text x="300" y="535" text-anchor="middle" font-size="14" font-weight="bold">Embedded Graphics</text>
            <text x="300" y="555" text-anchor="middle" font-size="12">PostScript Objects</text>
            
            <rect x="400" y="510" width="150" height="60" fill="#ffe6cc" stroke="#ff6600" stroke-width="2"/>
            <text x="475" y="535" text-anchor="middle" font-size="14" font-weight="bold">Link Highlighting</text>
            <text x="475" y="555" text-anchor="middle" font-size="12">Visual Feedback</text>
            
            <rect x="575" y="510" width="150" height="60" fill="#ffe6cc" stroke="#ff6600" stroke-width="2"/>
            <text x="650" y="535" text-anchor="middle" font-size="14" font-weight="bold">History Stack</text>
            <text x="650" y="555" text-anchor="middle" font-size="12">Navigation State</text>
        </g>
    </svg>
</body>
</html>
```

</div>

## Architecture Components

### Authoring Tool
- **UniPress Emacs**: Commercial version of Gosling Emacs, providing the editing environment
- **Lisp Extensions**: Custom LISP code for HyperTIES-specific functionality
- **Article & Link Editor**: Interface for creating hypertext articles and defining links

### Browser
- **NeWS Interface**: Network extensible Window System providing the display layer
- **PostScript Engine**: Renders text and graphics, executes embedded interactive components
- **Interactive Components**: Live PostScript objects that respond to user input

### Database
- **Forth Engine**: High-performance scripting and data access layer
- **B-tree Index**: Efficient storage and retrieval of articles and links

### Key Features
- **Pie Menus**: Circular contextual menus for quick navigation
- **Embedded Graphics**: Interactive PostScript components within articles
- **Link Highlighting**: Visual indication of clickable hyperlinks
- **History Stack**: Back/forward navigation through visited articles

This architecture enabled HyperTIES to be the earliest hypermedia browser to support many features that wouldn't become common for years, like embedded interactive PostScript components similar to Java Applets. 