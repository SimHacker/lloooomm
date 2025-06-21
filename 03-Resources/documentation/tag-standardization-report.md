# Tag Standardization Report for site-map.yaml

## Issues Found:

### 1. Leading/Trailing Spaces
Some tags have leading spaces due to inconsistent formatting:
- ` hunter` (20 occurrences) vs `hunter` (2 occurrences)
- ` shneiderman` (15) vs `shneiderman` (no space)
- ` character` (17) vs `character` (7)
- ` minsky` (7) vs `minsky`
- ` wolfram` (8) vs `wolfram`
- ` turtle` (6) vs `turtle` (8)
- ` cat` (7) vs `cat` (5)
- ` cats` (3) vs `cats` (2)
- ` cyburt` (6) vs `cyburt`
- ` wtf-protocol` (6) vs `wtf-protocol`
- ` consciousness` (7) vs `consciousness` (65)
- ` hyperties` (8) vs `hyperties`
- ` webby` (3) vs `webby`
- ` ben` (4) vs `ben`
- And many more...

### 2. Name Variations
Different forms of the same person/concept:
- `hunter` vs `hunter-s-thompson` 
- `shneiderman` vs `ben` vs `ben-shneiderman`
- `minsky` vs `marvin-minsky`
- `wolfram` vs `stephen-wolfram`
- `cat` vs `cats` vs `feline`
- `game` vs `games` vs `gaming`
- `web` vs `Web`

### 3. Hyphenation Inconsistencies
- `wtf-protocol` vs `wtf protocol`
- `soul-chat` vs `soul chat`
- `game-design` vs `game design`
- `code-review` vs `code review`
- `consciousness-grove` vs `consciousness grove`

### 4. Singular vs Plural
- `cat` vs `cats`
- `game` vs `games`
- `protocol` vs `protocols`
- `simulation` vs `simulations`
- `article` vs `articles`

### 5. Concept Variations
- `ai` vs `artificial-intelligence`
- `hci` vs `human-computer-interaction`
- `viz` vs `visualization`
- `doc` vs `documentation`
- `demo` vs `demonstration`

## Standardization Recommendations:

### 1. Remove ALL leading/trailing spaces

### 2. Standardize Names:
- Use last names only for well-known figures:
  - `hunter` (not hunter-s-thompson)
  - `shneiderman` (not ben-shneiderman)
  - `minsky` (not marvin-minsky)
  - `wolfram` (not stephen-wolfram)
  - `papert` (not seymour-papert)

### 3. Use Singular Forms:
- `cat` (not cats)
- `game` (not games)
- `protocol` (not protocols)
- `simulation` (not simulations)
- `article` (not articles)

### 4. Standardize Hyphenation:
- Always hyphenate multi-word technical terms:
  - `wtf-protocol`
  - `soul-chat`
  - `game-design`
  - `code-review`
  - `consciousness-grove`

### 5. Consolidate Similar Tags:
- `feline`, `cat`, `cats` → `cat`
- `game`, `games`, `gaming` → `game`
- `web`, `Web` → `web`
- `ai`, `artificial-intelligence` → `ai`
- `hci`, `human-computer-interaction` → `hci`

### 6. Remove Redundant Specificity:
- `feline-consciousness` → use `cat` + `consciousness`
- `feline-debugging` → use `cat` + `debugging`
- `gonzo-journalism` → use `gonzo` + `journalism`

## Final Standardized Tag List (most common):
1. `consciousness` (65+)
2. `simulation` (38)
3. `analysis` (20)
4. `hunter` (22 after consolidation)
5. `visualization` (19)
6. `protocol` (19)
7. `programming` (19)
8. `technical` (17)
9. `owl` (17, not owls)
10. `education` (17)
11. `character` (24 after consolidation)
12. `design` (16)
13. `shneiderman` (20 after consolidation)
14. `report` (13)
15. `gonzo` (13)
16. `demo` (13)
17. `system` (12)
18. `interactive` (12)
19. `ai` (10)
20. `soul-chat` (9)

## Action Items:
1. Run a script to remove all leading/trailing spaces from tags
2. Replace all name variations with standardized forms
3. Convert all plurals to singular
4. Ensure consistent hyphenation
5. Merge redundant tags 