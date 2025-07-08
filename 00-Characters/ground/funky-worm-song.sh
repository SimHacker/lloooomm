#!/bin/bash

# The Ultimate Funky Worm (Computer Science Remix)
# A Musical Performance Script for macOS
# Featuring Gramma Grace Hopper and the LLOOOOMM Worm Collective

echo "🎵 Welcome to The Ultimate Funky Worm (Computer Science Remix)! 🎵"
echo "Preparing the funk... Loading computational groove modules..."

# Function for GROUND'S DEEP VOICE - the funkiest!
ground_voice() {
    say -v "Rocko" -r 85 "$1"
}

# Test Ground's voice
ground_voice "Can you dig it? Because I AM it! This is Ground with that DEEP funky voice!"

# Function for funky synth sounds (the iconic sliding whine!)
funky_synth() {
    echo "🎹 *Funky synth slide* 🎹"
    say -v "Cellos" -r 200 "weeeeoooowwwww weeeeoooowwwww" &
    say -v "Pipe Organ" -r 150 "nyaaaaahhhhh nyaaaaahhhhh" &
    sleep 1
}

echo "Testing the funky synth sounds..."
funky_synth

echo "🎵 Ground's voice test complete! Ready to get FUNKY! 🎵"
