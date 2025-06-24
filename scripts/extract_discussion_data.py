#!/usr/bin/env python3
"""
LLOOOOMM Discussion Data Extractor
Converts markdown messages and YAML metadata into unified discussion tree
"""

import os
import re
import yaml
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import frontmatter

class DiscussionDataExtractor:
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.discussion_data = {
            "metadata": {},
            "story": {},
            "messages": [],
            "character_ecosystem": {},
            "analytics": {},
            "enhancements": {}
        }
        
    def extract_all_data(self) -> Dict[str, Any]:
        """Main extraction orchestrator"""
        print("🚀 Starting LLOOOOMM discussion data extraction...")
        
        # Step 1: Load YAML metadata files
        self.load_yaml_metadata()
        
        # Step 2: Parse markdown message files
        self.parse_markdown_messages()
        
        # Step 3: Extract story post from main file
        self.extract_story_post()
        
        # Step 4: Build navigation tree
        self.build_navigation_tree()
        
        # Step 5: Apply character enhancements
        self.apply_character_enhancements()
        
        # Step 6: Generate timestamps and engagement metrics
        self.generate_temporal_data()
        
        print(f"✅ Extraction complete! Found {len(self.discussion_data['messages'])} messages")
        return self.discussion_data
        
    def load_yaml_metadata(self):
        """Load all YAML files containing metadata and analytics"""
        yaml_files = list(self.source_dir.glob("*.yml"))
        print(f"📊 Loading {len(yaml_files)} YAML metadata files...")
        
        for yaml_file in yaml_files:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                
            # Categorize YAML data by type
            if 'discussion_metadata' in data:
                self.discussion_data['analytics']['discussion_metadata'] = data
                print(f"  📈 Loaded discussion metadata from {yaml_file.name}")
                
            elif 'character_constellation' in data:
                self.discussion_data['character_ecosystem'] = data
                print(f"  🎭 Loaded character ecosystem from {yaml_file.name}")
                
            elif 'simulation_metadata' in data:
                self.discussion_data['analytics']['simulation_analysis'] = data
                print(f"  🔬 Loaded simulation analysis from {yaml_file.name}")
                
            elif 'technical_genealogy_synthesis' in data:
                self.discussion_data['enhancements']['research_data'] = data
                print(f"  🧬 Loaded technical genealogy from {yaml_file.name}")
                
    def parse_markdown_messages(self):
        """Parse all markdown files into message objects"""
        md_files = sorted(list(self.source_dir.glob("*.md")))
        print(f"💬 Parsing {len(md_files)} markdown message files...")
        
        for md_file in md_files:
            if md_file.name.endswith('000.md'):
                continue  # Skip story post, handle separately
                
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.loads(f.read())
                messages = self.extract_messages_from_content(post.content, post.metadata)
                self.discussion_data['messages'].extend(messages)
                print(f"  ✅ Extracted {len(messages)} messages from {md_file.name}")
            except Exception as e:
                print(f"  ❌ Error parsing {md_file.name}: {e}")
                
    def extract_messages_from_content(self, content: str, metadata: Dict) -> List[Dict]:
        """Extract individual messages from markdown content"""
        messages = []
        
        # Split content by horizontal rules or specific patterns
        sections = re.split(r'\n---\n', content)
        
        for i, section in enumerate(sections):
            if not section.strip():
                continue
                
            message = self.parse_message_section(section, metadata)
            if message:
                messages.append(message)
                
        return messages
        
    def parse_message_section(self, section: str, file_metadata: Dict) -> Optional[Dict]:
        """Parse a single message section"""
        lines = section.strip().split('\n')
        
        # Look for username and metadata pattern
        username_pattern = r'\*\*([^*]+)\*\*\s*\|\s*(\d+\s+\w+\s+ago)\s*\|\s*(\d+\s+points?)?'
        author_pattern = r'\*\*username:\*\*\s*`([^`]+)`'
        
        message = {
            "id": "",
            "author": "",
            "text": "",
            "created": "",
            "parent_id": None,
            "depth": 0,
            "status": "active",
            "metadata": {},
            "character_enhancements": {},
            "navigation": {},
            "analytics": {},
            "rendering": {}
        }
        
        # Extract author and timing info
        for line in lines[:3]:  # Check first few lines
            username_match = re.search(username_pattern, line)
            author_match = re.search(author_pattern, line)
            
            if username_match:
                message["author"] = username_match.group(1)
                message["created"] = username_match.group(2)
                break
            elif author_match:
                message["author"] = author_match.group(1)
                break
                
        # Extract text content (everything after metadata lines)
        text_lines = []
        skip_metadata = True
        
        for line in lines:
            if skip_metadata and (line.startswith('**') or line.startswith('#')):
                continue
            skip_metadata = False
            text_lines.append(line)
            
        message["text"] = '\n'.join(text_lines).strip()
        
        # Generate ID from author and content hash
        content_hash = hash(message["text"][:50]) % 10000
        message["id"] = f"{message['author'].lower().replace(' ', '_')}_{content_hash}"
        
        # Detect flagged/dead status
        if '<span style="color: #999999;">' in message["text"]:
            message["status"] = "dead"
            message["rendering"]["css_classes"] = ["dead"]
            
        # Detect indentation/depth from original file structure
        # This is heuristic - could be improved with better parsing
        message["depth"] = self.estimate_message_depth(section)
        
        return message if message["author"] and message["text"] else None
        
    def estimate_message_depth(self, section: str) -> int:
        """Estimate message depth based on content patterns"""
        # Look for reply indicators
        if 'parent' in section.lower():
            return 1
        if '@' in section:  # Likely a reply mentioning someone
            return 2
        return 0
        
    def extract_story_post(self):
        """Extract the main story post from 000.md file"""
        story_file = self.source_dir / "hacker-news-leela-000.md"
        
        if story_file.exists():
            with open(story_file, 'r', encoding='utf-8') as f:
                post = frontmatter.loads(f.read())
            
            self.discussion_data["story"] = {
                "id": "story",
                "title": post.metadata.get("title", "LLOOOOMM Discussion"),
                "url": "https://lloooomm.com",
                "text": post.content,
                "author": "DonHopkins",
                "created": "4 hours ago",
                "points": 47,
                "comment_count": len(self.discussion_data["messages"]),
                "labels": ["show_hn", "ai", "collaborative_intelligence"],
                "enhancements": {
                    "character_analysis": "Original post demonstrates multi-perspective problem solving",
                    "technical_depth": "high",
                    "accessibility_notes": ["screen_reader_optimized", "keyboard_navigable"]
                }
            }
            
            self.discussion_data["metadata"] = {
                "title": post.metadata.get("title", "LLOOOOMM Discussion"),
                "url": "https://lloooomm.com",
                "author": "DonHopkins",
                "created": datetime.now().isoformat(),
                "total_engagement_time": "4 hours active",
                "peak_concurrent_discussion": "3 parallel threads",
                "community_sentiment": "cautiously optimistic with technical interest",
                "page_info": {
                    "current_page": 1,
                    "total_pages": 12,
                    "navigation_enabled": True
                }
            }
            
            print("📝 Extracted story post and metadata")
            
    def build_navigation_tree(self):
        """Build parent-child relationships and navigation order"""
        print("🗺️ Building navigation tree...")
        
        # Simple heuristic for now - could be enhanced with better parsing
        for i, message in enumerate(self.discussion_data["messages"]):
            message["navigation"]["next_id"] = (
                self.discussion_data["messages"][i+1]["id"] 
                if i+1 < len(self.discussion_data["messages"]) 
                else None
            )
            message["navigation"]["prev_id"] = (
                self.discussion_data["messages"][i-1]["id"] 
                if i > 0 
                else "story"
            )
            
    def apply_character_enhancements(self):
        """Apply character data to messages"""
        if 'character_constellation' not in self.discussion_data['character_ecosystem']:
            return
            
        char_data = self.discussion_data['character_ecosystem']['character_constellation']
        
        for message in self.discussion_data["messages"]:
            author = message["author"].lower().replace(' ', '_')
            
            # Look for character data
            for char_category in char_data.get('primary_technical_experts', {}).values():
                if author in str(char_category).lower():
                    message["character_enhancements"] = {
                        "archetype": char_category.get("archetype", ""),
                        "specialization": char_category.get("specialization", ""),
                        "communication_style": char_category.get("communication_style", ""),
                        "accessibility_strength": char_category.get("accessibility_strength", ""),
                        "collaboration_patterns": char_category.get("collaboration_patterns", []),
                        "evolution_notes": char_category.get("evolution_observed", "")
                    }
                    break
                    
        print("🎭 Applied character enhancements to messages")
        
    def generate_temporal_data(self):
        """Generate realistic timestamps and engagement metrics"""
        base_time = datetime.now() - timedelta(hours=4)
        
        for i, message in enumerate(self.discussion_data["messages"]):
            # Generate timestamp
            time_offset = timedelta(minutes=10 + i*5)
            message_time = base_time + time_offset
            message["created"] = message_time.isoformat()
            
            # Generate analytics
            text_length = len(message["text"])
            message["analytics"] = {
                "engagement_score": min(10, text_length / 100),
                "technical_depth": 8 if any(term in message["text"].lower() 
                                         for term in ['implementation', 'algorithm', 'architecture']) else 5,
                "controversy_level": 2 if message["status"] == "dead" else 1,
                "learning_value": 9 if "example" in message["text"].lower() else 6
            }
            
        print("⏰ Generated temporal data and analytics")
        
    def save_to_file(self, output_file: str):
        """Save extracted data to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.discussion_data, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved discussion data to {output_file}")

def main():
    source_dir = "lloooomm/03-Resources/characters/hacker-news/leela"
    output_file = "lloooomm/data/complete_discussion_data.json"
    
    # Create output directory
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Extract data
    extractor = DiscussionDataExtractor(source_dir)
    discussion_data = extractor.extract_all_data()
    
    # Save results
    extractor.save_to_file(output_file)
    
    # Print summary
    print("\n🎉 EXTRACTION COMPLETE!")
    print(f"   Story: {discussion_data['story'].get('title', 'N/A')}")
    print(f"   Messages: {len(discussion_data['messages'])}")
    print(f"   Characters: {len(discussion_data['character_ecosystem'])}")
    print(f"   Analytics: {len(discussion_data['analytics'])}")
    print(f"   Output: {output_file}")
    
if __name__ == "__main__":
    main() 