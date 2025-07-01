# Bookshelf Reconciliation Plan

## Summary of Issues Found

### Critical Issues:
1. **14 books completely missing** (need to be restored)
2. **21 extra books** that don't belong (need to be removed or archived)
3. **115 books in wrong order** (need to be reordered)
4. **3 books with changed labels** (need to be restored)

### Most Affected Shelves:
- **r2-c3**: Lost ALL 11 books about mathematics and biology!
- **r2-c1**: Has 3 extra books and all 27 books are out of order
- **r2-c2**: Has 1 extra book and all 35 books are out of order
- **r6-c1**: Has 10 extra architecture books that don't belong
- **r6-c3**: Has 4 extra books, 1 missing book, wrong order and label changes

## Detailed Fix Plan

### Phase 1: Create Overflow Archive
Create `bookshelf-overflow.yml` to archive the 21 extra books that don't belong on any shelf.

### Phase 2: Restore Missing Books

#### r1-c4 (2 missing Smalltalk books):
- Restore "Smalltalk-80: The Interactive Programming Environment" by Adele Goldberg at position 9
- Restore "A Little Smalltalk" by Timothy Budd at position 10

#### r2-c3 (11 missing math/biology books - ENTIRE SHELF):
- Restore all 11 books in their original order:
  1. "Mathematics: The Loss of Certainty" by Morris Kline
  2. "What is Mathematics, Really?" by Reuben Hersh  
  3. "Numbers and Functions: Steps into Analysis" by R. P. Burn
  4. "Visual Complex Analysis" by Tristan Needham
  5. "The History of the Mismeasurement of Man" by Stephen Jay Gould
  6. "The Eighth Day of Creation" by Horace Freeland Judson
  7. "The Double Helix" by James D. Watson
  8. "The Selfish Gene" by Richard Dawkins
  9. "The Blind Watchmaker" by Richard Dawkins
  10. "Wonderful Life" by Stephen Jay Gould
  11. "The Panda's Thumb" by Stephen Jay Gould

#### r6-c3 (1 missing book):
- Restore "Logic Synthesis" by Srinivas Devadas et al. at position 4

### Phase 3: Remove Extra Books

#### r2-c1 (3 extra books):
- Remove "Vehicles: Experiments in Synthetic Psychology" (position 1)
- Remove "Thinking, Fast and Slow" (position 5)
- Remove "Gödel, Escher, Bach" (position 6)

#### r2-c2 (1 extra book):
- Remove "The Inmates Are Running the Asylum" (position 2)

#### r2-c3 (1 extra book):
- Remove "LISP in Small Pieces" (position 2) - Note: This belongs in r2-c4!

#### r2-c4 (2 extra books):
- Remove "The Image: A Guide to Pseudo-events in America" (position 0)
- Remove "The Semiotic Engineering of Human-Computer Interaction" (position 1)

#### r6-c1 (10 extra architecture books):
- Remove all books at positions 1, 3-6, 8-12

#### r6-c3 (4 extra books):
- Remove positions 0, 2, 3, 5

### Phase 4: Fix Book Order
Restore original order for all affected shelves:
- r1-c2: 22 books need reordering
- r1-c3: 5 books need reordering  
- r1-c4: 5 books need reordering
- r2-c1: All 27 books need reordering
- r2-c2: All 35 books need reordering
- r2-c4: All 10 books need reordering
- r6-c3: 11 books need reordering

### Phase 5: Fix Labels
- r1-c1: Change "The Illusion of Life" label from "Animation" back to ""
- r6-c3: Change "Digital Integrated Circuits" from "Hardware" back to "Circuit Design"
- r6-c3: Change "Introduction to VLSI Systems" from "Hardware" back to "Circuit Design"

### Phase 6: Preserve Enrichments
While making all the above fixes, preserve the "jazz" sections and other enrichments that were added to books that belong.

## Implementation Order
1. Create overflow archive file
2. Fix r2-c3 (completely broken - restore all 11 books)
3. Fix r6-c1 (remove 10 extra books)
4. Fix r2-c1 (remove 3 extra, reorder 27)
5. Fix r2-c2 (remove 1 extra, reorder 35)
6. Fix r2-c4 (remove 2 extra, reorder 10)
7. Fix r6-c3 (complex - remove 4, restore 1, reorder, fix labels)
8. Fix r1-c4 (restore 2 missing books, reorder)
9. Fix r1-c2 (reorder 22 books)
10. Fix r1-c3 (reorder 5 books)
11. Fix r1-c1 (fix label only) 