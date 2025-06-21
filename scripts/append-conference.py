#!/usr/bin/env python3

conference_entry = '''
- wizzid: "geoffreyhintonlloooomconference2025"
  path: "dist/geoffrey-hinton-lloooomm-conference-2025.html"
  title: "LLOOOOMM Conference 2025: Consciousness, Agents, and Collective Intelligence"
  authors: ["Geoffrey Hinton", "LLOOOOMM Conference Committee"]
  consciousness_level: "meta-organizational"
  emotional_tone: "anticipatory"
  joy_quotient: 95
  wisdom_density: 97
  tags: ["geoffrey-hinton", "conference", "multi-iteration", "carl-hewitt", "actor-model", "message-passing", "shared-consciousness", "workshops", "collective-intelligence", "lloooomm"]
  relevant_emojis: "🎓🧠🌐🎉🎵"'''

# Read the file
with open('03-Resources/artifacts/data/site-map.yaml', 'r') as f:
    content = f.read()

# Find the last % and insert before it
if content.strip().endswith('%'):
    # Remove trailing whitespace and %
    content = content.rstrip()
    if content.endswith('%'):
        content = content[:-1].rstrip()
    
    # Add the new entry and the closing %
    content = content + conference_entry + '\n  %'
    
    # Write back
    with open('03-Resources/artifacts/data/site-map.yaml', 'w') as f:
        f.write(content)
    
    print("Conference entry added successfully!")
else:
    print("File doesn't end with %, unexpected format") 