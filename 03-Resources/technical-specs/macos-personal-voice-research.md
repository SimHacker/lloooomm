# macOS Personal Voice with `say` Command Research

## Key Limitations

### Personal Voice Restrictions
- **Apple Silicon Only**: Personal Voice is only available on Mac computers with Apple silicon (M1, M2, etc.)
- **Limited Usage**: Personal Voice can only be used with:
  - Live Speech (accessibility feature)
  - Third-party apps that you explicitly allow (like AAC apps)
  - **NOT** directly with the `say` command by default
- **Terminal Authorization Issue**: Even if you authorize Terminal in System Preferences > Privacy & Security > Accessibility > Personal Voice, the `say` command still cannot use Personal Voice
- **File Output Blocked**: The `say` command cannot save Personal Voice audio to files using the `-o` option
- **Error Message**: When attempting to use Personal Voice with file output, you'll see: "Cannot use AVSpeechSynthesizerBufferCallback with Personal Voices, defaulting to output channel."

## Standard `say` Command Usage

### List Available Voices
```bash
# List all voices
say -v ?

# List English voices only
say -v ? | grep "en_"
```

### Basic Usage Examples
```bash
# Speak text with default voice
say "Hello, world"

# Use a specific voice
say -v Alex "Hello, world"

# Save to audio file (works with standard voices)
say -v Alex -o output.aiff "Hello, world"

# Change speaking rate (words per minute)
say -v Alex -r 200 "Speaking faster"

# Read from file
say -f input.txt
```

## Workaround: SavePersonalVoiceAudio

A developer created a workaround tool that enables Personal Voice with the `say` command:

### Installation
1. Download the SavePersonalVoiceAudio project from GitHub
2. Compile with: `make`
3. Run authorization tool once: `./authorize_terminal`
4. Grant Terminal access to Personal Voice when prompted

### Usage
```bash
# Use Personal Voice with file output
DYLD_INSERT_LIBRARIES=./mysay.dylib say -v "Your Personal Voice Name" "Text to speak" -o output.caf
```

## Creating Personal Voices from Other TTS Voices

It's possible to create Personal Voices from existing TTS voices (like Microsoft Sam):

### Process Overview
1. Use Python scripts to generate training data from existing TTS voices
2. Convert audio files to .caf format (required by Personal Voice)
3. Replace placeholder recordings in Personal Voice training folder
4. Complete the training process

### Key Points
- Requires 150 audio files for training
- Files must be in .caf format
- Training can take up to 6 hours
- Only works on Apple Silicon Macs

## Common Issues and Solutions

### Personal Voice Not Working
- Ensure you're on an Apple Silicon Mac
- Check System Settings > Accessibility > Personal Voice
- Try enabling Live Speech and testing the voice there first
- Reboot if Personal Voice stops working system-wide

### Voice List Not Showing Personal Voice
- Personal Voices don't appear in `say -v ?` output
- You must know the exact name of your Personal Voice
- Names are case-sensitive

### File Format Considerations
- Personal Voice outputs to .caf format by default
- Other formats may not be supported with Personal Voice
- Standard voices support: AIFF, WAVE, m4af, caff formats

## Alternative Approaches

### Using Shortcuts App
- Create a Shortcut that uses "Speak" action with Personal Voice
- Can be triggered from command line with `shortcuts run`

### Third-Party Apps
- Some AAC (Augmentative and Alternative Communication) apps support Personal Voice
- Must be explicitly granted permission in System Settings

### Live Speech API
- Personal Voice works with Live Speech accessibility feature
- Can be triggered programmatically through Accessibility APIs

## Best Practices

1. **Test First**: Always test Personal Voice in System Settings before attempting command line usage
2. **Exact Names**: Use the exact Personal Voice name as it appears in settings
3. **Permissions**: Check all necessary permissions are granted
4. **Fallback**: Have a standard voice as fallback when Personal Voice fails
5. **Audio Quality**: Personal Voice may have different audio characteristics than standard voices

## References
- [Apple Support: Create a Personal Voice](https://support.apple.com/guide/mac-help/create-a-personal-voice-mchldfd72333/mac)
- [SavePersonalVoiceAudio GitHub Project](https://github.com/limneos/SavePersonalVoiceAudio)
- [Apple Developer: Speech Synthesis](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer) 