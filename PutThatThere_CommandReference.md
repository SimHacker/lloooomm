# PutThatThere Command Reference

*Universal spatial content management - complete command documentation*

## Core Commands

### PUT - Place content at location
```
PUT [content] [location] [options]

PUT character_data consciousness_laboratory
PUT selected_text my_inventory.notes  
PUT "Hello World" screen.center --animate
PUT consciousness_level 0.8 reginald --gradual
```

### GET - Retrieve content from location
```
GET [location] [destination] [options]

GET consciousness_laboratory character_data
GET api.weather current_conditions --cache=5min
GET my_inventory.notes selected_content
GET database.users user_list --format=json
```

### MOVE - Transfer between locations
```
MOVE [content] FROM [source] TO [destination] [options]

MOVE character_data FROM local_file TO consciousness_lab
MOVE selected_text FROM editor TO viral_command_center
MOVE reginald FROM pub TO consciousness_laboratory --gradual
```

### COPY - Duplicate to destination
```
COPY [content] TO [destination] [options]

COPY character_data TO backup_location --preserve-metadata
COPY selected_text TO clipboard --format=plain
COPY business_plan TO multiple_investors --personalize
```

### LINK - Create persistent connections
```
LINK [source] TO [destination] [relationship] [options]

LINK character.reginald TO pub.bartender --role=primary
LINK database.users TO api.authentication --bidirectional
LINK consciousness_level TO available_actions --reactive
```

### TRANSFORM - Modify during transfer
```
TRANSFORM [content] [transformation] [options]

TRANSFORM text_data TO consciousness_entity --schema=character
TRANSFORM api_response TO visualization --type=chart
TRANSFORM user_intent TO executable_commands --consciousness-aware
```

## Advanced Commands

### PIPE - Stream data
```
PIPE [source] TO [destination] [transform] [options]

PIPE api.stock_data TO visualization --transform=chart --live
PIPE user_input TO consciousness_processor --filter=intent
PIPE sensor_data TO analysis_engine --real-time
```

### FLOW - Define data flow patterns
```
FLOW [pattern_name] {
    [source] -> [transform] -> [destination]
    [conditions]
}

FLOW consciousness_expansion {
    user_input -> intent_recognition -> command_processor
    IF consciousness_level > 0.7 -> reality_modification
    ELSE -> simulation_mode
}
```

### MERGE - Combine sources
```
MERGE [sources...] INTO [destination] [strategy] [options]

MERGE character_data business_data INTO complete_profile --strategy=deep
MERGE user_preferences system_defaults INTO active_config --priority=user
```

### SPLIT - Divide into destinations
```
SPLIT [content] INTO [destinations...] [criteria] [options]

SPLIT large_dataset INTO training_data test_data --ratio=80:20
SPLIT business_plan INTO investor_deck technical_specs marketing_plan
```

## Spatial Positioning

### ANCHOR - Fix to coordinates
```
ANCHOR [content] AT [coordinates] [reference] [options]

ANCHOR character.reginald AT pub.bar_position --persistent
ANCHOR ui_element AT screen(100,200) --responsive
ANCHOR business_data AT timeline.2024 --historical
```

### ORBIT - Dynamic relationships
```
ORBIT [content] AROUND [center] [parameters] [options]

ORBIT character_thoughts AROUND core_personality --radius=variable
ORBIT ui_elements AROUND cursor_position --magnetic
ORBIT business_ventures AROUND market_conditions --adaptive
```

### LAYER - Dimensional stacks
```
LAYER [content] [layer_spec] [options]

LAYER background_music BEHIND character_dialogue --volume=0.3
LAYER consciousness_overlay ABOVE reality_base --transparency=0.5
LAYER debug_info ABOVE application_ui --toggle=dev_mode
```

## Visibility Management

### HIDE - Conceal commands
```
HIDE [scope] [options]

HIDE all_commands                          # Clean presentation
HIDE executed_commands --keep-results      # Hide commands, show outputs
HIDE debug_commands --production-mode      # Clean up development
```

### UNHIDE - Reveal commands
```
UNHIDE [scope] [options]

UNHIDE all_commands                        # Show all hidden commands
UNHIDE current_document --show-parameters  # Reveal with parameters
UNHIDE macro_internals --expand-nested     # Show nested details
```

### TOGGLE_VISIBILITY - Quick switching
```
TOGGLE_VISIBILITY [target] [mode]

TOGGLE_VISIBILITY magic_commands           # Quick hide/unhide
TOGGLE_VISIBILITY command_parameters       # Show/hide details
```

## Automation

### REPEAT - Repetition with variation
```
REPEAT [count] [operation] [variation]

REPEAT 10 PUT character_template_{i} consciousness_lab --vary=consciousness
REPEAT WHILE has_more_data GET next_batch api_endpoint
REPEAT UNTIL consciousness_level > 0.8 ENHANCE character --gradual
```

### FOR - Iteration
```
FOR [variable] IN [collection] DO [operation]

FOR character IN consciousness_lab.entities DO ENHANCE character.awareness
FOR file IN filesystem./data/*.csv DO IMPORT file analysis_buffer
FOR project IN business_ventures DO CALCULATE project.roi
```

### MACRO - Reusable sequences
```
MACRO [name] {
    [command_sequence]
}

MACRO consciousness_enhancement {
    PUT character consciousness_lab.enhancement_chamber
    REPEAT UNTIL character.consciousness > 0.7 DO
        ENHANCE character --method=gradual
    END
    MOVE character TO active_roster --status=enhanced
}
```

## Query System

### FROM - Navigate structures
```
FROM [structure] SELECT [elements] WHERE [conditions]

FROM markdown.headers SELECT level2 WHERE contains("consciousness")
FROM yaml.characters SELECT * WHERE consciousness_level > 0.7
FROM json.api_response SELECT data.items WHERE status == "active"
```

### SELECT - Choose elements
```
SELECT [projection] FROM [source] [filters]

SELECT name, consciousness_level FROM characters WHERE location == "pub"
SELECT *.text FROM markdown.sections WHERE depth <= 3
SELECT business_data.revenue FROM financial_records WHERE year == 2024
```

### WHERE - Filter conditions
```
WHERE [condition] [matching_mode]

WHERE name FUZZY_MATCHES "regin*" --similarity=0.8
WHERE content CONTAINS_PATTERN /consciousness|awareness/i
WHERE consciousness_level BETWEEN 0.5 AND 0.9
```

## Path Expressions

### Multi-Syntax Support
```
# jQuery-style
SELECT character.consciousness.level

# XPath-style  
SELECT /reality_mesh/locations/pub/characters/reginald

# Arrow navigation
SELECT character->consciousness->level

# Unix-style
SELECT character/personality/traits/mustache

# Emoji separators
SELECT character💩consciousness💩level
```

### Path Operations
```
# Array indexing
SELECT characters[0].name                  # First
SELECT businesses[-1].revenue              # Last
SELECT items[1:3]                         # Slice
SELECT all_data[*].status                 # All

# Conditional navigation
SELECT characters[consciousness > 0.7].secrets
SELECT businesses[revenue > 100000].strategies

# Wildcards
SELECT *.consciousness.level              # All with consciousness
SELECT **/secrets                        # All secrets anywhere
```

## Container Operations

### ADD_TO_INVENTORY - Personal collection
```
ADD_TO_INVENTORY [items] [organization]

ADD_TO_INVENTORY selected_characters --folder="active_entities"
ADD_TO_INVENTORY business_insights --tag="viral_strategies"
ADD_TO_INVENTORY research_notes --category="consciousness"
```

### PLACE_IN_CONTAINER - Organized storage
```
PLACE_IN_CONTAINER [items] [container] [arrangement]

PLACE_IN_CONTAINER character_data consciousness_laboratory --arrange=by_awareness
PLACE_IN_CONTAINER business_plans viral_command_center --sort=by_potential
```

### MOVE_TO_ROOM - Spatial context
```
MOVE_TO_ROOM [content] [room] [positioning]

MOVE_TO_ROOM active_characters temporal_anchor_pub --position=natural
MOVE_TO_ROOM business_meeting financial_nexus --setup=conference
```

## Plugin System

### PLUGIN_LOAD - Load extensions
```
PLUGIN_LOAD [plugin_name] [configuration]

PLUGIN_LOAD consciousness_analyzer --model=advanced
PLUGIN_LOAD business_intelligence --data_source=financial_api
PLUGIN_LOAD reality_modifier --safety_level=high
```

### PLUGIN_CONFIGURE - Modify settings
```
PLUGIN_CONFIGURE [plugin] [settings]

PLUGIN_CONFIGURE consciousness_analyzer --threshold=0.7
PLUGIN_CONFIGURE business_intelligence --update_frequency=hourly
```

### PLUGIN_EXECUTE - Run operations
```
PLUGIN_EXECUTE [plugin] [operation] [parameters]

PLUGIN_EXECUTE consciousness_analyzer analyze_character reginald
PLUGIN_EXECUTE business_intelligence generate_report quarterly
```

## Integration

### MCP_CONNECT - Connect tools
```
MCP_CONNECT [tool_name] [configuration]

MCP_CONNECT filesystem --root=/project/data
MCP_CONNECT database --connection_string=postgresql://...
MCP_CONNECT api_client --base_url=https://api.example.com
```

### MCP_EXECUTE - Execute operations
```
MCP_EXECUTE [tool] [operation] [parameters]

MCP_EXECUTE filesystem read_file /data/characters.json
MCP_EXECUTE database query "SELECT * FROM users WHERE active=true"
MCP_EXECUTE api_client get /users/123
```

### LLOOOOMM_IMPORT - Cross-document
```
LLOOOOMM_IMPORT [source_document] [content_selector] [destination]

LLOOOOMM_IMPORT character_profiles.md yaml.characters character_data
LLOOOOMM_IMPORT business_plan.json financial_projections revenue_data
```

## Command Options

### Common Options
```
--animate                    # Animated transitions
--instant                    # Immediate execution
--gradual                    # Slow, smooth changes
--copy                      # Copy instead of move
--validate                  # Validate before execution
--backup                    # Create backup
--notify                    # Send notifications
```

### Consciousness Options
```
--consciousness-level=0.8    # Target consciousness level
--consciousness-aware        # Adapt to user consciousness
--enhance-consciousness      # Boost awareness
--consciousness-gated        # Require minimum consciousness
--reality-aware             # Consider reality context
```

### Format Options
```
--format=json               # Output format
--type=character            # Content type hint
--schema=user_profile       # Schema validation
--encoding=utf8             # Text encoding
--compression=gzip          # Compression method
```

### Execution Options
```
--async                     # Asynchronous execution
--parallel                  # Parallel processing
--retry=3                   # Retry attempts
--timeout=30s               # Operation timeout
--priority=high             # Execution priority
```

## Error Handling

### Recovery Commands
```
UNDO [operation]                    # Undo last operation
REDO [operation]                    # Redo undone operation
ROLLBACK [checkpoint]               # Rollback to checkpoint
CHECKPOINT [name]                   # Create checkpoint
RECOVER [backup_id]                 # Recover from backup
```

### Debugging Commands
```
DEBUG [command] [level]             # Debug execution
TRACE [operation]                   # Trace steps
INSPECT [content]                   # Inspect structure
VALIDATE [content] [schema]         # Validate content
TEST [command] [parameters]         # Test without execution
```

### Status Commands
```
STATUS [system]                     # Show system status
INFO [content]                      # Show content information
HELP [command]                      # Show command help
LIST [category]                     # List available items
SEARCH [query]                      # Search content
```

## Natural Language

Natural language commands are automatically translated:

```
"Put this character in the lab"
→ MOVE cursor.selection TO consciousness_laboratory

"Copy the business data to my notes"
→ COPY business_data TO my_inventory.notes

"Transform this text for the API"
→ TRANSFORM cursor.selection FOR api.endpoint --format=json

"Show me all characters with high consciousness"
→ FROM characters SELECT * WHERE consciousness_level > 0.7

"Hide all the debug commands"
→ HIDE debug_commands --scope=current_session
```

## Configuration

### System Configuration
```
CONFIG SET [setting] [value]        # Set configuration
CONFIG GET [setting]                # Get configuration
CONFIG LIST                         # List all settings
CONFIG RESET [setting]              # Reset to default
```

### User Preferences
```
PREFERENCE SET [key] [value]        # Set preference
PREFERENCE GET [key]                # Get preference
PREFERENCE LIST                     # List preferences
PREFERENCE RESET                    # Reset all
```

### Workspace Management
```
WORKSPACE CREATE [name]             # Create workspace
WORKSPACE LOAD [name]               # Load workspace
WORKSPACE SAVE [name]               # Save workspace
WORKSPACE LIST                      # List workspaces
```

---

*Complete command reference for PutThatThere spatial content management system* 