#!/usr/bin/env python3
"""
LLOOOOMM Data Extraction Pipeline
Extracts all markdown discussion files into structured YAML
"""

import os
import re
import yaml
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

class LLOOOOMMDataExtractor:
    def __init__(self, source_dir: str, output_dir: str):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.extracted_threads = {}
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extract_all_markdown_files(self):
        """Extract all markdown files into individual thread YAML files"""
        print("🚀 LLOOOOMM Data Extraction Starting...")
        
        # Find all markdown files
        md_files = sorted([f for f in self.source_dir.glob("*.md") 
                          if "hacker-news-leela" in f.name])
        
        print(f"📁 Found {len(md_files)} markdown files to process")
        
        for md_file in md_files:
            try:
                self.extract_single_file(md_file)
            except Exception as e:
                print(f"❌ Error processing {md_file.name}: {e}")
        
        print(f"✅ Extracted {len(self.extracted_threads)} discussion threads")

    def extract_single_file(self, filepath: Path):
        """Extract a single markdown file"""
        # Extract thread number from filename
        thread_match = re.search(r'(\d+)\.md$', filepath.name)
        if not thread_match:
            print(f"⚠️  Skipping {filepath.name} - no thread number found")
            return
        
        thread_num = thread_match.group(1)
        print(f"📝 Processing Thread {thread_num}: {filepath.name}")
        
        # Read and parse file content
        content = filepath.read_text(encoding='utf-8')
        thread_data = self.parse_markdown_file(content, thread_num)
        
        if thread_data['messages']:
            self.extracted_threads[thread_num] = thread_data
            
            # Save individual thread file
            output_file = self.output_dir / f"messages_{thread_num}.yml"
            self.save_thread_data(thread_data, output_file)
            
            print(f"  ✅ Extracted {len(thread_data['messages'])} messages from Thread {thread_num}")
        else:
            print(f"  ⚠️  No messages found in Thread {thread_num}")

    def parse_markdown_file(self, content: str, thread_num: str) -> Dict[str, Any]:
        """Parse markdown content into structured data"""
        messages = []
        
        # Handle frontmatter if present
        body_content = content
        if content.startswith('---'):
            frontmatter_end = content.find('---', 3)
            if frontmatter_end != -1:
                body_content = content[frontmatter_end + 3:].strip()
        
        # Split by --- separators to get individual messages
        sections = [s.strip() for s in re.split(r'\n---\n', body_content) if s.strip()]
        
        message_index = 1
        thread_pattern = 'general_discussion'
        key_breakthrough = 'collaborative_exchange'
        
        for section in sections:
            message = self.parse_message_section(section, thread_num, message_index)
            if message:
                messages.append(message)
                message_index += 1
                
                # Extract patterns for thread metadata
                if 'skeptic' in message['character_archetype']:
                    thread_pattern = 'skeptic_to_collaborator_conversion'
                if 'breakthrough' in message['content_type']:
                    key_breakthrough = message['content_type']
        
        # Generate thread metadata
        thread_metadata = self.generate_thread_metadata(thread_num, messages, thread_pattern, key_breakthrough)
        
        return {
            'messages': messages,
            'thread_metadata': thread_metadata
        }

    def parse_message_section(self, section: str, thread_num: str, index: int) -> Optional[Dict[str, Any]]:
        """Parse a single message section"""
        lines = section.strip().split('\n')
        if not lines:
            return None
        
        # Initialize message object
        message = {
            'id': f"msg_{thread_num}_{index:02d}",
            'parent_id': 'story' if index == 1 else f"msg_{thread_num}_{(index-1):02d}",
            'index': index,
            'thread': f"thread_{thread_num}",
            'author': '',
            'timestamp': '',
            'points': None,
            'status': 'active',
            'depth': index,
            'character_archetype': 'community_participant',
            'content_type': 'discussion_contribution',
            'text': '',
            'metadata': {},
            'analytics': {
                'wink_energy_impact': 7.0,
                'discourse_quality_contribution': 7.0,
                'learning_catalyst_rating': 7.0,
                'collaborative_potential': 7.0
            }
        }
        
        # Extract author and metadata from first few lines
        text_start_index = 0
        for i, line in enumerate(lines[:5]):
            # Look for username patterns
            username_match = (re.search(r'\*\*username:\*\*\s*`([^`]+)`', line) or 
                            re.search(r'\*\*([^*]+)\*\*\s*\|\s*(\d+\s+\w+\s+ago)', line))
            
            if username_match:
                message['author'] = username_match.group(1)
                if len(username_match.groups()) > 1 and username_match.group(2):
                    message['timestamp'] = username_match.group(2)
                text_start_index = i + 1
                break
            
            # Look for header patterns
            if line.startswith('#'):
                text_start_index = i + 1
                message['thread'] = re.sub(r'^#+\s*', '', line).lower().replace(' ', '_')
                continue
        
        # Extract text content
        text_lines = [line for line in lines[text_start_index:] 
                     if not line.startswith('**') or '|' in line]
        message['text'] = '\n'.join(text_lines).strip()
        
        if not message['text']:
            return None
        
        # Detect status from styling
        if '<span style="color: #999999;">' in message['text']:
            message['status'] = 'dead'
            message['metadata']['heavily_downvoted'] = True
        
        # Analyze content for archetype and metadata
        self.analyze_message_content(message)
        
        return message

    def analyze_message_content(self, message: Dict[str, Any]):
        """Analyze message content to determine archetype and generate metadata"""
        text = message['text'].lower()
        
        # Determine character archetype
        if 'question' in text and '?' in text:
            message['character_archetype'] = 'technical_questioner'
        elif any(word in text for word in ['skeptic', 'doubt', 'evidence']):
            message['character_archetype'] = 'constructive_skeptic'
        elif any(word in text for word in ['research', 'academic', 'mit']):
            message['character_archetype'] = 'academic_researcher'
        elif 'example' in text and 'breakthrough' in text:
            message['character_archetype'] = 'breakthrough_documenter'
        elif message['author'].lower() == 'donhopkins':
            message['character_archetype'] = 'creative_technologist_explainer'
        
        # Determine content type
        if '?' in text and message['text'].count('?') > 2:
            message['content_type'] = 'challenging_questions'
        elif any(marker in text for marker in ['example:', 'breakthrough:']):
            message['content_type'] = 'breakthrough_story_explanation'
        elif 'thanks' in text and 'interesting' in text:
            message['content_type'] = 'acceptance_and_expansion'
        
        # Calculate analytics based on content
        word_count = len(message['text'].split())
        question_count = message['text'].count('?')
        example_count = len(re.findall(r'\b(?:example|instance|case)\b', message['text'], re.IGNORECASE))
        
        message['analytics'] = {
            'wink_energy_impact': min(10, 5 + (word_count / 50) + (question_count * 0.5) + (example_count * 0.3)),
            'discourse_quality_contribution': min(10, 6 + (example_count * 0.8) + (question_count * 0.4)),
            'learning_catalyst_rating': min(10, 5 + (example_count * 1.2) + (question_count * 0.6)),
            'collaborative_potential': min(10, 6 + (2 if 'collaborate' in message['text'] else 0) + (example_count * 0.5))
        }
        
        # Add metadata
        message['metadata'] = {
            'word_count': word_count,
            'question_count': question_count,
            'example_count': example_count,
            'engagement_quality': 'high' if word_count > 100 else 'medium' if word_count > 50 else 'low',
            'community_value': ('inquiry_driving' if question_count > 0 else 
                              'example_providing' if example_count > 0 else 
                              'discussion_contributing')
        }

    def generate_thread_metadata(self, thread_num: str, messages: List[Dict], pattern: str, breakthrough: str) -> Dict[str, Any]:
        """Generate thread-level metadata"""
        if not messages:
            avg_wink_energy = 7.0
        else:
            avg_wink_energy = sum(m['analytics']['wink_energy_impact'] for m in messages) / len(messages)
        
        return {
            'thread_id': f"thread_{thread_num}",
            'primary_pattern': pattern,
            'key_breakthrough': breakthrough,
            'community_value': 'collaborative_intelligence_demonstration',
            'engagement_flow': [m['content_type'] for m in messages],
            'wink_energy_metrics': {
                'thread_coherence': min(10, avg_wink_energy * 0.9),
                'collaborative_intelligence_emergence': min(10, avg_wink_energy * 1.1),
                'technical_depth_achievement': min(10, avg_wink_energy * 0.95),
                'overall_thread_wink_score': avg_wink_energy
            },
            'participant_count': len(set(m['author'] for m in messages)),
            'message_count': len(messages),
            'depth_achieved': max((m['depth'] for m in messages), default=0)
        }

    def save_thread_data(self, thread_data: Dict[str, Any], output_file: Path):
        """Save thread data to YAML file"""
        header = f"""---
# LLOOOOMM Discussion Thread {thread_data['thread_metadata']['thread_id']}
# Extracted and enhanced with metadata
# Generated: {datetime.now().isoformat()}

"""
        
        yaml_content = yaml.dump(thread_data, 
                                default_flow_style=False, 
                                width=120, 
                                indent=2,
                                allow_unicode=True)
        
        output_file.write_text(header + yaml_content, encoding='utf-8')

    def merge_all_data(self):
        """Merge all thread data with master metadata"""
        print("🔄 Merging all thread data with master metadata...")
        
        # Load master metadata
        master_metadata_file = self.output_dir / 'master_metadata.yml'
        master_metadata = {}
        
        if master_metadata_file.exists():
            with open(master_metadata_file, 'r', encoding='utf-8') as f:
                master_metadata = yaml.safe_load(f)
        
        # Combine all threads
        all_messages = []
        all_thread_metadata = []
        
        for thread_num, thread_data in self.extracted_threads.items():
            all_messages.extend(thread_data['messages'])
            all_thread_metadata.append(thread_data['thread_metadata'])
        
        # Create complete data structure
        complete_data = {
            **master_metadata,
            'extracted_threads': self.extracted_threads,
            'all_messages': all_messages,
            'thread_summaries': all_thread_metadata,
            'extraction_metadata': {
                'total_threads': len(self.extracted_threads),
                'total_messages': len(all_messages),
                'extracted_at': datetime.now().isoformat(),
                'wink_energy_stats': self.calculate_wink_energy_stats(all_messages)
            }
        }
        
        # Save complete data
        complete_data_file = self.output_dir / 'complete_discussion_data.yml'
        
        header = f"""---
# LLOOOOMM Complete Discussion Data
# All threads + Master metadata + Analytics
# Generated: {datetime.now().isoformat()}
# 
# This file contains the complete JAZZ YAML data structure
# ready for SvelteKit rendering and viral nugget generation
#

"""
        
        yaml_content = yaml.dump(complete_data, 
                                default_flow_style=False, 
                                width=120, 
                                indent=2,
                                allow_unicode=True)
        
        complete_data_file.write_text(header + yaml_content, encoding='utf-8')
        print(f"✅ Complete data saved to: {complete_data_file}")

    def calculate_wink_energy_stats(self, messages: List[Dict]) -> Dict[str, Any]:
        """Calculate aggregate WINK energy statistics"""
        if not messages:
            return {
                'average': 0,
                'maximum': 0,
                'minimum': 0,
                'total_messages': 0,
                'high_wink_count': 0,
                'breakthrough_count': 0
            }
        
        wink_scores = [m['analytics']['wink_energy_impact'] for m in messages]
        return {
            'average': sum(wink_scores) / len(wink_scores),
            'maximum': max(wink_scores),
            'minimum': min(wink_scores),
            'total_messages': len(messages),
            'high_wink_count': len([s for s in wink_scores if s >= 9.0]),
            'breakthrough_count': len([s for s in wink_scores if s >= 9.5])
        }

def main():
    """Main execution function"""
    source_dir = 'lloooomm/03-Resources/characters/hacker-news/leela'
    output_dir = 'lloooomm/data'
    
    extractor = LLOOOOMMDataExtractor(source_dir, output_dir)
    
    # Extract all markdown files
    extractor.extract_all_markdown_files()
    
    # Merge with master metadata
    extractor.merge_all_data()
    
    print('\n🎉 LLOOOOMM Data Extraction Complete!')
    print(f'📂 Output directory: {output_dir}')
    print('🎯 Ready for SvelteKit viral nugget generation!')

if __name__ == "__main__":
    main() 