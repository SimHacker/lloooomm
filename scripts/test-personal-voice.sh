#!/bin/bash

echo "=== Personal Voice Test Script ==="
echo

# Check if on Apple Silicon
if [[ $(uname -m) == "arm64" ]]; then
    echo "✓ Running on Apple Silicon (required for Personal Voice)"
else
    echo "✗ Not running on Apple Silicon - Personal Voice not supported"
    echo "  Your architecture: $(uname -m)"
    exit 1
fi

echo
echo "Testing various voice names..."
echo "Listen for which one works:"
echo

# Common Personal Voice name patterns to test
VOICE_NAMES=(
    "Don's Personal Voice"
    "Don's Voice"
    "Don Personal Voice"
    "Don"
    "Personal Voice"
    "My Voice"
)

FOUND_VOICE=""

for voice in "${VOICE_NAMES[@]}"; do
    echo -n "Testing '$voice'... "
    
    # Try to speak with the voice, suppress all output
    if say -v "$voice" "Testing voice" 2>/dev/null; then
        echo "✓ WORKS!"
        FOUND_VOICE="$voice"
        break
    else
        echo "✗ not found"
    fi
done

echo

if [ -n "$FOUND_VOICE" ]; then
    echo "Success! Found working voice: '$FOUND_VOICE'"
    echo
    echo "Speaking a test message..."
    say -v "$FOUND_VOICE" "Hello from LLOOOOMM! This is your Personal Voice speaking. PRE PRE PRE!"
    
    echo
    echo "To use this voice in scripts, use:"
    echo "  say -v \"$FOUND_VOICE\" \"Your text here\""
else
    echo "No Personal Voice found."
    echo
    echo "Please check:"
    echo "1. Open System Settings > Accessibility > Personal Voice"
    echo "2. Verify your Personal Voice shows as 'Ready' (not 'Processing')"
    echo "3. Note the EXACT name shown for your voice"
    echo "4. You may need to restart your Mac"
    echo
    echo "For file output, you'll need the SavePersonalVoiceAudio workaround:"
    echo "  https://github.com/limneos/SavePersonalVoiceAudio"
fi 