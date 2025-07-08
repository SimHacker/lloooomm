# Directory Scanner Worm Examples

## Basic Directory Scanning

```worm directory-scanner (crawling, filesystem-mode)
# Scan directories for files matching patterns
scan_directory("/project", {
  pattern: "*.js",
  recursive: true
})

while has_files():
  file = next_file()
  eat(file)
  content = peek()
  
  if contains("TODO") or contains("FIXME"):
    poop(f"{file.path}: {extract_todos(content)}", "todos-{n}.txt")
  
  next()
```

## Natural Language Pattern Matching

```worm nl-scanner (intelligent, nl-mode)
# Use natural language to find files
scan_directory("/home/user/documents", {
  nl_filter: "files I worked on last week but forgot to commit",
  pattern: "*.*"
})

while has_matches():
  file = next_match()
  eat(file)
  
  # Check git status
  if not in_git(file):
    poop(file.path, "forgotten-files-{n}.txt")
    suggest_commit_message(file)
```

## SQL-Style Directory Queries

```worm sql-scanner (querying, database-mode)
# Treat filesystem as a database
results = scan_directory("/", {
  sql: """
    SELECT * FROM files
    WHERE size > 100MB
    AND modified < '2023-01-01'
    AND name LIKE '%backup%'
    AND owner != 'root'
    ORDER BY size DESC
    LIMIT 100
  """
})

for file in results:
  eat(file)
  analyze_for_deletion = check_if_needed(file)
  if analyze_for_deletion.can_delete:
    poop(file.path, "candidates-for-deletion-{n}.txt")
```

## Advanced Pattern Matching with Empathic SQL

```worm empathic-scanner (understanding, empathy-mode)
# Find files based on emotional content
scan_directory("/journal", {
  empathic_sql: """
    SELECT * FROM documents
    WHERE emotional_tone = 'anxious'
    AND mentions_topic('deadline')
    AND urgency_level > 8
    AND author_stress_level = 'coffee-overdose'
  """
})

while has_results():
  doc = next_result()
  eat(doc)
  
  # Analyze and provide support
  stress_level = analyze_stress(peek())
  if stress_level.critical:
    generate_calming_response()
    poop(doc.path, "high-stress-documents-{n}.txt")
    schedule_break_reminder()
```

## Multi-Pattern Directory Pipeline

```worm pipeline-scanner (orchestrating, pipeline-mode)
# Complex scanning with multiple filters
scan_directory("/codebase", {
  patterns: ["*.py", "*.js", "*.go"],
  exclude: ["node_modules", ".git", "vendor"],
  nl_filter: "files that look like they have security issues",
  sql_filter: "WHERE line_count > 500 AND complexity > 10"
}) |
filter(has_no_tests) |
map(extract_functions) |
filter(looks_suspicious) |
tee("security-audit-{n}.json") |
alert_security_team()
```

## Parallel Directory Scanning

```worm parallel-scanner (distributed, swarm-mode)
# Spawn multiple worms for large directories
directories = ["/data/2021", "/data/2022", "/data/2023", "/data/2024"]

# Create a worm swarm
swarm = spawn_worms(4, "worker-scanner")

# Distribute work
for i, dir in enumerate(directories):
  assign_to_worm(swarm[i], {
    directory: dir,
    pattern: "*.log",
    nl_filter: "files containing errors or exceptions",
    output: f"errors-{dir.year}-{{n}}.txt"
  })

# Wait for all worms to complete
wait_for_swarm(swarm)
consolidate_results("all-errors-{n}.txt")
```

## Intelligent File Classification

```worm classifier-scanner (categorizing, ml-mode)
# Use ML to classify files
scan_directory("/downloads", {
  pattern: "*",
  nl_filter: "files I downloaded but never organized"
})

while has_files():
  file = next_file()
  eat(file)
  
  # Classify using multiple criteria
  classification = classify({
    content: peek(),
    filename: file.name,
    metadata: file.metadata,
    context: get_surrounding_files()
  })
  
  # Organize into folders
  suggested_location = suggest_folder(classification)
  poop({
    file: file.path,
    classification: classification,
    suggested_move: suggested_location
  }, "organization-plan-{n}.json")
```

## Time-Based Scanning

```worm temporal-scanner (time-traveling, history-mode)
# Find files based on temporal patterns
scan_directory("/projects", {
  temporal_sql: """
    SELECT * FROM files
    WHERE touched_during('crunch time')
    AND edited_between('11pm', '4am')
    AND commits_contain('fix', 'bug', 'please work')
    AND coffee_consumption > normal * 3
  """
})

for file in results:
  eat(file)
  crunch_analysis = analyze_crunch_pattern(file)
  poop(crunch_analysis, "crunch-time-files-{n}.txt")
  
  if crunch_analysis.needs_refactor:
    schedule_technical_debt_review(file)
```

## Recursive Pattern Matching

```worm recursive-scanner (deep-diving, fractal-mode)
# Scan with recursive patterns
scan_directory("/", {
  recursive_pattern: {
    find: "Makefile",
    then_scan: {
      pattern: "*.c",
      nl_filter: "C files that look complicated",
      action: scan_for_dependencies
    }
  }
})

# Build dependency graph
while has_results():
  makefile = next_result()
  eat(makefile)
  
  dependencies = extract_dependencies(peek())
  for dep in dependencies:
    sub_scan = scan_relative(dep.path, {
      pattern: dep.pattern,
      nl_filter: "files that might break if I change this"
    })
    
    poop(sub_scan.results, f"impact-analysis-{n}.txt")
```

## The Ultimate Scanner

```worm ultimate-scanner (omniscient, god-mode)
# The scanner to end all scanners
scan_directory("/", {
  pattern: "*",
  nl_filter: """
    Files that:
    - I'll need next week but will forget about
    - Contain TODO items from 2019
    - Have that one function I wrote that one time
    - My future self will thank me for finding
    - Are named terribly but contain gold
  """,
  sql_filter: """
    SELECT * FROM all_files
    WHERE importance = 'critical'
    AND i_remember_it_exists = false
    AND will_cause_production_issue = true
    AND location = 'somewhere in this mess'
  """,
  empathic_filter: "files that feel lonely and neglected"
})

# Process everything
while universe_exists():
  file = next_file()
  eat(file)
  
  revelation = achieve_enlightenment(peek())
  poop(revelation, "meaning-of-life-{n}.txt")
  
  if revelation.is_ultimate_answer:
    print("42")
    break
```

*"Worm Pipelines: Better Than Boring, We're WORMS!"* 🪱📁 