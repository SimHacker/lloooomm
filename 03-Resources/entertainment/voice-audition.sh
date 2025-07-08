#!/bin/bash

# 🎭 VOICE AUDITION SCRIPT FOR THE ULTIMATE FUNKY WORM 🎭
# Casting Call for Ground, Grace Hopper, Worms, and More!

# Narrator voice (quirky but clear)
narrator() {
    echo "🎙️ NARRATOR: $1"
    say -v "Trinoids" -r 140 "$1"
}

# Audition announcement function
audition_intro() {
    echo ""
    echo "🎬 === AUDITIONING: $1 === 🎬"
    echo "🎤 VOICE: $2"
    echo "📝 SAYS: $3"
    say -v "$2" -r "$4" "$3"
    sleep 1
}

# Worm sound audition function
worm_sound_audition() {
    echo ""
    echo "🪱 === WORM SOUND AUDITION: $1 === 🪱"
    echo "🎵 VOICE: $2"
    echo "🎶 SOUND: $3"
    say -v "$2" -r "$4" "$3"
    sleep 1
}

# Start the auditions!
clear
echo "🎭🎵🪱 WELCOME TO THE ULTIMATE FUNKY WORM VOICE AUDITIONS! 🪱🎵🎭"
echo ""
narrator "Welcome to our casting call! Today we're auditioning voices for the funkiest computational worm song ever created! Let's meet our candidates!"

sleep 2

echo ""
echo "🌍 === AUDITIONING FOR: GROUND (The Funky Earth Entity) === 🌍"
narrator "First up, we need a DEEP, RICH, SOULFUL voice for Ground, our funky earth entity!"

audition_intro "ROCKO" "Rocko" "🌍 Can you dig it? Because I AM it! I'm Ground, baby, and I got that deep funk flowing through my soil! 🎵" 100

audition_intro "RALPH" "Ralph" "🌱 Hey there, I'm the earth beneath your feet, and I've been grooving since the continents started drifting! 🎶" 95

audition_intro "FRED" "Fred" "🌿 I'm Ground, the funkiest dirt you ever did hear! My bass goes DEEP like my root systems! 🎸" 85

narrator "Excellent! Now let's hear some granny voices for Admiral Grace Hopper!"

echo ""
echo "👵 === AUDITIONING FOR: GRACE HOPPER (Computer Science Legend) === 👵"

audition_intro "GRANDMA" "Grandma" "👩‍💻 Listen here, young programmers! Back in my day, we debugged with ACTUAL bugs! These worms today have it easy! 🐛" 110

audition_intro "VICTORIA" "Victoria" "⚓ I'm Admiral Grace Hopper, and I helped compile the future! A ship in port is safe, but that's not what ships are built for! 🚢" 105

audition_intro "PRINCESS" "Princess" "💎 Ahoy there! I invented the first compiler, and now I'm ready to compile some FUNK! 🎵" 115

narrator "Fabulous! Now for our male supporting voices!"

echo ""
echo "👨 === MALE VOICE AUDITIONS === 👨"

audition_intro "ALEX" "Alex" "🎤 I'm Alex, your standard narrator voice, ready to drop some computational knowledge with style! 💻" 120

audition_intro "ALBERT" "Albert" "🧠 Greetings! I'm Albert, and I find the intersection of algorithms and funk absolutely fascinating! 🤓" 110

audition_intro "DANIEL" "Daniel" "🇬🇧 Hello! I'm Daniel with a British accent, ready to make these worms sound quite sophisticated! 🎩" 115

narrator "Now for the fun novelty voices!"

echo ""
echo "🎭 === NOVELTY VOICE AUDITIONS === 🎭"

audition_intro "BAD NEWS" "Bad News" "😈 I'm Bad News, and I'm here to tell you... these worms are GOOD news for funk! 📰" 130

audition_intro "GOOD NEWS" "Good News" "😄 I'm Good News! And the good news is, we're about to get FUNKY! 🎉" 135

audition_intro "BUBBLES" "Bubbles" "🫧 I'm Bubbles! My voice floats like bubbles, perfect for those light worm harmonies! ✨" 140

audition_intro "BOING" "Boing" "🤖 BOING! I'm the voice that goes BOING! Perfect for robotic worm sound effects! 🔧" 150

narrator "And now, the moment we've all been waiting for... WORM SOUND AUDITIONS!"

echo ""
echo "🪱🎵 === WORM SOUND AUDITIONS === 🎵🪱"

worm_sound_audition "MORRIS WORM GLIDE" "Cellos" "weeeeoooowwwww nyaaahhhhh weeeeoooowwwww" 200

worm_sound_audition "SITE MAPPER WHISTLE" "Pipe Organ" "wheeeeee whooooo wheeeeee whooooo" 180

worm_sound_audition "TREE WORM CHIRP" "Bells" "ting ting tiiiiing ting ting tiiiiing" 160

worm_sound_audition "BULLDOZER WORM RUMBLE" "Fred" "grrrrrr brrrrrr grrrrrr brrrrrr" 70

worm_sound_audition "DREAM WORM ETHEREAL" "Whisper" "ahhhhhh ohhhhhhh ahhhhhh ohhhhhhh" 90

worm_sound_audition "FUNKY SYNTH SLIDE" "Trinoids" "wah wah wah weeeeooooowwww wah wah wah" 220

narrator "Let's hear some musical instrument voices for our funk section!"

echo ""
echo "🎸🎹 === MUSICAL INSTRUMENT AUDITIONS === 🎹🎸"

worm_sound_audition "BASS LINE" "Organ" "boom boom boom boom boom boom boom boom" 80

worm_sound_audition "SYNTH STABS" "Bells" "ding! ding! ding! ding!" 150

worm_sound_audition "WAH GUITAR" "Trinoids" "wah chicka wah wah chicka wah wah" 180

narrator "And finally, let's test some silly voices for comic relief!"

echo ""
echo "🤡 === SILLY VOICE AUDITIONS === 🤡"

audition_intro "BAHH" "Bahh" "🐑 Bahhhh! I'm a sheep voice, ready to make these worms sound baaaaa-dass! 🐑" 140

audition_intro "ZARVOX" "Zarvox" "🤖 GREETINGS EARTHLINGS! I AM ZARVOX! PREPARE FOR COMPUTATIONAL FUNK DOMINATION! 👽" 120

audition_intro "JESTER" "Jester" "🃏 Hark! I jest, but these worms are no joke when it comes to funky algorithms! 🎪" 130

echo ""
echo "🎭 === AUDITIONS COMPLETE! === 🎭"
narrator "Thank you all for auditioning! We'll be in touch soon. Remember, keep it funky, keep it computational!"

echo ""
echo "🎵 RECOMMENDED CASTING: 🎵"
echo "🌍 GROUND: Rocko (deep and soulful)"
echo "👵 GRACE HOPPER: Victoria (authoritative but warm)"
echo "🎤 NARRATOR: Alex (clear and versatile)"
echo "🪱 WORM SOUNDS: Cellos + Trinoids (maximum funk!)"
echo "🎸 BASS: Organ (that deep groove)"
echo ""
narrator "That's a wrap! Time to make some funky computational music!"

echo "🎬 END OF AUDITIONS 🎬" 