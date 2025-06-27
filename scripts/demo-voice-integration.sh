#!/bin/bash

# 🎭🎵 LLOOOOMM VOICE INTEGRATION DEMONSTRATION 🎵🎭
# Shows how to integrate Mac say command with all LLOOOOMM scripts

echo "🎭🎵 LLOOOOMM VOICE INTEGRATION DEMONSTRATION 🎵🎭"
echo "================================================="
echo ""
echo "This system integrates Mac's 'say' command with LLOOOOMM scripts to:"
echo "✨ Make characters speak their dialogue"
echo "🎵 Enable characters to sing"
echo "🎭 Add emoji sound effects"
echo "🌈 Create interactive voice experiences"
echo ""

# Function to demonstrate voice capability (works without say command)
demo_voice() {
    local character="$1"
    local text="$2"
    local voice="${3:-Samantha}"
    
    echo "🎭 [$character]: $text"
    
    # Try to use say command if available
    if command -v say >/dev/null 2>&1; then
        say -v "$voice" "$text" 2>/dev/null &
        echo "🔊 Speaking with voice: $voice"
    else
        echo "🔇 (say command not available - showing text only)"
    fi
}

echo "🎪 DEMONSTRATION SCENES:"
echo ""

# Scene 1: Character introductions
echo "Scene 1: Character Introductions"
echo "================================"
demo_voice "Don Hopkins" "PRE PRE PRE! Welcome to LLOOOOMM!" "Samantha"
sleep 2
demo_voice "Mickey Mouse" "OH BOY! This is amazing!" "Junior"
sleep 2
demo_voice "Hunter S. Thompson" "We can't stop here, this is bat country!" "Ralph"
sleep 2

echo ""
echo "Scene 2: Musical Performance"
echo "==========================="
demo_voice "YAML Coltrane" "Every indent is a universe, every reference a doorway!" "Rocko (English (US))"
sleep 2
demo_voice "Rocky" "I am the eternal stone. Time flows through me." "Bad News"
sleep 2

echo ""
echo "Scene 3: Emoji Sound Effects"
echo "============================"
echo "🎵 Music emoji -> Bells voice"
echo "🔥 Fire emoji -> Trinoids voice"
echo "⭐ Star emoji -> Good News voice"
echo "🌈 Rainbow emoji -> Organ voice"
echo "💫 Sparkles emoji -> Whisper voice"

# Demonstrate emoji sounds if say is available
if command -v say >/dev/null 2>&1; then
    echo ""
    echo "🔊 Playing emoji sounds..."
    say -v "Bells" "Music" 2>/dev/null &
    sleep 0.5
    say -v "Trinoids" "Fire" 2>/dev/null &
    sleep 0.5
    say -v "Good News" "Star" 2>/dev/null &
    sleep 0.5
    say -v "Organ" "Rainbow" 2>/dev/null &
    sleep 0.5
    say -v "Whisper" "Sparkles" 2>/dev/null &
    wait
fi

echo ""
echo "🎯 HOW TO USE WITH EXISTING SCRIPTS:"
echo "===================================="
echo ""
echo "1. Enhanced Diverse Voices:"
echo "   python3 scripts/diverse-voice-visualizations-with-sound.py"
echo ""
echo "2. Voice-enabled file operations:"
echo "   ./scripts/voice-integration-wrapper.sh"
echo ""
echo "3. Add voice to any script:"
echo "   source scripts/lloooomm-enhanced-voice-system.sh"
echo "   enhanced_speak \"Character\" \"Message\""
echo ""
echo "4. Make characters sing:"
echo "   sing_as_character \"Character\" \"Lyrics\""
echo ""
echo "5. Play emoji sounds:"
echo "   play_emojis_from_text \"🎵🔥⭐🌈💫\""
echo ""

echo "🎭 INTEGRATION EXAMPLES:"
echo "========================"
echo ""
echo "# Add voice to organize-lloooomm-files.sh:"
echo "enhanced_speak \"File Organizer\" \"Moving HTML files to dist\""
echo ""
echo "# Add voice to wizzid_generator.py output:"
echo "enhanced_speak \"WIZZID Generator\" \"Generated new chess piece identity\""
echo ""
echo "# Add singing to any celebration:"
echo "sing_as_character \"Victory Voice\" \"Success in LLOOOOMM land\""
echo ""

echo "🎪 INTERACTIVE MODE DEMO:"
echo "========================="
echo "Try these commands:"
echo "• speak Mickey Mouse: OH BOY! This is great!"
echo "• sing Rocky: I am the stone that sings"
echo "• emoji: 🎵🔥⭐🌈💫"
echo ""

# Simple interactive demo
read -p "🎭 Try speaking (enter text or 'skip'): " user_input
if [[ "$user_input" != "skip" && -n "$user_input" ]]; then
    demo_voice "User" "$user_input" "Samantha"
fi

echo ""
echo "✨ INTEGRATION COMPLETE! ✨"
echo "==========================="
echo ""
echo "Your LLOOOOMM scripts now have:"
echo "🎭 Character voices for every personality"
echo "🎵 Singing capabilities with melody"
echo "🔊 Emoji sound effects"
echo "🎪 Interactive voice commands"
echo "🌈 Full audio-visual experience"
echo ""
echo "🎯 Next steps:"
echo "1. Run any script with voice-integration-wrapper.sh"
echo "2. Try the enhanced diverse-voice-visualizations-with-sound.py"
echo "3. Source lloooomm-enhanced-voice-system.sh in your scripts"
echo "4. Experiment with character voices and singing!"
echo ""

if command -v say >/dev/null 2>&1; then
    demo_voice "Don Hopkins" "🎵 PRE PRE PRE! Voice integration complete! 🎵" "Samantha"
else
    echo "🔇 Install macOS or enable 'say' command for full audio experience!"
fi

echo ""
echo "🎪 End of demonstration! Welcome to the speaking LLOOOOMM universe! 🎪" 