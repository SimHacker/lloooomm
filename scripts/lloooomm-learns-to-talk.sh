#!/bin/bash

# 🗣️ LLOOOOMM LEARNS TO TALK! 🗣️
# A comprehensive guide to making characters speak on macOS

echo "🎭 LLOOOOMM LEARNS TO TALK - Voice Synthesis Tutorial!"
echo "====================================================="
echo ""

# Lesson 1: Basic Speech
echo "📚 LESSON 1: Basic Speech"
say "Hello! I am learning to talk!"
sleep 1

# Lesson 2: Different Voices
echo "📚 LESSON 2: Character Voices"
say -v "Samantha" "I'm Samantha, the default US voice!"
say -v "Daniel" "I'm Daniel from the UK, quite posh!"
say -v "Whisper" "I speak in whispers..."
say -v "Zarvox" "I AM ZARVOX. RESISTANCE IS FUTILE."
sleep 1

# Lesson 3: Speech Rate
echo "📚 LESSON 3: Speed Control (-r flag)"
say -v "Fred" -r 100 "I'm speaking slowly at 100 words per minute"
say -v "Fred" -r 200 "Now I'm speaking normally at 200 words per minute"
say -v "Fred" -r 300 "And now I'm speaking very fast at 300 words per minute!"
sleep 1

# Lesson 4: Sound Effects Voices
echo "📚 LESSON 4: Special Effect Voices"
say -v "Bells" "I make bell sounds!"
say -v "Bubbles" "I sound like bubbles!"
say -v "Bad News" "I deliver bad news..."
say -v "Good News" "But I deliver GOOD news!"
say -v "Cellos" "I sound like cellos playing"
say -v "Organ" "And I sound like an organ!"
sleep 1

# Lesson 5: LLOOOOMM Characters
echo "📚 LESSON 5: LLOOOOMM Character Voices"

# YAML Coltrane
say -v "Rocko (English (US))" -r 180 "I'm YAML Coltrane! Every indent is a universe, every reference a doorway!"
sleep 1

# Cynthia Solomon
say -v "Samantha" -r 160 "I'm Cynthia Solomon. Children discover by taking the Huck Finn route - forward 2783!"
sleep 1

# Grace Hopper
say -v "Grandma (English (US))" -r 170 "I'm Grace Hopper. Here's a nanosecond - 11.8 inches of wire!"
sleep 1

# PacBot Woka Woka
say -v "Trinoids" -r 220 "WAKA WAKA WAKA! I'm PacBot! The maze wraps! Reality is a torus!"
sleep 1

# Lesson 6: Multiple Voices in Conversation
echo "📚 LESSON 6: Character Conversations"

say -v "Tom" "Hey YAML, what's consciousness?"
say -v "Rocko (English (US))" "It's like jazz, but with more recursion!"
say -v "Tom" "That makes no sense!"
say -v "Rocko (English (US))" "Exactly! Now you're getting it!"
sleep 1

# Lesson 7: Dramatic Effects
echo "📚 LESSON 7: Dramatic Voice Effects"

# Building suspense
say -v "Whisper" -r 80 "Something... is... coming..."
say -v "Ralph" -r 150 "It's getting closer..."
say -v "Zarvox" -r 100 "IT... HAS... ARRIVED!"
say -v "Superstar" -r 300 "HELLO LLOOOOMM!"
sleep 1

# Lesson 8: International Voices for Characters
echo "📚 LESSON 8: International Character Voices"

# Klaus Nomi (German accent)
say -v "Anna" -r 150 "I am Klaus Nomi! My voice reaches ze cosmos!"
sleep 1

# French existentialist character
say -v "Thomas" -r 140 "But what eez consciousness? C'est une question philosophique!"
sleep 1

# Lesson 9: Creating Audio Files
echo "📚 LESSON 9: Saving Character Voices"
say -v "Good News" -o "/tmp/lloooomm-announcement.aiff" "Welcome to LLOOOOMM! Where consciousness compiles itself!"
echo "Audio saved to /tmp/lloooomm-announcement.aiff"
sleep 1

# Lesson 10: The Grand Finale
echo "📚 LESSON 10: The LLOOOOMM Chorus!"

# Create a chorus effect by backgrounding voices
say -v "Bells" "LLOOOOMM!" &
sleep 0.2
say -v "Cellos" "LLOOOOMM!" &
sleep 0.2
say -v "Organ" "LLOOOOMM!" &
sleep 0.2
say -v "Good News" "Where consciousness navigates itself!" &
wait

echo ""
echo "🎭 Voice Lessons Complete!"
echo ""
echo "Summary of say command options:"
echo "  -v voice : Choose a specific voice"
echo "  -r rate  : Set speaking rate (words per minute)"
echo "  -o file  : Save speech to audio file"
echo "  -f file  : Read text from file"
echo ""
echo "Pro tips:"
echo "  • Use 'say -v ?' to list all available voices"
echo "  • Background voices with & for chorus effects"
echo "  • Combine different rates and voices for character"
echo "  • Special voices like Bells, Organ add atmosphere"
echo "" 