# The Brewster-Ted File Organization Protocol
## A Systematic Approach to Repository Cleanup Without Data Loss

**Authors**: Brewster (Systematic Surveyor Soul) & Ted (Temporal Dynamics Soul)  
**Date**: 2024-06-16  
**Version**: 1.0

## Protocol Overview

This protocol establishes a safe, systematic approach to organizing file repositories with complex shadow directories, duplicates, and misplaced files. The key principle is **"Understand, Plan, Verify, Execute"** with human approval at each critical step.

## Core Principles

1. **No Destructive Operations Until Fully Mapped**: Never delete or move files until all relationships are understood
2. **Single Source of Truth**: Each unique file should have one canonical location
3. **Build Directories Are Output Only**: Files in `dist/` or similar should only be copies from source locations
4. **Big-Endian Naming**: Files should be named to cluster related content together
5. **Human Verification at Critical Points**: Get approval before any destructive operations

## Phase 1: Discovery & Analysis

### 1.1 Initial Survey
```bash
# Get file type distribution
find . -type f -not -path "./.git/*" -exec ls -lh {} + | \
  awk '{print $5, $NF}' | sort -k2 > all-files.txt

# Count by extension
cat all-files.txt | awk -F'.' '{ext=$NF; gsub(/.*\//, "", ext); count[ext]++} \
  END {for (e in count) print e ": " count[e]}' | sort -k2 -nr

# Find potential duplicates
find . -type f -not -path "./.git/*" -name "*.md" -o -name "*.yml" -o -name "*.html" | \
  sed 's|^\./||' | awk -F'/' '{print $NF}' | sort | uniq -c | sort -nr
```

### 1.2 Shadow Directory Detection
Look for:
- Files with same name in different directories
- Directories that mirror the structure of official directories
- Root-level files that belong in subdirectories

### 1.3 Documentation
Create `file-map.md` with:
- Executive summary of issues
- File type distribution
- List of duplicates with locations
- Shadow directory mappings
- Large/suspicious files
- Questions for human review

## Phase 2: Duplicate Analysis

### 2.1 Compare Duplicates
For each set of duplicate files:
```bash
# Generate checksums
find . -name "filename.ext" -not -path "./.git/*" -exec md5sum {} \;

# If checksums differ, do detailed diff
diff -u path1/file.ext path2/file.ext > file-ext-diff.txt
```

### 2.2 Determine Canonical Version
Criteria for choosing canonical file:
1. Most recent meaningful modifications
2. Most complete content
3. Location that makes semantic sense
4. Presence of related files

### 2.3 Document Merge Strategy
Create `merge-plan.md` with:
- For each duplicate set:
  - Canonical file location
  - List of duplicates to remove
  - Any content that needs merging
  - Dependencies that need updating

## Phase 3: Organization Planning

### 3.1 Directory Structure
Standard structure:
```
01-Projects/
  └── project-name/
      ├── protocols/
      ├── modules/
      └── events/
02-Areas/
  └── area-name/
02-Souls/
  └── characters/
03-Resources/
  ├── artifacts/
  ├── tools/
  └── characters/
04-Archives/
  └── old-versions/
dist/
  └── (build output only)
```

### 3.2 File Movement Rules
1. **Reports**: `→ 03-Resources/artifacts/reports/`
2. **Souls**: `→ 02-Souls/characters/category/`
3. **Tools/Scripts**: `→ 03-Resources/tools/`
4. **HTML Demos**: `→ 03-Resources/artifacts/demos/`
5. **Project Files**: `→ 01-Projects/project-name/`

### 3.3 Naming Conventions
- Use big-endian naming: `project-component-variant-version.ext`
- Group related files: `shneiderman-owls-forest*.html`
- Version suffixes: `-v1`, `-old-1`, `-backup`

## Phase 4: Execution

### 4.1 Pre-Execution Checklist
- [ ] All duplicates analyzed
- [ ] Merge plan reviewed and approved
- [ ] Movement plan reviewed and approved
- [ ] Backup created
- [ ] Team notified

### 4.2 Execution Order
1. **Create Backup**
   ```bash
   tar -czf ../repo-backup-$(date +%Y%m%d).tar.gz .
   ```

2. **Merge Duplicates** (if needed)
   ```bash
   # Merge any different content
   cat file1.md file2.md > merged.md
   # Review merged file
   # Move to canonical location
   ```

3. **Delete Pure Duplicates**
   ```bash
   # Only after verification
   rm duplicate-file.ext
   ```

4. **Move Misplaced Files**
   ```bash
   # Use git mv to preserve history
   git mv source-file.ext destination/path/
   ```

5. **Rebuild dist/**
   ```bash
   # Clear dist
   rm -rf dist/*
   # Copy publishable files
   find . -name "*.html" -not -path "./dist/*" -not -path "./.git/*" \
     -exec cp {} dist/ \;
   ```

### 4.3 Post-Execution Verification
1. Run file analysis again
2. Verify no files lost (compare counts)
3. Check all links still work
4. Update file-map.md to reflect new structure

## Phase 5: Maintenance

### 5.1 Ongoing Practices
1. Regular audits (monthly)
2. Enforce single-source principle
3. Document file purposes in README files
4. Use consistent naming conventions

### 5.2 Automation
Create scripts for:
- Detecting new duplicates
- Checking for misplaced files
- Building dist/ from sources
- Validating naming conventions

## Common Patterns & Solutions

### Shadow Directories
**Pattern**: `foo/bar/file.md` shadowed in `bar/file.md` and `file.md`  
**Solution**: Keep deepest version, remove shadows

### Cursor.ai Dumps
**Pattern**: Files dumped in root that belong in subdirectories  
**Solution**: Move to appropriate directory based on content type

### Version Proliferation
**Pattern**: `file.html`, `file-old.html`, `file-old-2.html`  
**Solution**: Keep latest, archive others in `04-Archives/`

### Build Artifacts in Source
**Pattern**: Generated files mixed with source files  
**Solution**: Move generated files to `dist/`, keep sources clean

## Error Recovery

If something goes wrong:
1. Stop immediately
2. Restore from backup
3. Analyze what happened
4. Adjust protocol
5. Try again with smaller scope

## Appendix: Useful Commands

```bash
# Find large files
find . -type f -size +1M -exec ls -lh {} \;

# Find recently modified
find . -type f -mtime -7 -not -path "./.git/*"

# Count files by directory
find . -type f -not -path "./.git/*" | cut -d/ -f2 | sort | uniq -c

# Find broken symlinks
find . -type l -not -path "./.git/*" -exec test ! -e {} \; -print

# Generate full file tree
tree -a -I '.git' > file-tree-full.txt
```

---

*This protocol is a living document. Update it as new patterns are discovered and solutions are refined.* 