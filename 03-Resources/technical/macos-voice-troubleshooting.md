# 🎙️ Finding Your Custom Voice on macOS

## Where to Look

### 1. **System Settings → Accessibility → Personal Voice**
- Open System Settings (System Preferences on older macOS)
- Go to Accessibility → Personal Voice
- Your custom voice should appear here
- Make sure it shows as "Ready" not "Processing"

### 2. **Check Spoken Content Settings**
- System Settings → Accessibility → Spoken Content
- Click on "System Voice" dropdown
- Look under "Personal Voices" section (may be at the bottom)
- If using older macOS, check under "Customized" section

### 3. **Terminal Check** (Quick verification)
```bash
# List all available voices
say -v ?

# Look for your voice name
say -v ? | grep -i "your_voice_name"
```

**⚠️ IMPORTANT: Personal Voices DON'T appear in `say -v ?` output!**
- This is a known limitation
- You must know the exact name from System Settings
- Use the test script below to verify

### 4. **Common Issues**

**Voice Still Processing:**
- Personal Voice creation can take 15-60 minutes
- Check Personal Voice settings for progress
- Mac must stay awake during processing

**Voice Not Showing:**
- Restart your Mac
- Toggle Personal Voice off and on in Accessibility
- Check if you're signed into the same Apple ID

**Wrong Menu:**
- Don't look in Siri settings
- Not in Sound settings
- Must be in Accessibility → Spoken Content

## Personal Voice Limitations with `say` Command

### Key Restrictions:
1. **Apple Silicon Only** - M1, M2, M3 Macs only
2. **No File Output** - Cannot use `-o` flag to save audio files
3. **Hidden from List** - Won't show in `say -v ?` output
4. **Exact Name Required** - Case-sensitive, must match perfectly
5. **No Terminal Auth** - Even with permissions, limitations remain

### Test Your Personal Voice:
```bash
# Run our test script
./scripts/test-personal-voice.sh

# Or test manually with exact name
say -v "Your Personal Voice Name" "Test message"
```

### Workaround for File Output:
If you need to save Personal Voice audio to files:
1. Use [SavePersonalVoiceAudio](https://github.com/limneos/SavePersonalVoiceAudio)
2. Or use Shortcuts app with "Speak" action
3. Or record system audio while speaking

### 5. **Test Your Voice**
```bash
# Once you find your voice name
say -v "YourVoiceName" "Hello from LLOOOOMM! PRE PRE PRE!"
```

### Pro Tip for LLOOOOMM Integration! 🎭

Once you find your voice, we could make the Late Night show speak with it:

```javascript
// Add to the Late Night HTML console
function speakWithCustomVoice(text, voiceName) {
    const utterance = new SpeechSynthesisUtterance(text);
    const voices = speechSynthesis.getVoices();
    const customVoice = voices.find(v => v.name.includes(voiceName));
    if (customVoice) {
        utterance.voice = customVoice;
        speechSynthesis.speak(utterance);
    }
}

// Example:
speakWithCustomVoice("FOR ME TO POOP ON!", "YourVoiceName");
```

---

**Quick Check List:**
- [ ] Personal Voice shows as "Ready" in settings
- [ ] Checked Spoken Content → System Voice dropdown  
- [ ] Restarted Mac if needed
- [ ] Tested with exact name using `say -v "Voice Name" "test"`
- [ ] Run `./scripts/test-personal-voice.sh` to find working name

Let me know which macOS version you're on if you still can't find it! 