#!/usr/bin/env python3
"""
Link Hopper Worms Implementation
Worms that treat links as living characters with bidirectional context
"""

import os
import re
import json
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import networkx as nx

class LinkPersonality(Enum):
    CURIOUS = "curious"          # New link, exploring
    SHY = "shy"                  # Rarely followed
    POPULAR = "popular"          # Frequently followed
    TEACHER = "teacher"          # Introduces concepts
    BRIDGE = "bridge"            # Connects clusters
    SCHOLAR = "scholar"          # Academic reference
    GHOST = "ghost"              # Broken link
    OUROBOROS = "ouroboros"      # Circular reference

class LinkRelationship(Enum):
    REFERENCE = "reference"
    ELABORATION = "elaboration"
    CONTRADICTION = "contradiction"
    DEPENDENCY = "dependency"
    SIBLING = "sibling"
    EXAMPLE = "example"

@dataclass
class LinkCharacter:
    """A link with personality and metadata"""
    source_file: str
    target_file: str
    link_text: str
    personality: LinkPersonality = LinkPersonality.CURIOUS
    relationship: LinkRelationship = LinkRelationship.REFERENCE
    follow_count: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    last_followed: Optional[datetime] = None
    last_updated: datetime = field(default_factory=datetime.now)
    bidirectional: bool = False
    context_summary: Dict[str, str] = field(default_factory=dict)
    metadata: Dict[str, any] = field(default_factory=dict)
    
    def evolve_personality(self, new_personality: LinkPersonality):
        """Evolve the link's personality based on usage"""
        self.metadata['previous_personality'] = self.personality.value
        self.personality = new_personality
        self.last_updated = datetime.now()
    
    def follow(self):
        """Record that this link was followed"""
        self.follow_count += 1
        self.last_followed = datetime.now()
        
        # Auto-evolve based on usage
        if self.follow_count > 50 and self.personality == LinkPersonality.CURIOUS:
            self.evolve_personality(LinkPersonality.POPULAR)
        elif self.follow_count < 5 and self.personality == LinkPersonality.CURIOUS:
            self.evolve_personality(LinkPersonality.SHY)

@dataclass
class LinkContext:
    """Context around a link"""
    before_text: str
    after_text: str
    section_title: str
    keywords: List[str]
    summary: str

class DirectoryScanner:
    """Scans directories and builds link graphs"""
    
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.graph = nx.DiGraph()
        self.file_contents = {}
        
    def scan(self) -> Dict:
        """Scan directory for markdown/yaml files and extract links"""
        manifest = {
            'scan_time': datetime.now().isoformat(),
            'root': str(self.root_path),
            'files': {}
        }
        
        for file_path in self.root_path.rglob('*.md'):
            relative_path = file_path.relative_to(self.root_path)
            links = self._extract_links(file_path)
            
            manifest['files'][str(relative_path)] = {
                'links': links,
                'backlinks': [],  # Will be populated later
                'last_modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            }
            
            # Add to graph
            self.graph.add_node(str(relative_path))
            for link in links:
                self.graph.add_edge(str(relative_path), link['target'])
        
        # Calculate backlinks
        for file_path, file_info in manifest['files'].items():
            for link in file_info['links']:
                target = link['target']
                if target in manifest['files']:
                    manifest['files'][target]['backlinks'].append({
                        'source': file_path,
                        'context': link.get('context', '')
                    })
        
        return manifest
    
    def _extract_links(self, file_path: Path) -> List[Dict]:
        """Extract all links from a file"""
        content = file_path.read_text(encoding='utf-8')
        self.file_contents[str(file_path.relative_to(self.root_path))] = content
        
        links = []
        
        # Wiki-style [[links]]
        for match in re.finditer(r'\[\[([^\]]+)\]\]', content):
            links.append({
                'type': 'wiki',
                'text': match.group(1),
                'target': match.group(1) + '.md',
                'position': match.start(),
                'context': self._extract_context(content, match.start())
            })
        
        # Markdown [text](link)
        for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
            if not match.group(2).startswith('http'):
                links.append({
                    'type': 'markdown',
                    'text': match.group(1),
                    'target': match.group(2),
                    'position': match.start(),
                    'context': self._extract_context(content, match.start())
                })
        
        return links
    
    def _extract_context(self, content: str, position: int, context_size: int = 200) -> str:
        """Extract context around a position"""
        start = max(0, position - context_size)
        end = min(len(content), position + context_size)
        context = content[start:end]
        
        # Clean up context
        context = ' '.join(context.split())
        return context

class LinkHopperWorm:
    """A worm that follows links and maintains bidirectional context"""
    
    def __init__(self, worm_id: str, root_path: str):
        self.worm_id = worm_id
        self.root_path = Path(root_path)
        self.current_file = None
        self.link_characters: Dict[str, LinkCharacter] = {}
        self.scanner = DirectoryScanner(root_path)
        
    def scan_directory(self) -> Dict:
        """Scan directory and create link characters"""
        manifest = self.scanner.scan()
        
        # Create link characters for each link
        for file_path, file_info in manifest['files'].items():
            for link in file_info['links']:
                char_id = f"{file_path}->{link['target']}"
                
                # Determine initial personality
                personality = self._determine_personality(link, file_info)
                
                self.link_characters[char_id] = LinkCharacter(
                    source_file=file_path,
                    target_file=link['target'],
                    link_text=link['text'],
                    personality=personality,
                    context_summary={
                        'source_context': link['context'],
                        'target_context': ''  # Will be filled when we hop there
                    }
                )
        
        return manifest
    
    def _determine_personality(self, link: Dict, file_info: Dict) -> LinkPersonality:
        """Determine initial personality based on link characteristics"""
        # Check if target exists
        target_path = self.root_path / link['target']
        if not target_path.exists():
            return LinkPersonality.GHOST
        
        # Check for common patterns
        if 'introduction' in link['text'].lower() or 'getting started' in link['text'].lower():
            return LinkPersonality.TEACHER
        elif link['target'] in [l['target'] for l in file_info['links'] if l != link]:
            return LinkPersonality.BRIDGE
        else:
            return LinkPersonality.CURIOUS
    
    def hop_to(self, file_path: str):
        """Hop to a different file"""
        self.current_file = file_path
        
    def follow_link(self, link_character: LinkCharacter) -> Optional[str]:
        """Follow a link and update its character"""
        link_character.follow()
        
        target_path = self.root_path / link_character.target_file
        if not target_path.exists():
            link_character.evolve_personality(LinkPersonality.GHOST)
            return None
        
        # Hop to target
        self.hop_to(link_character.target_file)
        
        # Extract target context
        target_content = target_path.read_text(encoding='utf-8')
        link_character.context_summary['target_context'] = target_content[:200]
        
        return target_content
    
    def maintain_bidirectional_context(self, link_character: LinkCharacter):
        """Ensure bidirectional context is maintained"""
        source_path = self.root_path / link_character.source_file
        target_path = self.root_path / link_character.target_file
        
        if not target_path.exists():
            return
        
        target_content = target_path.read_text(encoding='utf-8')
        
        # Check if backlink exists
        backlink_pattern = rf'\[{re.escape(source_path.stem)}\]|##\s*Backlinks.*{re.escape(source_path.stem)}'
        has_backlink = re.search(backlink_pattern, target_content, re.IGNORECASE | re.DOTALL)
        
        if not has_backlink:
            # Add backlink section
            backlink_section = f"\n\n## Backlinks\n\n- [{source_path.stem}]({link_character.source_file})"
            backlink_section += f"\n  - Context: {link_character.context_summary['source_context'][:100]}..."
            backlink_section += f"\n  - Relationship: {link_character.relationship.value}"
            backlink_section += f"\n  - Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            
            # Append to file
            with open(target_path, 'a', encoding='utf-8') as f:
                f.write(backlink_section)
            
            link_character.bidirectional = True

class LinkLinter:
    """Maintains link quality and suggests improvements"""
    
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.issues = []
        
    def lint_directory(self) -> List[Dict]:
        """Lint all links in directory"""
        scanner = DirectoryScanner(self.root_path)
        manifest = scanner.scan()
        
        for file_path, file_info in manifest['files'].items():
            self._lint_file(file_path, file_info, manifest)
        
        return self.issues
    
    def _lint_file(self, file_path: str, file_info: Dict, manifest: Dict):
        """Lint a single file's links"""
        for link in file_info['links']:
            # Check if target exists
            if link['target'] not in manifest['files']:
                self.issues.append({
                    'type': 'broken_link',
                    'file': file_path,
                    'link': link['text'],
                    'target': link['target'],
                    'suggestion': self._suggest_alternative(link['target'], manifest)
                })
            
            # Check for missing backlinks
            elif link['target'] in manifest['files']:
                target_backlinks = manifest['files'][link['target']]['backlinks']
                has_backlink = any(bl['source'] == file_path for bl in target_backlinks)
                
                if not has_backlink:
                    self.issues.append({
                        'type': 'missing_backlink',
                        'file': file_path,
                        'target': link['target'],
                        'action': 'add_backlink'
                    })
    
    def _suggest_alternative(self, broken_target: str, manifest: Dict) -> Optional[str]:
        """Suggest alternative for broken link"""
        # Simple fuzzy matching
        broken_name = Path(broken_target).stem.lower()
        
        for file_path in manifest['files']:
            file_name = Path(file_path).stem.lower()
            if broken_name in file_name or file_name in broken_name:
                return file_path
        
        return None

# Example usage
if __name__ == "__main__":
    # Create a link hopper worm
    worm = LinkHopperWorm("hopper-001", "./lloooomm")
    
    # Scan directory
    print("Scanning directory...")
    manifest = worm.scan_directory()
    
    # Display link characters
    print(f"\nFound {len(worm.link_characters)} link characters:")
    for char_id, character in list(worm.link_characters.items())[:5]:
        print(f"  {character.link_text}: {character.personality.value}")
        print(f"    {character.source_file} -> {character.target_file}")
    
    # Follow some links
    print("\nFollowing links...")
    for char_id, character in list(worm.link_characters.items())[:3]:
        content = worm.follow_link(character)
        if content:
            print(f"  Followed '{character.link_text}' ({character.follow_count} times)")
    
    # Lint directory
    print("\nLinting links...")
    linter = LinkLinter("./lloooomm")
    issues = linter.lint_directory()
    
    if issues:
        print(f"Found {len(issues)} issues:")
        for issue in issues[:5]:
            print(f"  {issue['type']}: {issue.get('file', '')} -> {issue.get('target', '')}")
    else:
        print("No issues found!")
    
    # Save manifest
    manifest_path = Path("worm-manifest.yml")
    with open(manifest_path, 'w') as f:
        yaml.dump(manifest, f, default_flow_style=False)
    print(f"\nManifest saved to {manifest_path}") 