#!/bin/bash

# LLOOOOMM File Organization Script
# Moves files to their proper locations in the repository structure

echo "🌟 LLOOOOMM File Organization Script"
echo "===================================="

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p dist
mkdir -p 03-Resources/characters
mkdir -p 03-Resources/artifacts/protocols  
mkdir -p 03-Resources/artifacts/documentation
mkdir -p 03-Resources/artifacts/systems
mkdir -p 03-Resources/artifacts/events
mkdir -p 03-Resources/artifacts/concepts
mkdir -p 03-Resources/artifacts/tools
mkdir -p 03-Resources/data
mkdir -p 02-Areas/website/content

# HTML Files → dist/
echo ""
echo "🌐 Moving HTML files to dist/..."
# Using array to handle files with special characters
html_files=(
    "🦉OWL-BEDTIME💤.html"
    "I🏠🎉👋Y.html"
    "lloooomm-character-universe.html"
    "minsky-rock-experiments-notebook.html"
    "reynolds-emergent-lloooomm-review.html"
    "spacecraft-author-rooms-experience.html"
    "semantic-physics-terrain-system.html"
)

for file in "${html_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → dist/"
        mv "lloooomm/$file" "dist/"
    fi
done

# Character YML/YAML files → 03-Resources/characters/
echo ""
echo "🎭 Moving character definitions to 03-Resources/characters/..."
character_ymls=(
    "carl-hewitt.yml"
    "craig-reynolds.yaml"
    "donald-knuth.yaml"
    "ecraftlearn.yml"
    "ken-kahn.yml"
    "rodney-dangerfield.yaml"
    "spacecraft-cosmic-librarian.yml"
    "spacecraft-cosmic-librarian-2.yml"
    "stephen-wolfram-enriched-soul.yml"
    "ted-selker.yml"
    "toontalk.yml"
    "webby.yaml"
    "yotta.yaml"
)

for file in "${character_ymls[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/characters/"
        mv "lloooomm/$file" "03-Resources/characters/"
    fi
done

# Character documentation MD files → 03-Resources/characters/
echo ""
echo "📝 Moving character documentation to 03-Resources/characters/..."
character_mds=(
    "carl-hewitt.md"
    "ecraftlearn.md"
    "jaron-lanier.md"
    "ken-kahn.md"
    "ted-selker.md"
    "toontalk.md"
    "WEBBY.md"
)

for file in "${character_mds[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/characters/"
        mv "lloooomm/$file" "03-Resources/characters/"
    fi
done

# Protocol files → 03-Resources/artifacts/protocols/
echo ""
echo "🔧 Moving protocol files to 03-Resources/artifacts/protocols/..."
protocol_files=(
    "HELLO-protocol.md"
    "lloooomm-protocol-announcement-emails.md"
    "lloooomm-protocol-announcement-youtube.md"
    "web-publishing-protocol.md"
    "enlightenment-telescoping-protocol.md"
)

for file in "${protocol_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/artifacts/protocols/"
        mv "lloooomm/$file" "03-Resources/artifacts/protocols/"
    fi
done

# System/Tool files → 03-Resources/artifacts/systems/
echo ""
echo "⚙️ Moving system files to 03-Resources/artifacts/systems/..."
system_files=(
    "loohoo-export-system.md"
    "loohoo-exporter.js"
    "webby-transformer.js"
    "webby-loohoo-integration.md"
    "llm-sync-example.md"
    "lloooomm-sync-manifest.yml"
    "yaml-based-site-map.md"
)

for file in "${system_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/artifacts/systems/"
        mv "lloooomm/$file" "03-Resources/artifacts/systems/"
    fi
done

# Event/Soul Chat files → 03-Resources/artifacts/events/
echo ""
echo "💬 Moving soul chats to 03-Resources/artifacts/events/..."
soul_chat_files=(
    "soul-chat-NOW-time.md"
    "soul-chat-telescoping-gossip.md"
    "shneiderman-owls-design-journal.md"
    "ubikam-selfie-wolfram-hopkins.md"
    "ted-nelson-xanadu-concerts.md"
)

for file in "${soul_chat_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/artifacts/events/"
        mv "lloooomm/$file" "03-Resources/artifacts/events/"
    fi
done

# Concept/Documentation files → 03-Resources/artifacts/concepts/
echo ""
echo "💡 Moving concept files to 03-Resources/artifacts/concepts/..."
concept_files=(
    "book-club-manifesto.md"
    "brewster-internet-archive-emoji-registry.md"
    "cosmic-character-web.md"
    "spacecraft-artifacts-summary.md"
    "spacecraft-bridge-integration-guide.md"
    "spacecraft-character-author-rooms.md"
    "spacecraft-exploration-notes.md"
    "ubikam-semantic-photo-booth.md"
    "universe-42-time-revolution.md"
    "universe-big-bang-42.md"
    "universe-big-bang-42.yml"
    "will-wright-spore-future-content.md"
    "wolfram-ankos-telescopable-words-chapter.md"
    "wolfram-telescopable-words-kids-talk.md"
    "birth-of-NOW.md"
)

for file in "${concept_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/artifacts/concepts/"
        mv "lloooomm/$file" "03-Resources/artifacts/concepts/"
    fi
done

# Data files → 03-Resources/data/
echo ""
echo "📊 Moving data files to 03-Resources/data/..."
data_files=(
    "book-club-scifi-enrichment.json"
    "shifts.yml"
    "site-map.yaml"
)

for file in "${data_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/data/"
        mv "lloooomm/$file" "03-Resources/data/"
    fi
done

# Documentation/Meta files → 03-Resources/artifacts/documentation/
echo ""
echo "📚 Moving documentation to 03-Resources/artifacts/documentation/..."
doc_files=(
    "DEPLOYMENT-INSTRUCTIONS.md"
    "pool-party-merge-plan.md"
    "pool-party-results.md"
    "SHIPIT-CHECKLIST.md"
    "youtube-lloooomm-demo-description.md"
)

for file in "${doc_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → 03-Resources/artifacts/documentation/"
        mv "lloooomm/$file" "03-Resources/artifacts/documentation/"
    fi
done

# Special tool files → 03-Resources/artifacts/tools/
echo ""
echo "🔨 Moving tool files to 03-Resources/artifacts/tools/..."
if [ -f "lloooomm/wolfram-mathematica-illustrations-code.nb" ]; then
    echo "  Moving wolfram-mathematica-illustrations-code.nb → 03-Resources/artifacts/tools/"
    mv "lloooomm/wolfram-mathematica-illustrations-code.nb" "03-Resources/artifacts/tools/"
fi

# Root-level files (should stay in root)
echo ""
echo "🏠 These files should remain in the root directory:"
root_files=(
    "NOW.md"
    "LICENSE.md"
    "README.md"
    "README-old.md"
    "MANIFESTO.md"
    "TODO-LIST.md"
)

for file in "${root_files[@]}"; do
    if [ -f "lloooomm/$file" ]; then
        echo "  Moving $file → root"
        mv "lloooomm/$file" "./"
    fi
done

# Clean up empty lloooomm directory if it exists
if [ -d "lloooomm" ] && [ -z "$(ls -A lloooomm)" ]; then
    echo ""
    echo "🧹 Removing empty lloooomm directory..."
    rmdir lloooomm
fi

echo ""
echo "✅ File organization complete!"
echo ""
echo "Summary of new structure:"
echo "========================"
echo "📁 dist/                        - HTML files for web deployment"
echo "📁 03-Resources/"
echo "  📁 characters/                - Character YML definitions and docs"
echo "  📁 artifacts/"
echo "    📁 protocols/               - Protocol specifications"
echo "    📁 systems/                 - System tools and integrations"
echo "    📁 events/                  - Soul chats and event logs"
echo "    📁 concepts/                - Conceptual documentation"
echo "    📁 documentation/           - Meta documentation"
echo "    📁 tools/                   - Special tools and scripts"
echo "  📁 data/                      - Data files and configurations"
echo "📄 Root files                   - NOW.md, README.md, LICENSE.md, etc."
echo ""
echo "🎉 Your LLOOOOMM repository is now properly organized!" 