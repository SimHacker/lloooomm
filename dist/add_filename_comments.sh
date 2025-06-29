#!/bin/bash

echo "Adding filename comments to ALL HTML files..."

for file in *.html; do
    if [[ -f "$file" ]]; then
        echo "Processing $file..."
        # Create temp file with filename comment inserted after DOCTYPE
        sed "1a\\
<!-- $file -->" "$file" > "${file}.tmp"
        mv "${file}.tmp" "$file"
    fi
done

echo "Filename comments added to all HTML files!"
