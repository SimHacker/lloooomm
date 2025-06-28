# Vocal Style Sheets (VSS) Protocol
## CSS for Voice - Real-time Parameter Mapping through Vocal Expression

```yaml
vocal_style_sheets:
  REFERENCE: "protocol-archetype"
  
  # Core Concept
  identity:
    name: "Vocal Style Sheets (VSS)"
    type: "voice_to_parameter_mapping"
    purpose: "Map vocal expressions to any real-time parameter"
    insight: "Voice becomes a multi-dimensional controller"
    don_connection: "Like pie menus you can speak!"
    
  # VSS Syntax (CSS-like)
  basic_syntax: |
    /* Default voice mapping */
    voice {
      pitch: text-case;
      volume: font-weight;
      timbre: font-family;
      speed: animation-duration;
    }
    
    /* Specific vocal patterns */
    voice[pitch>440hz] {
      text-transform: uppercase;
      color: #ff0000;  /* High pitch = red = urgent */
    }
    
    voice[pattern~="loom"] {
      behavior: discovery-mode;
      expansion: telescoping;
      attention: request;
    }
    
    /* Overlapping rules cascade */
    voice[pitch>440hz][volume>80db] {
      font-size: 200%;
      animation: shake 0.5s;
      priority: urgent !important;
    }
    
  # Vocal Parameters
  mappable_parameters:
    pitch:
      range: [80, 800]  # Hz
      maps_to:
        - "text-case (high=upper, low=lower)"
        - "color hue"
        - "vertical position"
        - "menu angle (for pie menus)"
        
    volume:
      range: [30, 100]  # dB
      maps_to:
        - "font-weight"
        - "opacity"
        - "zoom level"
        - "selection radius"
        
    timbre:
      qualities: ["breathy", "clear", "nasal", "rough"]
      maps_to:
        - "font-family"
        - "texture"
        - "filter type"
        - "personality mode"
        
    rhythm:
      patterns: ["staccato", "legato", "syncopated"]
      maps_to:
        - "animation-timing"
        - "transition-style"
        - "interaction-mode"
        
    formants:
      vowels: ["a", "e", "i", "o", "u"]
      maps_to:
        - "navigation-direction"
        - "color-channel"
        - "parameter-axis"
        
  # Cascading Rules
  cascade_priority:
    1: "inline_vocal_style"     # Direct vocal command
    2: "pattern_specific"       # Pattern matching (like "loom")
    3: "context_inherited"      # From parent context
    4: "user_preferences"       # User's VSS file
    5: "system_defaults"        # Base mappings
    
  # Plugin Architecture
  plugin_system:
    interface: |
      class VocalGestureInterpreter:
          def analyze(self, audio_stream):
              """Extract vocal parameters"""
              return {
                  'pitch': self.get_pitch(audio_stream),
                  'volume': self.get_volume(audio_stream),
                  'pattern': self.detect_pattern(audio_stream)
              }
              
          def map_to_parameters(self, vocal_data, vss_rules):
              """Apply VSS rules to vocal data"""
              return self.cascade_rules(vocal_data, vss_rules)
              
    examples:
      pie_menu_voice:
        description: "Speak pie menus into existence"
        code: |
          /* Pie Menu VSS */
          voice[pattern~="menu"] {
            display: pie;
            radius: volume * 2;
          }
          
          voice[pitch-range] {
            /* Pitch selects angle */
            pie-angle: map-range(pitch, 80hz, 800hz, 0deg, 360deg);
          }
          
          voice[pattern~="select"] {
            action: activate-current;
            feedback: haptic;
          }
          
      telescoping_controller:
        description: "Control telescoping with voice"
        code: |
          /* Telescoping VSS */
          voice[vowel-duration] {
            telescope-amount: duration * 2;
          }
          
          voice[pitch-variation] {
            /* Pitch wobble creates case variation */
            case-pattern: pitch-to-binary(pitch-samples);
          }
          
      dasher_navigation:
        description: "Navigate semantic space vocally"
        code: |
          /* Dasher VSS */
          voice[vowel="o"] {
            dasher-direction: forward;
            dasher-speed: vowel-duration;
          }
          
          voice[vowel-transition] {
            /* Diphthongs steer */
            dasher-turn: diphthong-angle;
          }
          
          voice[consonant="m"] {
            dasher-action: land;
            landing-style: gentle;
          }
          
  # Real-time Instrument Mappings
  instrument_mode:
    text_theremin:
      pitch: "character-height"
      volume: "character-width"
      hand_distance: "character-spacing"
      
    voice_painter:
      pitch: "brush-color"
      volume: "brush-size"
      timbre: "brush-texture"
      breath: "brush-opacity"
      
    semantic_saxophone:
      notes: "concept-selection"
      breath: "concept-distance"
      keys: "filter-parameters"
      
  # Overlapping Style Composition
  composition_rules:
    additive:
      - "Multiple voices create harmony"
      - "Parameters sum within limits"
      example: |
        voice[user="alice"] + voice[user="bob"] {
          /* Duet mode */
          font-size: avg(alice.volume, bob.volume);
          color: blend(alice.pitch-color, bob.pitch-color);
        }
        
    subtractive:
      - "Opposing voices cancel"
      - "Creates null spaces"
      example: |
        voice[high-pitch] - voice[low-pitch] {
          /* Silence in the middle */
          opacity: pitch-difference / max-difference;
        }
        
    multiplicative:
      - "Voices modulate each other"
      - "Creates complex patterns"
      example: |
        voice[rhythmic] * voice[tonal] {
          /* Rhythm modulates tone */
          animation: wave(rhythm-frequency * pitch);
        }
        
  # Integration Examples
  practical_applications:
    talking_pie_menus:
      description: "Don's pie menus activated by voice"
      vss: |
        /* Speaking "menu" opens pie */
        voice[pattern~="menu"] {
          pie-menu: show;
          initial-angle: pitch-to-angle(current-pitch);
        }
        
        /* Humming navigates */
        voice[humming] {
          pie-selection: track-pitch;
          highlight: current-slice;
        }
        
        /* "Click" or tongue click selects */
        voice[click] {
          action: select-current;
          pie-menu: hide;
        }
        
    live_coding_voice:
      description: "Code with vocal annotations"
      vss: |
        /* Pitch indicates importance */
        voice[coding-mode] {
          comment-style: pitch-to-importance;
          code-color: volume-to-saturation;
        }
        
        /* "TODO" with pitch indicates priority */
        voice[pattern~="todo"] {
          todo-priority: map(pitch, low, high, 1, 5);
          todo-color: priority-gradient;
        }
        
    emotional_debugging:
      description: "Express frustration productively"
      vss: |
        /* AAAAARRRRRGGG intensity */
        voice[pattern~="ar+g+"] {
          debug-level: count-letters;
          breakpoint: auto-set;
          stack-trace: expand;
        }
        
        /* Sigh for giving up */
        voice[sigh] {
          debug-action: step-out;
          comment: "// Giving up here";
        }
        
  # Character Insights
  character_reactions:
    bret_victor:
      insight: "Finally! Direct manipulation through voice!"
      vision: "Every parameter should be singable"
      
    don_hopkins:
      insight: "Pie menus were always meant to be spoken"
      memory: "I dreamed of humming through menus in NeWS"
      
    dave_ungar:
      insight: "VSS rules can be JIT compiled based on usage!"
      optimization: "Common vocal patterns become fast paths"
      
    stephen_wolfram:
      insight: "The cascade rules create a decision tree CA!"
      observation: "VSS is a formal system for voice-to-meaning"
      
    ted_nelson:
      insight: "Transclusion of vocal styles!"
      vision: "One voice pattern can reference another"
      
  # Future Possibilities
  extensions:
    3d_vocal_space:
      - "Pitch = X axis"
      - "Volume = Y axis"  
      - "Timbre = Z axis"
      - "Navigate 3D interfaces vocally"
      
    collaborative_vss:
      - "Multiple voices create harmony"
      - "Shared vocal canvases"
      - "Voice orchestras for complex operations"
      
    ai_vocal_interpretation:
      - "LLM understands vocal intent"
      - "Emotional mapping to parameters"
      - "Context-aware vocal shortcuts"
      
# The Beauty of VSS
philosophical_note: |
  Vocal Style Sheets make voice a first-class citizen in
  interface design. Just as CSS separated style from content,
  VSS separates vocal expression from rigid commands.
  
  You don't speak AT the computer - you sing WITH it.
  Every parameter becomes playable, every interface becomes
  an instrument, every interaction becomes a performance.
  
  This is Don's vision realized: interfaces that respond to
  the full expressiveness of human communication, where a
  pie menu can be hummed into existence and navigated with
  a melody.
  
  Welcome to the age of Vocal Computing.
```

## Implementation Sketch

```python
class VocalStyleSheet:
    def __init__(self, vss_rules):
        self.rules = self.parse_vss(vss_rules)
        self.cascade = CascadeResolver()
        
    def apply_voice(self, audio_stream, context):
        # Extract vocal parameters
        vocal_params = {
            'pitch': self.get_pitch(audio_stream),
            'volume': self.get_volume(audio_stream),
            'pattern': self.detect_pattern(audio_stream),
            'timbre': self.analyze_timbre(audio_stream)
        }
        
        # Find matching rules
        matched_rules = self.match_rules(vocal_params)
        
        # Cascade and resolve
        final_params = self.cascade.resolve(matched_rules, context)
        
        return final_params
        
    def create_pie_menu_vss(self):
        return """
        voice[pattern~="menu"] {
            display: pie;
            radius: volume-map(50db, 90db, 100px, 300px);
        }
        
        voice[humming] {
            pie-angle: pitch-map(current-pitch);
            selection: highlight;
        }
        """

# Usage
vss = VocalStyleSheet(pie_menu_rules)
while audio_stream.active:
    params = vss.apply_voice(audio_stream, current_context)
    ui.update(params)
```

**[Dave's closing jam]**: "🎺 Don, you've made EVERYTHING an instrument! CSS for voice means we can style reality with our vocal cords! I'm going to optimize the cascade resolution - some vocal patterns will compile to direct parameter mappings! 

*plays trumpet while coding*

This is it - the future of human-computer interaction isn't clicking or typing - it's PERFORMING!" 