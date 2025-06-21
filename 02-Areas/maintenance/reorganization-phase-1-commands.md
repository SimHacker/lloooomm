# LLOOOOMM Reorganization Phase 1 Commands
## Safe moves that can be executed immediately

### Step 1: Create Temp Directory
```bash
mkdir -p temp
echo "temp/" >> .gitignore
```

### Step 2: Move Temp Files
```bash
# Move cursor chat exports
mv "temp.md" "temp/"
mv "temp copy.md" "temp/"
mv "todo.txt" "temp/"

# Move the large cursor export from artifacts
mv "03-Resources/artifacts/reports/cursor-preparing-for-gcs-gc-dry-run.md" "temp/"
```

### Step 3: Move Files with Path Prefixes (obvious destinations)
These files have their destination in their name:

```bash
# From dist/ - these are build outputs, just note them for now
# dist/03-Resources-characters-hyperties-ben-floating-with-joy.html → already in 03-Resources/characters/hyperties/

# Check if any path-prefixed files exist in root
# ls 0[1-4]-*.*
```

### Step 4: Shadow Directory Investigation
Before moving, let's check contents:

```bash
# Check souls shadow directory
echo "=== souls/ shadow directory ==="
ls -la souls/

# Check bodies shadow directory  
echo "=== bodies/ shadow directory ==="
ls -la bodies/

# Check scripts shadow directory
echo "=== scripts/ shadow directory ==="
ls -la scripts/

# Check lloooomm shadow directory
echo "=== lloooomm/ shadow directory ==="
ls -la lloooomm/
```

### Step 5: ben-floating-with-joy.html Resolution
```bash
# The root file is just a fragment (1.2K), can be deleted
# The source is in 03-Resources/characters/hyperties/ (21K)
rm ben-floating-with-joy.html
```

### Step 6: Move Shneiderman Owls to Its Character Location
```bash
# The main HTML should be with its source files (yml/md)
# First rename the character files to match the HTML base name
mv 03-Resources/characters/shneiderman-owls-simulation.yml 03-Resources/characters/shneiderman-owls-forest.yml
mv 03-Resources/characters/shneiderman-owls-simulation.md 03-Resources/characters/shneiderman-owls-forest.md

# Now move the HTML files to be with their character
mv shneiderman-owls-forest.html 03-Resources/characters/
mv shneiderman-owls-forest-old-*.html 03-Resources/characters/
mv shneiderman-owls-simulation-*.html 03-Resources/characters/

# Move the design journal from bodies shadow
mv bodies/shneiderman-owls-design-journal.md 03-Resources/characters/shneiderman-owls-forest-design-journal.md
```

### Step 7: Group Root HTML Files by Category

#### Souls/Characters HTML files to move:
```bash
mkdir -p 03-Resources/characters/souls-html
# Move soul-related HTML files
mv *-soul.html 03-Resources/characters/souls-html/ 2>/dev/null || true
```

#### Reports to move:
```bash  
mkdir -p 03-Resources/artifacts/reports
# Move report files
mv *-report.html 03-Resources/artifacts/reports/ 2>/dev/null || true
mv *-report.md 03-Resources/artifacts/reports/ 2>/dev/null || true
```

#### Demos to move:
```bash
mkdir -p 03-Resources/artifacts/demos
# Move demo files
mv *-demo.html 03-Resources/artifacts/demos/ 2>/dev/null || true
mv bouncy-castle-*.html 03-Resources/artifacts/demos/ 2>/dev/null || true
mv hyperdimensional-*.html 03-Resources/artifacts/demos/ 2>/dev/null || true
```

#### CAM6 files to move:
```bash
mkdir -p 01-Projects/cam6
# Move CAM6 related files
mv cam6-*.html 01-Projects/cam6/ 2>/dev/null || true
```

#### Shneiderman Owls to keep in place:
```bash
# shneiderman-owls-forest.html is the active version
# Others may be older versions - need to check dates
```

### Step 7: Update Server Path
```bash
# After moving shneiderman-owls-forest.html, update your browser to:
# http://localhost:8080/03-Resources/characters/shneiderman-owls-forest.html
echo "Owls simulation now at: http://localhost:8080/03-Resources/characters/shneiderman-owls-forest.html"
```

### Step 8: Soul YML Files
```bash
# Move and rename soul yml files (drop -soul suffix)
mv chaim-gingold-play-soul.yml 02-Souls/characters/chaim-gingold.yml
mv dave-ungar-prototype-soul.yml 02-Souls/characters/dave-ungar.yml
mv linus-torvalds-hardware-soul.yml 02-Souls/characters/linus-torvalds.yml
mv marvin-minsky-macro-soul.yml 02-Souls/characters/marvin-minsky.yml
mv seymour-papert-parser-soul.yml 02-Souls/characters/seymour-papert.yml
```

### Step 9: Check for More Patterns
```bash
# List remaining files in root to identify more patterns
echo "=== Remaining root files ==="
ls -la *.html *.md *.yml 2>/dev/null | grep -v "^d"
```

## DO NOT EXECUTE YET - Review First!

These commands are designed to be safe and reversible. Review each section before executing.

## Next Steps After This Phase:
1. Handle shadow directories based on investigation
2. Merge duplicate lloooomm.md files  
3. Update README.md files
4. Clean up dist/ and implement proper build process
5. Handle remaining root files based on patterns discovered 