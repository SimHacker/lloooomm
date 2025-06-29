#!/bin/bash

echo "Fixing HTML files to standard format..."

# Fix ties-newdb-index.html - add DOCTYPE
if [[ -f "ties-newdb-index.html" ]]; then
    echo "Fixing ties-newdb-index.html..."
    sed -i.bak '1i\
<!DOCTYPE html>' ties-newdb-index.html
fi

# Fix files missing lang="en" - add it to <html> tag
for file in "mit-ai-memo-consciousness-emergence.html" "ubikam-reality-levels-myspace.html" "rfc-1996-gossip-protocol.html" "john-waters-rocky-movie.html" "hackernews-rocky-concert.html"; do
    if [[ -f "$file" ]]; then
        echo "Fixing $file..."
        sed -i.bak 's/<html>/<html lang="en">/' "$file"
    fi
done

# Fix look-back-at-hyperties.html - add DOCTYPE
if [[ -f "look-back-at-hyperties.html" ]]; then
    echo "Fixing look-back-at-hyperties.html..."
    sed -i.bak '1i\
<!DOCTYPE html>' look-back-at-hyperties.html
fi

echo "HTML standardization complete!"
