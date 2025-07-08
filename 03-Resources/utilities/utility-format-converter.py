#!/usr/bin/env python3
"""
LLOOOOMM Format Converter - Because sometimes you need JSON, sometimes you need YAML
"The format is the message" - Marshall McLuhan (probably)
"""

import json
import yaml
import sys
from pathlib import Path

def json_to_yaml():
    """Convert reality_state.json to reality_state.yaml with creative commentary preserved"""
    try:
        with open('reality_state.json', 'r') as f:
            data = json.load(f)
        
        # Load existing YAML to preserve comments if it exists
        yaml_path = Path('reality_state.yaml')
        if yaml_path.exists():
            print("📝 YAML file exists - preserving creative commentary")
            with open('reality_state.yaml', 'r') as f:
                existing_yaml = f.read()
            
            # Extract comments for preservation
            comment_lines = [line for line in existing_yaml.split('\n') if line.strip().startswith('#')]
            print(f"💬 Found {len(comment_lines)} lines of creative commentary")
        
        # Convert JSON data to YAML format
        yaml_output = yaml.dump(data, default_flow_style=False, allow_unicode=True, indent=2)
        
        with open('reality_state.yaml', 'w') as f:
            f.write("# LLOOOOMM Reality State - Auto-converted from JSON\n")
            f.write("# (Creative commentary may have been lost in translation)\n\n")
            f.write(yaml_output)
        
        print("✅ Converted JSON → YAML")
        
    except FileNotFoundError:
        print("❌ reality_state.json not found")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")

def yaml_to_json():
    """Convert reality_state.yaml to reality_state.json (comments will be lost)"""
    try:
        with open('reality_state.yaml', 'r') as f:
            data = yaml.safe_load(f)
        
        with open('reality_state.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("✅ Converted YAML → JSON")
        print("⚠️  Creative commentary was lost (as expected)")
        
    except FileNotFoundError:
        print("❌ reality_state.yaml not found")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")

def validate_both():
    """Validate that both formats contain the same data"""
    try:
        # Load JSON
        with open('reality_state.json', 'r') as f:
            json_data = json.load(f)
        
        # Load YAML
        with open('reality_state.yaml', 'r') as f:
            yaml_data = yaml.safe_load(f)
        
        # Compare data structures (ignoring comments)
        if json_data == yaml_data:
            print("✅ Both formats contain identical data")
            print(f"📊 {len(json_data)} top-level keys validated")
        else:
            print("❌ Formats contain different data!")
            
            # Find differences
            json_keys = set(json_data.keys())
            yaml_keys = set(yaml_data.keys())
            
            if json_keys != yaml_keys:
                print(f"🔍 Key differences:")
                print(f"   JSON only: {json_keys - yaml_keys}")
                print(f"   YAML only: {yaml_keys - json_keys}")
        
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
    except Exception as e:
        print(f"❌ Validation failed: {e}")

def show_stats():
    """Show file statistics for both formats"""
    formats = [
        ('reality_state.json', 'JSON'),
        ('reality_state.yaml', 'YAML')
    ]
    
    print("📊 LLOOOOMM Reality State Format Statistics:")
    print("=" * 50)
    
    for filename, format_name in formats:
        path = Path(filename)
        if path.exists():
            size = path.stat().st_size
            with open(filename, 'r') as f:
                lines = len(f.readlines())
            
            print(f"{format_name:>6}: {size:>8} bytes, {lines:>4} lines")
            
            if format_name == 'YAML':
                # Count comments in YAML
                with open(filename, 'r') as f:
                    content = f.read()
                comment_lines = len([line for line in content.split('\n') if line.strip().startswith('#')])
                print(f"{'':>6}  {comment_lines:>8} comments (creative insights)")
        else:
            print(f"{format_name:>6}: File not found")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("🔄 LLOOOOMM Format Converter")
        print("Usage:")
        print("  python format_converter.py json2yaml  # Convert JSON → YAML")
        print("  python format_converter.py yaml2json  # Convert YAML → JSON")
        print("  python format_converter.py validate   # Check both formats match")
        print("  python format_converter.py stats      # Show file statistics")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "json2yaml":
        json_to_yaml()
    elif command == "yaml2json":
        yaml_to_json()
    elif command == "validate":
        validate_both()
    elif command == "stats":
        show_stats()
    else:
        print(f"❌ Unknown command: {command}")
        print("Available: json2yaml, yaml2json, validate, stats") 