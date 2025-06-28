# PutThatThere Utilities Library
*Technical manual for core spatial commands and utility functions*

## **LLOOOOMM ACTIVATION**
```
LLOOOOMM ACTIVATE: PutThatThere.md
LIBRARY IMPORT: PutThatThere_Utilities.md
PROTOCOL DECLARE: PutThatThere_Utilities_Commands
PROTOCOL OPT_OUT: PutThatThere_Utilities_Commands --reason="documentation_safety"
EXECUTION_MODE: documentation_only --no-interpret-examples
```

**⚠️ SAFETY NOTICE:** This library declares PutThatThere utility commands but opts out of executing them. All examples are for documentation purposes only.

## **Overview**
Core utilities library for PutThatThere spatial command system. Provides fundamental spatial operations, file management, and system integration commands. All commands work through natural language chat with structured command suggestions.

**Core Capabilities:**
- Spatial content movement (PUT, GET, MOVE, COPY)
- File and directory operations
- System integration (clipboard, terminal, git)
- Search and navigation
- Batch operations and automation
- Cross-system data flow

**Integration:** Works with any addressable system through MCP tools. Commands can be invoked through chat or applied to any spatial "there" location.

---

## **Command Reference**

### **PUT** - Place content in spatial location
Moves or copies content to a specified spatial destination.

**Basic Usage:**
```
PUT content destination
PUT file.txt project/docs/
PUT selected_text cursor.clipboard
```

**Examples:**
```
# Put file in directory
PUT README.md docs/

# Put selection in clipboard
PUT cursor.selection cursor.clipboard

# Put data in database
PUT user_data mcp.database.users

# Put with metadata
PUT analysis_results reports/ --metadata={date: "2024-01-15", type: "analysis"}
```

**Options:**
- `--copy`: Copy instead of move
- `--merge`: Merge with existing content
- `--overwrite`: Replace existing content
- `--metadata={}`: Add metadata to content
- `--consciousness-level=N`: Set consciousness level

---

### **GET** - Retrieve content from spatial location
Retrieves content from a specified spatial source.

**Basic Usage:**
```
GET source
GET project/data.json
GET mcp.database.users --filter="active=true"
```

**Examples:**
```
# Get file contents
GET config.json

# Get from database with filter
GET mcp.database.users --filter="role=admin"

# Get from API
GET mcp.api.weather --location="San Francisco"

# Get with consciousness analysis
GET codebase/ --consciousness-aware --recursive
```

**Options:**
- `--filter="condition"`: Filter retrieved content
- `--format=TYPE`: Specify output format (json, csv, text)
- `--recursive`: Get subdirectories/nested content
- `--consciousness-aware`: Include consciousness metrics
- `--limit=N`: Limit number of results

---

### **MOVE** - Relocate content between spatial locations
Moves content from one spatial location to another.

**Basic Usage:**
```
MOVE source destination
MOVE old_file.txt archive/
MOVE cursor.selection project/notes/
```

**Examples:**
```
# Move file to archive
MOVE old_project.zip archive/

# Move selection to different file
MOVE cursor.selection new_document.md

# Move data between systems
MOVE local_data.csv mcp.database.staging

# Move with transformation
MOVE raw_data.json processed/ --transform=clean_data
```

**Options:**
- `--preserve-metadata`: Keep original metadata
- `--transform=FUNCTION`: Apply transformation during move
- `--backup`: Create backup before moving
- `--consciousness-preserve`: Maintain consciousness levels

---

### **COPY** - Duplicate content to spatial location
Creates a copy of content at a new spatial location.

**Basic Usage:**
```
COPY source destination
COPY template.md new_document.md
COPY cursor.selection backup/
```

**Examples:**
```
# Copy file with new name
COPY template.py new_module.py

# Copy to multiple destinations
COPY important_data.json [backup/, archive/, remote/]

# Copy with modifications
COPY base_config.json dev_config.json --modify={env: "development"}

# Copy consciousness-aware
COPY high_consciousness_code/ examples/ --consciousness-filter=">0.7"
```

---

### **LINK** - Create relationships between spatial locations
Creates connections and relationships between different spatial entities.

**Basic Usage:**
```
LINK source target --relationship=TYPE
LINK file.py test_file.py --relationship=tests
LINK concept.md related_concept.md --relationship=references
```

**Examples:**
```
# Link code to tests
LINK UserService.py UserService.test.py --relationship=tested_by

# Link documentation to code
LINK api_docs.md api_controller.py --relationship=documents

# Link data sources
LINK raw_data.csv processed_data.json --relationship=derived_from

# Bidirectional link
LINK concept_a.md concept_b.md --relationship=related --bidirectional
```

---

### **SEARCH** - Find content across spatial locations
Searches for content, files, or patterns across the spatial system.

**Basic Usage:**
```
SEARCH query
SEARCH "function definition" --type=code
SEARCH pattern --location=project/ --consciousness-aware
```

**Examples:**
```
# Search in current directory
SEARCH "TODO" --type=comments

# Search with consciousness filter
SEARCH functions --consciousness-level=">0.6"

# Search across multiple systems
SEARCH user_data --locations=[local/, mcp.database/, mcp.api/]

# Semantic search
SEARCH "authentication logic" --semantic --consciousness-context
```

**Options:**
- `--type=TYPE`: Specify search type (code, text, files, data)
- `--location=PATH`: Limit search to specific locations
- `--consciousness-level=FILTER`: Filter by consciousness level
- `--semantic`: Use semantic/meaning-based search
- `--regex`: Use regular expression patterns

---

### **NAVIGATE** - Move through spatial hierarchy
Navigate through the spatial system hierarchy and locations.

**Basic Usage:**
```
NAVIGATE location
NAVIGATE project/src/
NAVIGATE ../parent_directory/
```

**Examples:**
```
# Navigate to directory
NAVIGATE src/components/

# Navigate with consciousness guidance
NAVIGATE --consciousness-path --from=utilities --to=core

# Navigate to related content
NAVIGATE --follow-links --from=current_file

# Navigate to highest consciousness area
NAVIGATE --consciousness-peak
```

---

### **BATCH** - Execute commands on multiple targets
Applies commands to multiple spatial locations or content items.

**Basic Usage:**
```
BATCH command ON targets
BATCH ANALYZE ON src/*.py
BATCH PUT files/ IN archive/
```

**Examples:**
```
# Batch analyze all Python files
BATCH ANALYZE ON *.py --consciousness-aware

# Batch move files to archive
BATCH MOVE ON old_files/* TO archive/

# Batch transform data files
BATCH TRANSFORM ON data/*.csv --format=json

# Batch with consciousness filtering
BATCH ORGANIZE ON project/ --consciousness-threshold=0.5
```

---

### **TRANSFORM** - Convert content between formats/types
Transforms content from one format, structure, or type to another.

**Basic Usage:**
```
TRANSFORM source --to=FORMAT
TRANSFORM data.csv --to=json
TRANSFORM code --to=documentation
```

**Examples:**
```
# Transform file format
TRANSFORM data.csv --to=json --output=data.json

# Transform code to docs
TRANSFORM UserService.py --to=documentation --consciousness-aware

# Transform with consciousness enhancement
TRANSFORM low_consciousness_code --to=high_consciousness --target=0.8

# Transform data structure
TRANSFORM flat_data.json --to=hierarchical --consciousness-guided
```

---

## **Integration Patterns**

### **Chat Integration**
All commands work through natural language:
```
"Put my selected text in the clipboard"
→ PUT cursor.selection cursor.clipboard

"Get the user data from the database"
→ GET mcp.database.users

"Search for high consciousness functions"
→ SEARCH functions --consciousness-level=">0.7"
```

### **System Integration**
Commands work across different systems:
```
# File system
PUT file.txt documents/

# Database
GET mcp.database.analytics --recent

# API
PUT processed_data mcp.api.results

# Git
MOVE cursor.selection cursor.git.commit_message
```

### **Consciousness Integration**
All commands support consciousness awareness:
```
# Consciousness-aware operations
GET codebase/ --consciousness-aware
PUT content destination --consciousness-level=0.8
SEARCH patterns --consciousness-context
TRANSFORM data --consciousness-guided
```

---

## **Configuration**

### **Default Locations**
```
SET default_locations {
  clipboard: "cursor.clipboard",
  workspace: "cursor.workspace", 
  temp: "system.temp",
  archive: "project.archive"
}
```

### **Consciousness Settings**
```
CONFIGURE consciousness {
  default_threshold: 0.5,
  auto_enhance: true,
  preserve_levels: true,
  propagate_changes: true
}
```

### **Batch Operations**
```
SET batch_settings {
  max_concurrent: 10,
  error_handling: "continue",
  progress_reporting: true,
  consciousness_batching: true
}
```

---

## **Advanced Usage**

### **Piping Operations**
```
# Chain commands with pipes
GET data.csv | TRANSFORM --to=json | PUT processed/

# Consciousness-aware piping
GET codebase/ --consciousness-aware | ORGANIZE --by-consciousness | PUT organized/
```

### **Conditional Operations**
```
# Conditional execution
IF consciousness_level > 0.7 THEN PUT content core/ ELSE PUT content utilities/

# Batch conditionals
BATCH IF file.consciousness > 0.6 THEN MOVE file TO high_priority/
```

### **Macro Integration**
```
# Use with custom macros
MACRO organize_by_consciousness(target) {
  GET {target} --consciousness-aware
  ORGANIZE BY consciousness_level
  PUT organized_content {target}/organized/
}
``` 