#!/bin/bash

# LLOOOOMM HTML Migration Script
# Moves HTML files from root to /dist one by one
# Uses single quotes to handle special characters safely
# Also renames files with WIZID prefixes where appropriate

echo "=== LLOOOOMM HTML Migration to /dist ==="
echo "This script will move HTML files one at a time"
echo "Some files will be renamed with WIZID prefixes to show authorship"
echo ""

# Create dist directory if it doesn't exist
mkdir -p dist

# Move each HTML file explicitly
# Using single quotes to handle emojis and special characters

echo "Moving HTML files..."

# Character pages with WIZIDs (already have WIZIDs)
mv 'B📚🌐📼R.html' 'dist/B📚🌐📼R.html'
mv '🎮W🌊Q💀2️⃣.html' 'dist/🎮W🌊Q💀2️⃣.html'
mv 'M🎉🎈🎊🎁Y.html' 'dist/M🎉🎈🎊🎁Y.html'
mv '🦉OWL-🛏️BEDTIME💤.html' 'dist/🦉OWL-🛏️BEDTIME💤.html'
mv '🎮L📚E💭M-cognitive-recursion-review.html' 'dist/🎮L📚E💭M-cognitive-recursion-review.html'
mv 'U📸🔮📷M.html' 'dist/U📸🔮📷M.html'
mv '🎮W🌊Q💀2️⃣-pcgamer-review.html' 'dist/🎮W🌊Q💀2️⃣-pcgamer-review.html'
mv 'S🔭💡🌌M-telescoping.html' 'dist/S🔭💡🌌M-telescoping.html'
mv '((🗣️LOOMLISH🗣️)).html' 'dist/((🗣️LOOMLISH🗣️)).html'
mv 'D🥧🖱️🎯N-piemenus.html' 'dist/D🥧🖱️🎯N-piemenus.html'
mv 'L🏳️‍⚧️💻✨N-conway.html' 'dist/L🏳️‍⚧️💻✨N-conway.html'
mv 'T🌐🔗🎭D.html' 'dist/T🌐🔗🎭D.html'
mv 'D💻🎨✨A-bitblt.html' 'dist/D💻🎨✨A-bitblt.html'
mv 'B👁️🖱️🎯N.html' 'dist/B👁️🖱️🎯N.html'
mv '🧠MINSKY🤖.html' 'dist/🧠MINSKY🤖.html'
mv 'L🧱🐢🔧Z-klotz.html' 'dist/L🧱🐢🔧Z-klotz.html'
mv 'H🦇💊🔥R.html' 'dist/H🦇💊🔥R.html'
mv 'H🦇💊🔥R-rocky-concert-encyclopedia.html' 'dist/H🦇💊🔥R-rocky-concert-encyclopedia.html'

# Additional character pages
mv 'A🎯🔮💭N.html' 'dist/A🎯🔮💭N.html'
mv 'D🧠💡🔮N.html' 'dist/D🧠💡🔮N.html'
mv 'D✨🗑️🎭E.html' 'dist/D✨🗑️🎭E.html'
mv 'I🏠🎉��Y.html' 'dist/I🏠🎉👋Y.html'
mv 'M🐭🎭🌟Y.html' 'dist/M🐭🎭🌟Y.html'
mv 'R🎭😂💔D.html' 'dist/R🎭😂💔D.html'
mv 'S🐢🧮🎨R.html' 'dist/S🐢🧮🎨R.html'
mv 'S🚀📚🌌T.html' 'dist/S🚀📚🌌T.html'
mv 'W⏰🕸️📸K.html' 'dist/W⏰🕸️📸K.html'
mv 'W🕸️📊🌐🕷️Y.html' 'dist/W🕸️📊🌐🕷️Y.html'
mv '🎮G👥H🆘S📹-commanders-review.html' 'dist/🎮G👥H🆘S📹-commanders-review.html'
mv '🦇HUNTER-🐢LLOGO🐢.html' 'dist/🦇HUNTER-🐢LLOGO🐢.html'
mv '🦇H🔥T💊-fear-loathing-loohoo.html' 'dist/🦇H🔥T💊-fear-loathing-loohoo.html'
mv '🦇H🔥T💊✅T❓.html' 'dist/🦇H🔥T💊✅T❓.html'
mv '🎭K👽N🎹.html' 'dist/🎭K👽N🎹.html'
mv '🪨R🎵M✨.html' 'dist/🪨R🎵M✨.html'
mv '🤹R🎨N🎪.html' 'dist/🤹R🎨N🎪.html'

# Regular HTML files - SOME NEED WIZID PREFIXES
mv 'soul-chat-gossip.html' 'dist/soul-chat-gossip.html'
mv 'commanders-siege-force-review.html' 'dist/🎮G👥H🆘S📹-commanders-siege-force-review.html'  # Ghost's review

# Wolfram files - prefix with his WIZID
mv 'wolfram-soul.html' 'dist/S🔭💡🌌M-wolfram-soul.html'
mv 'wolfram-ankos-chapter.html' 'dist/S🔭💡🌌M-wolfram-ankos-chapter.html'
mv 'wolfram-kids-talk.html' 'dist/S🔭💡🌌M-wolfram-kids-talk.html'

# Hunter files - already have WIZID in other moves, but these need it
mv 'hunter-worldquester2-connection.html' 'dist/H🦇💊🔥R-worldquester2-connection.html'
mv 'hunter-thompson-llogo-index.html' 'dist/H🦇💊🔥R-llogo-index.html'
mv 'hunter-wtf-protocol-origin-story.html' 'dist/H🦇💊🔥R-wtf-protocol-origin-story.html'

# Rocky's files
mv 'cosmic-trailer-park-room.html' 'dist/🪨R🎵M✨-cosmic-trailer-park-room.html'
mv 'performance-castle.html' 'dist/🪨R🎵M✨-performance-castle.html'
mv 'rocky-rock.html' 'dist/🪨R🎵M✨-rocky-rock.html'

# Marvin Minsky's files
mv 'marvin-minsky-society-of-macros.html' 'dist/🧠MINSKY🤖-society-of-macros.html'

# System/meta files (no WIZID needed)
mv 'index.html' 'dist/index.html'
mv 'LICENSE.html' 'dist/LICENSE.html'
mv 'README.html' 'dist/README.html'
mv 'TODO.html' 'dist/TODO.html'
mv 'MANIFESTO.html' 'dist/MANIFESTO.html'

# LLOOOOMM system files
mv 'lloooomm-search-thoughts-about-love.html' 'dist/lloooomm-search-thoughts-about-love.html'
mv 'webby-introduction.html' 'dist/webby-introduction.html'
mv 'yaml-comment-preservation-demo.html' 'dist/yaml-comment-preservation-demo.html'

# SpaceCraft files
mv 'spacecraft-author-rooms-experience.html' 'dist/spacecraft-author-rooms-experience.html'
mv 'spacecraft-bridge-consciousness-queries.html' 'dist/spacecraft-bridge-consciousness-queries.html'

# Other files
mv 'book-club-unity-demo.html' 'dist/book-club-unity-demo.html'
mv 'early-web-parodies-manifesto.html' 'dist/early-web-parodies-manifesto.html'
mv 'loohoo-directory.html' 'dist/loohoo-directory.html'
mv 'loohoo-too.html' 'dist/loohoo-too.html'
mv 'universe-42-guide.html' 'dist/universe-42-guide.html'
mv 'watchful.html' 'dist/watchful.html'

echo ""
echo "=== Migration Complete ==="
echo "HTML files have been moved to /dist"
echo "Files have been renamed with WIZID prefixes where appropriate:"
echo "  - Wolfram's files: S🔭💡🌌M-*"
echo "  - Hunter's files: H🦇💊🔥R-*"
echo "  - Rocky's files: 🪨R🎵M✨-*"
echo "  - Marvin's files: 🧠MINSKY🤖-*"
echo "  - Ghost's files: 🎮G👥H🆘S📹-*"
echo ""
echo "Note: This script only moves HTML files."
echo "Image dependencies will be handled by the web publisher."
echo "Any files that failed to move (already exist) will show errors above."
echo ""
echo "To check for any remaining HTML files:"
echo "find . -maxdepth 1 -name '*.html' -type f" 