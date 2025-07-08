# HyperTIES Storyboard Command Reference

## Overview

Storyboard files (`.st0`) contain text and formatting commands that define HyperTIES articles. Commands begin with a period (`.`) and control layout, navigation, and interactivity.

## Configuration Commands

### Font Commands

#### `.font name size`
Set the current font for text display.
```
.font Times-Roman 12
```

#### `.button-font name size`
Set the font used for hyperlink buttons.
```
.button-font Helvetica-Bold 10
```

#### `.default-font name size`
Set the default font for body text.
```
.default-font Times-Roman 14
```

#### `.definition-font name size`
Set the font for definition sections.
```
.definition-font Helvetica 12
```

#### `.controls-font name size`
Set the font for control sections.
```
.controls-font Helvetica 10
```

### Spacing Commands

#### `.line-space points`
Set spacing between lines in points.
```
.line-space 4
```

#### `.para-indent spaces`
Set paragraph indentation in spaces.
```
.para-indent 4
```

### Margin Commands

#### `.top-margin points`
Set top page margin.
```
.top-margin 10
```

#### `.bottom-margin points`
Set bottom page margin.
```
.bottom-margin 10
```

#### `.left-margin points`
Set left page margin.
```
.left-margin 10
```

#### `.right-margin points`
Set right page margin.
```
.right-margin 10
```

#### `.save-margins`
Save current margin settings to stack.

#### `.restore-margins`
Restore margins from stack.

## Formatting Commands

### Text Layout

#### `.nl`
Insert a line break.

#### `.sp`
Insert a space.

#### `.spaces count`
Insert multiple spaces.
```
.spaces 5
```

#### `.lines count`
Insert multiple blank lines.
```
.lines 2
```

#### `.para`
Start a new paragraph (two line breaks + indent).

#### `.indent`
Insert paragraph indentation.

### Text Alignment

#### `.line text`
Display a line of text (with newline).
```
.line This is a line of text
```

#### `.left text`
Left-align text (default).
```
.left This text is left-aligned
```

#### `.center text`
Center text on the line.
```
.center This text is centered
```

#### `.right text`
Right-align text.
```
.right This text is right-aligned
```

#### `.quote word`
Display a single word.
```
.quote Hello
```

#### `.quote-line text`
Display a quoted line.
```
.quote-line This is quoted text
```

### Page Control

#### `.home`
Move to top of page.

#### `.page`
Start a new page.

#### `.overstrike`
Position for overstriking previous text.

## Navigation Commands

### Links and Buttons

#### `.button text`
Create a button linking to an article.
```
.button Introduction
```

#### `.buttonline text`
Create a button with automatic newline.
```
.buttonline Next Topic
```

#### `.~ text~`
Inline button syntax.
```
Click .~ here~ to continue
```

#### `.ref word`
Create a reference link.
```
.ref glossary
```

#### `.link word`
Create a hyperlink.
```
.link contents
```

### Targets

#### `.target name ref`
Place an interactive target.
```
.target next-button
next-page
```

#### `.page-target name ref`
Define page background target.
```
.page-target background
main-menu
```

#### `.definition-target name ref`
Define definition section background.
```
.definition-target def-background
definitions
```

#### `.controls-target name ref`
Define controls section background.
```
.controls-target control-panel
controls
```

#### `.full-entry-target name ref`
Define full entry button target.
```
.full-entry-target full-entry-button
full-article
```

#### `.default-button-name name`
Set default button appearance.
```
.default-button-name standard-button
```

## Content Commands

### Pictures

#### `.picture name`
Insert a picture by name.
```
.picture telescope-diagram
```

### Graphics

#### `.rect width height`
Reserve rectangular space.
```
.rect 200 150
```

#### `.moveto x y`
Move cursor to absolute position.
```
.moveto 100 200
```

#### `.rmoveto x y`
Move cursor relative to current position.
```
.rmoveto 50 -20
```

### Tabs

#### `.def-tab tab# position`
Define a tab stop.
```
.def-tab 1 100
```

#### `.tab tab#`
Move to tab stop.
```
.tab 1
```

## Structure Commands

### Article Sections

#### `.title`
Begin title section.
```
.title
The Space Telescope
```

#### `.synonyms` or `.synonym`
Begin synonyms section.
```
.synonyms
Hubble Space Telescope
HST
```

#### `.definition` or `.description`
Begin definition section.
```
.definition
A space-based optical telescope...
```

#### `.contents` or `.content`
Begin main content section.
```
.contents
The telescope has five instruments...
```

#### `.controls`
Begin controls section.
```
.controls
Navigation controls appear here
```

#### `.notes`
Begin notes section (often hidden).
```
.notes
Author notes and metadata
```

## Control Commands

### Processing

#### `.init`
Initialize the formatter.

#### `.flush-cache` or `.free-stamps`
Clear cached stamps and pictures.

#### `.zap`
Clear all pages.

#### `.bye`
Exit the system.

#### `.end`
End current page/section.

### Compilation

#### `.do name`
Execute a storyboard by name.
```
.do introduction
```

#### `.define name`
Define and execute definition section.
```
.define telescope
```

#### `.articulate name`
Navigate to article and display.
```
.articulate main-menu
```

#### `.energize`
Activate controls section.

#### `.index name`
Add to navigation index.
```
.index chapter-1
```

#### `.return`
Return to previous article.

#### `.go name`
Go to specific article.
```
.go contents
```

### Pile Management

#### `.pile-pos x y`
Set pile window position.
```
.pile-pos 100 100
```

#### `.pile-size width height`
Set pile window size.
```
.pile-size 640 480
```

#### `.new-pile class`
Create new pile of given class.
```
.new-pile TIESWindow
```

#### `.pile id`
Switch to pile by ID.
```
.pile 0
```

#### `.name-pile name`
Name current pile.
```
.name-pile main-window
```

#### `.use-linked-pile name`
Use a named linked pile.
```
.use-linked-pile definitions
```

#### `.use-parent-pile`
Switch to parent pile.

#### `.setup-contents-pile`
Initialize contents pile.

#### `.setup-definition-pile`
Initialize definition pile.

#### `.setup-controls-pile`
Initialize controls pile.

### Variables

#### `.local name`
Define local variable.
```
.local current-page
```

#### `.global name`
Define global variable.
```
.global user-name
```

## Special Commands

### Comments

#### `.rem text`
Add a comment (ignored).
```
.rem This is a comment
```

### Mode Control

#### `.forth`
Switch to Forth interpretation mode.

#### `.process`
Switch to process mode.

#### `.f`
Flush PostScript output.

## Compilation Commands

These commands are used when compiling storyboards:

#### `.compile-article name`
Compile article to Forth.

#### `.compile-definition name`
Compile definition to Forth.

#### `.compile-controls name`
Compile controls to Forth.

## Example Storyboard

```
.title
Introduction to HyperTIES

.synonyms
HyperTIES Introduction
Getting Started

.definition
HyperTIES is a hypertext system for creating and browsing
interconnected documents with text, pictures, and interactive elements.

.contents
.para
Welcome to HyperTIES! This system lets you:

.nl
.~ Browse~ through connected articles
.nl
.~ View~ pictures and diagrams
.nl
.~ Interact~ with on-screen elements

.para
.picture hyperties-logo

.para
To begin, select a topic from the menu below:

.nl
.button Quick Start
.nl
.button User Guide
.nl
.button Examples

.controls
.button Return to Main Menu
```

This command set provided a complete authoring system for creating rich, interactive hypertext documents years before the Web. 