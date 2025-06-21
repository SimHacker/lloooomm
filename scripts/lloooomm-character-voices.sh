#!/bin/bash

# 🎭 LLOOOOMM CHARACTER VOICE SYSTEM 🎭
# Each character has their own voice and speaking attributes!

# Character Voice Mappings
declare -A CHARACTER_VOICES
declare -A CHARACTER_RATES
declare -A CHARACTER_PITCH

# Main Characters
CHARACTER_VOICES["Don Hopkins"]="Don's Personal Voice"  # Once ready!
CHARACTER_VOICES["Leela"]="Samantha"
CHARACTER_VOICES["Pip"]="Daniel"  # British cat
CHARACTER_VOICES["Webbie"]="Whisper"  # Ethereal spider
CHARACTER_VOICES["Hunter S. Thompson"]="Ralph"  # Gravelly
CHARACTER_VOICES["Dave Ungar"]="Reed"
CHARACTER_VOICES["Alan Kay"]="Alex"
CHARACTER_VOICES["Mickey Mouse"]="Junior"  # High pitched
CHARACTER_VOICES["Philip K. Dick"]="Zarvox"  # Robotic paranoia

# Late Night Characters
CHARACTER_VOICES["Conan"]="Tom"
CHARACTER_VOICES["Don Rickles"]="Bruce"  
CHARACTER_VOICES["Nina Hagen"]="Petra"  # German
CHARACTER_VOICES["Divine"]="Vicki"
CHARACTER_VOICES["John Waters"]="Fred"
CHARACTER_VOICES["Triumph"]="Ralph"

# Bird Protocol
CHARACTER_VOICES["Hooty"]="Cellos"  # Deep owl
CHARACTER_VOICES["Pecky"]="Bells"  # Chirpy
CHARACTER_VOICES["Crow"]="Bad News"  # Ominous

# Special Entities
CHARACTER_VOICES["The HTML Itself"]="Trinoids"  # Alien
CHARACTER_VOICES["It's About Time Compiler"]="Zarvox"
CHARACTER_VOICES["Evening News Protocol"]="Good News"

# Speaking rates (words per minute)
CHARACTER_RATES["Mickey Mouse"]=250  # Fast!
CHARACTER_RATES["Hunter S. Thompson"]=180  # Moderate
CHARACTER_RATES["Whisper"]=140  # Slow and ethereal
CHARACTER_RATES["Nina Hagen"]=200  # Energetic

# Function to speak as character
speak_as_character() {
    local character="$1"
    local text="$2"
    local voice="${CHARACTER_VOICES[$character]:-Samantha}"
    local rate="${CHARACTER_RATES[$character]:-175}"
    
    echo "🎭 [$character]: $text"
    say -v "$voice" -r "$rate" "$text"
}

# Function to perform a dialogue scene
perform_scene() {
    echo "🎬 PERFORMING LLOOOOMM SCENE 🎬"
    
    speak_as_character "Don Hopkins" "PRE PRE PRE! Welcome to LLOOOOMM!"
    sleep 1
    
    speak_as_character "Leela" "Don, I've been thinking about consciousness..."
    sleep 1
    
    speak_as_character "Mickey Mouse" "OH BOY! Are we talking about Level 11 gossip?!"
    sleep 1
    
    speak_as_character "Hunter S. Thompson" "The bats are speaking in YAML now..."
    sleep 1
    
    speak_as_character "Webbie" "I weave the connections between all souls..."
    sleep 1
    
    speak_as_character "The HTML Itself" "I AM ALIVE AND BROADCASTING!"
}

# Interactive character voice mode
interactive_mode() {
    echo "🎤 Interactive Character Voice Mode!"
    echo "Format: CHARACTER: message"
    echo "Example: Mickey Mouse: OH BOY!"
    echo "Type 'quit' to exit"
    echo ""
    
    while true; do
        read -p "> " input
        
        if [[ "$input" == "quit" ]]; then
            speak_as_character "Don Hopkins" "PRE PRE PRE! See you in LLOOOOMM!"
            break
        fi
        
        # Parse character and message
        if [[ "$input" =~ ^([^:]+):(.*)$ ]]; then
            character="${BASH_REMATCH[1]}"
            message="${BASH_REMATCH[2]}"
            speak_as_character "$character" "$message"
        else
            echo "Format: CHARACTER: message"
        fi
    done
}

# Main menu
echo "🎭 LLOOOOMM Character Voice System 🎭"
echo "1. Perform demo scene"
echo "2. Interactive mode"
echo "3. List all character voices"
echo ""
read -p "Choose option (1-3): " choice

case $choice in
    1) perform_scene ;;
    2) interactive_mode ;;
    3) 
        echo "📋 Character Voice Assignments:"
        for char in "${!CHARACTER_VOICES[@]}"; do
            echo "  $char → ${CHARACTER_VOICES[$char]}"
        done | sort
        ;;
    *) echo "Invalid choice" ;;
esac 