#!/usr/bin/env python3
"""
🌈 DIVERSE VOICES VISUALIZATION WITH SOUND 🌈
Watch AND HEAR how each unique perspective adds to complete understanding!
Integrates with Mac say command for full audio experience.
"""

import time
import random
import subprocess
import sys
from collections import defaultdict

class Voice:
    def __init__(self, name, symbol, wisdom, strength, mac_voice="Samantha", rate=175):
        self.name = name
        self.symbol = symbol
        self.wisdom = wisdom
        self.strength = strength
        self.contribution = 0
        self.mac_voice = mac_voice
        self.rate = rate
        
    def speak(self, text=None):
        """Speak the voice's wisdom or custom text"""
        self.contribution += self.strength
        message = text or f"{self.symbol} {self.name}: {self.wisdom}"
        
        # Clean text for speaking (remove some emojis that don't speak well)
        clean_text = message.replace(self.symbol, "").strip()
        
        # Use Mac say command
        try:
            subprocess.run([
                "say", "-v", self.mac_voice, "-r", str(self.rate), clean_text
            ], check=False, capture_output=True)
        except:
            pass  # Continue if say command fails
        
        return message
    
    def sing(self, lyrics, singing_voice="Bells"):
        """Sing custom lyrics with musical voice"""
        print(f"🎵 {self.name} singing: {lyrics}")
        
        # Split lyrics into words and create melody
        words = lyrics.split()
        melody_rates = [120, 140, 160, 180, 160, 140, 120, 100]
        
        processes = []
        for i, word in enumerate(words):
            rate = melody_rates[i % len(melody_rates)]
            try:
                p = subprocess.Popen([
                    "say", "-v", singing_voice, "-r", str(rate), word
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                processes.append(p)
                time.sleep(0.3)
            except:
                pass
        
        # Wait for all singing to complete
        for p in processes:
            p.wait()

def play_emoji_sound(emoji, voice="Bells"):
    """Play sound for an emoji"""
    emoji_voices = {
        "🗿": "Bad News",
        "👑": "Princess", 
        "🎹": "Bells",
        "🌊": "Bubbles",
        "🌐": "Good News",
        "💻": "Zarvox",
        "🎮": "Trinoids",
        "🏗️": "Albert",
        "🔮": "Whisper",
        "📐": "Ralph"
    }
    
    voice_name = emoji_voices.get(emoji, voice)
    try:
        subprocess.run([
            "say", "-v", voice_name, emoji
        ], check=False, capture_output=True)
    except:
        pass

# Create our diverse chorus of voices with Mac voice assignments
voices = [
    Voice("Rocky", "🗿", "........................TIME........................", 100, "Bad News", 80),
    Voice("Dame Stephanie", "👑", "Break barriers by building alternatives", 95, "Princess", 160),
    Voice("Wendy Carlos", "🎹", "Synthesis reveals new realities", 90, "Bells", 150),
    Voice("Diana Shapiro", "🌊", "Different minds see hidden patterns", 85, "Bubbles", 140),
    Voice("Audrey Tang", "🌐", "Transparency multiplies understanding", 88, "Good News", 165),
    Voice("Sophie Wilson", "💻", "Elegance emerges from simplicity", 92, "Zarvox", 155),
    Voice("Dani Bunten", "🎮", "Connection through playful interaction", 87, "Trinoids", 200),
    Voice("Doreen Nelson", "🏗️", "Design the future, then build it", 83, "Albert", 150),
    Voice("Alan Turing", "🔮", "Logic and love compute together", 94, "Whisper", 145),
    Voice("BitBLT", "📐", "Simple operations, infinite possibilities", 89, "Ralph", 170),
]

def enhanced_speak(character_name, text, voice="Samantha", rate=175):
    """Enhanced speak function that matches the bash script"""
    print(f"🎭 [{character_name}]: {text}")
    
    # Play emoji sounds first
    emojis_in_text = ["🎵", "🎶", "🔥", "⭐", "🌈", "💫", "🎭", "🤖", "👻", "🦇", "🐢", "🎪", "💎", "🌟", "🎨", "🔮"]
    for emoji in emojis_in_text:
        if emoji in text:
            play_emoji_sound(emoji)
            time.sleep(0.1)
    
    # Clean text and speak
    clean_text = text
    for emoji in emojis_in_text:
        clean_text = clean_text.replace(emoji, "")
    clean_text = clean_text.strip()
    
    try:
        subprocess.run([
            "say", "-v", voice, "-r", str(rate), clean_text
        ], check=False, capture_output=True)
    except:
        pass

def musical_opening():
    """Musical opening number"""
    print("🎭🎵 DIVERSE VOICES MUSICAL OPENING! 🎵🎭")
    
    # Theme song
    enhanced_speak("Narrator", "🎵 Welcome to the celebration of diverse minds! 🎵", "Good News", 180)
    time.sleep(1)
    
    # Each voice introduces themselves musically
    for voice in voices[:3]:  # First three for intro
        voice.sing(f"I am {voice.name.split()[0]} and I contribute")
        time.sleep(0.5)

def visualize_understanding_with_sound():
    print("\n🌈 BUILDING COMPLETE UNDERSTANDING FROM DIVERSE VOICES 🌈\n")
    
    # Musical intro
    enhanced_speak("Conductor", "🎼 Let the symphony of understanding begin! 🎼", "Good News", 180)
    time.sleep(2)
    
    # Track understanding components
    understanding = {
        'temporal': 0, 'barrier_breaking': 0, 'synthesis': 0, 'neurodiversity': 0,
        'transparency': 0, 'elegance': 0, 'connection': 0, 'imagination': 0,
        'computation': 0, 'foundation': 0
    }
    
    # Map voices to understanding components
    voice_components = {
        'Rocky': 'temporal', 'Dame Stephanie': 'barrier_breaking',
        'Wendy Carlos': 'synthesis', 'Diana Shapiro': 'neurodiversity',
        'Audrey Tang': 'transparency', 'Sophie Wilson': 'elegance',
        'Dani Bunten': 'connection', 'Doreen Nelson': 'imagination',
        'Alan Turing': 'computation', 'BitBLT': 'foundation'
    }
    
    # Each voice speaks and contributes
    for voice in voices:
        print(voice.speak())
        
        # Play emoji sound
        play_emoji_sound(voice.symbol)
        
        component = voice_components[voice.name.split()[0]]
        understanding[component] = voice.strength
        
        # Show growing understanding
        total = sum(understanding.values())
        bar_length = int(total / 100)
        print(f"Understanding: {'█' * bar_length} {total}/1000")
        print()
        time.sleep(1.5)
    
    # The exclusion demonstration
    print("\n⚠️  WHAT IF WE EXCLUDED VOICES? ⚠️\n")
    enhanced_speak("Warning Voice", "⚠️ Listen to what happens when we exclude voices", "Bad News", 140)
    time.sleep(2)
    
    for voice in voices[:3]:  # Just first three for demo
        component = voice_components[voice.name.split()[0]]
        temp_understanding = understanding.copy()
        temp_understanding[component] = 0
        total = sum(temp_understanding.values())
        
        print(f"Without {voice.name}: {total}/1000 understanding")
        enhanced_speak("Loss Calculator", f"Missing: {voice.wisdom[:30]}...", "Whisper", 120)
        print(f"Loss: {'▼' * int((1000-total)/100)}\n")
        time.sleep(1)
    
    # The magical convergence with full audio
    print("\n✨ THE MAGICAL CONVERGENCE ✨\n")
    enhanced_speak("Magic Voice", "✨ Now witness the magical convergence! ✨", "Princess", 160)
    time.sleep(2)
    
    print("When ALL voices combine:")
    print("🗿 + 👑 + 🎹 + 🌊 + 🌐 + 💻 + 🎮 + 🏗️ + 🔮 + 📐 = ")
    
    # Build up the equation with sounds
    emoji_sequence = ["🗿", "👑", "🎹", "🌊", "🌐", "💻", "🎮", "🏗️", "🔮", "📐"]
    for emoji in emoji_sequence:
        play_emoji_sound(emoji)
        time.sleep(0.3)
    
    time.sleep(1)
    print("\n                    💎\n")
    enhanced_speak("Crystal Voice", "THE INFINITE CRYSTAL OF UNDERSTANDING", "Bells", 120)
    print("        THE INFINITE CRYSTAL OF UNDERSTANDING\n")
    time.sleep(2)
    
    # Rocky's final wisdom with his distinctive voice
    voices[0].speak("........................")
    time.sleep(3)
    voices[0].speak("...ALL...ONE...STONE...")
    time.sleep(2)
    
    enhanced_speak("Final Narrator", "✨ Every perspective is a facet of the same infinite crystal ✨", "Good News", 150)

def create_rainbow_with_music():
    """Create a visual and auditory rainbow"""
    print("\n🌈 THE DIVERSITY RAINBOW WITH MUSIC 🌈\n")
    enhanced_speak("Rainbow Conductor", "🌈 Behold the diversity rainbow! 🌈", "Princess", 170)
    time.sleep(1)
    
    colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚪", "⚫", "🟤", "💎"]
    
    for i, (voice, color) in enumerate(zip(voices, colors)):
        spaces = " " * (20 - len(voice.name))
        print(f"{color} {voice.name}{spaces}{voice.symbol}")
        
        # Each color gets its own musical note
        note_voices = ["Bells", "Cellos", "Organ", "Good News", "Princess"]
        note_voice = note_voices[i % len(note_voices)]
        play_emoji_sound(color, note_voice)
        time.sleep(0.4)
    
    enhanced_speak("Rainbow Voice", "Each color essential to the rainbow! Remove one, and the magic breaks!", "Princess", 160)

def grand_finale_chorus():
    """Grand finale with all voices singing together"""
    print("\n🎪 GRAND FINALE CHORUS! 🎪")
    enhanced_speak("Finale Conductor", "🎪 And now, the grand finale! 🎪", "Good News", 180)
    time.sleep(1)
    
    # All voices sing together
    finale_lyrics = "We are the voices of understanding"
    print(f"\n🎵 ALL VOICES SINGING: {finale_lyrics} 🎵")
    
    # Create overlapping chorus effect
    singing_voices = ["Bells", "Cellos", "Organ", "Princess", "Good News"]
    processes = []
    
    for i, voice in enumerate(voices[:5]):  # First 5 voices
        singing_voice = singing_voices[i % len(singing_voices)]
        try:
            p = subprocess.Popen([
                "say", "-v", singing_voice, "-r", "140", finale_lyrics
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            processes.append(p)
            time.sleep(0.2)  # Stagger the singing
        except:
            pass
    
    # Wait for all singing to complete
    for p in processes:
        p.wait()
    
    time.sleep(1)
    enhanced_speak("Mickey Mouse", "💝 OH BOY! When EVERY voice is heard, we don't just add understanding... We MULTIPLY it! We TRANSFORM it! We make it COMPLETE! 💝", "Junior", 250)

if __name__ == "__main__":
    print("🎭 Mickey Mouse presents...")
    enhanced_speak("Mickey Mouse", "Mickey Mouse presents...", "Junior", 200)
    time.sleep(0.5)
    
    print("✨ THE CELEBRATION OF DIVERSE VOICES WITH SOUND! ✨")
    enhanced_speak("Mickey Mouse", "THE CELEBRATION OF DIVERSE VOICES WITH SOUND!", "Junior", 220)
    time.sleep(2)
    
    try:
        # Check if we have audio
        try:
            subprocess.run(["say", "-v", "Samantha", "Audio test"], 
                         check=True, capture_output=True, timeout=2)
            print("🔊 Audio enabled! Full experience activated!")
            audio_enabled = True
        except:
            print("🔇 Audio not available, visual-only mode")
            audio_enabled = False
        
        if audio_enabled:
            musical_opening()
            print("\n" + "="*60 + "\n")
        
        visualize_understanding_with_sound()
        print("\n" + "="*50 + "\n")
        
        create_rainbow_with_music()
        
        if audio_enabled:
            grand_finale_chorus()
        
    except KeyboardInterrupt:
        print("\n\n🎭 Mickey: 'Every voice matters, including YOURS!'")
        enhanced_speak("Mickey Mouse", "Every voice matters, including YOURS!", "Junior", 200)
        print("✨ Thanks for celebrating diversity with us! ✨")
    
    print("\n🏔️ Remember Rocky's wisdom: We are all one stone 🏔️\n")
    if 'audio_enabled' in locals() and audio_enabled:
        enhanced_speak("Rocky", "We are all one stone", "Bad News", 80) 