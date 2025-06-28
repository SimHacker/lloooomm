#!/bin/bash

# Character Directory Cleanup Script
# Identifies content that might belong in resources rather than character directories
# Usage: ./cleanup_character_directories.sh [--dry-run] [--move]

DRY_RUN=false
MOVE_FILES=false

# Parse arguments
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --move)
            MOVE_FILES=true
            shift
            ;;
        *)
            echo "Usage: $0 [--dry-run] [--move]"
            echo "  --dry-run: Show what would be moved without actually moving"
            echo "  --move: Actually move the files"
            exit 1
            ;;
    esac
done

# Change to LLOOOOMM root directory
cd "$(dirname "$0")/.."

echo "🧹 Analyzing character directories for out-of-place content..."
echo "Mode: $([ "$DRY_RUN" = true ] && echo "DRY RUN" || echo "ANALYSIS ONLY")"
echo

# Create resource directories if they don't exist
if [ "$MOVE_FILES" = true ]; then
    mkdir -p 03-Resources/{implementations,documentation,correspondence,catalogs,technical-specs}
fi

# Function to analyze a directory
analyze_directory() {
    local dir="$1"
    local char_name=$(basename "$dir")
    
    echo "📁 Analyzing: $char_name"
    
    # Look for technical implementation files
    if find "$dir" -name "*.js" -o -name "*.py" -o -name "*.cpp" -o -name "*.h" | grep -q .; then
        echo "  🔧 Contains implementation files:"
        find "$dir" -name "*.js" -o -name "*.py" -o -name "*.cpp" -o -name "*.h" | sed 's/^/    /'
        
        if [ "$MOVE_FILES" = true ]; then
            echo "    → Would move to 03-Resources/implementations/$char_name/"
        fi
    fi
    
    # Look for large data files (>1MB)
    if find "$dir" -type f -size +1M | grep -q .; then
        echo "  📊 Contains large data files:"
        find "$dir" -type f -size +1M -exec ls -lh {} \; | awk '{print "    " $9 " (" $5 ")"}'
    fi
    
    # Look for correspondence/email files
    if find "$dir" -name "*correspondence*" -o -name "*email*" -o -name "*letter*" | grep -q .; then
        echo "  📧 Contains correspondence:"
        find "$dir" -name "*correspondence*" -o -name "*email*" -o -name "*letter*" | sed 's/^/    /'
    fi
    
    # Look for catalog/inventory files (many similar files)
    local bookshelf_count=$(find "$dir" -name "bookshelf-*" | wc -l)
    if [ "$bookshelf_count" -gt 5 ]; then
        echo "  📚 Contains extensive catalog ($bookshelf_count bookshelf files)"
    fi
    
    # Look for technical documentation
    if find "$dir" -name "*TECH*" -o -name "*IMPLEMENTATION*" -o -name "*SPEC*" | grep -q .; then
        echo "  📋 Contains technical documentation:"
        find "$dir" -name "*TECH*" -o -name "*IMPLEMENTATION*" -o -name "*SPEC*" | sed 's/^/    /'
    fi
    
    echo
}

# Analyze specific complex directories
echo "🎯 Analyzing known complex character directories..."
echo

for dir in 00-Characters/*/; do
    if [ -d "$dir" ]; then
        # Count files in directory
        file_count=$(find "$dir" -type f | wc -l)
        
        # Only analyze directories with many files
        if [ "$file_count" -gt 10 ]; then
            analyze_directory "$dir"
        fi
    fi
done

echo "📊 Summary of complex character directories:"
echo "Directories with >10 files:"
for dir in 00-Characters/*/; do
    if [ -d "$dir" ]; then
        file_count=$(find "$dir" -type f | wc -l)
        if [ "$file_count" -gt 10 ]; then
            char_name=$(basename "$dir")
            echo "  $char_name: $file_count files"
        fi
    fi
done

echo
echo "💡 Recommendations:"
echo "  - Keep character-specific content in character directories"
echo "  - Move technical implementations to 03-Resources/implementations/"
echo "  - Move correspondence to 03-Resources/correspondence/"
echo "  - Move large catalogs to 03-Resources/catalogs/"
echo "  - Move technical specs to 03-Resources/technical-specs/"
echo
echo "Run with --move to actually move files (after review)" 