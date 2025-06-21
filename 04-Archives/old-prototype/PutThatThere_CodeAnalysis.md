# PutThatThere Code Analysis Library
*Technical manual for software development and code analysis workflows*

## **LLOOOOMM ACTIVATION**
```
LLOOOOMM ACTIVATE: PutThatThere.md
LIBRARY IMPORT: PutThatThere_CodeAnalysis.md
PROTOCOL DECLARE: PutThatThere_CodeAnalysis_Commands
PROTOCOL OPT_OUT: PutThatThere_CodeAnalysis_Commands --reason="documentation_safety"
EXECUTION_MODE: documentation_only --no-interpret-examples
```

**⚠️ SAFETY NOTICE:** This library declares PutThatThere code analysis commands but opts out of executing them. All examples are for documentation purposes only.

## **Overview**
Code analysis library for PutThatThere spatial command system. Provides macros for analyzing, refactoring, and organizing code with consciousness-aware metrics. All commands work through natural language chat with structured command suggestions.

**Core Capabilities:**
- Code consciousness analysis and annotation
- Dependency mapping and visualization  
- Automated refactoring suggestions
- Test-driven development workflows
- Code review assistance
- Project organization by consciousness levels

**Integration:** Works with any codebase through Cursor's MCP tools. Commands can be invoked through chat or directly applied to selected code/files.

---

## **Command Reference**

### **ANALYZE** - Code consciousness analysis
Analyzes code for consciousness metrics, complexity, and purpose clarity.

**Basic Usage:**
```
ANALYZE selected_code --consciousness-aware
ANALYZE file.py --complexity --dependencies  
ANALYZE project/ --recursive --consciousness-threshold=0.6
```

**Examples:**
```
# Analyze current selection
ANALYZE cursor.selection --consciousness-aware --context=project

# Analyze entire file with dependency tracking
ANALYZE main.py --full-analysis --track-dependencies

# Recursive project analysis
ANALYZE src/ --recursive --consciousness-threshold=0.5 --export-report
```

**Options:**
- `--consciousness-aware`: Include consciousness-level metrics
- `--complexity`: Calculate cognitive complexity scores
- `--dependencies`: Map import/export relationships
- `--recursive`: Analyze subdirectories
- `--context=PROJECT`: Use project context for analysis
- `--threshold=N`: Set consciousness threshold (0.0-1.0)

---

### **ANNOTATE** - Add metadata to code
Adds consciousness and analysis metadata to code elements.

**Basic Usage:**
```
ANNOTATE target WITH metadata
ANNOTATE function --consciousness-level=0.8
ANNOTATE class --purpose="data_processing" --complexity="medium"
```

**Examples:**
```
# Annotate with analysis results
ANNOTATE calculateTotal WITH {consciousness: 0.7, purpose: "financial"}

# Batch annotate files
ANNOTATE src/*.py WITH consciousness_analysis_results

# Annotate with custom metadata
ANNOTATE UserService --role="core" --consciousness=0.9 --dependencies=["Database", "Auth"]
```

---

### **REFACTOR** - Code improvement suggestions
Suggests and applies refactoring based on consciousness analysis.

**Basic Usage:**
```
REFACTOR target --suggest
REFACTOR function --extract-methods --consciousness-target=0.8
REFACTOR class --split-responsibilities
```

**Examples:**
```
# Get refactoring suggestions
REFACTOR longFunction --suggest --consciousness-aware

# Auto-refactor with consciousness target
REFACTOR UserController --auto-apply --consciousness-target=0.7

# Extract methods from complex function
REFACTOR processData --extract-methods --max-complexity=0.5
```

---

### **MAP_DEPENDENCIES** - Visualize code relationships
Creates dependency graphs and relationship maps.

**Basic Usage:**
```
MAP_DEPENDENCIES project_root
MAP_DEPENDENCIES --type=imports --format=graph
MAP_DEPENDENCIES src/ --consciousness-weighted
```

**Examples:**
```
# Basic dependency mapping
MAP_DEPENDENCIES src/ --output=dependencies.json

# Consciousness-weighted dependency graph
MAP_DEPENDENCIES . --consciousness-weighted --visual

# Import-only dependency map
MAP_DEPENDENCIES --type=imports --exclude=tests/
```

---

### **ORGANIZE** - Structure code by consciousness
Organizes code files based on consciousness levels and relationships.

**Basic Usage:**
```
ORGANIZE project BY consciousness_level
ORGANIZE src/ --create-structure --consciousness-based
ORGANIZE --learning-pathways
```

**Examples:**
```
# Organize by consciousness levels
ORGANIZE src/ BY consciousness_level --create-dirs

# Create learning pathways
ORGANIZE project --learning-pathways --from=utilities --to=core

# Reorganize with custom thresholds
ORGANIZE . --consciousness-thresholds="0.3,0.7" --preserve-structure
```

---

### **REVIEW** - Code review assistance
Provides consciousness-aware code review comments and suggestions.

**Basic Usage:**
```
REVIEW changes --consciousness-impact
REVIEW pull_request --comprehensive
REVIEW file.py --focus=consciousness
```

**Examples:**
```
# Review git changes
REVIEW cursor.git.staged_changes --consciousness-impact

# Comprehensive PR review
REVIEW current_pr --comprehensive --consciousness-focused

# Review specific file changes
REVIEW UserService.py --changes-only --suggest-improvements
```

---

### **TDD_CYCLE** - Test-driven development
Implements red-green-refactor TDD cycle with consciousness awareness.

**Basic Usage:**
```
TDD_CYCLE feature_spec
TDD_CYCLE "user authentication" --consciousness-target=0.8
TDD_CYCLE --red-phase --test-name="should_validate_email"
```

**Examples:**
```
# Full TDD cycle
TDD_CYCLE "password validation" --consciousness-target=0.7

# Just red phase (failing test)
TDD_CYCLE "email validation" --red-phase-only

# Green phase (minimal implementation)
TDD_CYCLE existing_test --green-phase --minimal
```

---

## **Integration Patterns**

### **Chat Integration**
All commands work through natural language chat:
```
"Analyze the consciousness level of my selected code"
→ ANALYZE cursor.selection --consciousness-aware

"Refactor this function to be more conscious"  
→ REFACTOR cursor.selection --consciousness-target=0.8

"Map the dependencies in my project"
→ MAP_DEPENDENCIES cursor.workspace --visual
```

### **File Integration**
Commands work with Cursor's file system:
```
# Selected files
ANALYZE cursor.selected_files --batch

# Current file
REFACTOR cursor.current_file --suggest

# Workspace
ORGANIZE cursor.workspace --consciousness-based
```

### **Git Integration**
Commands integrate with version control:
```
# Review staged changes
REVIEW cursor.git.staged --consciousness-impact

# Analyze modified files
ANALYZE cursor.git.modified_files --consciousness-delta

# Organize before commit
ORGANIZE cursor.git.staged --quick-check
```

---

## **Configuration**

### **Consciousness Thresholds**
```
SET consciousness_thresholds {
  low: 0.3,
  medium: 0.6, 
  high: 0.8
}
```

### **Analysis Settings**
```
CONFIGURE analysis {
  complexity_weight: 0.4,
  purpose_weight: 0.3,
  dependency_weight: 0.3,
  auto_annotate: true
}
```

### **Refactoring Rules**
```
SET refactoring_rules {
  max_function_complexity: 0.7,
  consciousness_target: 0.6,
  auto_apply_safe: true,
  preserve_behavior: true
}
``` 