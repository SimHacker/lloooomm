import yaml
import sys
from collections import defaultdict

# Read the YAML file
with open('03-Resources/artifacts/data/site-map.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Track wizzids and their associated file paths
wizzid_to_files = defaultdict(list)

# Process all pages
for page in data.get('pages', []):
    wizzid = page.get('wizzid')
    path = page.get('path')
    if wizzid and path:
        wizzid_to_files[wizzid].append(path)

# Find duplicates
duplicates = {wizzid: files for wizzid, files in wizzid_to_files.items() if len(files) > 1}

# Categorize duplicates
same_file_dups = {}
different_file_dups = {}

for wizzid, files in duplicates.items():
    unique_files = list(set(files))
    if len(unique_files) == 1:
        same_file_dups[wizzid] = files[0]
    else:
        different_file_dups[wizzid] = unique_files

# Print results
print("=== DUPLICATES POINTING TO SAME FILE (can be removed) ===")
for wizzid, file in sorted(same_file_dups.items()):
    count = len([f for f in wizzid_to_files[wizzid] if f == file])
    print(f"{wizzid}: {file} (appears {count} times)")

print("\n=== DUPLICATES POINTING TO DIFFERENT FILES (need unique wizzids) ===")
for wizzid, files in sorted(different_file_dups.items()):
    print(f"\n{wizzid}:")
    for file in files:
        print(f"  - {file}")

print(f"\nTotal duplicate wizzids: {len(duplicates)}")
print(f"Same file duplicates: {len(same_file_dups)}")
print(f"Different file duplicates: {len(different_file_dups)}") 