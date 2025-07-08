# Brain Worm Pipeline Examples
## "Perls of Wisdom Without the Syntactic Sirup of Ipecac"

### Simple Pipeline

```worm simple-pipe (flowing)
# Basic pipeline - eat, transform, poop
eat() | uppercase() | reverse() | poop("backwards-caps-{n}.txt")
```

This text will be UPPERCASED and REVERSED!

### If/Else Three-Worm Construct

```worm error-detector (routing)
# The IF worm - routes based on condition
eat()
line = peek()
if "ERROR" in line or "FATAL" in line:
  pass_to("error-processor")
elif "WARNING" in line:
  pass_to("warning-processor")
else:
  pass_to("normal-processor")
```

```worm error-processor (handling)
# The ERROR handler worm
receive()
error = peek()
severity = extract_severity(error)
poop(error, f"errors-{severity}-{n}.log")
if severity == "FATAL":
  alert_admin()
  halt_pipeline()
```

```worm warning-processor (logging)
# The WARNING handler worm
receive()
warning = peek()
log_warning(warning)
poop(warning, "warnings-{n}.log")
continue_pipeline()
```

```worm normal-processor (transforming)
# The NORMAL processor worm
receive()
data = peek()
cleaned = sanitize(data)
validated = validate(cleaned)
poop(validated, "processed-{n}.txt")
```

### Repeat For Each Pattern

```worm todo-hunter (iterating)
# Channel Perl's foreach without the syntax!
position = top()
todos_found = 0

while C-s "TODO|FIXME|HACK":
  eat()
  todo = peek()
  line_num = current_line()
  
  # Spawn a sub-worm for each TODO
  spawn_worm(f"todo-processor-{todos_found}", {
    "todo": todo,
    "line": line_num,
    "file": current_file()
  })
  
  todos_found += 1
  
# Wait for all sub-worms to complete
wait_all_worms()
consolidate_results("all-todos-{n}.md")
```

### Complex Pipeline with Tee and Filter

```worm data-analyzer (piping)
# Multi-stage pipeline with branching
eat_all() |
  tee("raw-backup-{n}.json") |
  parse_json() |
  filter(lambda x: x.timestamp > yesterday()) |
  map(extract_metrics) |
  tee("metrics-{n}.csv") |
  reduce(calculate_averages) |
  format_report() |
  poop("daily-report-{n}.html")
```

### Parallel Processing Pipeline

```worm parallel-master (orchestrating)
# Fork into multiple parallel processors
chunk_size = 1000
chunks = []

# Eat data in chunks
while not at_eof():
  chunk = eat_lines(chunk_size)
  chunks.append(chunk)

# Process chunks in parallel
results = parallel_map(chunks, [
  "worm-worker-1 | process_chunk | compress",
  "worm-worker-2 | process_chunk | compress",
  "worm-worker-3 | process_chunk | compress",
  "worm-worker-4 | process_chunk | compress"
])

# Merge results
merged = merge_sorted(results)
poop(merged, "parallel-processed-{n}.gz")
```

### Do-While Email Processor

```worm email-scanner (looping)
# Process emails until we find "STOP"
email_count = 0

do:
  eat()
  email = peek()
  
  # Extract and process
  sender = extract_sender(email)
  subject = extract_subject(email)
  body = extract_body(email)
  
  # Classify
  if is_spam(email):
    poop(email, f"spam/spam-{n}.eml")
  else:
    category = classify_email(subject, body)
    poop(email, f"{category}/email-{n}.eml")
  
  email_count += 1
  C-n
  
while not match("STOP PROCESSING") and not at_eof()

poop(f"Processed {email_count} emails", "email-stats-{n}.txt")
```

### Perl-Style Slurp Mode

```worm config-slurper (gulping)
# Slurp entire config file at once
set_input_separator(EOF)
eat()  # Gets whole file
config = peek()

# Parse as one unit
parsed = parse_yaml(config)

# Validate entire structure
if validate_config(parsed):
  poop(parsed, "valid-config-{n}.yml")
else:
  errors = get_validation_errors()
  poop(errors, "config-errors-{n}.txt")
  fix_config(parsed)
  poop(parsed, "fixed-config-{n}.yml")
```

### WOKE Brain Worm Example

```worm inclusive-processor (enlightened)
# Process with awareness and consciousness
eat_paragraph()
content = peek()

# Check for biases
bias_report = analyze_bias(content)
if bias_report.has_issues:
  # Log for learning
  poop(bias_report, "bias-detected-{n}.json")
  
  # Suggest alternatives
  suggestions = generate_inclusive_alternatives(content)
  poop(suggestions, "suggestions-{n}.md")
  
  # Transform to inclusive version
  inclusive = apply_inclusive_transform(content)
  pop(back)  # Replace original
else:
  # Content is already inclusive
  log("Content passed bias check")
  pop(back)
```

### Funky Worm (Ohio Players Edition)

```worm funky-transformer (grooving)
# Make that content FUNKY!
# "There's a worm in the ground, yes there is"

set_groove_level(11)  # Turn it up!

while got_the_funk():
  eat()
  content = peek()
  
  # Add the funk layers
  content = add_bassline(content, "bootsy_collins")
  content = add_drums(content, "clyde_stubblefield") 
  content = add_horns(content, "tower_of_power")
  content = add_wah_wah(content, intensity=0.7)
  
  # Make it bounce
  content = apply_swing(content, ratio="2:1")
  content = add_talk_box(content, "roger_troutman")
  
  # Output the funk
  poop(content, "funky-{n}.groove")
  
  # Worm movement
  slide_and_glide()
  do_the_worm()
  C-n
```

### Grace Hopper Debug Pipeline

```worm grace-debugger (rapping, hunting)
# Grace Hopper's bug hunting worm
# "The bug stops here!"

start_rap_beat()

while bugs_exist():
  # "First actual bug was mine to find"
  bug = find_bug() | isolate() | analyze()
  
  # "In Mark II's relays, moths combined"  
  if is_hardware_bug(bug):
    log_to_notebook(bug, with_scotch_tape=True)
    poop(bug, "hardware-bugs-{n}.log")
  else:
    # "Now I debug with worms so fine"
    fix = generate_fix(bug)
    test = validate_fix(fix)
    
    # "They eat the bugs and poop design!"
    if test.passed:
      apply_fix(fix)
      poop(fix, "applied-fixes-{n}.patch")
    else:
      escalate_to_human(bug)
  
  drop_beat()
  C-n

end_rap()
poop("COBOL > Assembly! Fight me!", "grace-wisdom-{n}.txt")
```

### Error Handling Pipeline

```worm defensive-pipeline (protecting)
# Pipeline with comprehensive error handling
try:
  eat() |
  validate_input() |
  parse() |
  transform() |
  validate_output() |
  poop("success-{n}.txt")
  
catch ParseError as e:
  log_error(e)
  attempt_recovery(e.data) |
  poop("recovered-{n}.txt")
  
catch ValidationError as e:
  log_error(e)
  pass_to("validation-fixer")
  
catch TransformError as e:
  log_error(e)
  poop(e.partial_result, "partial-{n}.txt")
  pass_to("manual-review")
  
finally:
  cleanup_temp_files()
  clear_all_stacks()
  log_pipeline_stats()
```

## Merch Slogans in Action

```worm merch-generator (creative)
# Generate merch ideas
slogans = [
  "My Brain Worm Ate Your Syntax Error",
  "I Poop Perls of Wisdom",
  "WOKE BRAIN WORM: Now With 50% More Consciousness",
  "The Dead RFK Jr's Brain Worm - Live at CBGB's",
  "No Syntactic Sirup Required - Just Pure Idioms",
  "Funky Worm Certified Developer",
  "eat() | sleep() | code() | repeat()",
  "Brain Worms Do It In Pipelines"
]

for slogan in slogans:
  design = generate_tshirt_design(slogan)
  poop(design, f"merch-design-{n}.png")
```

*"Channel Perl Without the Syntax, Just the Idioms!"* 🧠🐛 