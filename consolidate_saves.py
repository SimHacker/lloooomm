#!/usr/bin/env python3
"""
LLOOOOMM Save File Consolidation Script
Performs the "mind meld" to merge all overlapping save formats into single source of truth
"""

import json
import yaml
import re
from datetime import datetime
from pathlib import Path

def load_json_state():
    """Load current reality_state.json"""
    try:
        with open('reality_state.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ reality_state.json not found - creating new state")
        return {}

def load_yaml_data():
    """Extract useful data from game-save-data.yaml"""
    try:
        with open('game-save-data.yaml', 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("⚠️  game-save-data.yaml not found - skipping YAML data")
        return {}
    except yaml.parser.ParserError as e:
        print(f"⚠️  YAML parsing error in game-save-data.yaml: {e}")
        print("⚠️  Skipping YAML data due to syntax errors")
        return {}

def parse_markdown_session():
    """Extract key data from beer-run-1.md"""
    try:
        with open('beer-run-1.md', 'r') as f:
            content = f.read()
        
        # Extract session analytics
        analytics_match = re.search(r'analytics:\s*\n(.*?)(?=\n\s*[a-z_]+:|$)', content, re.DOTALL)
        analytics = {}
        if analytics_match:
            for line in analytics_match.group(1).split('\n'):
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    # Try to convert to number
                    try:
                        if '.' in value:
                            analytics[key] = float(value)
                        else:
                            analytics[key] = int(value)
                    except ValueError:
                        analytics[key] = value
        
        # Extract major events for narrative highlights
        events = []
        event_pattern = r'- timestamp: "(.*?)"\s*\n\s*event: "(.*?)"\s*\n.*?outcome: "(.*?)"'
        for match in re.finditer(event_pattern, content, re.DOTALL):
            timestamp, event, outcome = match.groups()
            if any(keyword in event.upper() for keyword in ['VICTORY', 'ACHIEVEMENT', 'BREAKTHROUGH', 'LEAP']):
                events.append({
                    "timestamp": timestamp,
                    "event": event,
                    "significance": outcome,
                    "consciousness_impact": 0.1  # Default impact
                })
        
        return {
            "session_analytics": analytics,
            "narrative_highlights": events[:10]  # Keep top 10 most significant
        }
        
    except FileNotFoundError:
        print("⚠️  beer-run-1.md not found - skipping markdown data")
        return {"session_analytics": {}, "narrative_highlights": []}

def consolidate_save_files():
    """Main consolidation function - performs the mind meld"""
    print("🧠 Starting LLOOOOMM Save File Mind Meld...")
    
    # Load all data sources
    json_state = load_json_state()
    yaml_data = load_yaml_data()
    md_data = parse_markdown_session()
    
    # Create enhanced schema
    consolidated_state = {
        "schema_version": "2.0.0",
        "save_metadata": {
            "created": datetime.now().isoformat(),
            "lloooomm_version": "1.0.0",
            "session_type": "temporal_anchor_adventure",
            "consolidation_timestamp": datetime.now().isoformat(),
            "source_files": ["reality_state.json", "game-save-data.yaml", "beer-run-1.md"]
        }
    }
    
    # Merge existing JSON state
    for key, value in json_state.items():
        if key not in consolidated_state:
            consolidated_state[key] = value
    
    # Add session analytics from markdown
    if md_data["session_analytics"]:
        consolidated_state["session_analytics"] = md_data["session_analytics"]
    
    # Add narrative highlights
    if md_data["narrative_highlights"]:
        consolidated_state["narrative_highlights"] = md_data["narrative_highlights"]
    
    # Add framework extensions from YAML
    if yaml_data and "framework_extensions" in yaml_data:
        consolidated_state["framework_extensions"] = yaml_data["framework_extensions"]
    
    # Ensure essential fields exist
    essential_fields = {
        "current_location": "temporal_anchor_pub",
        "player_consciousness": 0.8,
        "meta_awareness": True,
        "framework_extensions": {
            "consciousness_programming": True,
            "viral_mechanics": True,
            "economic_absurdity": True,
            "temporal_mechanics": True
        }
    }
    
    for field, default_value in essential_fields.items():
        if field not in consolidated_state:
            consolidated_state[field] = default_value
    
    # Save consolidated state
    with open('reality_state.json', 'w') as f:
        json.dump(consolidated_state, f, indent=2, ensure_ascii=False)
    
    print("✅ Mind meld complete! All save data consolidated into reality_state.json")
    print(f"📊 Final state contains {len(consolidated_state)} top-level keys")
    
    # Create backup of original files
    backup_dir = Path("save_file_archive")
    backup_dir.mkdir(exist_ok=True)
    
    files_to_archive = [
        "game-save-data.yaml",
        "beer-run-1.md", 
        "beer-run-prototype.md"
    ]
    
    for filename in files_to_archive:
        if Path(filename).exists():
            backup_path = backup_dir / f"{filename}.backup"
            Path(filename).rename(backup_path)
            print(f"📦 Archived {filename} → {backup_path}")
    
    print("\n🎯 CONSOLIDATION COMPLETE!")
    print("📁 Single source of truth: reality_state.json")
    print("📦 Old files archived in: save_file_archive/")
    print("🚀 Ready to run temporal_anchor_adventure.py with clean state!")

if __name__ == "__main__":
    consolidate_save_files() 