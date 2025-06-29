#!/bin/bash

echo "Fixing filename comment formatting - adding newlines..."

for file in *.html; do
    if [[ -f "$file" ]]; then
        echo "Processing $file..."
        # Replace -->< with -->\n< to separate comment from html tag
        sed -i.bak 's/--><html/-->\n<html/' "$file"
    fi
done

echo "Comment formatting fixed for all HTML files!"
