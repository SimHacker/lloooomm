#!/bin/bash

# Rename all .yaml files to .yml in LLOOOOMM
# Usage: ./rename_yaml_to_yml.sh

echo "🔄 Renaming all .yaml files to .yml in LLOOOOMM..."

# Change to LLOOOOMM root directory
cd "$(dirname "$0")/.."

# Find and rename all .yaml files
find . -name "*.yaml" -type f | while read -r file; do
    # Get the directory and filename without extension
    dir=$(dirname "$file")
    base=$(basename "$file" .yaml)
    
    # New filename with .yml extension
    new_file="$dir/$base.yml"
    
    echo "  $file -> $new_file"
    mv "$file" "$new_file"
done

echo "✅ Done! All .yaml files have been renamed to .yml" 