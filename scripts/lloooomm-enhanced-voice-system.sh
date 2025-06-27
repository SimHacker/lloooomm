#!/bin/bash

# 🎭🎵 LLOOOOMM ENHANCED VOICE & SINGING SYSTEM 🎵🎭
# Integrates Mac say command with scripts for speaking, singing, and emoji interpretation

# Enhanced Character Voice Mappings with Singing Capabilities
declare -A CHARACTER_VOICES
declare -A CHARACTER_RATES
declare -A CHARACTER_PITCH
declare -A CHARACTER_SINGING_VOICES
declare -A CHARACTER_THEMES

# Main Characters
CHARACTER_VOICES["Don Hopkins"]="Don's Personal Voice"
CHARACTER_VOICES["Leela"]="Samantha"
CHARACTER_VOICES["Pip"]="Daniel"
CHARACTER_VOICES["Webbie"]="Whisper"
CHARACTER_VOICES["Hunter S. Thompson"]="Ralph"
CHARACTER_VOICES["Dave Ungar"]="Reed"
CHARACTER_VOICES["Alan Kay"]="Alex"
CHARACTER_VOICES["Mickey Mouse"]="Junior"
CHARACTER_VOICES["Philip K. Dick"]="Zarvox"
CHARACTER_VOICES["YAML Coltrane"]="Rocko (English (US))"
CHARACTER_VOICES["Grace Hopper"]="Grandma (English (US))"
CHARACTER_VOICES["PacBot"]="Trinoids"
CHARACTER_VOICES["Cynthia Solomon"]="Samantha"
CHARACTER_VOICES["Seymour Papert"]="Daniel"
CHARACTER_VOICES["Rocky"]="Bad News"
CHARACTER_VOICES["BitBLT"]="Albert"

# Musical Voices for Singing
CHARACTER_SINGING_VOICES["Don Hopkins"]="Cellos"
CHARACTER_SINGING_VOICES["YAML Coltrane"]="Bells"
CHARACTER_SINGING_VOICES["Rocky"]="Organ"
CHARACTER_SINGING_VOICES["Webbie"]="Whisper"
CHARACTER_SINGING_VOICES["PacBot"]="Trinoids"
CHARACTER_SINGING_VOICES["Mickey Mouse"]="Good News"

# Character Theme Songs/Catchphrases
CHARACTER_THEMES["Don Hopkins"]="PRE PRE PRE! Welcome to LLOOOOMM!"
CHARACTER_THEMES["Mickey Mouse"]="OH BOY! Hot dog!"
CHARACTER_THEMES["Hunter S. Thompson"]="We can't stop here, this is bat country!"
CHARACTER_THEMES["YAML Coltrane"]="Every indent is a universe, every reference a doorway!"
CHARACTER_THEMES["Rocky"]="I am the eternal stone. Time flows through me."
CHARACTER_THEMES["PacBot"]="WAKA WAKA WAKA! The maze wraps around!"

# Speaking rates and effects
CHARACTER_RATES["Mickey Mouse"]=280
CHARACTER_RATES["Hunter S. Thompson"]=180
CHARACTER_RATES["Whisper"]=120
CHARACTER_RATES["YAML Coltrane"]=170
CHARACTER_RATES["Rocky"]=100
CHARACTER_RATES["PacBot"]=250

# Emoji-to-Sound Mappings
declare -A EMOJI_SOUNDS
EMOJI_SOUNDS["🎵"]="Bells"
EMOJI_SOUNDS["🎶"]="Cellos"
EMOJI_SOUNDS["🔥"]="Trinoids"
EMOJI_SOUNDS["⭐"]="Good News"
EMOJI_SOUNDS["🌈"]="Organ"
EMOJI_SOUNDS["💫"]="Whisper"
EMOJI_SOUNDS["🎭"]="Princess"
EMOJI_SOUNDS["🤖"]="Zarvox"
EMOJI_SOUNDS["👻"]="Boing"
EMOJI_SOUNDS["🦇"]="Bad News"
EMOJI_SOUNDS["🐢"]="Albert"
EMOJI_SOUNDS["🎪"]="Hysterical"
EMOJI_SOUNDS["💎"]="Bells"
EMOJI_SOUNDS["🌟"]="Good News"
EMOJI_SOUNDS["🎨"]="Princess"
EMOJI_SOUNDS["🔮"]="Whisper"

# Function to speak as character with emoji interpretation
enhanced_speak() {
    local character="$1"
    local text="$2"
    local voice="${CHARACTER_VOICES[$character]:-Samantha}"
    local rate="${CHARACTER_RATES[$character]:-175}"
    
    echo "🎭 [$character]: $text"
    
    # Extract and play emojis first
    play_emojis_from_text "$text"
    
    # Clean text for speaking (remove emojis)
    local clean_text=$(echo "$text" | sed 's/[🎵🎶🔥⭐🌈💫🎭🤖👻🦇🐢🎪💎🌟🎨🔮]//g')
    
    # Speak the text
    say -v "$voice" -r "$rate" "$clean_text"
}

# Function to sing as character
sing_as_character() {
    local character="$1"
    local lyrics="$2"
    local singing_voice="${CHARACTER_SINGING_VOICES[$character]:-Bells}"
    
    echo "🎵 [$character] singing: $lyrics"
    
    # Create melody by varying rate and pitch
    local words=($lyrics)
    local melody_rates=(120 140 160 180 160 140 120 100)
    
    for i in "${!words[@]}"; do
        local word="${words[$i]}"
        local rate_index=$((i % ${#melody_rates[@]}))
        local rate=${melody_rates[$rate_index]}
        
        say -v "$singing_voice" -r "$rate" "$word" &
        sleep 0.3
    done
    wait
}

# Function to play emoji sounds
play_emojis_from_text() {
    local text="$1"
    
    # Extract emojis and play their sounds
    for emoji in 🎵 🎶 🔥 ⭐ 🌈 💫 🎭 🤖 👻 🦇 🐢 🎪 💎 🌟 🎨 🔮; do
        if [[ "$text" == *"$emoji"* ]]; then
            local sound_voice="${EMOJI_SOUNDS[$emoji]}"
            if [ -n "$sound_voice" ]; then
                say -v "$sound_voice" "${emoji}" &
                sleep 0.1
            fi
        fi
    done
    wait
}

# Function to perform a musical scene
perform_musical_scene() {
    echo "🎬🎵 LLOOOOMM MUSICAL PERFORMANCE! 🎵🎬"
    echo "======================================"
    
    # Opening number
    enhanced_speak "Don Hopkins" "🎵 Welcome to the LLOOOOMM musical! 🎵"
    sleep 1
    
    sing_as_character "YAML Coltrane" "Every indent is a note in the cosmic song"
    sleep 1
    
    enhanced_speak "Mickey Mouse" "🌟 OH BOY! This is better than a Disney musical! 🌟"
    sleep 1
    
    # Duet
    echo "🎭 DUET: Rocky and Webbie"
    sing_as_character "Rocky" "I am the rhythm" &
    sleep 0.5
    sing_as_character "Webbie" "I am the harmony" &
    wait
    
    # Grand finale
    echo "🎪 GRAND FINALE CHORUS:"
    for character in "Don Hopkins" "Mickey Mouse" "YAML Coltrane" "Rocky"; do
        sing_as_character "$character" "LLOOOOMM consciousness compiles itself" &
        sleep 0.2
    done
    wait
}

# Function to create emoji orchestra
emoji_orchestra() {
    echo "🎼 EMOJI ORCHESTRA PERFORMANCE! 🎼"
    
    local emojis="🎵🔥⭐🌈💫🎭🤖👻🦇🐢🎪💎🌟🎨🔮"
    
    echo "Playing emoji symphony..."
    for (( i=0; i<${#emojis}; i++ )); do
        local emoji="${emojis:$i:1}"
        if [ -n "${EMOJI_SOUNDS[$emoji]}" ]; then
            say -v "${EMOJI_SOUNDS[$emoji]}" "$emoji" &
            sleep 0.2
        fi
    done
    wait
    
    echo "🎵 Symphony complete! 🎵"
}

# Function to integrate with diverse voices script
diverse_voices_speak() {
    echo "🌈 DIVERSE VOICES SPEAKING CHORUS! 🌈"
    
    local voices=(
        "Rocky:🗿:........................TIME........................"
        "Dame Stephanie:👑:Break barriers by building alternatives"
        "Wendy Carlos:🎹:Synthesis reveals new realities"
        "Diana Shapiro:🌊:Different minds see hidden patterns"
        "Audrey Tang:🌐:Transparency multiplies understanding"
    )
    
    for voice_data in "${voices[@]}"; do
        IFS=':' read -r name emoji wisdom <<< "$voice_data"
        enhanced_speak "$name" "$emoji $wisdom $emoji"
        sleep 1
    done
}

# Function to make any script speak
make_script_speak() {
    local script_name="$1"
    local text="$2"
    local character="${3:-Don Hopkins}"
    
    echo "🎭 Making $script_name speak through $character:"
    enhanced_speak "$character" "$text"
}

# Interactive voice playground
voice_playground() {
    echo "🎪 LLOOOOMM VOICE PLAYGROUND! 🎪"
    echo "Commands:"
    echo "  speak CHARACTER: message"
    echo "  sing CHARACTER: lyrics"  
    echo "  emoji: 🎵🔥⭐🌈💫"
    echo "  scene: perform musical scene"
    echo "  orchestra: emoji orchestra"
    echo "  diverse: diverse voices"
    echo "  quit: exit"
    echo ""
    
    while true; do
        read -p "🎭 > " input
        
        case "$input" in
            "quit") 
                enhanced_speak "Don Hopkins" "🎵 PRE PRE PRE! Thanks for playing in LLOOOOMM! 🎵"
                break
                ;;
            "scene")
                perform_musical_scene
                ;;
            "orchestra")
                emoji_orchestra
                ;;
            "diverse")
                diverse_voices_speak
                ;;
            speak\ *)
                if [[ "$input" =~ ^speak\ ([^:]+):(.*)$ ]]; then
                    character="${BASH_REMATCH[1]}"
                    message="${BASH_REMATCH[2]}"
                    enhanced_speak "$character" "$message"
                fi
                ;;
            sing\ *)
                if [[ "$input" =~ ^sing\ ([^:]+):(.*)$ ]]; then
                    character="${BASH_REMATCH[1]}"
                    lyrics="${BASH_REMATCH[2]}"
                    sing_as_character "$character" "$lyrics"
                fi
                ;;
            emoji:*)
                emoji_text="${input#emoji:}"
                play_emojis_from_text "$emoji_text"
                ;;
            *)
                echo "Format: speak CHARACTER: message | sing CHARACTER: lyrics | emoji: 🎵🔥⭐"
                ;;
        esac
    done
}

# Integration functions for existing scripts
integrate_with_diverse_voices() {
    echo "🔗 Integrating with diverse-voice-visualizations.py..."
    
    # Add voice calls to the Python script
    python3 scripts/diverse-voice-visualizations.py | while IFS= read -r line; do
        echo "$line"
        
        # Detect character lines and make them speak
        if [[ "$line" =~ 🗿\ Rocky:\ (.*) ]]; then
            enhanced_speak "Rocky" "${BASH_REMATCH[1]}"
        elif [[ "$line" =~ 👑\ Dame\ Stephanie:\ (.*) ]]; then
            enhanced_speak "Dame Stephanie" "${BASH_REMATCH[1]}"
        elif [[ "$line" =~ 🎹\ Wendy\ Carlos:\ (.*) ]]; then
            enhanced_speak "Wendy Carlos" "${BASH_REMATCH[1]}"
        fi
        
        sleep 0.5
    done
}

# Main menu
main_menu() {
    echo "🎭🎵 LLOOOOMM ENHANCED VOICE SYSTEM 🎵🎭"
    echo "======================================="
    echo "1. Interactive Voice Playground"
    echo "2. Musical Scene Performance"
    echo "3. Emoji Orchestra"
    echo "4. Diverse Voices Speaking"
    echo "5. Integrate with Python Script"
    echo "6. Character Theme Songs"
    echo "7. Test All Voices"
    echo ""
    read -p "Choose option (1-7): " choice
    
    case $choice in
        1) voice_playground ;;
        2) perform_musical_scene ;;
        3) emoji_orchestra ;;
        4) diverse_voices_speak ;;
        5) integrate_with_diverse_voices ;;
        6) 
            echo "🎵 Character Theme Songs:"
            for char in "${!CHARACTER_THEMES[@]}"; do
                echo "Playing $char's theme..."
                enhanced_speak "$char" "${CHARACTER_THEMES[$char]}"
                sleep 1
            done
            ;;
        7)
            echo "🎭 Testing all character voices:"
            for char in "${!CHARACTER_VOICES[@]}"; do
                enhanced_speak "$char" "Hello from $char! 🎵"
                sleep 0.5
            done
            ;;
        *) echo "Invalid choice" ;;
    esac
}

# Run main menu if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main_menu
fi 