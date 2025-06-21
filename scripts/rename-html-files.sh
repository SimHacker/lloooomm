#!/bin/bash

# Script to rename index.html files (except the main one) and ensure unique HTML filenames

echo "🔄 Renaming duplicate index.html files..."

# Rename index.html files (keeping the main website one)
# The main website index.html is at 02-Areas/website/index.html

# HyperTIES index files
if [ -f "03-Resources/characters/hyperties/index.html" ]; then
    mv "03-Resources/characters/hyperties/index.html" "03-Resources/characters/hyperties/index-hyperties.html"
    echo "✅ Renamed hyperties/index.html to index-hyperties.html"
fi

if [ -f "03-Resources/characters/hyperties/demos/space-telescope/index.html" ]; then
    mv "03-Resources/characters/hyperties/demos/space-telescope/index.html" "03-Resources/characters/hyperties/demos/space-telescope/index-space-telescope.html"
    echo "✅ Renamed space-telescope/index.html to index-space-telescope.html"
fi

# TIES imports index files
if [ -f "03-Resources/imports/ties/index.html" ]; then
    mv "03-Resources/imports/ties/index.html" "03-Resources/imports/ties/index-ties.html"
    echo "✅ Renamed ties/index.html to index-ties.html"
fi

if [ -f "03-Resources/imports/ties/newdb/index.html" ]; then
    mv "03-Resources/imports/ties/newdb/index.html" "03-Resources/imports/ties/newdb/index-newdb.html"
    echo "✅ Renamed newdb/index.html to index-newdb.html"
fi

# Remove backup file
if [ -f "03-Resources/imports/ties/newdb/index.html~" ]; then
    rm "03-Resources/imports/ties/newdb/index.html~"
    echo "🗑️  Removed backup file index.html~"
fi

# Rename gonzo index files (they already have unique names but let's make them clearer)
# These are already uniquely named, so we'll leave them as-is

echo "✨ HTML file renaming complete!"
echo ""
echo "📋 Summary:"
echo "- Main website index.html remains at: 02-Areas/website/index.html"
echo "- Other index.html files have been renamed with descriptive suffixes"
echo "- Ready for flat directory deployment!" 