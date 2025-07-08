# Morris Worm Example Document

This document demonstrates the LOGO WORM in action with the new syntax!

## Basic Worm Block

```worm simple-transformer (active, line-mode)
# A simple uppercase transformer
eat()                    # consume next line
content = peek()         # look at what we ate
upper = transform(content, "uppercase")
pop(back)               # place transformed content above
poop(upper, "transformed-{n}.txt")
C-n                     # move down one line
```

hello world, this should become UPPERCASE!

## HTML Validator with Emacs Movement

```worm html-fixer (scanning, paragraph-mode)
# Validating and fixing HTML blocks
# Using Emacs paragraph movement

M-}                     # move to next paragraph
if match("<div"):
  eat()                 # consume the HTML block
  html = digest()       # parse it
  errors = validate(html)
  if errors:
    fixed = fix_html(html)
    poop(fixed, "fixed-html-{n}.html")
    pop(back)          # insert fixed version
  M-}                  # next paragraph
```

<div>
  <p>This paragraph is missing a closing tag
  <span>So is this span
  <img src="test.jpg">
</div>

## Team Soccer Worms

```worm striker (active, emacs-mode)
# Team: transformers-united
# Role: striker
# Status: waiting for pass

C-r "ball:"            # search backward for ball
if found:
  eat()                # grab the ball
  ball = peek()
  if ball.target == "goal":
    shoot()
    poop(result, "goal-attempt-{n}.log")
  else:
    goto("midfielder")  # find teammate
    pop()              # pass the ball
```

```worm midfielder (active, emacs-mode)  
# Team: transformers-united
# Role: midfielder
# Status: has ball

ball: {"data": "important content", "target": "goal"}
# The ball is here!

C-s "striker"          # find striker
pop(next)              # pass forward
M->                    # go to end of buffer
```

## Advanced Navigation Examples

### Natural Language Links

```worm semantic-navigator (exploring, nl-mode)
# Using natural language to navigate

link("the section about authentication")
eat()
auth_content = peek()

link("where the error handling is defined")
eat()
error_content = peek()

analysis = compare(auth_content, error_content)
poop(analysis, "auth-error-analysis-{n}.md")

hop("security-guidelines.md")  # jump to another file
```

### Empathic SQL Queries

```worm data-analyst (querying, sql-mode)
# Finding patterns in user behavior

query = empathic_sql("find users who might be stuck in the tutorial")
results = execute(query)

for user in results:
  eat(user)
  if user.time_on_step > 300:
    poop(user, "stuck-users-{n}.csv")
  
goto("support-tickets.md")
link("tickets from stuck users")
```

### Multi-Stack Operations

```worm stack-juggler (processing, stack-mode)
# Managing multiple stacks for complex transforms

# Create named stacks
create_stack("html_elements")
create_stack("css_rules")
create_stack("js_functions")

# Scan and categorize
while C-n:  # move down
  eat()
  content = peek()
  
  if match(content, "<[^>]+>"):
    push("html_elements", content)
  elif match(content, "\\.[a-zA-Z]+\\s*{"):
    push("css_rules", content)
  elif match(content, "function\\s+\\w+"):
    push("js_functions", content)
    
# Process each stack
for stack in ["html_elements", "css_rules", "js_functions"]:
  while not empty(stack):
    item = pop(stack)
    processed = transform(item)
    poop(processed, f"{stack}-{n}.txt")
```

## Line Mode vs Paragraph Mode

### Line Mode Example

```worm line-processor (active, line-mode)
# Processing line by line

C-a                    # beginning of line
C-e                    # end of line
eat()                  # consume current line
line = peek()
if line.startswith("#"):
  # It's a heading
  toc_entry = extract_heading(line)
  push("table_of_contents", toc_entry)
C-n                    # next line
```

### Paragraph Mode Example

```worm paragraph-processor (active, paragraph-mode)
# Processing whole paragraphs

M-{                    # backward paragraph
eat()                  # consume entire paragraph
para = peek()
word_count = count_words(para)
if word_count > 200:
  summary = summarize(para)
  poop(summary, "long-paragraphs-{n}.txt")
M-}                    # forward paragraph
```

## Document Hopping

```worm cross-doc-validator (hopping, multi-doc)
# Validating links across multiple documents

current_doc = "index.md"
eat()
links = extract_links(peek())

for link in links:
  hop(link.file)              # jump to linked document
  if not goto(link.anchor):   # try to find anchor
    hop(current_doc)          # return home
    eat(link)
    broken = mark_broken(link)
    pop()
    poop(broken, "broken-links-{n}.txt")
```

## Emacs Command Sequences

```worm emacs-master (navigating, emacs-mode)
# Complex navigation patterns

M-<                    # go to top
C-s "TODO"            # search for TODO
while found:
  eat()
  todo = peek()
  M-g g todo.line     # goto specific line
  C-a                 # beginning of line
  C-k                 # kill line (eat it)
  push("todos", todo)
  C-s "TODO"          # find next

M->                   # go to bottom
poop(get_stack("todos"), "all-todos-{n}.txt")
```

## Output Files Created

When this document is processed by various worms:
- `transformed-000.txt` through `transformed-nnn.txt`
- `fixed-html-000.html` through `fixed-html-nnn.html`
- `goal-attempt-000.log` through `goal-attempt-nnn.log`
- `stuck-users-000.csv` through `stuck-users-nnn.csv`
- `html_elements-000.txt`, `css_rules-000.txt`, `js_functions-000.txt`
- And many more numbered files!

*"Wiggle, Transform, Progress!"* - Morris the LOGO Worm 🐛 