#!/bin/bash

# 🎭 VOICE AUDITION SCRIPT FOR THE ULTIMATE FUNKY WORM 🎭
# Casting Call for Ground, Grace Hopper, Worms, and More!

# Narrator voice (quirky but clear)
narrator() {
    echo "🎙️ NARRATOR: $1"
    say -v "Trinoids" -r 160 "$1"
}

# Audition announcement function
audition_intro() {
    echo ""
    echo "🎬 === AUDITIONING: $1 === 🎬"
    echo "🎤 VOICE: $2"
    echo "📝 SAYS: $3"
    say -v "$2" -r "$4" "$3"
    sleep 0.5
}

# Earth voice with pitch-bent yeah
earth_voice_audition() {
    echo ""
    echo "🌍 === EARTH VOICE AUDITION: $1 === 🌍"
    echo "🎤 VOICE: $2"
    echo "📝 SAYS: $3"
    say -v "$2" -r "$4" "$3"
    sleep 0.5
    echo "🎵 *Pitch-bent response* 🎵"
    say -v "$2" -r 80 "yyyeeeeaaaaaaahhhhhhhhhh" &
    sleep 1.5
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

earth_voice_audition "ROCKO" "Rocko" "🌍 Can you dig it? Because I AM it! I'm Ground, baby, and I got that deep funk flowing through my soil! 🎵" 140

earth_voice_audition "RALPH" "Ralph" "🌱 Hey there, I'm the earth beneath your feet, and I've been grooving since the continents started drifting! 🎶" 130

earth_voice_audition "FRED" "Fred" "🌿 I'm Ground, the funkiest dirt you ever did hear! My bass goes DEEP like my root systems! 🎸" 120

narrator "Excellent! Now let's hear some female voices for Admiral Grace Hopper!"

echo ""
echo "👵 === AUDITIONING FOR: GRACE HOPPER (Computer Science Legend) === 👵"

audition_intro "GRANDMA" "Grandma" "👩‍💻 Listen here, young programmers! Back in my day, we debugged with ACTUAL bugs! These worms today have it easy! 🐛" 140

audition_intro "VICTORIA" "Victoria" "⚓ I'm Admiral Grace Hopper, and I helped compile the future! A ship in port is safe, but that's not what ships are built for! 🚢" 135

audition_intro "PRINCESS" "Princess" "💎 Ahoy there! I invented the first compiler, and now I'm ready to compile some FUNK! 🎵" 145

audition_intro "SAMANTHA" "Samantha" "🖥️ Hello! I'm Samantha, ready to debug these funky algorithms with style! 💻" 140

narrator "Now for some male supporting voices!"

echo ""
echo "👨 === MALE VOICE AUDITIONS === 👨"

audition_intro "ALEX" "Alex" "🎤 I'm Alex, your standard narrator voice, ready to drop some computational knowledge with style! 💻" 150

audition_intro "ALBERT" "Albert" "🧠 Greetings! I find the intersection of algorithms and funk absolutely fascinating! 🤓" 140

audition_intro "DANIEL" "Daniel" "🇬🇧 Hello! I'm Daniel with a British accent, ready to make these worms sound quite sophisticated! 🎩" 145

narrator "Now for the fun novelty voices!"

echo ""
echo "🎭 === NOVELTY VOICE AUDITIONS === 🎭"

audition_intro "BAD NEWS" "Bad News" "😈 I'm Bad News, and I'm here to tell you... these worms are GOOD news for funk! 📰" 160

audition_intro "GOOD NEWS" "Good News" "😄 I'm Good News! And the good news is, we're about to get FUNKY! 🎉" 165

audition_intro "BUBBLES" "Bubbles" "🫧 I'm Bubbles! My voice floats like bubbles, perfect for those light worm harmonies! ✨" 170

audition_intro "ZARVOX" "Zarvox" "🤖 GREETINGS EARTHLINGS! I AM ZARVOX! PREPARE FOR COMPUTATIONAL FUNK DOMINATION! 👽" 150

narrator "And now, the moment we've all been waiting for... WORM SOUND AUDITIONS!"

echo ""
echo "🪱🎵 === WORM SOUND AUDITIONS === 🎵🪱"

worm_sound_audition "MORRIS WORM GLIDE" "Cellos" "weeeeoooowwwww nyaaahhhhh weeeeoooowwwww" 220

worm_sound_audition "SITE MAPPER WHISTLE" "Pipe Organ" "wheeeeee whooooo wheeeeee whooooo" 200

worm_sound_audition "TREE WORM CHIRP" "Bells" "ting ting tiiiiing ting ting tiiiiing" 180

worm_sound_audition "BULLDOZER WORM RUMBLE" "Fred" "grrrrrr brrrrrr grrrrrr brrrrrr" 90

worm_sound_audition "DREAM WORM ETHEREAL" "Whisper" "ahhhhhh ohhhhhhh ahhhhhh ohhhhhhh" 110

worm_sound_audition "FUNKY SYNTH SLIDE" "Trinoids" "wah wah wah weeeeooooowwww wah wah wah" 250

narrator "Let's hear some musical instrument voices for our funk section!"

echo ""
echo "🎸🎹 === MUSICAL INSTRUMENT AUDITIONS === 🎹🎸"

worm_sound_audition "BASS LINE" "Organ" "boom boom boom boom boom boom boom boom" 100

worm_sound_audition "SYNTH STABS" "Bells" "ding! ding! ding! ding!" 170

worm_sound_audition "WAH GUITAR" "Trinoids" "wah chicka wah wah chicka wah wah" 200

echo ""
echo "🎭 === AUDITIONS COMPLETE! === 🎭"
narrator "Thank you all for auditioning! We'll be in touch soon. Remember, keep it funky, keep it computational!"

echo ""
echo "🎵 RECOMMENDED CASTING: 🎵"
echo "🌍 GROUND: Rocko (deep and soulful with pitch-bent yeahs!)"
echo "👵 GRACE HOPPER: Victoria (authoritative but warm)"
echo "🎤 NARRATOR: Alex (clear and versatile)"
echo "🪱 WORM SOUNDS: Cellos + Trinoids (maximum funk!)"
echo "🎸 BASS: Organ (that deep groove)"
echo ""
narrator "That's a wrap! Time to make some funky computational music!"

echo "🎬 END OF AUDITIONS 🎬" 