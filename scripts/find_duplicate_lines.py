#!/usr/bin/env python3

import re

# Read the file
with open('03-Resources/artifacts/data/site-map.yaml', 'r') as f:
    lines = f.readlines()

# Track wizzids and their line numbers
wizzid_lines = {}
duplicate_lines = []

# Find all wizzids and their line numbers
for i, line in enumerate(lines):
    match = re.match(r'^\s*-\s*wizzid:\s*"([^"]+)"', line)
    if match:
        wizzid = match.group(1)
        if wizzid in wizzid_lines:
            # This is a duplicate
            duplicate_lines.append((i + 1, wizzid))  # Line numbers are 1-based
        else:
            wizzid_lines[wizzid] = i + 1

# Sort by line number
duplicate_lines.sort()

print("=== DUPLICATE WIZZID ENTRIES (line numbers to remove) ===")
print("These are the SECOND occurrences that should be removed:\n")

for line_num, wizzid in duplicate_lines:
    print(f"Line {line_num}: wizzid: \"{wizzid}\"")
    # Find the entry boundaries (from current wizzid to next wizzid or end)
    start_line = line_num - 1
    end_line = start_line
    
    # Find the start of this entry (look backwards for previous entry or start)
    for j in range(start_line - 1, -1, -1):
        if j == 0 or (lines[j].strip().startswith('- wizzid:') and j != start_line - 1):
            entry_start = j + 1 if j > 0 else 0
            break
    
    # Find the end of this entry (look forward for next entry)
    for j in range(start_line + 1, len(lines)):
        if lines[j].strip().startswith('- wizzid:'):
            entry_end = j - 1
            break
    else:
        entry_end = len(lines) - 1
    
    print(f"  Entry spans lines {entry_start + 1} to {entry_end + 1}")
    print()

print(f"\nTotal duplicate entries found: {len(duplicate_lines)}")
print("\nFirst occurrences (to keep):")
for wizzid, line in sorted(wizzid_lines.items()):
    if any(w == wizzid for _, w in duplicate_lines):
        print(f"Line {line}: wizzid: \"{wizzid}\"") 