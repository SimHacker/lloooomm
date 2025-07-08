#!/bin/bash

# The Ultimate Funky Worm (Computer Science Remix)
# A Musical Performance Script for macOS
# Featuring Gramma Grace Hopper and the LLOOOOMM Worm Collective

# === FUNCTION DEFINITIONS (Must be at top!) ===

# Function for GROUND'S DEEP VOICE - the funkiest!
ground_voice() {
    echo "🌍 GROUND: $1"
    say -v "Rocko" -r 95 "$1"
}

# Function for Grace Hopper's voice
grace_voice() {
    echo "👩‍💻 GRACE HOPPER: $1"
    say -v "Victoria" -r 105 "$1"
}

# Function for main vocals
main_vocals() {
    echo "🎤 VOCALS: $1"
    say -v "Alex" -r 115 "$1"
}

# Function for backing vocals
backing_vocals() {
    echo "🎵 BACKING: $1"
    say -v "Princess" -r 125 "$1" &
}

# Function to add bass line effect
bass_line() {
    echo "🎶 *Deep bass line starts, CPUs overclocking to the rhythm* 🎶"
    say -v "Fred" -r 60 "boom boom boom boom boom boom boom boom" &
    sleep 2
}

# Function for funky synth sounds (the iconic sliding whine!)
funky_synth() {
    echo "🎹 *Funky synth slide* 🎹"
    say -v "Cellos" -r 200 "weeeeoooowwwww weeeeoooowwwww" &
    say -v "Pipe Organ" -r 150 "nyaaaaahhhhh nyaaaaahhhhh" &
    sleep 1
}

# Function for synth stabs
synth_stab() {
    echo "🎸 *Synth stabs* 🎸"
    say -v "Bells" -r 180 "ding ding ding ding" &
}

# Function for wah-wah effect
wah_wah() {
    echo "🎵 *Wah-wah guitar* 🎵"
    say -v "Trinoids" -r 250 "wah wah wah wah wah wah" &
}

# Function for worm voices
worm_voice() {
    echo "🪱 WORMS: $1"
    say -v "Trinoids" -r 130 "$1" &
}

# === START THE SHOW! ===

clear
echo "🎭🎵🪱🌍🎵🎭🎵🪱🌍🎵🎭🎵🪱🌍🎵🎭"
echo ""
echo "    ♪♫♪ THE ULTIMATE FUNKY WORM ♪♫♪"
echo "     (Computer Science Remix)"
echo ""
echo "         🎤 Performed by: GROUND 🌍"
echo "    🎵 Featuring: Admiral Grace Hopper 👩‍💻"
echo "       🪱 With the LLOOOOMM Worm Collective 🪱"
echo ""
echo "🎭🎵🪱🌍🎵🎭🎵🪱🌍🎵🎭🎵🪱🌍🎵🎭"
echo ""
echo "🎵 Welcome to The Ultimate Funky Worm (Computer Science Remix)! 🎵"
echo "Preparing the funk... Loading computational groove modules..."
ground_voice "Can you dig it? Because I AM it!"
sleep 2

bass_line
funky_synth

echo ""
echo "🎤 INTRO:"
grace_voice "She's here, Admiral Hopper!"
sleep 1
ground_voice "Okay, thank you very much"
grace_voice "Gramma Grace, they're expecting you. You're a little late. So come debug this way. Right here."
ground_voice "What? Compile it now. Oh, compile it now, compile it now, ahem"
funky_synth

echo ""
echo "🎵 VERSE 1:"
ground_voice "Me and the LLOOOOMM Players are gonna tell you about some worms"
ground_voice "They're the funkiest worms in the code"
grace_voice "Okay, sing it, Grace!"

ground_voice "There's a worm in the ground, yes there is"
backing_vocals "That's right, that's right!"
sleep 1
ground_voice "It's six layers deep in the stack"
backing_vocals "Six layers deep!"
sleep 1
ground_voice "It only comes around when the database needs indexing"
ground_voice "But when it comes out of its function call, it sounds something like this..."
funky_synth

echo ""
echo "🎵 CHORUS:"
ground_voice "Oh, that's funky, that's funky"
ground_voice "Like nine Map-Reduce operations, that's funky!"
backing_vocals "Come on with it again, wormies"
backing_vocals "Come on with it!"
synth_stab
wah_wah

echo ""
echo "🎵 VERSE 2:"
ground_voice "All through the filesystem, yeah yeah"
backing_vocals "Sing it!"
sleep 1
ground_voice "They parse and they process"
backing_vocals "Parse and process!"
sleep 1
ground_voice "They debug without any IDE. Pretty slick, I might add. Yeah!"
ground_voice "When the Morris worm grabs its regex and starts to match"
ground_voice "Every programmer wants to get up and dance"
backing_vocals "Ah, get it baby!"

echo ""
echo "🎵 VERSE 3:"
ground_voice "Site-mapper worms crawling through the DOM"
backing_vocals "Getting really computational!"
ground_voice "Tree worms climbing B+ structures"
ground_voice "Dream worms parsing consciousness streams"
ground_voice "Bulldozer worms pushing Big Data, getting funky with their cursors"

ground_voice "Visitor pattern worms traversing every node"
backing_vocals "Polymorphic dispatching!"
ground_voice "Iterator worms stepping through collections"
backing_vocals "One element at a time!"
ground_voice "Continuation worms capturing execution state"
ground_voice "Async task worms never blocking the main thread!"

echo ""
echo "🎵 GRACE HOPPER SPEAKS:"
grace_voice "Listen here, young programmers, back in my day we had to manually debug with actual bugs! These worms today, they've got visitor patterns, continuations, and async await! They're living the dream I helped compile!"

echo ""
echo "🎵 FINAL CHORUS:"
ground_voice "Morris worms doing their text processing thing"
ground_voice "Site-mappers web-crawling with that swing"
ground_voice "Tree worms got those data structures locked down tight"
ground_voice "Dimensional derby worms racing through spacetime tonight!"

ground_voice "Visitor pattern worms polymorphically dispatching"
ground_voice "Iterator worms through collections they're catching"
ground_voice "Continuation worms capturing execution state"
ground_voice "Async task worms never making you wait!"

echo ""
echo "🎶 *Bass line fades with the gentle hum of cooling fans* 🎶"
say -v "Fred" -r 60 "boom boom boom... fade out..." &

ground_voice "Do we get paid for this processing?"
grace_voice "Yes, in computational cycles"
ground_voice "I just wanted to make sure, we do, okay"
grace_voice "OK, you're welcome, my funky little algorithms!"

echo ""
echo "🎵 GRAMMA GRACE'S OUTRO:"
grace_voice "A ship in port is safe, but that's not what ships are built for. Same goes for worms - they're meant to be out there processing data, not sitting idle in the heap!"

echo ""
echo "🎵 Performance Complete! 🎵"
ground_voice "Can you dig it? Because I AM it!"

# Wait for all background voices to finish
wait

echo ""
echo "🪱 Thank you for experiencing The Ultimate Funky Worm! 🪱"
echo "🎵 Keep it computational, keep it funky! 🎵" 