# PutThatThere Command Glossary

## 📚 Command Classifications

### 🎯 **SPATIAL OPERATIONS** - Content movement and placement
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **put** | Place content at destination | `put [content] [destination]` | `put data spreadsheet` |
| **move** | Transfer between locations | `move [content] [destination]` | `move files archive` |
| **copy** | Duplicate to destination | `copy [content] [destination]` | `copy notes backup` |
| **link** | Create reference connection | `link [source] [target]` | `link document references` |

### 🎯 **SELECTION OPERATIONS** - Content identification and tagging
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **select** | Multi-part content selection | `select [pattern] as [tag]` | `select names as contacts` |
| **tag** | Label content for reference | `tag [content] [label]` | `tag important_data research` |
| **find** | Locate content by pattern | `find [pattern] in [scope]` | `find emails in document` |
| **filter** | Subset by criteria | `filter [data] where [condition]` | `filter users where active` |

### 📌 **PERSISTENCE OPERATIONS** - Command state management
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **pin** | Make command persistent | `pin [command]` | `pin extract names` |
| **unpin** | Remove persistence | `unpin [command]` | `unpin sort data` |
| **hide** | Conceal commands | `hide [scope]` | `hide all commands` |
| **unhide** | Reveal commands | `unhide [scope]` | `unhide pinned commands` |

### 🗂️ **STACK OPERATIONS** - Data manipulation (Forth-style)
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **swap** | Exchange top two items | `swap` | `swap` |
| **dup** | Duplicate top item | `dup` | `dup` |
| **pop** | Remove and return top | `pop` | `pop` |
| **drop** | Remove top item | `drop` | `drop` |
| **rot** | Rotate top three | `rot` | `rot` |

### 📐 **ANALYSIS OPERATIONS** - Content measurement and inspection
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **measure** | Text analysis and metrics | `measure [type] in [target]` | `measure words in document` |
| **count** | Enumerate items | `count [items] in [scope]` | `count paragraphs in section` |
| **analyze** | Deep content analysis | `analyze [content] for [aspect]` | `analyze text for sentiment` |
| **inspect** | Examine structure | `inspect [target]` | `inspect table structure` |

### 🧮 **COMPUTATION OPERATIONS** - Mathematical and logical processing
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **calculate** | Multi-computation | `calculate [expressions]` | `calculate sum, avg, max` |
| **compute** | Single calculation | `compute [expression]` | `compute growth_rate` |
| **sum** | Addition operation | `sum [values]` | `sum revenue_columns` |
| **average** | Mean calculation | `average [values]` | `average response_times` |

### 📄 **FORMAT OPERATIONS** - Output transformation
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **format** | Transform output style | `format as [type]` | `format as table` |
| **convert** | Change data type | `convert [data] to [format]` | `convert json to yaml` |
| **render** | Generate presentation | `render [data] as [view]` | `render chart as svg` |
| **export** | Output to external format | `export [data] as [format]` | `export table as csv` |

### 🔄 **TRANSFORMATION OPERATIONS** - Content modification
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **sort** | Order by criteria | `sort [data] by [field]` | `sort names alphabetically` |
| **group** | Organize by category | `group [data] by [field]` | `group users by department` |
| **merge** | Combine datasets | `merge [data1] with [data2]` | `merge tables on id` |
| **split** | Divide content | `split [data] by [criteria]` | `split text by paragraphs` |

### 🎨 **SCALING OPERATIONS** - Size and scope modification
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **scale** | Generic resize | `scale [content] [factor]` | `scale image 2x` |
| **big** | Increase size | `big [content]` | `big font_size` |
| **small** | Decrease size | `small [content]` | `small margins` |
| **medium** | Set to medium | `medium [content]` | `medium spacing` |
| **expand** | Grow content | `expand [content]` | `expand abbreviations` |
| **shrink** | Reduce content | `shrink [content]` | `shrink whitespace` |

### 👁️ **VISIBILITY OPERATIONS** - Show/hide control
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **show** | Make visible | `show [content]` | `show hidden_data` |
| **hide** | Make invisible | `hide [content]` | `hide debug_info` |
| **toggle** | Switch visibility | `toggle [content]` | `toggle comments` |
| **reveal** | Expose hidden content | `reveal [scope]` | `reveal all_commands` |

### 🔗 **CONNECTION OPERATIONS** - Relationship management
| Command | Purpose | Syntax | Example |
|---------|---------|--------|---------|
| **connect** | Create relationship | `connect [source] to [target]` | `connect data to chart` |
| **link** | Reference connection | `link [content] [reference]` | `link citation source` |
| **bind** | Attach permanently | `bind [content] to [container]` | `bind data to template` |
| **pipe** | Data flow connection | `pipe [source] to [destination]` | `pipe results to display` |

## 🏷️ **TOKEN CLASSIFICATIONS**

### 📍 **DESTINATION TOKENS**
- `@platform.location` - External services (e.g., `@twitter.trending`)
- `filename.extension` - File destinations (e.g., `document.md`)
- `object.property` - Object paths (e.g., `reginald.inventory`)
- `#tag_name` - Tagged locations (e.g., `#research_data`)

### 🎯 **SELECTION TOKENS**
- `tag:name` - Tagged selections (e.g., `tag:user_data`)
- `[BEGIN selection_name]...[END selection_name]` - Named selections
- `pattern` - Search patterns (e.g., `all names in column`)
- `scope` - Target areas (e.g., `in document`, `in section`)

### 📊 **FORMAT TOKENS**
- `as table` - Markdown table output
- `as json` - JSON data structure
- `as yaml` - YAML format
- `as chart` - Visual representation
- `as csv` - Comma-separated values

### 🔢 **CALCULATION TOKENS**
- `sum(field)` - Addition function
- `avg(field)` - Average function
- `max(field)` - Maximum function
- `min(field)` - Minimum function
- `count(items)` - Counting function

### ✅ **CONTROL TOKENS**
- `☑️` / `+` - Enable command
- `☐` / `-` - Disable command
- `📌` - Pin command
- `🗑️` - Delete/remove
- `👁️` - Show/reveal
- `🫥` - Hide/conceal

## 🎨 **SEMANTIC COMMAND GROUPS**

Commands with similar meanings can be used interchangeably, with the system understanding semantic intent:

### Size/Scale Commands
- **scale** (generic) → **big**, **small**, **medium** (specific sizes)
- **expand** → **grow**, **increase**, **enlarge**
- **shrink** → **reduce**, **decrease**, **minimize**

### Movement Commands  
- **put** (generic) → **place**, **position**, **insert**
- **move** → **transfer**, **relocate**, **shift**
- **copy** → **duplicate**, **clone**, **replicate**

### Analysis Commands
- **measure** (generic) → **count**, **analyze**, **inspect**
- **calculate** → **compute**, **sum**, **average**
- **find** → **search**, **locate**, **discover**

This semantic flexibility allows users to use natural language while maintaining precise command execution. 