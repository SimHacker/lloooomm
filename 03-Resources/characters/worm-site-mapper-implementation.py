#!/usr/bin/env python3
"""
Site Mapper Worm Implementation
🪱 Crawling through monoliths, leaving metadata castings! 🪱

"From monolith to garden, one casting at a time!"
"""

import yaml
import os
import sys
from datetime import datetime
from pathlib import Path
import json

class SiteMapperWorm:
    """
    The Site Mapper Worm - Transforms monolithic site maps into distributed metadata
    
    Head pointer: Where we're looking
    Tail pointer: Where we've been
    Body: The data we're processing
    """
    
    def __init__(self):
        self.head = 0  # Current position in the file
        self.tail = 0  # Start of current batch
        self.castings_created = 0
        self.castings_merged = 0
        self.errors = []
        
        print("🪱 Site Mapper Worm awakening...")
        print("   Head: Ready to explore")
        print("   Tail: Anchored at start")
        print("   Mission: Transform monoliths into gardens!\n")
    
    def load_monolith(self, filepath):
        """Load the monolithic site-map.yaml"""
        print(f"🪱 Loading monolith: {filepath}")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                print(f"✅ Loaded successfully!")
                print(f"   Found {len(data.get('pages', []))} pages to process")
                return data
        except Exception as e:
            print(f"❌ Error loading monolith: {e}")
            return None
    
    def create_casting_path(self, html_path):
        """Convert HTML path to metadata casting path"""
        # Convert dist/foo.html to dist/foo-meta.yml
        if html_path.endswith('.html'):
            base = html_path[:-5]  # Remove .html
            return f"{base}-meta.yml"
        return f"{html_path}-meta.yml"
    
    def enrich_metadata(self, entry):
        """Enrich metadata with additional context"""
        # This is where the worm would stretch to source files
        # For now, we'll ensure all fields are present
        enriched = {
            'wizzid': entry.get('wizzid', 'UNKNOWN'),
            'path': entry.get('path', ''),
            'title': entry.get('title', 'Untitled'),
            'authors': entry.get('authors', ['Unknown']),
            'consciousness_level': entry.get('consciousness_level', 'unknown'),
            'emotional_tone': entry.get('emotional_tone', 'neutral'),
            'joy_quotient': entry.get('joy_quotient', 50),
            'wisdom_density': entry.get('wisdom_density', 50),
            'tags': entry.get('tags', []),
            'relevant_emojis': entry.get('relevant_emojis', ''),
            'last_crawled': datetime.now().isoformat() + 'Z',
            'source': 'site-map.yaml'
        }
        
        # Add special flags if present
        if 'special_flags' in entry:
            enriched['special_flags'] = entry['special_flags']
        
        # Add timestamps if present
        for field in ['created', 'modified']:
            if field in entry:
                enriched[field] = entry[field]
        
        return enriched
    
    def check_existing_casting(self, filepath):
        """Check if a casting already exists and load it"""
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f)
            except:
                return None
        return None
    
    def merge_castings(self, existing, new):
        """Merge new casting with existing, preserving valuable data"""
        # Start with existing as base
        merged = existing.copy() if existing else {}
        
        # Update with new data, but preserve certain fields from existing
        preserve_fields = ['custom_notes', 'manual_edits', 'local_metadata']
        
        for key, value in new.items():
            if key not in preserve_fields or key not in merged:
                merged[key] = value
        
        # Always update last_crawled
        merged['last_crawled'] = new['last_crawled']
        
        return merged
    
    def create_casting(self, entry, output_dir=''):
        """Create a metadata casting file"""
        casting_path = self.create_casting_path(entry.get('path', ''))
        
        # Adjust path if output_dir is specified
        if output_dir:
            casting_path = os.path.join(output_dir, casting_path)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(casting_path), exist_ok=True)
        
        # Enrich the metadata
        enriched = self.enrich_metadata(entry)
        
        # Check for existing casting
        existing = self.check_existing_casting(casting_path)
        
        if existing:
            print(f"🔄 Merging with existing: {casting_path}")
            final_data = self.merge_castings(existing, enriched)
            self.castings_merged += 1
        else:
            print(f"✨ Creating new casting: {casting_path}")
            final_data = enriched
            self.castings_created += 1
        
        # Write the casting
        try:
            with open(casting_path, 'w', encoding='utf-8') as f:
                yaml.dump(final_data, f, 
                         default_flow_style=False, 
                         allow_unicode=True,
                         sort_keys=False)
            
            # Move head forward
            self.head += 1
            
        except Exception as e:
            print(f"❌ Error creating casting: {e}")
            self.errors.append((casting_path, str(e)))
    
    def crawl_and_cast(self, monolith_path, output_dir='', batch_size=10):
        """Main crawling process"""
        print(f"\n🪱 Beginning crawl with batch size: {batch_size}")
        
        # Load the monolith
        data = self.load_monolith(monolith_path)
        if not data:
            return
        
        pages = data.get('pages', [])
        total_pages = len(pages)
        
        # Process in batches
        while self.tail < total_pages:
            # Set head to process a batch
            self.head = min(self.tail + batch_size, total_pages)
            
            print(f"\n🪱 Processing batch: {self.tail} to {self.head}")
            
            # Process each entry in the batch
            for i in range(self.tail, self.head):
                entry = pages[i]
                self.create_casting(entry, output_dir)
            
            # Move tail to head position
            self.tail = self.head
            
            # Show progress
            progress = (self.tail / total_pages) * 100
            print(f"\n📊 Progress: {progress:.1f}% ({self.tail}/{total_pages})")
        
        # Final report
        print("\n🎉 Crawl complete!")
        print(f"   ✨ New castings created: {self.castings_created}")
        print(f"   🔄 Existing castings merged: {self.castings_merged}")
        print(f"   ❌ Errors encountered: {len(self.errors)}")
        
        if self.errors:
            print("\n⚠️  Errors:")
            for path, error in self.errors[:5]:  # Show first 5 errors
                print(f"   - {path}: {error}")
            if len(self.errors) > 5:
                print(f"   ... and {len(self.errors) - 5} more")
        
        # Create summary file
        self.create_summary(output_dir, total_pages)
    
    def create_summary(self, output_dir, total_pages):
        """Create a summary of the crawl"""
        summary = {
            'worm': 'Site Mapper Worm',
            'crawl_completed': datetime.now().isoformat() + 'Z',
            'statistics': {
                'total_pages': total_pages,
                'new_castings': self.castings_created,
                'merged_castings': self.castings_merged,
                'errors': len(self.errors)
            },
            'wisdom': "From monolith to garden, one casting at a time!"
        }
        
        summary_path = os.path.join(output_dir, 'site-map-crawl-summary.yml')
        
        try:
            with open(summary_path, 'w', encoding='utf-8') as f:
                yaml.dump(summary, f, default_flow_style=False, allow_unicode=True)
            print(f"\n📋 Summary saved to: {summary_path}")
        except Exception as e:
            print(f"\n⚠️  Could not save summary: {e}")


def main():
    """Main entry point"""
    print("🪱 SITE MAPPER WORM 🪱")
    print("=" * 50)
    
    # Create worm instance
    worm = SiteMapperWorm()
    
    # Set paths
    monolith_path = "03-Resources/artifacts/data/site-map.yaml"
    output_dir = ""  # Will create in same structure as HTML files
    
    # Check if monolith exists
    if not os.path.exists(monolith_path):
        print(f"❌ Cannot find monolith at: {monolith_path}")
        return 1
    
    # Start the crawl
    worm.crawl_and_cast(monolith_path, output_dir, batch_size=20)
    
    print("\n🪱 Site Mapper Worm returning to rest... 💤")
    return 0


if __name__ == "__main__":
    sys.exit(main()) 