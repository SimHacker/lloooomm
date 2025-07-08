# HyperTIES Source Code Reference

## Overview

HyperTIES was implemented as a multi-language system leveraging the strengths of each language:
- **C** for performance-critical formatting and layout
- **PostScript** for display and graphics
- **Forth** for scripting and control flow
- **MockLisp** for authoring tools

## Core Components

### 1. C Formatter (fmt.c)

The heart of HyperTIES text layout engine.

#### Key Data Structures

```c
struct font_metrics {
    char *name;
    int size;
    int ascent;
    int descent;
    int height;
    int *widths;
    struct font_metrics *next;
};
```

#### Key Functions

- `find_metrics()` - Font lookup with caching
- `string_width()` - Calculate text width
- `start_page()/end_page()` - Page composition
- `show_string()` - Text rendering
- `stamp_target()` - Place interactive elements
- `define_picture()` - Load images
- `paint_picture()` - Display images

### 2. Forth Interpreter (fmt.f)

Processes storyboard files and controls navigation.

#### Key Words

```forth
: .title      \ Set article title
: .button     \ Create hyperlink button  
: .~          \ Inline button syntax
: .picture    \ Insert picture
: .target     \ Place interactive target
: articulate  \ Navigate to article
: .contents   \ Begin content section
: .definition \ Begin definition section
```

#### Navigation Stack

```forth
256 stack: saved-fonts
32 constant /piles
128 constant /path
create piles  /piles /n* allot
```

### 3. PostScript Display (fmt.ps)

Server-side rendering and interaction.

#### Key Functions

```postscript
/FF { % Find Font - name size => -
    /FontSize exch store
    /FontName exch store
    {FontName findfont} errored {
        % Handle missing font
    } {
        FontSize scalefont
        /Font exch store
    } ifelse
} def

/PT { % Put Target - x y width height ref id => -
    StampDict exch get
    /compile exch send
} def
```

### 4. C-PostScript Bridge (fmt.cps)

Defines communication protocol between C and NeWS.

#### Protocol Tags

```c
#define GET_METRICS_TAG 1
#define NO_FONT_TAG 2
#define FOUND_FONT_TAG 3
#define GET_RECT_TAG 4
#define PAGE_SIZE_TAG 5
#define MEASURE_STAMP_TAG 6
#define USE_LINKED_PILE_TAG 7
#define USE_PARENT_PILE_TAG 8
```

## File Formats

### Storyboard Files (.st0)

Text files with embedded formatting commands:

```
.title
The Space Telescope in Orbit

.synonyms
Hubble Space Telescope
HST

.definition
The Space Telescope is a large optical telescope in orbit around Earth.

.contents
The telescope has five scientific instruments:
.~ WFPC~ - Wide Field/Planetary Camera
.~ FOC~ - Faint Object Camera
.picture telescope-diagram
```

### Master Index Format

Tab-delimited registry of all content:

```
----- ARTICLES -----
"The Space Telescope in Orbit"          ./newdb/spacetel/spacetel.st0
"Hubble Space Telescope"
"HST"

----- PICTURES -----
"telescope-diagram"                     ./newdb/spacetel/main.image.pn0

----- TARGETS -----
"default-button"                        ./global/default-button.tn0
```

## Build System

### Compilation Flow

1. `fc database` - Compile storyboards to Forth
2. `fl database` - Load compiled database
3. `br database` - Browse with NeWS

### Shell Scripts

- `b` - Run compiled database
- `br` - Browse database with NeWS
- `f` - Run formatter on database
- `fc` - Compile storyboards to Forth
- `fl` - Load compiled database
- `ff` - Browse with formatter

## Emacs Integration (ht.ml)

MockLisp mode for authoring:

```lisp
(defun (articulate &ea-name &ea-file
    (setq &ea-name (arg 1 ": articulate (name) "))
    (if (= (setq &ea-file (ht-lookup &ea-name)) ".unknown")
        (message (concat &ea-file " <" (ht-canonicalize &ea-name) ">"))
        (progn (message "Found " &ea-name " in " &ea-file)
               (find-file &ea-file)
               (narrow-storyboard)
        )
    )
))
```

## Modern Converter (convert.py)

Python tool to preserve HyperTIES content:

```python
def CompileStoryboard(storyboardName, txt, out, masterIndex):
    interp = {
        'buf': txt,
        'index': 0,
        'definitionOut': definitionOut,
        'contentOut': contentOut,
        'debugOut': debugOut,
        'out': debugOut,
        'masterIndex': masterIndex,
        'mode': 'word',
        'consumer': 'none',
    }
    Interpret(interp, out)
```

## Key Innovations

### Font Metrics Caching

```c
struct font_metrics *find_metrics(name, size)
     char *name;
     int size;
{
    register struct font_metrics *cache = cached_metrics;
    
    while (cache != NULL) {
        if (cache->size == size)
            if (strcmp(cache->name, name) == 0)
                return(cache);
        cache = cache->next;
    }
    return(get_metrics(name, size));
}
```

### Stamp-Pad Architecture

Pictures and targets are "stamps" that can be placed on pages:

```c
define_picture(ent)
     ENTRY *ent;
{
    if (InstanceOfEntry(ent) == NULL) {
        new = CreateInstanceHeader(ent, instance_id_count++, 0, 0);
        send_entry_pos(ent);
        class = send_entry_body(ent);
        do_def_picture(class, KeyOfEntry(ent), InstanceId(new));
        do_measure_stamp(InstanceId(new),
                         &InstanceWidth(new), &InstanceHeight(new));
    }
}
```

### Event-Driven Targets

Interactive elements with PostScript event handlers:

```postscript
/activate-page { % DL => -
    Page /Can Can put
    Page /DL 3 -1 roll put
    [ Page /Targets get {pop TargetDict exch get} forall ] iteminterests
    [ exch aload pop
        /Damaged
          {CurrentEvent /Canvas get /damage-paint-canvas Win send}
          null Can eventmgrinterest
    ] forkeventmgr
    Page /ItemMgr 3 -1 roll put
} def
```

## Memory Management

### Instance Headers

```c
typedef struct instance_header {
    int instance_id;
    int width, height;
    struct entree *entree;
    struct instance_header *next;
} INSTANCE_HEADER;
```

### Entry Management

```c
typedef struct entree {
    ENTRY_TYPE type;
    char *identifier;
    char *file_name;
    long offset;
    long length;
    struct instance_header *instance;
} ENTRY;
```

## Error Handling

Graceful degradation throughout:

```forth
: find-font ( size name --- font / 0 )
  _find_metrics ret ?dup if
    swap drop swap drop
  else
    ." Can't find font " cscount type space . cr
    0
  then
;
```

## Network Transparency

Through NeWS PostScript:

```postscript
/send-to-hookfile {
    hookfile exch writestring hookfile flushfile
} def

systemdict /sendtoemacs known {
    /ties-key-prefix ($[T) def
    ties-key-prefix 0 27 put
    
    /send-to-ties {
        ties-key-prefix exch append sendtoemacs
    } def
} if
```

This architecture enabled HyperTIES to be the earliest hypermedia browser to support many features that wouldn't become common for years, like embedded interactive PostScript components like Java Applets and JavaScript "AJAX" web apps. It's no coincidence James Gosling wrote Emacs that was used to implement the HyperTIES authoring tool, and NeWS that was used to implement the HyperTIES user interface, while Mitch Bradley implemented the Forth system HyperTIES used, and only years later did James Gosling implement Java "applets" for web browsers.