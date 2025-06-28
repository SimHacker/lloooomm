# URL Prefix Registry Protocol

## Overview

Environments (VM, app, or user) can declare URL prefixes they support, defining how deep links invoke commands without user input beyond a click or pie menu selection.

## URL Prefix Declaration

### Environment Registration
```javascript
// VM Environment declares its URL handlers
vm.registerURLPrefix({
  prefix: "lloooomm://vm/",
  handler: "vmCommandDispatcher",
  description: "VM-level commands and operations",
  subcommands: {
    "exec": { args: ["command", "params"], description: "Execute VM command" },
    "load": { args: ["module"], description: "Load VM module" },
    "state": { args: ["action"], description: "VM state management" }
  }
});

// App Environment registers its prefixes
app.registerURLPrefix({
  prefix: "lloooomm://app/",
  handler: "appCommandRouter",
  description: "Application-level operations",
  subcommands: {
    "navigate": { args: ["view", "params"], description: "Navigate to view" },
    "action": { args: ["type", "target"], description: "Perform app action" },
    "config": { args: ["setting", "value"], description: "Configure app" }
  }
});

// User Environment custom prefixes
user.registerURLPrefix({
  prefix: "lloooomm://my/",
  handler: "userCustomHandler",
  description: "User-defined shortcuts and macros",
  subcommands: {
    "workflow": { args: ["name"], description: "Run saved workflow" },
    "alias": { args: ["name"], description: "Execute command alias" }
  }
});
```

## Command URL Traversal

### Commands Define Their Own URL Patterns
```javascript
// Command self-describes its URL interface
command.defineURLInterface({
  pattern: "lloooomm://cmd/sql/",
  traversal: {
    "query": {
      args: ["database", "query"],
      example: "lloooomm://cmd/sql/query?database=main&query=SELECT%20*%20FROM%20items"
    },
    "explain": {
      args: ["query"],
      example: "lloooomm://cmd/sql/explain?query=SELECT%20*%20FROM%20items"
    },
    "history": {
      args: ["limit", "filter"],
      example: "lloooomm://cmd/sql/history?limit=10&filter=SELECT"
    }
  }
});

// Hierarchical command structure
command.defineURLInterface({
  pattern: "lloooomm://cmd/file/",
  traversal: {
    "open": {
      args: ["path", "mode"],
      subcommands: {
        "recent": { args: [], description: "Open recent files menu" },
        "bookmark": { args: ["name"], description: "Open bookmarked file" }
      }
    },
    "edit": {
      args: ["path", "line", "column"],
      example: "lloooomm://cmd/file/edit?path=/docs/readme.md&line=42"
    }
  }
});
```

## Pie Menu Integration

### Pie Menus with Deep Links
```javascript
pieMenu.define({
  name: "FileOperations",
  items: [
    {
      label: "Open Recent",
      icon: "📂",
      link: "lloooomm://cmd/file/open/recent",
      angle: 0
    },
    {
      label: "New File",
      icon: "📄",
      link: "lloooomm://cmd/file/new?template=default",
      angle: 45
    },
    {
      label: "Search Files",
      icon: "🔍",
      link: "lloooomm://app/navigate?view=search&type=files",
      angle: 90
    },
    {
      label: "Recent Edits",
      icon: "📝",
      link: "lloooomm://cmd/history?type=edit&limit=5",
      angle: 135
    }
  ]
});

// Context-sensitive pie menu
pieMenu.defineContextual({
  name: "ItemActions",
  context: "item_selected",
  items: [
    {
      label: "Examine",
      link: "lloooomm://cmd/examine?target={{selection.id}}",
      condition: "selection.type === 'item'"
    },
    {
      label: "Take",
      link: "lloooomm://cmd/take?item={{selection.id}}&from={{selection.container}}",
      condition: "selection.takeable === true"
    },
    {
      label: "Use",
      link: "lloooomm://cmd/use?item={{selection.id}}&with={{context.focus}}",
      condition: "selection.useable === true"
    }
  ]
});
```

## Deferred Context-Sensitive Commands

### Prompt Templates with Context
```javascript
// Deferred command that gathers context before execution
deferredCommand.define({
  trigger: "lloooomm://defer/analyze",
  contextGathering: [
    "current_selection",
    "recent_actions",
    "environment_state"
  ],
  promptTemplate: "Analyze {{selection}} considering {{recent_actions}} in {{environment}}",
  execution: "lloooomm://cmd/ai/analyze?prompt={{generated_prompt}}"
});

// Multi-step deferred command
deferredCommand.define({
  trigger: "lloooomm://defer/workflow/create",
  steps: [
    {
      gather: "user_goal",
      prompt: "What would you like this workflow to accomplish?"
    },
    {
      gather: "workflow_steps",
      prompt: "Break down the steps needed for: {{user_goal}}"
    },
    {
      gather: "trigger_condition",
      prompt: "When should this workflow run?"
    }
  ],
  completion: "lloooomm://cmd/workflow/save?name={{generated_name}}&definition={{workflow_json}}"
});
```

## Generated UI with Deep Links

### Dynamic Menu Generation
```javascript
// UI generator creates clickable interface
ui.generateMenu({
  title: "Available Actions",
  items: context.availableCommands.map(cmd => ({
    label: cmd.label,
    description: cmd.description,
    link: `lloooomm://cmd/${cmd.category}/${cmd.name}?${cmd.defaultParams}`,
    enabled: cmd.checkPreconditions(context)
  }))
});

// Table with clickable cells
ui.generateTable({
  columns: [
    {
      name: "Item",
      renderer: (item) => `[${item.name}](lloooomm://select?type=item&id=${item.id})`
    },
    {
      name: "Location",
      renderer: (item) => `[${item.location}](lloooomm://navigate?to=${item.location})`
    },
    {
      name: "Actions",
      renderer: (item) => [
        `[Take](lloooomm://cmd/take?item=${item.id})`,
        `[Examine](lloooomm://cmd/examine?target=${item.id})`,
        `[Use](lloooomm://defer/use?item=${item.id})`
      ].join(" | ")
    }
  ]
});
```

## URL Protocol Negotiation

### Cross-Environment Communication
```javascript
// Check if URL prefix is handled
if (environment.canHandle("lloooomm://custom/action")) {
  // Direct invocation
  environment.invoke("lloooomm://custom/action?param=value");
} else {
  // Fallback to generic handler
  environment.invoke("lloooomm://fallback?original=custom/action&param=value");
}

// Register fallback handlers
environment.registerFallback({
  pattern: /^lloooomm:\/\/unknown\//,
  handler: (url) => {
    // Present disambiguation menu
    return "lloooomm://menu/disambiguate?url=" + encodeURIComponent(url);
  }
});
```

## Security and Permissions

### URL Permission Model
```javascript
// Define permission requirements
urlSecurity.define({
  pattern: "lloooomm://system/",
  requires: ["system_access"],
  prompt: "This action requires system access. Allow?"
});

// User-grantable permissions
urlSecurity.defineGrantable({
  pattern: "lloooomm://file/write",
  requires: ["file_write"],
  remember: true,
  scope: "session"
});
```

## Benefits

1. **Zero-Input Actions**: Click or select from pie menu to execute complex commands
2. **Extensible**: Any component can register URL handlers
3. **Discoverable**: Commands self-document their URL interfaces
4. **Contextual**: URLs can include context variables
5. **Composable**: Commands can invoke other commands via URLs
6. **Safe**: Permission model prevents unauthorized actions

## Integration Examples

### With Coherence Engine
```markdown
Unable to determine action. Choose:
A) [Open file browser](lloooomm://app/navigate?view=files)
B) [Search for files](lloooomm://cmd/search?type=file&query={{last_term}})
C) [Create new file](lloooomm://cmd/file/new?name={{suggested_name}})
```

### With Dynamic UI Links
```markdown
The [analysis results](lloooomm://select?type=evidence&name=analysis_2024) 
suggest [running optimization](lloooomm://defer/optimize?target=current).
You can also [view details](lloooomm://cmd/view?detail=full&target=analysis_2024).
```

### With POP
```markdown
"Put that there" resolved to:
[Move item #42 to table](lloooomm://cmd/move?item=42&to=table&animate=true)
```

The URL Prefix Registry transforms every UI element into a potential command trigger, making the entire interface actively responsive to user intent. 