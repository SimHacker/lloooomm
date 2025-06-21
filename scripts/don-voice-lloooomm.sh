#!/bin/bash

# IMPORTANT: Personal Voices have limitations with the say command:
# 1. They don't appear in 'say -v ?' output
# 2. They require exact name matching (case-sensitive)
# 3. They may not work for file output without special tools
# 4. They only work on Apple Silicon Macs

# Try to use Don's Personal Voice
# If it fails, fall back to a similar voice
VOICE_NAME="Don's Personal Voice"
FALLBACK_VOICE="Alex"

# Test if the voice works by speaking to null device
if say -v "$VOICE_NAME" "test" -o /dev/null 2>/dev/null; then
    # Voice works, use it
    say -v "$VOICE_NAME" "$@"
else
    # Voice doesn't work, notify and use fallback
    echo "Warning: '$VOICE_NAME' not available. Using $FALLBACK_VOICE instead." >&2
    echo "Make sure:" >&2
    echo "  1. You're on an Apple Silicon Mac" >&2
    echo "  2. Personal Voice is created and ready in System Settings > Accessibility > Personal Voice" >&2
    echo "  3. The voice name matches exactly (case-sensitive)" >&2
    
    # Use fallback voice
    say -v "$FALLBACK_VOICE" "$@"
fi
