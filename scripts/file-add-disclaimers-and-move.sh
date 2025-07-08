#!/bin/bash

# Script to add LLOOOOMM disclaimers to all HTML files and move them to dist/

DISCLAIMER_FILE="scripts/lloooomm-disclaimer-template.html"
DISCLAIMER_CONTENT=$(cat "$DISCLAIMER_FILE")

# Function to add disclaimer to an HTML file
add_disclaimer() {
    local file="$1"
    local output_file="$2"
    
    # Check if disclaimer already exists
    if grep -q "LLOOOOMM UNIVERSE" "$file"; then
        echo "Disclaimer already exists in $file, copying to $output_file"
        cp "$file" "$output_file"
        return
    fi
    
    # Insert disclaimer before closing body tag
    if grep -q "</body>" "$file"; then
        # Replace </body> with disclaimer + </body>
        sed "s|</body>|$DISCLAIMER_CONTENT</body>|" "$file" > "$output_file"
        echo "Added disclaimer to $file -> $output_file"
    else
        # If no </body> tag, append disclaimer at the end
        cp "$file" "$output_file"
        echo "$DISCLAIMER_CONTENT" >> "$output_file"
        echo "Appended disclaimer to $file -> $output_file"
    fi
}

# Create dist directory if it doesn't exist
mkdir -p dist

# Process all HTML files in the root directory
for html_file in *.html; do
    if [ -f "$html_file" ]; then
        echo "Processing $html_file..."
        add_disclaimer "$html_file" "dist/$html_file"
    fi
done

echo "All HTML files processed and moved to dist/"
