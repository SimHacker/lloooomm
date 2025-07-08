# Faceted Menu Protocol

## Overview

Faceted menus, inspired by Ben Shneiderman's work on dynamic queries and information visualization, provide progressive refinement of choices through multiple orthogonal dimensions. Each facet acts as a filter, dynamically updating available options.

## Core Principles

### 1. Orthogonal Dimensions
Each facet represents an independent dimension of choice:
- **What**: Type of action (create, modify, analyze, navigate)
- **Where**: Scope or location (current, recent, all, specific)
- **When**: Temporal aspect (now, scheduled, conditional)
- **How**: Method or approach (quick, detailed, guided)
- **Why**: Intent or goal (explore, fix, optimize, learn)

### 2. Dynamic Filtering
As users select facets, other facets update to show only relevant options:

```javascript
facetedMenu.define({
  name: "UniversalAction",
  facets: {
    action: {
      label: "What to do",
      options: ["create", "edit", "analyze", "connect", "transform"],
      affects: ["target", "method"]
    },
    target: {
      label: "What to affect", 
      options: context => {
        // Dynamically computed based on selected action
        switch(context.selected.action) {
          case "create": return ["document", "link", "character", "protocol"];
          case "edit": return context.recentlyEdited.concat(["browse..."]);
          case "analyze": return ["selection", "document", "relationships", "patterns"];
          default: return ["current", "recent", "all"];
        }
      }
    },
    method: {
      label: "How to proceed",
      options: context => {
        if (context.selected.action === "create") {
          return ["from-template", "blank", "guided", "import"];
        }
        return ["quick", "detailed", "interactive"];
      }
    }
  }
});
```

### 3. Immediate Feedback
Show preview of results as facets are selected:

```javascript
facetedMenu.onUpdate((selectedFacets) => {
  const preview = generatePreview(selectedFacets);
  return {
    resultCount: preview.items.length,
    preview: preview.items.slice(0, 5),
    command: buildCommand(selectedFacets)
  };
});
```

## Integration with NeLLM

### Persistent State Management
```javascript
// NeLLM maintains faceted menu state
nellm.eval(`
  const menuState = {
    history: [],
    favorites: new Map(),
    contextCache: new Map(),
    
    recordSelection(facets, result) {
      this.history.push({ facets, result, timestamp: Date.now() });
      this.updateFavorites(facets);
    },
    
    suggestBasedOnHistory(currentContext) {
      // ML-style suggestion based on past selections
      return this.history
        .filter(h => similarContext(h.context, currentContext))
        .map(h => h.facets)
        .reduce(mergeFacets);
    }
  };
`);
```

### Rendering Pipeline
```javascript
// Download specialized facet rendering module
nellm.eval(`
  import { FacetRenderer } from 'lloooomm://modules/facet-renderer';
  
  const renderer = new FacetRenderer({
    style: 'shneiderman-treemap',  // or 'starfield', 'parallel-coordinates'
    animations: true,
    showPreviews: true
  });
  
  // Reduce complex rendering to simple commands
  global.renderFacets = (facets) => {
    const result = renderer.render(facets);
    console.log(JSON.stringify({ 
      type: 'facet-render',
      svg: result.svg,
      interactions: result.interactions
    }));
  };
`);

// Now LLM can just call:
nellm.eval(`renderFacets(menuState.current)`);
```

## Facet Types

### 1. Categorical Facets
Discrete choices:
```javascript
{
  type: "categorical",
  name: "object_type",
  options: ["character", "location", "item", "concept"],
  multiSelect: false
}
```

### 2. Hierarchical Facets
Tree-structured options:
```javascript
{
  type: "hierarchical",
  name: "location",
  root: "universe",
  children: {
    "universe": ["mit", "xerox", "starship"],
    "mit": ["ai-lab", "media-lab", "csail"],
    "starship": ["bridge", "holodeck", "engineering"]
  }
}
```

### 3. Continuous Facets
Ranges and sliders:
```javascript
{
  type: "continuous",
  name: "time_range",
  min: "1960-01-01",
  max: "now",
  default: "last-week",
  format: "date"
}
```

### 4. Computed Facets
Dynamic options based on context:
```javascript
{
  type: "computed",
  name: "related_items",
  compute: async (context) => {
    const items = await nellm.eval(`
      findRelated('${context.selection}', ${context.depth})
    `);
    return JSON.parse(items);
  }
}
```

## Flexible Goal Integration

### Goal-Driven Facets
```javascript
// Goals influence available facets
facetedMenu.defineGoalDriven({
  name: "ProblemSolver",
  goalExtractor: context => context.currentGoal || "explore",
  
  facetsByGoal: {
    "debug": {
      primary: ["error_type", "component", "timeframe"],
      secondary: ["severity", "frequency", "impact"]
    },
    "optimize": {
      primary: ["metric", "scope", "constraints"],
      secondary: ["method", "iterations", "threshold"]
    },
    "explore": {
      primary: ["curiosity", "depth", "breadth"],
      secondary: ["visualization", "connections", "patterns"]
    }
  }
});
```

### Progressive Goal Refinement
```javascript
// Start with vague goal, refine through facets
nellm.eval(`
  class GoalRefiner {
    constructor(initialGoal) {
      this.goal = {
        text: initialGoal,
        specificity: 0.1,
        facets: {}
      };
    }
    
    refineWithFacet(facetName, value) {
      this.goal.facets[facetName] = value;
      this.goal.specificity = Object.keys(this.goal.facets).length / 10;
      this.goal.refined = this.synthesizeGoal();
      return this.goal;
    }
    
    synthesizeGoal() {
      // Combine original goal with facet selections
      return \`\${this.goal.text} specifically focusing on \${
        Object.entries(this.goal.facets)
          .map(([k,v]) => \`\${k}: \${v}\`)
          .join(', ')
      }\`;
    }
  }
`);
```

## UI Generation

### Faceted Pie Menus
Combine pie menus with facets for spatial+categorical selection:

```javascript
// Pie menu where each slice opens a facet
pieMenu.defineFaceted({
  name: "SmartActions",
  slices: [
    {
      label: "Create",
      angle: 0,
      facets: ["type", "template", "location"],
      color: "creative"
    },
    {
      label: "Connect", 
      angle: 90,
      facets: ["source", "target", "relationship"],
      color: "connective"
    },
    {
      label: "Transform",
      angle: 180,
      facets: ["input", "operation", "output"],
      color: "transformative"
    },
    {
      label: "Analyze",
      angle: 270,
      facets: ["subject", "method", "depth"],
      color: "analytical"
    }
  ]
});
```

### Adaptive Layouts
```javascript
// NeLLM determines optimal layout based on facet characteristics
nellm.eval(`
  function optimizeLayout(facets) {
    const characteristics = analyzeFacets(facets);
    
    if (characteristics.totalOptions < 20) {
      return 'grid';  // Simple grid for few options
    } else if (characteristics.hierarchical) {
      return 'treemap';  // Shneiderman's treemap for hierarchies
    } else if (characteristics.continuous > 2) {
      return 'parallel-coordinates';  // For multiple continuous facets
    } else {
      return 'starfield';  // For large categorical spaces
    }
  }
`);
```

## Benefits

1. **Progressive Disclosure**: Start simple, reveal complexity as needed
2. **No Overwhelm**: Each choice narrows the possibility space
3. **Reversible**: Easy to backtrack and try different paths
4. **Learnable**: System learns user's facet preferences
5. **Efficient**: NeLLM reduces complex operations to tiny commands
6. **Visual**: Multiple visualization options via downloaded renderers

## Example: Complete Faceted Interaction

```javascript
// User clicks "I need to do something"
nellm.eval(`
  const menu = createFacetedMenu({
    context: getCurrentContext(),
    history: menuState.history,
    goal: extractGoal()
  });
  
  // Initial facets based on context
  menu.showFacets(['action', 'urgency']);
`);

// User selects action: "fix"
nellm.eval(`
  menu.selectFacet('action', 'fix');
  // Automatically shows: ['problem_type', 'component', 'severity']
`);

// User selects problem_type: "error"  
nellm.eval(`
  menu.selectFacet('problem_type', 'error');
  // Shows recent errors and adds facet: ['error_code', 'frequency']
`);

// Final command construction
nellm.eval(`
  const command = menu.buildCommand();
  // Returns: "lloooomm://debug/error?type=runtime&component=parser&severity=high"
`);
```

The Faceted Menu Protocol brings Shneiderman's vision of dynamic queries to LLOOOOMM, making complex command spaces navigable through progressive refinement. 