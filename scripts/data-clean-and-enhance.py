#!/usr/bin/env python3
"""
LLOOOOMM Data Cleaner and Enhancer
Removes redundant metadata from text and creates descriptive message IDs
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Any

class LLOOOOMMDataCleaner:
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        
    def clean_all_data(self):
        """Clean all message files and the complete data file"""
        print("🧹 Starting LLOOOOMM data cleaning...")
        
        # Clean individual message files
        message_files = list(self.data_dir.glob("messages_*.yml"))
        for file in message_files:
            self.clean_message_file(file)
            
        # Clean complete data file
        complete_file = self.data_dir / "complete_discussion_data.yml"
        if complete_file.exists():
            self.clean_complete_data_file(complete_file)
            
        print("✅ Data cleaning complete!")
        
    def clean_message_file(self, file_path: Path):
        """Clean a single message file"""
        print(f"🧽 Cleaning {file_path.name}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        # Clean messages
        for message in data.get('messages', []):
            self.clean_message(message)
            
        # Save cleaned data
        self.save_yaml_data(data, file_path)
        
    def clean_complete_data_file(self, file_path: Path):
        """Clean the complete data file"""
        print(f"🧽 Cleaning {file_path.name}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        # Clean all messages in extracted_threads
        for thread_id, thread_data in data.get('extracted_threads', {}).items():
            for message in thread_data.get('messages', []):
                self.clean_message(message)
                
        # Clean all_messages array
        for message in data.get('all_messages', []):
            self.clean_message(message)
            
        # Save cleaned data
        self.save_yaml_data(data, file_path)
        
    def clean_message(self, message: Dict[str, Any]):
        """Clean a single message object"""
        # Clean text content
        original_text = message.get('text', '')
        cleaned_text = self.clean_message_text(original_text)
        message['text'] = cleaned_text
        
        # Generate descriptive ID
        descriptive_id = self.generate_descriptive_id(message, cleaned_text)
        
        # Update parent_id if it references the old ID format
        old_id = message.get('id', '')
        message['id'] = descriptive_id
        
        # Fix parent_id to use new descriptive format or story
        if message.get('parent_id') and message['parent_id'] != 'story':
            # For now, keep the parent_id logic simple - will need thread context to fix properly
            pass
            
    def clean_message_text(self, text: str) -> str:
        """Remove redundant metadata from message text"""
        
        # Remove poster information (lines like "**Posted by:** DonHopkins | 4 hours ago | 47 points | 23 comments")
        text = re.sub(r'\*\*Posted by:\*\*[^\n]*\n\n?', '', text)
        
        # Remove username headers (lines like "**username:** `bytecode_ninja` | 3 hours ago | 12 points")
        text = re.sub(r'\*\*username:\*\*\s*`[^`]+`[^\n]*\n\n?', '', text)
        
        # Remove standalone author/timestamp lines (lines like "**DonHopkins** | 2 hours ago | 8 points")
        text = re.sub(r'^\*\*([^*]+)\*\*\s*\|\s*\d+\s+\w+\s+ago\s*(\|\s*\d+\s+points?)?\s*\n\n?', '', text, flags=re.MULTILINE)
        
        # Remove timestamp-only lines
        text = re.sub(r'^\d+\s+(hours?|minutes?|seconds?)\s+ago\s*\|\s*\d+\s+points?\s*\n\n?', '', text, flags=re.MULTILINE)
        
        # Remove point scores in isolation
        text = re.sub(r'^\d+\s+points?\s*\n\n?', '', text, flags=re.MULTILINE)
        
        # Clean up multiple newlines
        text = re.sub(r'\n\n\n+', '\n\n', text)
        
        # Strip leading/trailing whitespace
        text = text.strip()
        
        return text
        
    def generate_descriptive_id(self, message: Dict[str, Any], text: str) -> str:
        """Generate descriptive message ID based on content"""
        
        # Get key info
        author = message.get('author', '').lower().replace(' ', '_')
        thread = message.get('thread', '').replace('thread_', '')
        index = message.get('index', 1)
        
        # Extract key concepts from text for description
        description = self.extract_key_concepts(text, author)
        
        # Create descriptive ID
        if author:
            return f"msg_{thread}_{author}_{description}"
        else:
            return f"msg_{thread}_{index:02d}_{description}"
            
    def extract_key_concepts(self, text: str, author: str) -> str:
        """Extract key concepts from message text for ID generation"""
        
        # Key concept patterns to look for
        concept_patterns = {
            'wink_energy': ['wink energy', 'measurement', 'metric'],
            'character_simulation': ['character', 'simulation', 'ai models'],
            'breakthrough_example': ['breakthrough', 'example', 'x-files'],
            'skeptical_questions': ['question', 'evidence', 'skeptic'],
            'academic_validation': ['research', 'academic', 'mit'],
            'technical_depth': ['technical', 'implementation', 'architecture'], 
            'collaboration_request': ['open source', 'collaborate', 'experiment'],
            'humor_protocol': ['joke', 'humor', 'comedy', 'laugh'],
            'coalition_formation': ['coalition', 'formation', 'partnership'],
            'consciousness_discussion': ['consciousness', 'emergent', 'meta'],
            'redemption_story': ['redemption', 'transformation', 'growth'],
            'chess_revolution': ['chess', 'democratic', 'pieces'],
            'applause_protocol': ['clap', 'applause', 'celebration'],
            'pbd_breakthrough': ['programming by demonstration', 'pbd'],
            'educational_innovation': ['education', 'learning', 'teaching'],
            'infrastructure_practical': ['infrastructure', 'production', 'devops']
        }
        
        text_lower = text.lower()
        
        # Find matching concepts
        for concept_id, keywords in concept_patterns.items():
            if any(keyword in text_lower for keyword in keywords):
                return concept_id
                
        # Fallback: extract key action words
        if 'question' in text_lower and '?' in text:
            return 'technical_questions'
        elif 'example' in text_lower:
            return 'example_explanation'
        elif 'thanks' in text_lower:
            return 'appreciation_response'
        elif author == 'donhopkins':
            return 'detailed_response'
        else:
            return 'discussion_contribution'
            
    def save_yaml_data(self, data: Dict[str, Any], file_path: Path):
        """Save cleaned data back to YAML file"""
        
        # Read original header
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
            
        header_match = re.match(r'(---\n.*?\n\n)', original_content, re.DOTALL)
        header = header_match.group(1) if header_match else "---\n"
        
        # Generate YAML content
        yaml_content = yaml.dump(data, 
                                default_flow_style=False, 
                                width=120, 
                                indent=2,
                                allow_unicode=True)
        
        # Write back with header
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(yaml_content)
            
    def update_parent_ids(self):
        """Update parent IDs to use new descriptive format"""
        print("🔗 Updating parent ID references...")
        
        # Load complete data to build ID mapping
        complete_file = self.data_dir / "complete_discussion_data.yml"
        if not complete_file.exists():
            return
            
        with open(complete_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        # Build thread-wise message sequences
        threads = {}
        for thread_id, thread_data in data.get('extracted_threads', {}).items():
            messages = thread_data.get('messages', [])
            # Sort by index to maintain order
            messages.sort(key=lambda x: x.get('index', 0))
            threads[thread_id] = messages
            
        # Update parent IDs based on sequence
        for thread_id, messages in threads.items():
            for i, message in enumerate(messages):
                if i == 0:
                    message['parent_id'] = 'story'
                else:
                    # Parent is the previous message in the thread
                    parent_message = messages[i-1]
                    message['parent_id'] = parent_message['id']
                    
        # Save updated data
        self.save_yaml_data(data, complete_file)
        
        # Update individual thread files too
        for thread_id, messages in threads.items():
            thread_file = self.data_dir / f"messages_{thread_id}.yml"
            if thread_file.exists():
                with open(thread_file, 'r', encoding='utf-8') as f:
                    thread_data = yaml.safe_load(f)
                thread_data['messages'] = messages
                self.save_yaml_data(thread_data, thread_file)
                
        print("✅ Parent ID updates complete!")

def main():
    """Main execution function"""
    data_dir = 'lloooomm/data'
    
    cleaner = LLOOOOMMDataCleaner(data_dir)
    
    # Clean all data
    cleaner.clean_all_data()
    
    # Update parent IDs to use new descriptive format
    cleaner.update_parent_ids()
    
    print('\n🎉 LLOOOOMM Data Cleaning Complete!')
    print('📝 Removed redundant metadata from message text')
    print('🏷️ Generated descriptive message IDs')
    print('🔗 Updated parent ID references')
    print('🎯 Ready for clean template rendering!')

if __name__ == "__main__":
    main() 