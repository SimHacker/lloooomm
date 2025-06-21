#!/usr/bin/env python3

import re

# List of duplicate line ranges to remove (from the analysis)
# Format: (start_line, end_line) - both inclusive, 1-based
duplicate_ranges = [
    (833, 853),   # shneidermanowlssimul
    (2262, 2282), # LookBackAtHyperTIES
    (2642, 2662), # CaptainsLog
    (2653, 2673), # LLOOOOMMCharacterUniverse
    (2664, 2684), # LLOOOOMMCharacterPortal
    (2675, 2695), # LLOOOOMMHistory
    (2686, 2706), # BellyCatPlotTwist
    (2697, 2717), # MetaMindWizzySynthesis
    (2708, 2730), # HackernewsRockyConcert
    (2754, 2774), # WolframSoul
    (2765, 2785), # FederationCloudCommand
    (3012, 3032), # BORGAnalysis
    (3045, 3065), # DE
    (4002, 4022), # LookBackAtHyperTIES
    (4013, 4033), # TODO
    (4123, 4143), # CaptainsLog
    (4255, 4275), # MANIFESTO
    (4310, 4330), # pounded-by-trekification
    (4398, 4418), # prototype
    (4519, 4539), # support
    (4739, 4759), # A🎯🔮💭N
    (4750, 4770), # B📚🌐📼R
    (4761, 4781), # B👁️🖱️🎯N
    (4783, 4803), # D🧠💡🔮N
    (4849, 4869), # L🧱🐢🔧Z-klotz
    (4860, 4880), # L🏳️‍⚧️💻✨N-conway
    (4882, 4902), # M🎉🎈🎊🎁Y
    (4904, 4924), # ((🗣️LOOMLISH🗣️))
]

# Convert to 0-based for easier processing
lines_to_remove = set()
for start, end in duplicate_ranges:
    for i in range(start - 1, end):  # Convert to 0-based
        lines_to_remove.add(i)

# Read the original file
with open('03-Resources/artifacts/data/site-map.yaml', 'r') as f:
    lines = f.readlines()

print(f"Original file has {len(lines)} lines")
print(f"Removing {len(lines_to_remove)} lines")

# Write the cleaned file
with open('03-Resources/artifacts/data/site-map.yaml.cleaned', 'w') as f:
    for i, line in enumerate(lines):
        if i not in lines_to_remove:
            f.write(line)

# Count remaining lines
with open('03-Resources/artifacts/data/site-map.yaml.cleaned', 'r') as f:
    new_lines = f.readlines()

print(f"New file has {len(new_lines)} lines")
print(f"Removed {len(lines) - len(new_lines)} lines")
print("\nCleaned file saved as: 03-Resources/artifacts/data/site-map.yaml.cleaned")
print("\nTo apply changes, run:")
print("  mv 03-Resources/artifacts/data/site-map.yaml.cleaned 03-Resources/artifacts/data/site-map.yaml") 