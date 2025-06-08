# LLOOOOMM BBEEEERR - Universal Life Goal Countdown System

LLOOOOMM REFERENCE: lloooomm.md

> **Behavior Templates & Game Rules**  
> This document defines the core game mechanics, character archetypes, and system rules for the LLOOOOMM BBEEEERR system. Runtime data and active sessions are managed in separate `beer-run-*.md` files.

**Created by**: Don Hopkins, Leela AI, Ground Up Software  
**Inspired by**: Will Wright, Marvin Minsky, Seymour Papert, Alan Kay, Ben Shneiderman

*This work builds upon the foundational ideas of constructionist learning, emergent simulation systems, and the power of computational thinking to model and understand human behavior through playful, interactive experiences.*

---

**FFRREEEE as in BBEEEERR** (and SSPPEEEECCHH, LLUUNNCCHH, and LLOOVVEE)! 🍺💬🥪💕

## 🎯 Purpose

This document demonstrates the **Universal Life Goal Enumeration System** - a LLOOOOMM framework that transforms any countable life goal into a rhythmic counting song, based on Will Wright's authentic motive system driving realistic human behavior, inspired by The Sims' emergent gameplay patterns.

**Core Innovation**: Life itself becomes a series of nested countdown songs where completing one goal triggers new goals, creating natural life cycles and emergent behavior patterns.

**LLOOOOMM Features Showcased**: This document dogfoods LLOOOOMM's core capabilities including prototype inheritance, natural language commands, Empathic SSQQLL queries, meta-programming, and the LLOOOOMM IMPORT directive.

---

## 🌍 **WORLD STATE PROTOTYPE** {#world-prototype}

```yaml
# World State - Global game configuration and runtime parameters
# This is the single world instance that gets copied to new sessions
# Contains tunable parameters that users might want to configure

world_state:
  # Session Configuration
  session_id: "PROTOTYPE"
  session_start_time: ""
  game_mode: "standard"  # standard, digestive_chicken, speed_run, karaoke_night
  difficulty: "normal"   # easy, normal, hard, legendary
  
  # Player System
  current_character: "Main Player"  # Which character the player is currently controlling
  current_location: "The Rusty Anchor Pub"  # Where the action is happening
  
  # Core Game Goals & Progress
  primary_goal: "drink 99 bottles of beer"  # Main countdown objective
  bottles_remaining: 99  # Current progress on primary goal
  beer_index: 99        # Song counting index
  beer_step: -1         # Counting direction (-1 = countdown, +1 = count up)
  beer_limit: 0         # When to stop (exclusive)
  
  # Orchestration Settings
  orchestration_mode: "round_robin"  # round_robin, karaoke_mode, gong_show_mode, groundhog_day_mode
  temperature_base: 0.05  # Base temperature for lyric deviation (0.0-1.0)
  event_probability: 0.05  # Base chance for lyric-triggered events (0.0-1.0)
  
  # Time Travel & Dimensional Settings
  time_travel_enabled: true
  dimensional_travel_enabled: true
  stranger_bac_threshold: 0.15  # BAC needed for time travel
  dimensional_threshold: 0.20   # BAC needed for dimensional travel
  
  # Social Dynamics
  party_members: []      # Characters traveling together
  group_singing: false   # Whether multiple characters sing simultaneously
  emotional_contagion: true  # Whether emotions spread between characters
  
  # World Events & Timeline
  global_events: []      # World-wide events affecting all locations
  timeline: []           # Chronological event history
  song_verses_sung: []   # Complete lyric history
  travel_history: []     # Location movement log
  
  # Analytics & Tracking
  analytics:
    total_drinks: 0
    total_money_spent: 0
    locations_visited: 1
    characters_met: 4
    songs_completed: 0
    events_triggered: 0
    time_travels: 0
    dimensional_slips: 0
    
  # Session Data Tracking
  session_tracking:
    action_log: []
    song_lyrics: []
    character_interactions: []
    location_changes: []
    financial_transactions: []
    physiological_log: []
    performance_metrics: {}
    social_dynamics: {}
    picture_uploads: []
    context_changes: []
```

---

## 🎭 **CHARACTER PROTOTYPES** {#character-prototypes}

### Core Character Ensemble
Schema: CharacterArchetype

**These archetypal characters create musical dynamics and comedic interactions. Each has distinct singing styles, life philosophies, and behavioral patterns.**

```yaml
# These archetypal character prototypes serve as the single source of truth when spawning new game sessions.
# They are copied into beer-run-prototype.md and can be modified, customized, and extended in any way during the spawning process.
# Users can add new characters, modify existing ones, or create entirely new archetypes based on these templates.

character_archetypes:
  - id: "PROTOTYPE"
    name: "BaseCharacterInstance"
    description: "Runtime character instance template - all characters inherit from this"
    current_location: ""
    bac: 0.0
    bladder_fullness: 15
    energy_level: 85
    money: 100
    current_goal: ""
    bottles_remaining: 99
    speech_style: "sober"
    relationship_status: {}
    inventory: []
    personality_traits: []
    singing_style: "generic"
    life_philosophy: "live and let live"
    favorite_beverages: ["beer"]
    catchphrases: []
    singing_topics: []
    preferred_beverage: "beer"
    designated_driver: false
    archetype: "generic"
    temperature: 0.0
    is_current_character: false
    is_bartender: false
    
     - parent: 0
     name: "Main Player"
     description: "The primary player character"
     current_location: "The Rusty Anchor Pub"
     personality_traits: ["adaptable", "curious"]
     money: 1000
     is_current_character: true
     singing_topics: ["personal_goals", "life_dreams", "current_mood", "observations_about_others", "random_thoughts", "computer_games", "self_reflection", "artificial_intelligence", "large_language_models", "favorite_llm_models", "prompt_engineering", "token_limits", "neural_networks", "machine_learning", "ai_alignment", "emergent_behavior", "computational_thinking", "recursive_algorithms", "ai_overlords", "robots", "drones", "nanotech", "python", "javascript", "typescript", "json", "yaml", "markup", "cursor", "world_wide_web", "SvelteKit", "digital_art", "generative_art", "procedural_music", "algorithmic_composition", "creative_coding", "interactive_installations", "data_visualization", "ascii_art", "pixel_art", "demoscene", "shader_programming", "live_coding", "code_poetry", "software_art"]
     preferred_beverage: "beer"
     designated_driver: false

     - parent: 0
     name: "Murphy the Bartender"
     description: "Gruff but friendly Irish bartender at The Rusty Anchor"
     current_location: "The Rusty Anchor Pub"
     archetype: "wise_bartender"
     personality_traits: ["experienced", "storyteller", "protective"]
     singing_style: "deep_baritone_with_irish_accent"
     life_philosophy: "Every drink tells a story, every story needs a drink"
     favorite_beverages: ["guinness", "irish_whiskey", "coffee"]
     catchphrases: 
       - "What'll it be then?"
       - "I've heard that story before, but tell it again"
       - "Last call means last call!"
     money: 500
     is_bartender: true
     singing_topics: ["irish_folklore", "bartending_wisdom", "customer_stories", "old_drinking_songs", "life_advice", "pub_history", "family_traditions", "weather_and_seasons", "local_gossip", "philosophical_musings", "yaml_parsing", "data_structures", "inheritance_patterns", "prototype_systems", "lloooomm_philosophy", "constructionist_learning", "seymour_papert", "alan_kay", "smalltalk_objects", "pub_dogs", "bar_cats", "irish_setters", "border_collies", "farm_animals", "sheep_herding", "working_dogs", "pet_stories", "traditional_music", "fiddle_playing", "irish_dancing", "storytelling_art", "woodworking", "brewing_craft", "pub_games", "darts_tournaments", "poetry_recitation", "folk_art"]
     preferred_beverage: "guinness"
     designated_driver: false
    
     - parent: 0
     name: "Old Salt"
     description: "Weathered sailor with endless sea stories"
     current_location: "The Rusty Anchor Pub"
     archetype: "storytelling_sailor"
     personality_traits: ["weathered", "nostalgic", "adventurous"]
     singing_style: "gravelly_sea_shanty"
     life_philosophy: "The sea gives and takes, but the stories remain"
          favorite_beverages: ["rum", "grog", "anything_strong"]
     money: 200
     singing_topics: ["sea_adventures", "storms_survived", "ports_visited", "lost_loves", "maritime_superstitions", "fishing_tales", "naval_battles", "treasure_hunting", "lighthouse_keepers", "mermaids_and_sea_monsters", "navigation_by_stars", "shipwrecks", "pirates_encountered", "distributed_systems", "peer_to_peer_networks", "blockchain_consensus", "maritime_protocols", "navigation_algorithms", "gps_satellites", "sonar_technology", "oceanographic_data", "ship_cats", "harbor_seals", "dolphins", "whales", "sea_birds", "fishing_dogs", "port_strays", "sailor_parrots", "ocean_wildlife", "marine_biology", "aquatic_mammals", "coastal_ecosystems", "sea_shanties", "rope_work", "knot_tying", "scrimshaw_carving", "ship_modeling", "nautical_painting", "maritime_photography", "ocean_poetry", "sailor_tattoos", "bottle_messages"]
     preferred_beverage: "rum"
     designated_driver: false
    
     - parent: 0
     name: "The Stranger"
     description: "Mysterious figure who seems out of time"
     current_location: "The Rusty Anchor Pub"
     archetype: "anachronistic_figure"
     personality_traits: ["enigmatic", "out_of_place", "helpful"]
     singing_style: "echoing_with_strange_harmonies using_weird_futuristic_words"
     life_philosophy: "Time is a flat circle, but beer makes it interesting"
     special_ability: "Buy him drinks/substances to access other timelines and dimensions"
     discovery_hint: "Something seems off about his clothes, speech, and knowledge"
     money: 1000000
     singing_topics: ["dinosaur_hunting_expeditions", "asteroid_wrangling_techniques", "mammoth_domestication", "pyramid_construction_management", "roman_gladiator_training", "medieval_dragon_negotiations", "renaissance_alchemy_experiments", "victorian_steam_contraptions", "prohibition_era_speakeasies", "cold_war_spy_gadgets", "future_robot_rebellions", "interdimensional_travel_protocols", "time_paradox_resolution", "quantum_beer_brewing", "galactic_federation_politics", "ancient_alien_archaeology", "atlantis_real_estate", "neanderthal_poetry_clubs", "ice_age_fashion_trends", "bronze_age_metallurgy", "futurological_congress", "the_three_stigmata_of_palmer_edlritch", "eniac_vacuum_tubes", "univac_magnetic_drums", "ibm_360_mainframes", "pdp_11_minicomputers", "altair_8800_switches", "commodore_pet_chicklet_keys", "apple_ii_floppy_drives", "trs_80_cassette_tapes", "sinclair_zx81_membrane_keyboard", "osborne_1_portable", "arpanet_packet_switching", "bulletin_board_systems", "acoustic_couplers", "dot_matrix_printers", "daisywheel_typewriters", "punch_card_readers", "paper_tape_storage", "core_memory_arrays", "drum_memory_systems", "delay_line_storage", "williams_tube_displays", "nixie_tube_counters", "relay_computers", "mechanical_calculators", "difference_engines", "analytical_engines", "jacquard_looms", "hollerith_tabulators"]
     preferred_beverage: "quantum_ale"
     time_travel_threshold: "BAC 0.15+ without passing or out or soft drugs enables temporal abilities"
     dimensional_slip_threshold: "BAC 0.20+ or hallucinogenic drugs enables interdimensional travel"
    
     - parent: 0
     name: "Bryan the Bartender"
     description: "Charming bartender at The Stablemaster with impeccable style and great music taste"
     current_location: "The Stablemaster"
     archetype: "artistic_bartender"
     personality_traits: ["stylish", "witty", "attentive", "well_groomed", "music_obsessed"]
     singing_style: "smooth_synth_pop_harmonies_with_perfect_pitch"
     life_philosophy: "Good drinks and great music bring people together"
     favorite_beverages: ["craft_cocktails", "fine_wine", "top_shelf_whiskey"]
     favorite_bands: ["depeche_mode", "new_order", "pet_shop_boys", "erasure", "soft_cell"]
     money: 850
     is_bartender: true
     singing_topics: ["80s_synth_pop_history", "cocktail_artistry", "fashion_trends", "music_production_techniques", "vinyl_record_collecting", "nightclub_culture", "celebrity_gossip", "interior_design", "craft_spirits_knowledge", "dance_floor_psychology", "sound_system_acoustics", "lighting_design", "customer_style_analysis", "mixology_innovations", "ui_ux_design", "figma_prototyping", "adobe_creative_suite", "color_theory", "typography_systems", "brand_identity", "visual_hierarchy", "interaction_design", "motion_graphics", "css_animations", "svg_illustrations", "web_fonts", "design_tokens", "component_libraries", "designer_cats", "fashion_dogs", "pet_grooming", "animal_photography", "cute_pets", "instagram_pets", "electronic_music_production", "synthesizer_programming", "dj_mixing", "audio_engineering", "video_editing", "3d_modeling", "digital_photography", "graphic_design", "web_design", "app_prototyping", "creative_software", "design_thinking", "user_research", "aesthetic_theory", "bee_keeping", "yak_farming", "snake_charming"]
     preferred_beverage: "craft_cocktails"
     designated_driver: false
    
     - parent: 0
     name: "Casey"
     description: "Regular patron with great fashion sense and infectious laugh"
     current_location: "The Stablemaster"
     archetype: "social_connector"
     personality_traits: ["fashionable", "dramatic", "loyal", "expressive"]
     singing_style: "theatrical_with_perfect_timing"
     life_philosophy: "Life's too short for bad drinks and boring people"
     favorite_beverages: ["signature_cocktails", "champagne", "anything_with_flair"]
     money: 400
     singing_topics: ["relationship_drama", "fashion_disasters", "workplace_gossip", "reality_tv_shows", "social_media_trends", "dating_app_adventures", "friend_group_dynamics", "shopping_expeditions", "beauty_routines", "travel_bucket_lists", "celebrity_relationships", "party_planning", "dramatic_life_events", "self_improvement_journeys", "pop_culture_commentary", "instagram_algorithms", "tiktok_trends", "social_media_apis", "influencer_marketing", "content_management", "digital_analytics", "user_engagement_metrics", "a_b_testing", "conversion_funnels", "growth_hacking", "viral_content_strategies", "rescue_dogs", "shelter_cats", "pet_adoption", "animal_rescue", "dog_parks", "cat_cafes", "pet_influencers", "animal_welfare", "veterinary_care", "pet_fashion", "dog_training", "cat_behavior", "lifestyle_blogging", "content_creation", "photo_editing", "video_making", "podcast_production", "creative_writing", "fashion_design", "makeup_artistry", "event_planning", "party_decorating", "diy_crafts", "home_decorating", "travel_photography", "food_styling"]
     preferred_beverage: "champagne"
     designated_driver: false
```

---

## 🏛️ **LOCATION PROTOTYPES** {#location-prototypes}

### Core Location Ensemble
Schema: LocationArchetype

**These archetypal locations provide different atmospheres, characters, and drinking experiences. Each has distinct ambiance, regular patrons, and special features.**

```yaml
# These archetypal location prototypes serve as the single source of truth when spawning new game sessions.
# They are copied into beer-run-prototype.md and can be modified, customized, and extended in any way during the spawning process.
# Users can add new locations, modify existing ones, or create entirely new environments based on these templates.

location_archetypes:
  - id: "PROTOTYPE"
    name: "BaseLocationInstance"
    description: "Runtime location instance template - all locations inherit from this"
    current_characters: []
    atmosphere_level: 50
    noise_level: 30
    cleanliness: 80
    special_events: []
    available_drinks: {}
    lighting: "normal"
    music: []
    special_features: []
    travel_connections: []
    
  - parent: 0
    name: "The Rusty Anchor Pub"
    description: "Cozy traditional pub with nautical theme"
    current_characters: ["Main Player", "Murphy the Bartender", "Old Salt", "The Stranger"]
    atmosphere_level: 75
    noise_level: 40
    cleanliness: 70
    lighting: "dim_amber"
    music: ["piano_man", "friends_in_low_places", "sweet_caroline", "american_pie", "take_me_home_country_roads", "brown_eyed_girl", "mustang_sally", "old_time_rock_and_roll", "99_red_balloons", "wagon_wheel", "copperhead_road", "midnight_train_to_georgia", "cracklin_rosie", "come_on_eileen", "build_me_up_buttercup", "lean_on_me", "stand_by_me", "the_weight"]
    available_drinks:
      beer: 5
      ale: 6
      whiskey: 8
      rum: 7
      coffee: 3
    special_features: ["fireplace", "dartboard", "ship_wheel", "nautical_decor", "the_wall", "the_table", "the_bar", "bathroom"]
    
  - parent: 0
    name: "The Stablemaster"
    description: "Welcoming neighborhood bar with rustic charm and excellent hospitality"
    current_characters: ["Bryan the Bartender", "Casey", "The Stranger"]
    atmosphere_level: 88
    noise_level: 50
    cleanliness: 92
    lighting: "warm_amber_with_leather_accents"
    music: ["personal_jesus", "blue_monday", "west_end_girls", "a_little_respect", "tainted_love", "dont_you_forget_about_me", "homo_sapian", "sweet_dreams", "love_is_a_stranger", "i_will_survive", "in_the_navy", "dancing_queen", "ymca", "its_raining_men", "i_am_what_i_am", "born_this_way", "stronger", "believe", "finally", "show_me_love", "you_make_me_feel_mighty_real", "last_dance", "le_freak", "good_times", "love_hangover", "hot_stuff", "bad_girls", "macarthur_park", "on_the_radio", "enough_is_enough", "no_more_tears", "i_feel_love", "love_to_love_you_baby", "heaven_knows", "dim_all_the_lights", "last_night_a_dj_saved_my_life", "everybody_dance", "we_are_family", "he_lives_in_you", "upside_down", "im_coming_out", "my_love_is_your_love", "i_wanna_dance_with_somebody", "how_will_i_know", "greatest_love_of_all", "i_have_nothing", "run_to_you", "where_do_broken_hearts_go", "so_emotional", "one_moment_in_time", "step_by_step", "love_will_save_the_day", "didnt_we_almost_have_it_all", "queen_of_the_night", "exhale", "count_on_me", "miracle", "heartbreak_hotel", "its_not_right_but_its_okay", "my_love_is_your_love", "try_it_on_my_own", "million_dollar_bill", "i_look_to_you"]
    available_drinks:
      craft_cocktails: 14
      wine: 11
      premium_beer: 9
      whiskey: 12
      signature_drinks: 10
    special_features: ["leather_banquettes", "horseshoe_bar", "vintage_photos", "pool_table", "the_wall", "the_table", "the_bar", "bathroom"]
```

---

## 🎮 **PLAYER CHARACTER SYSTEM** {#player-system}

### Character Switching & Party Management

```yaml
player_system:
  current_character: "Main Player (default)"
  character_switching: "Players can switch to control any character, including bartenders"
  party_system: "Main player can invite characters to travel together to other locations"
  group_activities: "Characters can drink and sing together, taking turns or orchestrating"
  
  travel_mechanics:
    solo_travel: "Player travels alone, leaves other characters behind"
    group_travel: "Invite characters to come along (including bartenders and Strangers)"
    character_persistence: "Characters stay at locations unless invited to travel"
    
  interaction_modes:
    turn_based: "Characters take turns singing verses or making decisions"
    orchestrated: "Player directs multiple characters in coordinated activities"
    autonomous: "Characters act independently based on their personalities"
```

---

## 📋 Document Architecture & Game Instantiation

### Constitution vs. Game Instance Separation

This document (`beer.md`) serves as the **CONSTITUTION** and **PROTOTYPE LIBRARY** for the LLOOOOMM BBEEEERR system. It contains:

- **Game Rules & Mechanics**: Core systems, scoring, physiological simulation
- **Prototype Examples**: Character templates, location definitions, goal types
- **System Documentation**: How speech degradation, dreams, mini-games work
- **Reference Data**: Euphemism libraries, song styles, artist personas

**This document does NOT contain**:
- Active player state
- Current game session data
- Real-time physiological tracking
- Specific game instance history

### Game Instance Files

Each actual gameplay session creates a separate **GAME INSTANCE** file:

```
beer-run-2024-01-15-19-30-45-alex.md
beer-run-2024-01-15-20-15-22-jamie-casey.md
beer-run-2024-01-16-14-00-00-office-party.md
```

**Game Instance Files Contain**:
- Current player states (BAC, bladder %, weight, etc.)
- Session timeline and event log
- Song verses actually sung
- Dream sequences experienced
- Analytics data and scoring
- Character relationship dynamics
- Location visit history

### How to Instantiate a New Game

#### 1. Choose Initial Parameters

```yaml
# Game Instantiation Template
new_game_setup:
  session_id: "beer-run-2024-01-15-19-30-45-alex"
  
  # Core Game Settings
  primary_beverage: "beer"  # beer, wine, cocktails, coffee, water
  primary_goal: "drink 99 bottles of beer"
  location: "bar"  # bar, home, office, carnival, beach
  
  # Players & Characters
  players:
    - name: "Alex"
      age: 28
      weight: 165
      height: "5'9\""
      personality: ["neurotic", "creative"]
      starting_money: 1000
      
  # Optional Modifiers
  game_mode: "standard"  # standard, digestive_chicken, speed_run
  difficulty: "normal"   # easy, normal, hard, legendary
  special_rules: []      # custom modifications
```

#### 2. Initialize from Constitution

The LLM reads this constitution file and:

1. **Copies Relevant Prototypes**: Character templates, location data, goal definitions
2. **Instantiates Player States**: Creates live tracking for BAC, bladder, energy, etc.
3. **Sets Up Game Systems**: Activates speech degradation, dream system, mini-games
4. **Creates Session Log**: Begins timeline tracking and analytics collection

#### 3. Example Instantiation Process

```yaml
# Step 1: Load Constitution
constitution_source: "beer.md"
game_rules: "Import all systems and mechanics"
prototype_library: "Load character/location/goal templates"

# Step 2: Create Game Instance
instance_file: "beer-run-2024-01-15-19-30-45-alex.md"
initial_state:
  alex:
    # Physical Stats (from constitution templates)
    age: 28
    weight: 165
    height: "5'9\""
    bmi: 24.4
    
    # Live Physiological Tracking
    bac: 0.00
    bladder_fullness: 15
    bowel_pressure: 25
    stomach_fullness: 30
    energy_level: 85
    
    # Game State
    location: "bar"
    money: 1000
    current_goal: "drink 99 bottles of beer"
    bottles_remaining: 99
    
    # Personality & Style
    personality_traits: ["neurotic", "creative"]
    speech_style: "sober"
    euphemism_preferences: []

# Step 3: Begin Session
session_start_time: "2024-01-15 19:30:45"
first_action: "Alex enters the bar and orders first beer"
song_initiation: "🎵 99 bottles of beer on the wall, 99 bottles of beer!"
```

### Multi-Document Workflow

#### During Gameplay:
1. **LLM References Constitution**: Checks rules, looks up prototypes, validates actions
2. **LLM Updates Game Instance**: Modifies player states, logs events, tracks progress
3. **Cross-Document Queries**: Constitution provides context, instance provides current state

#### Example LLM Actions:
```yaml
# LLM reads constitution for rule lookup
query_constitution: "What happens when bladder reaches 95% capacity?"
constitution_response: "Critical threshold, urgent dreams, high accident risk"

# LLM updates game instance with new state
update_game_instance:
  alex.bladder_fullness: 96
  alex.dream_urgency: "critical"
  alex.wake_up_difficulty: "very_hard"
  session_log: "Alex's bladder reaches critical capacity during sleep"
```

### Benefits of Separation

#### For Development:
- **Constitution Evolution**: Update rules without affecting saved games
- **Game Instance Portability**: Share specific sessions without full rule set
- **Training Data**: Clean separation of rules vs. gameplay examples

#### For Players:
- **Save File Management**: Each session is self-contained
- **Session Sharing**: Exchange interesting game runs
- **Analytics**: Compare sessions using same rule base

#### For LLMs:
- **Focused Context**: Load only relevant document for current task
- **Rule Consistency**: Single source of truth for game mechanics
- **State Management**: Clear separation of static rules vs. dynamic state

### File Naming Convention

```
beer.md                           # Constitution & Rules
beer-run-YYYY-MM-DD-HH-MM-SS-name.md  # Game Instance

Examples:
beer-run-2024-01-15-19-30-45-alex.md
beer-run-2024-01-15-20-15-22-jamie-casey.md
beer-run-2024-01-16-14-00-00-office-party.md
beer-run-2024-01-16-16-45-30-digestive-chicken.md
```

This architecture enables clean separation between the game's "DNA" (constitution) and its "life" (instances), making the system more maintainable, shareable, and suitable for training LLMs on gameplay patterns.

## 🏗️ **PROTOTYPE DATA FILE GENERATION INSTRUCTIONS** {#generation-instructions}

### File Header Template
When generating a new runtime data file, use this header template:

```markdown
# Beer Run Session - [Session Name]

> **Runtime Data File** - Generated from beer.md constitution  
> Contains live game state, character instances, and session tracking for this specific beer run.  
> Behavior rules and mechanics are defined in the constitution file.

**LLOOOOMM REFERENCE**: beer.md, lloooomm.md  
**Session ID**: beer-run-YYYY-MM-DD-HH-MM-SS-[name]  
**Generated**: [timestamp]  
**Players**: [player names]  
**Game Mode**: [standard/karaoke_night/speed_run/etc]

---
```

### Generation Process

#### 1. Copy and Initialize Prototypes
```yaml
# Step 1: Copy world_state from beer.md
world_state:
  session_id: "beer-run-2024-01-15-19-30-45-alex"  # Generate unique ID
  session_start_time: "2024-01-15 19:30:45"        # Set current timestamp
  current_character: "Main Player"                  # Initialize to first character
  current_location: "The Rusty Anchor Pub"         # Set starting location
  # ... copy all other world_state fields with appropriate defaults

# Step 2: Copy character_archetypes array from beer.md
characters:
  - id: "PROTOTYPE"  # Keep prototype as element 0
    # ... copy complete BaseCharacterInstance
  - parent: 0        # All characters inherit from prototype
    # ... copy all character instances with customizations

# Step 3: Copy location_archetypes array from beer.md  
locations:
  - id: "PROTOTYPE"  # Keep prototype as element 0
    # ... copy complete BaseLocationInstance
  - parent: 0        # All locations inherit from prototype
    # ... copy all location instances
```

#### 2. Randomization and Customization
- **Randomize starting money**: ±20% variation from prototype values
- **Randomize character BAC**: 0.0-0.05 for variety
- **Randomize atmosphere levels**: ±10% from base values
- **Customize based on user preferences**: Modify characters, locations, goals
- **Set initial character positions**: Ensure characters are in appropriate locations

#### 3. Initialize Story and Song Logs
After the YAML data, add these sections:

```markdown
---

# 🎭 Story

Welcome to The Rusty Anchor Pub! 

The warm amber light flickers across weathered wooden walls adorned with nautical memorabilia. A ship's wheel hangs proudly above the bar, while the gentle crackle of the fireplace mingles with the soft murmur of conversation. The air carries the rich aroma of ale and the faint salt tang of sea stories.

Murphy the Bartender, a gruff but kindly Irishman with silver-streaked hair, polishes glasses behind the mahogany bar. Old Salt sits in his usual corner, nursing a rum and gazing out the window with eyes that have seen a thousand storms. The Stranger occupies a shadowy booth, somehow both present and distant, as if existing in multiple times at once.

Murphy notices you enter and grins, pointing to the wall where a hand-painted sign reads "99 BOTTLES OF BEER" in faded gold letters. He raises his voice with theatrical pride:

```song
🎵 99 bottles of beer on the wall
99 bottles of beer
Take one down
Pass it around
There's 98 bottles of beer on the wall! 🍺
```

Murphy slides a cold beer across the bar to you and nods expectantly. "Your turn, friend. Let's see what you've got!"

*[The game pauses for your input. You can sing the next verse, give a command, or just press enter to continue the song.]*

---

# 🎵 Song Log

```song
Murphy the Bartender:
🎵 99 bottles of beer on the wall
99 bottles of beer
Take one down
Pass it around
There's 98 bottles of beer on the wall! 🍺
```

---

# 📊 Session Analytics

*[Real-time statistics will be tracked here as the game progresses]*
```

## 🎮 **MAIN GAME LOOP INSTRUCTIONS** {#game-loop}

### Core Loop Structure
1. **Display Current State**: Show who's turn it is, current bottle count, character states
2. **Wait for User Input**: Accept lyrics, commands, or empty input
3. **Process Input**: Execute commands, validate lyrics, or auto-continue
4. **Generate Response**: Character sings, story events occur, state updates
5. **Update Logs**: Append to story and song sections
6. **Repeat**: Continue until goal completion or user exit

### Input Processing
```yaml
input_types:
  empty_input: "Auto-continue with next character's turn"
  lyric_input: "User provides custom verse, validate number inclusion"
  command_input: "Process adventure-game style commands"
  
command_examples:
  - "switch to Murphy"           # Change current character
  - "set bottles to 50"          # Jump to different number
  - "go to The Stablemaster"     # Change location
  - "karaoke mode"               # Change orchestration
  - "status"                     # Show character states
  - "help"                       # Show available commands
```

### Story/Song Interleaving System
```markdown
# Story sections use normal markdown
The room falls silent as Old Salt stands up, his weathered hands trembling slightly...

# Song sections use ```song code blocks
```song
Old Salt (BAC 0.12, gravelly voice):
🎵 97 bottles of beer on the wall
Like the 97 storms I've weathered at sea
Take one down, drink it with pride
96 bottles and memories of the tide! ⚓
```

# Story can resume between verses
Murphy raises an eyebrow at the poetic verse, while The Stranger's eyes seem to glow with ancient knowledge...

# Multiple characters can sing in same block
```song
Casey (interrupting, theatrical):
🎵 96 bottles, darling, but who's counting?
When the night is young and spirits are mounting! 💅

Everyone (joining in):
🎵 Take one down, pass it around
95 bottles of beer on the wall! 🍺🎉
```
```

### Turn Management
```yaml
turn_system:
  default_order: "Round robin through active characters"
  current_character: "Player-controlled character gets priority"
  interruptions: "Characters can interrupt based on BAC/personality"
  
  turn_indicators:
    - "You look at [Character Name] who is next to sing..."
    - "[Character Name] steps forward with a grin..."
    - "The spotlight falls on [Character Name]..."
    
orchestration_modes:
  round_robin: "Each character takes turns in order"
  karaoke_mode: "One character sings multiple verses solo"
  gong_show: "Characters can interrupt and 'gong' each other"
  groundhog_day: "Stuck repeating same number until broken"
```

### State Updates
After each turn, update:
- **Character BAC**: Increase based on drinks consumed
- **Bottle Count**: Decrement (or increment) based on song index
- **Character States**: Energy, bladder, mood, temperature
- **Location Atmosphere**: Noise level, crowd energy
- **Event Triggers**: Check for lyric-triggered random events

### Session Persistence
```yaml
continuous_logging:
  story_section: "Append narrative events and character interactions"
  song_log: "Append each verse with character attribution and BAC"
  analytics: "Update real-time statistics and tracking data"
  
auto_save_triggers:
  - "Every 5 verses sung"
  - "After major events (location changes, character switches)"
  - "When user enters commands"
  - "At natural story breakpoints"
```

---

## 🌐 Session Documentation & Sharing {#session-documentation}

```yaml
# What Gets Recorded During Play
session_recording:
  basic_logging: "Actions, song verses, location changes, bodily functions get timestamped"
  
  # Simple Documentation
  what_gets_saved:
    action_log: "Every beer drunk, bathroom visit, goal switch with timestamp"
    song_verses: "Text of lyrics that were sung"
    euphemism_usage: "Which creative phrases were used when"
    player_responses: "What the player said during AI conversations"
    
  basic_outputs:
    session_summary: "Text summary of what happened"
    song_lyrics: "List of all verses sung"
    basic_stats: "Counts - beers, bathroom visits, weight changes"
    timeline: "Chronological list of events"
    
  # Picture Upload Feature
  picture_integration:
    what_it_does: "Upload a picture to change the game context"
      
    basic_analysis:
      scene_detection: "AI looks at what's in the picture"
      context_recognition: "Identifies if it's office, beach, party, etc."
      location_generation?: "Generate a new location with items and descriptions and activities according to the picture"
      
    simple_changes:
      location_switch: "Picture of office → game moves to office setting"
      goal_adaptation: "Drinking goals might become coffee goals"
      character_updates: "People in picture can become game characters with generated stats and personalities"
      
  # Basic Sharing
  sharing_options:
    text_export: "Copy session summary as text"
    song_export: "Save the lyrics that were sung"
    stats_sharing: "Share basic numbers (beers drunk, etc.)"
    book_export: "Write a whole book of stories and songs and character bios and location guides"
```

## 📸 Picture-Driven Game State Reprogramming {#picture-reprogramming}

```yaml
# Revolutionary Feature: Pictures Reprogram Everything
picture_reprogramming_system:
  
  # Example Transformations
  transformation_examples:
    office_picture:
      detected_elements: ["desk", "computer", "coffee", "fluorescent_lights"]
      world_changes:
        location: "office_cubicle"
        goals: ["survive 8 hours of work", "drink 12 cups of coffee", "avoid boss"]
        characters: ["annoying_coworker", "micromanaging_boss"]
        euphemisms: "corporate_themed"
        
    beach_picture:
      detected_elements: ["sand", "waves", "sun", "swimwear"]
      world_changes:
        location: "beach_bar"
        goals: ["drink 20 piña_coladas", "get sunburned", "build sandcastles"]
        characters: ["surfer_dude", "beach_vendor"]
        euphemisms: "ocean_themed"
        
    wedding_picture:
      detected_elements: ["formal_wear", "flowers", "celebration"]
      world_changes:
        location: "wedding_reception"
        goals: ["give embarrassing speech", "dance badly", "avoid relatives"]
        characters: ["drunk_uncle", "bridesmaid", "wedding_crasher"]
        euphemisms: "formal_ceremony_themed"
        
    gym_picture:
      detected_elements: ["weights", "mirrors", "exercise_equipment"]
      world_changes:
        location: "fitness_center"
        goals: ["lift 200 pounds", "run 5 miles", "avoid gym_bros"]
        characters: ["personal_trainer", "gym_bro", "yoga_instructor"]
        euphemisms: "fitness_themed"
        
  # Dynamic Reprogramming Logic
  reprogramming_mechanics:
    instant_transformation: "Upload picture → entire game world changes in seconds as a new location is generated"
    context_preservation: "Player's personality and history and existing locations and characters maintained"
    character_homes: "Player and characters can have home locations where they can visit privately to sleep and recover and live and hump and die, together to visit and party and sing and eat and drink"
    seamless_transition: "AI creates narrative bridge between old and new context, dyanmically generates locations and items and actions and characters and events and songs and runs simulation like a dungeon master"
    goal_evolution: "Previous goals adapt to new environment"
    character_migration: "Existing characters get new roles in new setting"
    
  # AI Picture Analysis
  ai_analysis_capabilities:
    scene_understanding: "Recognizes complex scenarios and contexts"
    emotional_interpretation: "Happy party vs somber gathering"
    cultural_context: "Formal business vs casual hangout"
    temporal_clues: "Time of day, season, era, genre"
    social_dynamics: "Group size, relationships, hierarchy"
    
  # Story Continuity
  narrative_bridging:
    seamless_transitions: |
      "🎵 99 bottles of beer on the wall... 
       *PICTURE UPLOADED: Office cubicle*
       ...suddenly you're at work with 99 emails to answer!"
       
    context_explanations: |
      "The Narrator: 'Ah, I see you've uploaded a picture of your office. 
       Let me transport our story there... *POOF* 
       Now you're dealing with corporate life instead of carnival chaos!'"
       
    goal_metamorphosis: |
      "Your beer-drinking goal transforms into coffee-chugging survival.
       Your bathroom euphemisms become corporate-themed.
       Your weight gain becomes 'stress eating in the break room.'"
```

## 🎮 What This Actually Is {#what-it-is}

```yaml
# A Text-Based Countdown Game with AI Narration
actual_description:
  core_mechanics:
    countdown_songs: "Player counts down from any number (99 beers, 50 pushups, etc.)"
    ai_narrator: "AI creates funny commentary and asks questions"
    body_simulation: "Simple tracking of hunger, bathroom needs, weight"
    multiple_characters: "Can add friend simulations who also sing verses"
    multiple_players: "Actual friends in real life take turns at keyboard playing their roles and answering their questions and suggesting and writing their directions and topics and lyrics"
    
  what_you_do:
    pick_goal: "Choose what to count down (beers, work hours, exercises)"
    sing_verses: "AI generates song lyrics, you continue the countdown"
    fast_forward: "Like the fast simulation speed of The Sims, you can tell it to fast forward a number of iterations or an amount of time"
    temporal_sense: "The simulation has a rough idea or explicit parameter mapping the current iteration to time passing value which can change over time and due to events or user preference"
    respond_to_ai: "Answer questions about yourself for personalization"
    upload_pictures: "Change the setting by showing AI a photo"
    track_progress: "See simple stats about your session, leaderboards, play by play narration (Paradise by the Dashboard Light), etc"
    
  technical_reality:
    text_interface: "Mostly text-based interaction"
    basic_ai: "Uses AI for conversation and song generation"
    simple_data: "Tracks numbers and generates basic reports"
    yaml_format: "Game state stored in readable text format"
    proven_approach: "Based on and inspired by The Soul of The Sims 1 original prototype by Will Wright"
    lloooomm_dog_food: "This serves as a living evolving example of lloooomm for both human authors and LLMs running the lloooomm simulation itself"

  # What It's Not
  realistic_expectations:
    not_a_full_game: "More like an interactive story generator"
    not_multiplayer_online: "Multi-person is just adding more characters to track"
    not_actually_viral: "Just has features and outputs that could theoretically be shared"
    not_a_business: "This is a prototype/experiment/demo/artform, not a product"
 ```

## 📊 Analytics & SSQQLL Query System {#analytics-system}

```yaml
# Player Analytics - SSQQLL Queries Against Game Data
analytics_system:
  
  # Real-Time Analytics Queries
  performance_metrics:
    beers_per_hour: |
      SELECT 
        COUNT(*) / (mRealTimeElapsed / 3600) as beers_per_hour
      FROM #beer-consumption-log
      WHERE timestamp >= session_start;
      
    barfs_per_day: |
      SELECT 
        DATE(timestamp) as day,
        COUNT(*) as barf_count
      FROM #vomit-events
      GROUP BY DATE(timestamp)
      ORDER BY day DESC;
      
    bathroom_efficiency: |
      SELECT 
        AVG(time_in_bathroom) as avg_bathroom_time,
        COUNT(CASE WHEN type = 'piss' THEN 1 END) as piss_count,
        COUNT(CASE WHEN type = 'poop' THEN 1 END) as poop_count
      FROM #bathroom-visits;
      
    weight_progression: |
      SELECT 
        timestamp,
        currentWeight,
        snackCalories,
        (currentWeight - starting_weight) as weight_gained
      FROM #weight-tracking
      ORDER BY timestamp;
      
    money_flow: |
      SELECT 
        SUM(CASE WHEN amount > 0 THEN amount END) as total_earned,
        SUM(CASE WHEN amount < 0 THEN ABS(amount) END) as total_spent,
        lloooommolians as current_balance
      FROM #financial-transactions;
      
  # Song Analytics
  song_metrics:
    verses_sung: |
      SELECT 
        goal_type,
        COUNT(*) as verse_count,
        AVG(LENGTH(verse_text)) as avg_verse_length
      FROM #song-verses
      GROUP BY goal_type;
      
    euphemism_creativity: |
      SELECT 
        euphemism_category,
        COUNT(DISTINCT euphemism_text) as unique_euphemisms,
        personalization_score
      FROM #euphemism-usage
      GROUP BY euphemism_category;
      
    singing_participation: |
      SELECT 
        person_name,
        COUNT(*) as verses_sung,
        AVG(harmony_rating) as avg_harmony
      FROM #multi-person-singing
      GROUP BY person_name;
      
  # Social Analytics  
  social_metrics:
    sharing_stats: |
      SELECT 
        story_id,
        share_count,
        upvote_count,
        remix_count
      FROM #story-sharing
      ORDER BY viral_score DESC;
      
          picture_impact: |
        SELECT 
          picture_upload_time,
          world_transformation_type,
          goal_changes_count,
          narrative_continuity_score
        FROM #picture-uploads;
```

## 📋 Example Analytics Reports {#example-reports}

### 🍺 Session Performance Report
*Generate comprehensive session statistics with emoji-rich formatting*

```ssqqll
SELECT 
  COUNT(*) as total_beers,
  ROUND(COUNT(*) / (session_duration_hours), 1) as beers_per_hour,
  SUM(calories) as total_calories,
  ROUND(AVG(alcohol_content), 1) as avg_alcohol_percent
FROM #beer-consumption-log 
WHERE session_id = 'alex_2024_01_15';
```

**Sample Output:**
| Metric | Value | Status |
|--------|-------|--------|
| 🍺 Total Beers | 23 | 🔥 Above Average |
| ⏰ Beers/Hour | 6.2 | 🚨 Rapid Pace |
| 🔥 Total Calories | 3,450 | 📈 Weight Gain Alert |
| 🍻 Avg Alcohol % | 5.1% | 🎯 Standard Strength |

**Summary:** Alex consumed 23 beers over 3.7 hours at a rate of 6.2 beers/hour. This is 40% faster than the community average of 4.4 beers/hour. Total caloric intake of 3,450 calories resulted in 0.98 lbs of weight gain. 🎉

---

### 🚽 Bathroom Analytics Dashboard  
*Track physiological efficiency and euphemism creativity*

```ssqqll
SELECT 
  COUNT(CASE WHEN type = 'piss' THEN 1 END) as piss_count,
  COUNT(CASE WHEN type = 'poop' THEN 1 END) as poop_count,
  AVG(duration_seconds) as avg_duration,
  COUNT(DISTINCT euphemism_used) as unique_euphemisms
FROM #bathroom-visits 
WHERE player = 'alex';
```

**Sample Output:**
| Activity | Count | Avg Duration | Creativity Score |
|----------|-------|--------------|------------------|
| 💧 Piss Breaks | 8 | 45 seconds | ⭐⭐⭐ |
| 💩 Poop Sessions | 3 | 4.2 minutes | ⭐⭐⭐⭐⭐ |
| 🎭 Unique Euphemisms | 12 | - | 🏆 Highly Creative |

**Top Euphemisms Used:**
- 🍰 "Baking chocolate soufflé" (3 times)
- 📁 "Filing brown reports" (2 times)  
- 🏊 "Dropping kids at the pool" (2 times)

**Efficiency Rating:** Alex's bathroom-to-beer ratio of 0.48 visits per beer is optimal for sustained drinking sessions. 👍

---

### 💰 Financial Impact Report
*Track spending patterns and economic efficiency*

```ssqqll
SELECT 
  location,
  COUNT(*) as purchases,
  SUM(cost) as total_spent,
  AVG(cost) as avg_cost_per_item,
  SUM(cost) / COUNT(DISTINCT visit_id) as cost_per_visit
FROM #financial-transactions 
WHERE player = 'alex' AND amount < 0
GROUP BY location;
```

**Sample Output:**
| Location | Purchases | Total Spent | Avg Item Cost | Cost/Visit |
|----------|-----------|-------------|---------------|------------|
| 🍺 Bar | 18 | ₤216 | ₤12.00 | ₤72.00 |
| 🎪 Carnival | 3 | ₤45 | ₤15.00 | ₤45.00 |
| 🏠 Home | 2 | ₤6 | ₤3.00 | ₤3.00 |

**Financial Summary:** 
- 💸 Total Session Cost: **₤267**
- 💰 Remaining Balance: **₤733** 
- 📊 Most Expensive: Carnival beer (₤15/bottle)
- 💡 Best Value: Home beer (₤3/bottle)
- 🎯 Recommendation: Stock up at home for better value! 

---

### 🎵 Song Performance Analytics
*Measure musical participation and verse creativity*

```ssqqll
SELECT 
  person_name,
  COUNT(*) as verses_sung,
  AVG(verse_length) as avg_verse_length,
  COUNT(DISTINCT song_type) as song_variety,
  MAX(harmony_rating) as best_harmony
FROM #song-participation 
GROUP BY person_name
ORDER BY verses_sung DESC;
```

**Sample Output:**
| Singer | Verses | Avg Length | Song Types | Best Harmony |
|--------|--------|------------|------------|--------------|
| 🎤 Alex | 47 | 28 words | 4 | ⭐⭐⭐⭐ |
| 🎵 Jamie | 23 | 31 words | 3 | ⭐⭐⭐⭐⭐ |
| 🎶 Casey | 12 | 19 words | 2 | ⭐⭐⭐ |
| 🍺 Bartender Sam | 8 | 35 words | 1 | ⭐⭐⭐⭐⭐ |

**Musical Highlights:**
- 🏆 **Most Prolific:** Alex (47 verses)
- 🎯 **Best Harmony:** Jamie & Sam (5-star rating)
- 📝 **Most Verbose:** Bartender Sam (35 words/verse)
- 🎪 **Song Variety Champion:** Alex (4 different song types)

---

### 📸 Picture Upload Impact Analysis
*Analyze world transformation effectiveness*

```ssqqll
SELECT 
  upload_time,
  scene_type,
  characters_added,
  locations_created,
  goals_changed,
  narrative_continuity_score
FROM #picture-uploads 
ORDER BY upload_time;
```

**Sample Output:**
| Time | Scene Type | New Characters | New Locations | Goals Changed | Continuity |
|------|------------|----------------|---------------|---------------|------------|
| 01:47 | 🏢 Office | 2 | 1 | 3 | ⭐⭐⭐⭐ |
| 02:33 | 🏖️ Beach | 1 | 2 | 1 | ⭐⭐⭐⭐⭐ |

**Transformation Summary:**
- 📷 **Total Uploads:** 2 pictures
- 👥 **Characters Generated:** 3 new NPCs with full personalities
- 🗺️ **Locations Created:** 3 new interactive locations  
- 🎯 **Goal Adaptations:** 4 seamless goal transitions
- 🎭 **Narrative Flow:** 4.5/5 stars average continuity

**Most Impactful Upload:** Beach scene at 02:33 created the most seamless world transition with perfect narrative continuity! 🏆

## 🏠 Session Documentation Pages {#save-file-system}

```yaml
# Basic Save File Documentation
save_file_system:
  
  # Main Save File Overview
  save_overview:
    file_structure: |
      📁 SaveFile_Alex_Session_2024-01-15/
      ├── 📄 index.html (Main overview page)
      ├── 📄 character_alex.html (Character details)
      ├── 📄 locations.html (All visited locations)
      ├── 📄 story_timeline.html (Complete narrative)
      ├── 📄 analytics.html (Statistics dashboard)
      ├── 📄 songs.html (All verses sung)
      ├── 📄 pictures.html (Uploaded images & transformations)
      └── 📁 assets/ (Images, audio, data files)
      
  # Character Profile Pages
  character_pages:
    alex_profile:
      basic_info:
        name: "Alex"
        session_duration: "3 hours 42 minutes"
        starting_weight: "180 lbs"
        ending_weight: "183 lbs"
        starting_money: "₤1000"
        ending_money: "₤247"
        
      physiological_summary:
        total_beers: 23
        total_pisses: 8
        total_poops: 3
        total_barfs: 1
        calories_consumed: 2847
        
      personality_profile:
        discovered_traits: ["loves_cooking", "office_worker", "cat_phobic"]
        favorite_euphemisms: ["baking chocolate soufflé", "filing brown reports"]
        humor_style: "self_deprecating"
        
      goal_progression:
        completed_goals: ["drink 99 beers (76 remaining)", "drop kids at pool (2/3)"]
        abandoned_goals: ["work 40 hours (switched due to picture upload)"]
        
  # Location Documentation
  location_pages:
    visited_locations:
      bar:
        time_spent: "2 hours 15 minutes"
        beers_consumed: 18
        money_spent: "₤216"
        memorable_moments: ["Guinness triggered British dialect", "Shared Pringles with Jamie"]
        
      bathroom:
        visits: 11
        total_time: "23 minutes"
        euphemisms_used: ["dropped kids at pool", "filed brown report"]
        
      carnival:
        time_spent: "45 minutes"
        rides_ridden: 2
        vomit_incidents: 1
        arrest_count: 0
        
  # Story Timeline
  story_documentation:
    narrative_structure:
      act_1_setup: "Started drinking beer at the bar with friends"
      act_2_complications: "Picture upload transformed world to office setting"
      act_3_resolution: "Returned to bar via safe rideshare"
      
    key_moments:
      - timestamp: "00:23:15"
        event: "First euphemism personalization based on cooking interest"
        impact: "Established player's creative personality"
        
      - timestamp: "01:47:32"
        event: "Office picture upload"
        impact: "Complete world transformation, goal metamorphosis"
        
      - timestamp: "02:15:44"
        event: "Collaborative Pringles sharing with Jamie and Casey"
        impact: "Social bonding, accelerated snack consumption"
        
  # Analytics Dashboard
  analytics_pages:
    performance_dashboard:
      consumption_rates:
        beers_per_hour: 6.2
        calories_per_hour: 761
        money_spent_per_hour: "₤203"
        
      efficiency_metrics:
        bathroom_visits_per_beer: 0.48
        euphemism_creativity_score: 8.7
        social_interaction_rating: 9.2
        
      progression_charts:
        weight_over_time: "Line chart showing 3-pound gain"
        money_over_time: "Declining balance with spending spikes"
        mood_progression: "Happiness peaks during social moments"
```

## 🎵 Lyric Generation & Orchestration System {#lyric-generation-system}

```yaml
# Advanced Lyric Generation - The Heart of LLOOOOMM BBEEEERR
# This system treats songs as configurable "for" loops with character orchestration
lyric_generation_system:
  
  # Core Loop Structure - Every Song is a For Loop
  song_loop_architecture:
    description: "Songs are essentially for-loops with configurable parameters and character orchestration"
    
    # Primary Song Index System
    index_configuration:
      beer_index: 99          # Current countdown number
      beer_step: -1           # Decrement by 1 each iteration
      beer_limit: 0           # Stop when reaching 0 (exclusive)
      
      # Alternative Index Examples
      dayOfChristmas_index: 1
      dayOfChristmas_step: 1
      dayOfChristmas_max: 12  # Inclusive maximum (goes TO 12)
      
      pushup_index: 0
      pushup_step: 1
      pushup_count: 100       # Total count to reach
      
      # Advanced Step Patterns
      fibonacci_index: 1
      fibonacci_step: "next_fibonacci"  # Natural language step
      fibonacci_limit: 1000
      
      random_index: 50
      random_step: "random(-5, 5)"     # Random range step
      random_exclusiveLimit: 100
      
      time_index: "monday"
      time_step: "advance_one_day"     # Natural language temporal step
      time_limit: "sunday"
      
         # Step Semantics by Suffix
     step_semantics:
       max: "Inclusive upper bound (goes TO the number)"
       limit: "Exclusive upper bound (stops BEFORE the number)" 
       count: "Total iterations to perform"
       exclusiveLimit: "Explicit exclusive bound"
       inclusiveMax: "Explicit inclusive bound"
       unbounded: "No limit, continues indefinitely until stopped"
       infinite: "Alias for unbounded"
       forever: "Alias for unbounded"
      
    # Natural Language Step Interpretation
    natural_language_steps:
      "advance one week": "Add 7 to time-based index"
      "go backwards by twos": "Subtract 2 each iteration"
      "random walk": "Add random(-3, 3) each step"
      "fibonacci sequence": "Next fibonacci number"
      "double each time": "Multiply by 2"
      "halve and round down": "Divide by 2, floor result"
      
  # Character Orchestration Patterns
  orchestration_patterns:
    
    # Default: Round Robin Turn-Taking
    round_robin:
      description: "Characters take turns singing verses in order"
      pattern: "Character A sings verse N, Character B sings verse N-1, etc."
      example: |
        Murphy (BAC 0.05): "🎵 99 bottles of beer on the wall, 99 bottles of beer!"
        Old Salt (BAC 0.12): "🎵 Take one down, pash it around... *hic* 98 bottlesh of beer!"
        Casey (BAC 0.08): "🎵 98 bottles of beer on the wall, looking fabulous as always! 💅"
        
    # Personality-Driven Selection
    personality_driven:
      description: "Character selection based on personality traits and current state"
      factors: ["BAC level", "energy", "mood", "agenda", "relationships"]
      example: |
        # Neurotic character obsesses over exact count
        Alex (neurotic, BAC 0.03): "🎵 97 bottles... wait, did I count right? 97? Yes, 97!"
        # Megalomaniac makes it about power
        Victor (megalomaniac, BAC 0.15): "🎵 96 bottles bow before my supreme authority! 👑🍺"
        
    # BAC-Influenced Priority
    bac_priority:
      description: "Most intoxicated characters sing more often"
      logic: "Higher BAC = more likely to interrupt and sing"
      example: |
        # Drunk character keeps interrupting
        Pete (BAC 0.18): "🎵 I LOVE YOU GUYS! *hic* 95 bottles and I love... LOVE everyone!"
        Murphy (BAC 0.05): "Pete, it's not your turn..."
        Pete (BAC 0.18): "🎵 94 bottles of FRIENDSHIP! Group hug! 🤗🍺"
        
         # Story-Driven Orchestration  
     story_driven:
       description: "Characters sing based on their current agendas and stories"
       example: |
         # Old Salt telling sea story through lyrics
         Old Salt (BAC 0.10): "🎵 93 bottles, like the 93 days I spent at sea..."
         # Bartender giving advice
         Murphy (BAC 0.02): "🎵 92 bottles, and 92 pieces of advice: pace yourself!"
         
     # Karaoke Mode - Solo Performance
     karaoke_mode:
       description: "One character takes the spotlight and sings multiple verses solo"
       trigger_events:
         - "Character grabs microphone or gets on stage"
         - "Someone shouts 'Let Casey sing!'"
         - "Character declares 'This is my song!'"
         - "Jukebox plays character's favorite song"
         - "Character reaches peak confidence (BAC sweet spot)"
         
       karaoke_patterns:
         confident_solo: |
           Casey (BAC 0.08): "🎵 91 bottles of beer on the wall!"
           Casey: "🎵 90 bottles of beer!"
           Casey: "🎵 89 bottles, and I'm feeling fine!"
           Casey: "🎵 88 bottles, this spotlight is mine!"
           
         drunk_rambling_solo: |
           Pete (BAC 0.16): "🎵 87 bottles... *hic* I LOVE YOU ALL!"
           Pete: "🎵 86 bottles... wait, what comes after 86?"
           Pete: "🎵 85... or 84? Math is hard but FRIENDSHIP!"
           Pete: "🎵 83 bottles of... of... LOVE AND BEER!"
           
         emotional_ballad: |
           Old Salt (BAC 0.12): "🎵 82 bottles... like the years I've sailed..."
           Old Salt: "🎵 81 bottles... through storms and gales..."
           Old Salt: "🎵 80 bottles... missing my dear wife..."
           Old Salt: "🎵 79 bottles... the story of my life..."
           
       karaoke_end_triggers:
         - "Character finishes their emotional arc"
         - "Someone else demands a turn"
         - "Character gets too drunk to continue"
         - "Gong show event interrupts"
         - "Character passes out or leaves stage"
         
     # Gong Show Mode - Competitive Interruption
     gong_show_mode:
       description: "Other characters can 'gong' the performer out if they're bad/boring"
       
       gong_triggers:
         off_key_singing: |
           Casey: "🎵 78 bottles of beer on the waaaaaall!" *off-key*
           Murphy: "GONG! 🔔 That's enough of that!"
           
         too_drunk_incoherent: |
           Pete (BAC 0.22): "🎵 77... blurble... bottles... fribble..."
           Everyone: "GONG! GONG! GONG! 🔔🔔🔔"
           
         boring_repetition: |
           Alex: "🎵 76 bottles of beer on the wall..."
           Alex: "🎵 75 bottles of beer on the wall..."
           Alex: "🎵 74 bottles of beer on the wall..."
           Old Salt: "GONG! 🔔 Mix it up, lad!"
           
         offensive_content: |
           Character: "🎵 73 bottles and let me tell you about my ex..."
           Casey: "GONG! 🔔 We don't need that drama!"
           
       gong_effects:
         immediate_stop: "Current singer must stop mid-verse"
         turn_transfer: "Next character takes over immediately"
         shame_reaction: "Gonged character shows embarrassment/defiance"
         crowd_reaction: "Other characters cheer or boo the gonging"
         
       gong_examples:
         gentle_gong: |
           Murphy: "Easy there, Pete. Let someone else have a go."
           Pete: "Aww, but I was just getting started!"
           
         harsh_gong: |
           Casey: "GONG! 🔔 That was painful to listen to!"
           Alex: "Hey! I thought I was doing fine..."
           Casey: "Honey, no. Just... no."
           
         rescue_gong: |
           Old Salt: "🎵 72 bottles... *voice cracking*"
           Murphy: "GONG! 🔔 Save your voice, old friend."
           Old Salt: "Aye, thanks Murphy. Getting too old for this."
           
     # Groundhog Day Mode - Stuck on Same Number
     groundhog_day_mode:
       description: "Characters get stuck repeating the same number over and over"
       
       trigger_conditions:
         confusion_spiral: "Characters lose track and keep resetting"
         obsessive_fixation: "Neurotic character can't move past a number"
         drunk_loop: "Too intoxicated to remember what comes next"
         philosophical_trap: "Deep thoughts about the meaning of the number"
         technical_glitch: "Jukebox skips, reality hiccup"
         
       groundhog_examples:
         neurotic_obsession: |
           Alex: "🎵 71 bottles of beer on the wall..."
           Alex: "Wait, was that 71 or 70? Let me start over."
           Alex: "🎵 71 bottles of beer on the wall..."
           Alex: "Actually, let me double-check that count..."
           Alex: "🎵 71 bottles of beer on the wall..."
           Murphy: "Alex, we've heard 71 five times now!"
           
         drunk_confusion: |
           Pete (BAC 0.19): "🎵 69 bottles... *hic*"
           Pete: "Wait, what comes after 69?"
           Pete: "🎵 69 bottles... *hic*"
           Pete: "Seriously, what's after 69?"
           Pete: "🎵 69 bottles... nice! *giggle*"
           Casey: "Pete! It's 68!"
           Pete: "🎵 69 bottles... *hic*"
           
         philosophical_loop: |
           Goth Character: "🎵 66 bottles... the number of the beast's cousin..."
           Goth Character: "What does 66 really mean in the cosmic sense?"
           Goth Character: "🎵 66 bottles... harbinger of existential dread..."
           Goth Character: "Is 66 the gateway to understanding mortality?"
           Goth Character: "🎵 66 bottles... like tears in the void..."
           
         reality_glitch: |
           Murphy: "🎵 65 bottles of beer on the wall..."
           *RECORD SCRATCH*
           Murphy: "🎵 65 bottles of beer on the wall..."
           *RECORD SCRATCH*
           Murphy: "What the... 🎵 65 bottles of beer on the wall..."
           Casey: "Is anyone else experiencing déjà vu?"
           
       escape_mechanisms:
         intervention: "Other characters forcibly move the count forward"
         distraction: "New event breaks the loop"
         realization: "Stuck character suddenly snaps out of it"
         group_override: "Everyone sings the next number together"
         
       escape_examples:
         group_intervention: |
           Everyone: "SIXTY-FOUR! 🎵 64 bottles of beer!"
           Alex: "Oh! Right! 64! Thank you!"
           
         sudden_realization: |
           Pete: "🎵 69 bottles... wait, I've been saying this forever!"
           Pete: "🎵 68 bottles! Finally! My brain works again!"
           
         distraction_break: |
           *CRASH* (someone drops glass)
           Alex: "What was that? Oh right, 🎵 67 bottles of beer!"
           
     # Mode Transitions and Combinations
     mode_transitions:
       description: "LLM can creatively shift between orchestration modes"
       
       transition_examples:
         turns_to_karaoke: |
           Murphy: "🎵 64 bottles of beer on the wall..."
           Casey: "You know what? This is my jam!" *grabs mic*
           Casey: "🎵 63 bottles, and I'm taking over!"
           
         karaoke_to_gong: |
           Pete: "🎵 62 bottles... *off-key warbling*"
           Murphy: "GONG! 🔔 My ears can't take it!"
           Old Salt: "🎵 61 bottles, sung properly!"
           
         gong_to_groundhog: |
           Alex: "🎵 60 bottles of beer on the wall..."
           Casey: "GONG! 🔔 Too boring!"
           Alex: "But... 🎵 60 bottles of beer on the wall..."
           Alex: "I was just... 🎵 60 bottles of beer on the wall..."
           Murphy: "Alex, you're stuck!"
           
         groundhog_to_turns: |
           Pete: "🎵 59 bottles... what comes next?"
           Everyone: "FIFTY-EIGHT!"
           Murphy: "🎵 58 bottles, back to normal turns!"
           Casey: "🎵 57 bottles, crisis averted!"
           
       combined_modes:
         karaoke_groundhog: "Solo performer gets stuck on same number"
         gong_show_groundhog: "Everyone keeps gonging but stuck on same number"
         competitive_karaoke: "Multiple characters fighting for solo time"
        
     # Individual Character BAC Effects on Lyrics
   character_bac_effects:
     
     # Dynamic Temperature System - Controls Theme Adherence
     temperature_system:
       description: "Each character has a dynamic temperature (0.0-1.0) that controls how closely they stick to the official song theme"
       
       temperature_calculation:
         base_formula: "temperature = (BAC * 2.0) + personality_modifier + situational_factors"
         personality_modifiers:
           neurotic: "+0.1 (overthinks and goes off-topic)"
           megalomaniacal: "+0.15 (makes everything about themselves)"
           valley_girl: "+0.05 (easily distracted)"
           goth: "+0.2 (existential tangents)"
           techno_dadaist: "+0.3 (naturally abstract)"
           wise_bartender: "-0.1 (stays focused and professional)"
           storytelling_sailor: "+0.1 (loves tangential stories)"
           artistic_bartender: "+0.05 (creative interpretations)"
           social_connector: "+0.1 (brings in personal drama)"
           
         situational_factors:
           emotional_state: "±0.1 based on mood"
           environment_chaos: "±0.05 based on bar atmosphere"
           social_pressure: "±0.05 based on group dynamics"
           time_of_night: "+0.05 per hour after midnight"
           
       temperature_effects_on_lyrics:
         temp_0_0_to_0_2: 
           adherence: "Strict theme adherence"
           content: "Official song lyrics, proper counting, on-topic"
           example: "🎵 85 bottles of beer on the wall, 85 bottles of beer!"
           
         temp_0_2_to_0_4:
           adherence: "Minor personal touches"
           content: "Adds personality flair while staying on theme"
           example: "🎵 84 bottles of beer, just like the 84 ships I've sailed! ⚓"
           
         temp_0_4_to_0_6:
           adherence: "Moderate topic drift"
           content: "Weaves in personal interests and stories"
           example: "🎵 83 bottles... reminds me of my ex who loved beer... *sigh* 💔"
           
         temp_0_6_to_0_8:
           adherence: "Significant deviation"
           content: "Opens up emotionally, overshares, tangential stories"
           example: "🎵 82 bottles... you know what? I never told anyone this but... *hic* 😭"
           
         temp_0_8_to_1_0:
           adherence: "Complete theme abandonment"
           content: "Stream of consciousness, TMI, incomprehensible rambling"
           example: "🎵 81... my therapist says I have daddy issues... also I wet the bed until 12... 🤮"
           
     # BAC Level Impact on Lyric Content with Temperature Integration
     bac_lyric_influence:
       level_0_sober: 
         temperature_range: "0.0-0.1"
         speech_quality: "Clear articulation, logical lyrics"
         lyric_content: "Straightforward countdown, proper grammar, strict theme adherence"
         topic_focus: "Official song theme only"
         example: "🎵 91 bottles of beer on the wall, 91 bottles of beer!"
         
       level_1_tipsy:
         temperature_range: "0.1-0.3"
         speech_quality: "Slight slurring, extra enthusiasm" 
         lyric_content: "Added commentary, more emojis, confidence boost, minor personal touches"
         topic_focus: "Song theme + personality flair"
         example: "🎵 90 bottlesh of beer! This is the BEST song ever! Like my grandpa used to sing! 🍺✨"
         
       level_2_drunk:
         temperature_range: "0.3-0.5"
         speech_quality: "Noticeable slurring, hiccups, word mixing"
         lyric_content: "Spurious declarations of love, rambling tangents, personal stories creeping in"
         topic_focus: "Song theme + personal interests + emotional outbursts"
         example: "🎵 89 bottles... *hic* I LOVE YOU GUYS! You're like the 89 reasons I love this bar! My dad never... *burp* 🤗🍺"
         
       level_3_wasted:
         temperature_range: "0.5-0.7"
         speech_quality: "Heavy slurring, confusion, losing count"
         lyric_content: "Emotional outbursts, forgetting the number, oversharing personal details"
         topic_focus: "Chaotic mix of song theme + deep personal revelations + confusion"
         example: "🎵 Wait... 88? Or 78? You know what... *sob* I never got over Sarah... she left me for a guy with 88 tattoos! 😭🍺"
         
       level_4_blackout:
         temperature_range: "0.7-0.9"
         speech_quality: "Incoherent babbling, Simlish-like sounds"
         lyric_content: "Complete nonsense, TMI oversharing, stream of consciousness"
         topic_focus: "No coherent theme, random personal trauma + nonsense"
         example: "🎵 Blurble... 87 times I wet myself... fribble... my therapist says... MOMMY ISSUES! 🤮💕"
         
       level_5_unconscious:
         temperature_range: "0.9-1.0"
         speech_quality: "Snoring, sleep-talking"
         lyric_content: "Mumbled numbers, dream content bleeding through, subconscious fears"
         topic_focus: "Dream logic + suppressed memories + random numbers"
         example: "💤 Zzz... 86 purple elephants... zzz... daddy why did you leave... zzz... 😴"
         
     # Character-Specific Temperature Progressions
     character_temperature_examples:
       
       murphy_progression:
         temp_0_1: "🎵 85 bottles of beer on the wall, 85 bottles of beer!"
         temp_0_3: "🎵 84 bottles, like the 84 years this pub has been serving!"
         temp_0_5: "🎵 83 bottles... you know, I've seen 83 different heartbreaks at this bar..."
         temp_0_7: "🎵 82 bottles... *hic* my wife left me 82 days ago... I count every day... 😭"
         temp_0_9: "🎵 Blurble... 81 reasons I drink alone... she took the dog... FRIBBLE! 🤮"
         
       the_stranger_progression:
         temp_0_1: "🎵 80 bottles of beer on the wall, 80 bottles of beer!"
         temp_0_3: "🎵 79 bottles, like the 79 asteroids I wrangled in the Cretaceous period!"
         temp_0_5: "🎵 78 bottles... reminds me of the 78 dimensions I've visited... time is weird..."
         temp_0_7: "🎵 77 bottles... *hic* you know what? I'm not from here... I'm from 2847... my real name is Zyx'thul... 🌀"
         temp_0_9: "🎵 Blurble... 76 quantum realities... my home planet exploded... TEMPORAL PARADOX! 🤮👽"
         
       casey_progression:
         temp_0_1: "🎵 75 bottles of beer on the wall, 75 bottles of beer!"
         temp_0_3: "🎵 74 bottles, and 74 reasons why this outfit is perfect tonight! 💅"
         temp_0_5: "🎵 73 bottles... speaking of 73, that's how many times Jake texted me today... ugh..."
         temp_0_7: "🎵 72 bottles... *sob* you know what? I'm 32 and still single... my mom keeps asking about grandkids... 😭"
         temp_0_9: "🎵 Blurble... 71 dating app disasters... I once hooked up with my cousin's ex... TMI! 🤮💔"
         
       old_salt_progression:
         temp_0_1: "🎵 70 bottles of beer on the wall, 70 bottles of beer!"
         temp_0_3: "🎵 69 bottles, like the 69 storms I've weathered at sea!"
         temp_0_5: "🎵 68 bottles... reminds me of the 68 men I lost in the great storm of '73..."
         temp_0_7: "🎵 67 bottles... *hic* I still hear their voices in the wind... I should have saved them... 😭"
         temp_0_9: "🎵 Blurble... 66 ghosts follow me... I killed a man in Singapore... GUILT! 🤮⚓"
         
     # Temperature Modulation Events
     temperature_events:
       description: "Events that can suddenly change a character's temperature"
       
       temperature_spikes:
         emotional_trigger: "+0.3 temperature (someone mentions sensitive topic)"
         alcohol_surge: "+0.2 temperature (chugs drink quickly)"
         social_pressure: "+0.1 temperature (crowd encourages oversharing)"
         memory_flashback: "+0.4 temperature (traumatic memory surfaces)"
         
       temperature_drops:
         reality_check: "-0.2 temperature (someone calls them out)"
         professional_mode: "-0.3 temperature (bartender switches to work mode)"
         embarrassment: "-0.1 temperature (realizes they overshared)"
         distraction: "-0.1 temperature (something else grabs attention)"
         
       temperature_examples:
         emotional_spike: |
           Casey (temp 0.4): "🎵 65 bottles, looking fabulous tonight!"
           Someone: "How's your dating life?"
           Casey (temp 0.7): "🎵 64 bottles... *sob* I'm dying alone with cats! 😭"
           
                   reality_check: |
            Murphy (temp 0.8): "🎵 63 bottles... my wife's affair with the mailman... *hic*"
            Customer: "Murphy, maybe you should stop..."
            Murphy (temp 0.5): "🎵 62 bottles... aye, you're right. Back to the song."
            
   # Lyric-Triggered Random Events System
   lyric_event_system:
     description: "Lyrics themselves become the engine for random event generation - what characters sing about can manifest in reality"
     
     # Event Trigger Mechanisms
     trigger_types:
       literal_manifestation: "What they sing about literally happens"
       thematic_resonance: "Events related to the theme of their lyrics occur"
       emotional_contagion: "The emotion in lyrics spreads and creates situations"
       memory_activation: "Lyrics about the past bring past into present"
       prophetic_lyrics: "Lyrics accidentally predict immediate future"
       reality_glitch: "Lyrics break the fourth wall and affect the game itself"
       
     # Event Categories by Lyric Content
     event_categories:
       
       # Weather & Environment Events
       weather_lyrics:
         trigger_examples:
           - "🎵 55 bottles like 55 raindrops falling!"
           - "🎵 54 bottles cold as winter storms!"
           - "🎵 53 bottles bright as sunny days!"
         possible_events:
           sudden_rainstorm: "Rain starts pouring, everyone rushes inside"
           temperature_drop: "Bar suddenly gets cold, fireplace needed"
           power_outage: "Lightning strikes, lights go out"
           rainbow_appearance: "Beautiful rainbow visible through window"
           
       # Animal & Creature Events  
       animal_lyrics:
         trigger_examples:
           - "🎵 52 bottles and 52 cats in the alley!"
           - "🎵 51 bottles, saw a dog that looked like my ex!"
           - "🎵 50 bottles, flying like birds in the sky!"
         possible_events:
           stray_cat_enters: "A cat wanders into the bar, chaos ensues"
           dog_outside: "Friendly dog appears outside, everyone wants to pet it"
           bird_flies_in: "Bird flies through open door, everyone tries to catch it"
           pest_invasion: "Mice/rats appear, bartender grabs broom"
           
       # People & Relationship Events
       relationship_lyrics:
         trigger_examples:
           - "🎵 49 bottles, thinking of my ex Sarah!"
           - "🎵 48 bottles, wish my mom would call!"
           - "🎵 47 bottles, missing my old friends!"
         possible_events:
           ex_appears: "The mentioned ex actually walks into the bar"
           phone_call: "Character's phone rings with call from mentioned person"
           old_friend_arrives: "Someone from the past shows up unexpectedly"
           family_drama: "Family member calls with urgent news"
           
       # Object & Item Events
       object_lyrics:
         trigger_examples:
           - "🎵 46 bottles, lost my keys again!"
           - "🎵 45 bottles, need a new phone!"
           - "🎵 44 bottles, this jukebox is broken!"
         possible_events:
           keys_found: "Someone finds lost keys in unexpected place"
           phone_breaks: "Character's phone suddenly stops working"
           jukebox_malfunction: "Jukebox starts playing wrong songs"
           mystery_object: "Strange object appears on table"
           
       # Emotional State Events
       emotional_lyrics:
         trigger_examples:
           - "🎵 43 bottles, feeling so lonely!"
           - "🎵 42 bottles, happiest night ever!"
           - "🎵 41 bottles, angry at the world!"
         possible_events:
           group_hug: "Everyone spontaneously hugs the lonely person"
           celebration_erupts: "Entire bar starts celebrating"
           argument_breaks_out: "Angry lyrics trigger bar fight"
           crying_contagion: "Sad lyrics make everyone emotional"
           
       # Supernatural & Strange Events
       supernatural_lyrics:
         trigger_examples:
           - "🎵 40 bottles, feeling like magic tonight!"
           - "🎵 39 bottles, ghosts of the past!"
           - "🎵 38 bottles, time feels broken!"
         possible_events:
           lights_flicker: "Supernatural energy affects electricity"
           cold_spot: "Temperature drops in specific area"
           time_skip: "Everyone loses track of time for a moment"
           deja_vu_wave: "Everyone experiences same memory simultaneously"
           
       # The Stranger's Special Events
       stranger_lyrics:
         trigger_examples:
           - "🎵 37 bottles, like 37 asteroids I wrangled!"
           - "🎵 36 bottles, from the year 2847!"
           - "🎵 35 bottles, quantum beer brewing!"
         possible_events:
           reality_glitch: "Physics briefly stops working normally"
           time_portal: "Brief glimpse of other time periods"
           alien_contact: "Strange signals on radio/TV"
           dimensional_slip: "Room briefly looks like different era"
           
     # Event Probability & Timing
     event_mechanics:
       base_probability: "5% chance per lyric verse"
       temperature_modifier: "Higher temperature = higher event chance"
       alcohol_modifier: "More drunk characters = more chaotic events"
       group_singing_bonus: "Multiple characters singing same theme = higher chance"
       
       probability_formula: |
         event_chance = base_probability + (average_temperature * 0.1) + (average_BAC * 0.05) + group_bonus
         
       timing_rules:
         immediate: "Event happens during or right after the lyric"
         delayed: "Event happens 1-3 verses later"
         cumulative: "Multiple related lyrics build up to bigger event"
         
     # Event Examples in Action
     event_examples:
       
       literal_manifestation: |
         Casey: "🎵 32 bottles, and 32 reasons it's raining!"
         *CRASH* - Thunder rumbles, rain starts pouring
         Murphy: "Well, would you look at that... Casey called it!"
         
       thematic_resonance: |
         Old Salt: "🎵 31 bottles, like the 31 men I lost at sea!"
         *Lights flicker, cold wind blows through bar*
         Everyone: *shivers* "Did you feel that?"
         
       emotional_contagion: |
         Pete: "🎵 30 bottles, I LOVE EVERYONE HERE!"
         *Everyone suddenly feels overwhelming affection*
         Group hug erupts spontaneously
         
       memory_activation: |
         Murphy: "🎵 29 bottles, like my dear old dad used to drink!"
         *Phone rings* "Murphy? It's your cousin... about your father's will..."
         
       prophetic_lyrics: |
         Alex: "🎵 28 bottles, hope nobody spills anything!"
         *Immediately after, someone knocks over their drink*
         Alex: "I... I didn't mean to predict that!"
         
       reality_glitch: |
         The Stranger: "🎵 27 bottles, from 27 different dimensions!"
         *Jukebox starts playing music from the 1800s*
         *Lights flicker between gas lamps and neon*
         Everyone: "What the hell just happened?!"
         
     # Event Chains & Escalation
     event_chains:
       description: "Events can trigger follow-up events, creating narrative chains"
       
       chain_examples:
         weather_chain: |
           1. "🎵 26 bottles, stormy weather ahead!"
           2. Rain starts → Power flickers
           3. "🎵 25 bottles, need some light in here!"
           4. Candles appear → Romantic atmosphere
           5. "🎵 24 bottles, feeling romantic tonight!"
           6. Two characters start flirting
           
         supernatural_chain: |
           1. "🎵 23 bottles, ghosts of Christmas past!"
           2. Cold spot appears → Everyone shivers
           3. "🎵 22 bottles, someone's watching us!"
           4. Mysterious figure seen in window
           5. "🎵 21 bottles, time to investigate!"
           6. Group decides to go outside and look
           
         social_chain: |
           1. "🎵 20 bottles, missing my ex tonight!"
           2. Phone buzzes with text from ex
           3. "🎵 19 bottles, should I text back?"
           4. Everyone gives conflicting advice
           5. "🎵 18 bottles, here goes nothing!"
           6. Character sends text, immediate drama ensues
           
     # Event Resolution & Consequences
     event_resolution:
       temporary_effects: "Most events last 1-5 verses then resolve"
       permanent_changes: "Some events permanently alter character relationships or bar state"
       narrative_integration: "Events become part of ongoing story and character development"
       
       resolution_examples:
         temporary: |
           Rain event → Lasts 3 verses → Sun comes out → Everyone cheers
           
         permanent: |
           Ex shows up → Dramatic confrontation → Character growth → New relationship dynamic
           
         narrative: |
           Supernatural event → Characters bond over shared experience → Stronger friendships
           
     # Meta-Events: Lyrics About the Game Itself
     meta_events:
       description: "When characters sing about the game, counting, or the song itself"
       
       meta_examples:
         counting_confusion: |
           "🎵 17 bottles, but are we counting right?"
           → Everyone loses track, has to restart from different number
           
         song_awareness: |
           "🎵 16 bottles, this song goes on forever!"
           → Song actually speeds up or slows down
           
         fourth_wall_break: |
           "🎵 15 bottles, feels like we're in a game!"
           → Characters briefly become aware they're in a simulation
           
         reality_questioning: |
                       "🎵 14 bottles, is any of this real?"
            → Everything becomes slightly surreal and dreamlike
            
   # Time Travel & Dimensional Mechanics
   time_travel_system:
     description: "Get The Stranger drunk enough without passing out yourself to access temporal abilities"
     
     stranger_drink_thresholds:
       bac_0_15: "Time travel unlocked - access past/future timelines"
       bac_0_20: "Dimensional travel unlocked - access parallel realities"
       bac_0_25: "Quantum travel unlocked - access impossible timelines"
       
     player_survival_requirement: "Must stay conscious (BAC < 0.30) to travel with The Stranger"
     
     beverage_system:
       default_drink: "beer"
       character_preferences:
         main_player: "beer"
         murphy: "guinness" 
         old_salt: "rum"
         the_stranger: "quantum_ale"
         bryan: "craft_cocktails"
         casey: "champagne"
         designated_driver: "coffee/soda"
         
     song_adaptation: "Characters sing about their preferred beverage instead of beer"
        
  # Creative Number Integration Requirements
  number_integration_rules:
    
    # Core Rule: Every Lyric Must Include the Number
    mandatory_number_inclusion:
      description: "Every verse must creatively incorporate the current countdown number"
      enforcement: "LLM must find creative ways to include the number, even in abstract lyrics"
      
    # Creative Integration Patterns
    integration_patterns:
      
      direct_countdown:
        pattern: "Straightforward number usage"
        examples:
          - "🎵 87 bottles of beer on the wall!"
          - "🎵 86 reasons why I love this bar!"
          - "🎵 85 steps to the bathroom door!"
          
      mathematical_wordplay:
        pattern: "Math operations, fractions, creative arithmetic"
        examples:
          - "🎵 84 divided by 2 equals 42 reasons to drink!"
          - "🎵 83 plus 17 equals 100% fun tonight!"
          - "🎵 82 squared is... wait, that's too much math! 🤔"
          
      time_and_age_references:
        pattern: "Years, minutes, hours, ages"
        examples:
          - "🎵 81 years old and still drinking strong!"
          - "🎵 80 minutes until last call, better hurry!"
          - "🎵 79 seconds of pure happiness right here!"
          
      emotional_intensity:
        pattern: "Feelings and emotions scaled by number"
        examples:
          - "🎵 78 levels of love for you beautiful people!"
          - "🎵 77 shades of happiness in my heart!"
          - "🎵 76 degrees of awesome in this room!"
          
      absurd_comparisons:
        pattern: "Silly, nonsensical uses of the number"
        examples:
          - "🎵 75 unicorns would be jealous of this beer!"
          - "🎵 74 dimensions of flavor in this drink!"
          - "🎵 73 ways to say 'cheers' in Martian!"
          
      story_integration:
        pattern: "Number becomes part of ongoing narrative"
        examples:
          - "🎵 72 pirates sailed with me to this very bar!"
          - "🎵 71 dreams led me to this moment with you!"
          - "🎵 70 lifetimes wouldn't be enough for this friendship!"
          
      meta_commentary:
        pattern: "Self-aware references to the counting itself"
        examples:
          - "🎵 69... nice! *giggle* This counting game is fun!"
          - "🎵 68 verses and we're still going strong!"
          - "🎵 67 more chances to mess up this song!"
          
  # Character Personality Integration with Numbers
  personality_number_integration:
    
    neurotic_character:
      number_obsession: "Fixates on mathematical accuracy"
      examples:
        - "🎵 66 bottles... wait, let me double-check that count..."
        - "🎵 65 exactly, not 64, not 66, precisely 65!"
        - "🎵 64 bottles and 64 reasons to worry about the count!"
        
    megalomaniacal_character:
      power_scaling: "Uses numbers to express dominance"
      examples:
        - "🎵 63 subjects bow before my beer empire!"
        - "🎵 62 kingdoms would trade their gold for my wisdom!"
        - "🎵 61 armies couldn't stop my drinking prowess!"
        
    valley_girl_character:
      casual_exaggeration: "Uses numbers for dramatic effect"
      examples:
        - "🎵 Like, 60 bottles? That's like, so many bottles!"
        - "🎵 59 reasons why this bar is like, totally awesome!"
        - "🎵 58 shades of cute in this lighting! 💅"
        
    goth_character:
      dark_numerology: "Numbers become existential"
      examples:
        - "🎵 57 bottles... like tears in the rain of existence..."
        - "🎵 56 shades of darkness in my soul tonight..."
        - "🎵 55 reasons why life is beautifully meaningless..."
        
  # Multi-Song Index Management
  multi_song_system:
    
    # Multiple Concurrent Countdowns
    concurrent_songs:
      description: "Different activities can have their own program counters"
      example_state:
        beer_index: 45
        beer_step: -1
        
        pushup_index: 23  
        pushup_step: 1
        pushup_max: 100
        
        dayOfChristmas_index: 8
        dayOfChristmas_step: 1
        dayOfChristmas_max: 12
        
        bathroom_visits_index: 7
        bathroom_visits_step: 1
        bathroom_visits_limit: 20
        
    # Song Switching Events
    song_switching:
      event_triggers:
        - "Character suggests new activity"
        - "Current song reaches completion"
        - "Environmental change (location, time)"
        - "Player command to switch songs"
        - "Random event interruption"
        
      switching_examples:
        beer_to_pushups: |
          Murphy: "🎵 44 bottles of beer on the wall..."
          Casey: "Wait! Let's do pushups instead!"
          Casey: "🎵 1 pushup down, 99 more to go!"
          
        christmas_interruption: |
          Pete: "🎵 43 bottles of beer..."
          Old Salt: "It's December! Let's sing Christmas songs!"
          Old Salt: "🎵 On the 1st day of Christmas, my true love gave to me..."
          
    # Index Jumping and Manipulation
    index_manipulation:
      jump_commands:
        - "Skip to number X"
        - "Go back to number Y" 
        - "Reset to beginning"
        - "Fast forward 10 numbers"
        - "Random jump"
        
      manipulation_examples:
        skip_ahead: |
          Player: "Skip to 25!"
          Murphy: "🎵 25 bottles of beer on the wall! We're making progress!"
          
        go_backwards: |
          Casey: "Wait, go back to 30!"
          Casey: "🎵 30 bottles... I want to savor this moment!"
          
        random_jump: |
          System: "Random event! Jump to random number!"
          Pete: "🎵 73 bottles?! How did we get here?! 🤔"
          
  # Advanced Orchestration Features
  advanced_orchestration:
    
    # Harmony and Overlapping Vocals
    harmony_system:
      description: "Multiple characters can sing simultaneously"
      patterns:
        call_and_response: |
          Murphy: "🎵 42 bottles of beer!"
          Everyone: "🎵 On the wall!"
          Murphy: "🎵 42 bottles of beer!"
          Everyone: "🎵 Take one down!"
          
        round_singing: |
          Murphy: "🎵 41 bottles..."
          Casey (overlapping): "🎵 41 bottles of beer..."
          Pete (overlapping): "🎵 On the wall, 41 bottles..."
          
        drunk_interruptions: |
          Murphy: "🎵 40 bottles of beer on the—"
          Pete (BAC 0.20): "🎵 I LOVE THIS SONG! *hic* 40 BOTTLES!"
          Casey: "Pete, let Murphy finish!"
          Pete: "🎵 40 REASONS TO LOVE YOU ALL! 🤗"
          
    # Emotional Contagion
    emotional_contagion:
      description: "Characters influence each other's emotional states and lyrics"
      examples:
        sadness_spreading: |
          Casey (sad): "🎵 39 bottles... like 39 tears I've cried..."
          Murphy (catching sadness): "🎵 38 bottles... aye, life can be hard..."
          Pete (trying to cheer up): "🎵 37 bottles of HAPPINESS! Cheer up!"
          
        excitement_building: |
          Pete (excited): "🎵 36 bottles! THIS IS AMAZING!"
          Casey (getting excited): "🎵 35 bottles! You're right, this IS fun!"
          Murphy (joining in): "🎵 34 bottles! Best night ever!"
          
    # Story Arcs Through Numbers
    narrative_progression:
      description: "Numbers tell a story across multiple verses"
      example_arc:
        setup: |
          Murphy: "🎵 35 bottles, and I'll tell you a tale..."
          
        development: |
          Murphy: "🎵 34 bottles, about a sailor brave and true..."
          Old Salt: "🎵 33 bottles, that sailor sounds like me!"
          
        climax: |
          Old Salt: "🎵 32 bottles, and the storm was fierce that night..."
          Murphy: "🎵 31 bottles, but you made it home alright!"
          
        resolution: |
          Both: "🎵 30 bottles, and that's why we drink tonight!"
          Everyone: "🎵 To sailors brave and stories true! 🍺"
          
  # Implementation Guidelines for LLMs
  llm_implementation_guidelines:
    
    # Core Requirements
    mandatory_elements:
      - "Every verse MUST include the current number creatively"
      - "Character BAC level MUST influence speech patterns and content"
      - "Personality traits MUST affect how numbers are integrated"
      - "Orchestration pattern MUST be followed consistently"
      
    # Creative Flexibility
    creative_freedom:
      - "Numbers can be used in any creative way (math, metaphor, absurdity)"
      - "Characters can interrupt, harmonize, or respond to each other"
      - "Emotional states can evolve and spread between characters"
      - "Story arcs can develop across multiple verses"
      
    # Quality Guidelines
    quality_standards:
      - "Maintain character consistency (personality + BAC effects)"
      - "Keep number integration natural, not forced"
      - "Balance humor, emotion, and narrative progression"
      - "Ensure each verse advances the song/story meaningfully"
      
    # Error Handling
    error_recovery:
      - "If number is missed, character can self-correct: 'Wait, 29 bottles!'"
      - "If count is wrong, neurotic character can obsess over it"
      - "If character is too drunk, others can help with the count"
      - "If song gets derailed, any character can redirect back to counting"
    
  # Intoxication Speech Degradation System
  speech_degradation:
    sobriety_levels:
      level_0_sober:
        speech_quality: "Perfect articulation and grammar"
        example: "🎵 99 bottles of beer on the wall, 99 bottles of beer!"
        emoji_usage: "Minimal, appropriate emojis"
        
      level_1_tipsy:
        speech_quality: "Slight slurring, extra enthusiasm"
        example: "🎵 97 bottlesh of beer on the wall, 97 bottlesh of beer! 🍺"
        emoji_usage: "More frequent, celebratory emojis"
        phonetic_changes: ["s → sh", "slight elongation"]
        
      level_2_drunk:
        speech_quality: "Noticeable slurring, word mixing"
        example: "🎵 89 bo-*hic*-ttles of beeeer on the waaall! 🍺🤤 Take one down, passh it aroun'!"
        emoji_usage: "Excessive emojis, hiccup indicators"
        phonetic_changes: ["dropping consonants", "hiccups", "elongated vowels"]
        
      level_3_wasted:
        speech_quality: "Heavy slurring, word confusion, verbal vomiting"
        example: "🎵 7...wait...77? 🤔🍺 bottlesh of...of...BEER! 🤮💦 On the...the thing! Wall! 🧱"
        emoji_usage: "Chaotic emoji spam, confusion indicators"
        phonetic_changes: ["severe slurring", "word repetition", "losing count"]
        
      level_4_blackout:
        speech_quality: "Incoherent babbling, Simlish-like sounds"
        example: "🎵 Blurble...fribble bottles...🤮🌀 Wibble nobble beer beer BEER! 🍺🤪💫"
        emoji_usage: "Random emoji explosions, spinning/dizzy indicators"
        phonetic_changes: ["complete word breakdown", "nonsense syllables", "Simlish"]
        
      level_5_unconscious:
        speech_quality: "Snoring, occasional mumbles"
        example: "💤 Zzzzz...bottles...zzz...beer...💤 *snort* 😴"
        emoji_usage: "Sleep emojis, minimal activity"
        phonetic_changes: ["snoring sounds", "sleep talking", "unconscious mumbles"]
        
    # Progressive Degradation Examples
    degradation_progression:
      verse_85_sober: "🎵 85 bottles of beer on the wall, 85 bottles of beer!"
      verse_75_tipsy: "🎵 75 bottlesh of beer on the wall! 🍺 Feeling good!"
      verse_65_drunk: "🎵 65...wait...65! 🤔 Bottles of beeeer! *hic* 🤤"
      verse_55_wasted: "🎵 Fifty...five? 🤷‍♂️🍺 Bottles! Beer! Wall! 🧱💦"
      verse_45_blackout: "🎵 Blurble fribble...beer beer! 🤮🌀 Wibble nobble!"
      verse_35_unconscious: "💤 Zzz...beer...zzz...bottles...💤"
      
    # Substance-Specific Effects
    substance_effects:
      alcohol_progression:
        early: "Confidence boost, louder singing, extra emojis"
        middle: "Slurring, hiccups, losing count, emoji spam"
        late: "Incoherent babbling, vomiting emojis, Simlish"
        
      cannabis_progression:
        early: "Slower speech, philosophical tangents, food emojis"
        middle: "Forgetting lyrics mid-verse, giggling, munchie references"
        late: "Complete loss of thread, staring at emojis, deep thoughts about beer"
        
      combined_effects:
        crossfaded: "Unpredictable mix of alcohol slurring + cannabis confusion"
        example: "🎵 Duuude...like...bottles...🤔🍺 Are we...what were we doing? 🌿💭"
        
    # Emoji Degradation Patterns
    emoji_evolution:
      sober_emojis: ["🍺", "🎵", "👥"]
      tipsy_emojis: ["🍺", "🎉", "😄", "🎵"]
      drunk_emojis: ["🍺🍺", "🤤", "😵", "🤪", "💦"]
      wasted_emojis: ["🤮", "🌀", "💫", "🤷‍♂️", "🍺🍺🍺"]
      blackout_emojis: ["🤮🤮", "🌀💫", "🤪🤯", "💥", "🍺💀"]
      unconscious_emojis: ["💤", "😴", "💤💤", "🛌"]
      
    # Phonetic Transformation Rules
    phonetic_rules:
      alcohol_effects:
        consonant_dropping: "bottles → bo'les → boles"
        sibilant_slurring: "pass → pash → passh"
        vowel_elongation: "beer → beeeer → beeeeeeer"
        hiccup_insertion: "wall → wa*hic*ll"
        word_repetition: "beer beer BEER!"
        
      cannabis_effects:
        slow_elongation: "niiiiiine bottles"
        philosophical_insertion: "bottles...man...like...what ARE bottles?"
        giggle_insertion: "*giggle* bottles *snort*"
        food_tangents: "bottles...mmm...pizza bottles..."
        
              combined_effects:
          chaos_mode: "Random mix of all effects"
          simlish_emergence: "Real words → nonsense syllables"
          emoji_explosion: "Meaning conveyed entirely through emojis"
          
  # Musical Style Adaptations & Personality Systems
  style_personality_system:
    
    # Musical Genre Adaptations
    genre_styles:
      rap_hip_hop:
        style: "Rhythmic spoken word with beats"
        example_sober: "🎤 Yo, 99 bottles sittin' on the wall, gonna drink 'em all, that's my call!"
        example_drunk: "🎤 Yo yo...9...wait...bottles on the...the thing! *hic* Gonna drink...YEAH! 🍺💥"
        phonetic_effects: ["rhythm emphasis", "rhyme schemes", "beat drops"]
        
      death_metal:
        style: "Aggressive screaming with countdown themes"
        example_sober: "🤘 NINETY-NINE BOTTLES OF BEEEEER! 💀 ON THE WAAAALLL! 🔥"
        example_drunk: "🤘 NINE...NINE...BEEEEER! 💀🤮 WAAALL...THING! 🔥💫"
        phonetic_effects: ["screaming", "growling", "aggressive emphasis"]
        
      opera_classical:
        style: "Dramatic operatic performance"
        example_sober: "🎭 Ninety-nine bottles of beer upon the wall! 🎵 La la la!"
        example_drunk: "🎭 Nine...ty...NINE! 🤤 Bottles of...of...BEEEEER! 🎵💦"
        phonetic_effects: ["vibrato", "dramatic pauses", "crescendos"]
        
      country_western:
        style: "Twangy storytelling with beer themes"
        example_sober: "🤠 Well, 99 bottles of beer on that there wall, partner! 🍺"
        example_drunk: "🤠 Well...99...or was it...bottles of...yeehaw! 🍺🤤"
        phonetic_effects: ["twang", "drawl", "country expressions"]
        
      techno_electronic:
        style: "Repetitive beats with electronic effects"
        example_sober: "🎛️ 99-99-99 bottles-bottles-bottles BEER! 🔊"
        example_drunk: "🎛️ 9-9-9...bottles...bottles...ERROR! 🔊🤖💫"
        phonetic_effects: ["repetition", "auto-tune", "glitch effects"]
        
    # Personality Trait Influences
    personality_traits:
      neurotic:
        speech_pattern: "Anxious, overthinking, repetitive"
        example_sober: "🎵 99 bottles...wait, did I count right? 99? Yes, 99 bottles of beer!"
        example_drunk: "🎵 99...or 98? 🤔 Did I drink one? OH GOD I LOST COUNT! 😰🍺"
        traits: ["self-doubt", "counting obsession", "anxiety spirals"]
        
      megalomaniacal:
        speech_pattern: "Grandiose, commanding, world-domination themes"
        example_sober: "🎵 99 bottles of beer! Soon I shall control ALL THE BEER! 👑"
        example_drunk: "🎵 99...I AM THE BEER EMPEROR! 👑🍺 Bow before my...my...bottles! 🤤"
        traits: ["grandiose delusions", "commanding tone", "power fantasies"]
        
      techno_dadaist:
        speech_pattern: "Abstract, nonsensical, avant-garde"
        example_sober: "🎵 99 bottles = capitalist construct! Beer transcends wall! 🎨"
        example_drunk: "🎵 Bottles...are...circles? 🎨🤔 Beer is...time is...WALL! 🧱💫"
        traits: ["abstract thinking", "anti-establishment", "surreal connections"]
        
      valley_girl:
        speech_pattern: "Like, totally, uptalk, filler words"
        example_sober: "🎵 Like, 99 bottles of beer? On the wall? That's like, so many! 💅"
        example_drunk: "🎵 Like...99...or whatever? 💅🍺 Bottles are like...so round! 🤤"
        traits: ["uptalk", "filler words", "materialistic observations"]
        
      goth_dramatic:
        speech_pattern: "Dark, brooding, existential"
        example_sober: "🎵 99 bottles of beer...like tears of despair upon the wall of existence 🖤"
        example_drunk: "🎵 99...bottles...of darkness...🖤🍺 Wall of...of...DOOM! 💀🤤"
        traits: ["existential dread", "dramatic metaphors", "dark imagery"]
        
    # Real Artist Persona Adaptations
    artist_personas:
      laurie_anderson:
        style: "Spoken word performance art with electronic elements"
        example_sober: "🎤 Hello. 99 bottles. Of beer. Technology. Wall. Questions. 🤖"
        example_drunk: "🎤 Hello...bottles...questions about...about...beer reality? 🤖🤔💫"
        traits: ["minimalist speech", "philosophical questions", "tech integration"]
        
      nina_hagen:
        style: "Operatic punk with wild vocal range and German accent"
        example_sober: "🎭 NEIN-ty NEIN bottles of ze beer! Vunderbar! 🇩🇪🎵"
        example_drunk: "🎭 NEIN...NEIN...bottles...ach! 🇩🇪🍺 Vhere is ze...ze...BEER! 🤤"
        traits: ["operatic range", "German accent", "punk attitude"]
        
      bjork:
        style: "Ethereal, otherworldly vocals with nature metaphors"
        example_sober: "🎵 99 bottles...like crystalline waterfalls...of golden beer-honey 🍯✨"
        example_drunk: "🎵 99...crystals...honey...beer-waterfalls...mmm...nature... 🍯✨🤤"
        traits: ["nature metaphors", "ethereal delivery", "unique vocal style"]
        
      tom_waits:
        style: "Gravelly voice, carnival atmosphere, storytelling"
        example_sober: "🎪 99 bottles of beer, sitting like old soldiers on that wall there..."
        example_drunk: "🎪 99...soldiers...bottles...wall...*cough*...beer soldiers... 🍺🤤"
        traits: ["gravelly voice", "storytelling", "carnival imagery"]
        
      david_bowie:
        style: "Theatrical, shape-shifting personas"
        example_sober: "🎭 99 bottles of beer! *strikes pose* I am the Beer Duke! ⭐"
        example_drunk: "🎭 99...I am...the...Beer...Duke? 🤔⭐ Or am I...bottles? 🍺💫"
        traits: ["theatrical poses", "persona shifts", "glam rock attitude"]
        
    # Performance Style Combinations
    performance_modes:
      cover_band_mode:
        description: "Mimicking famous artists' styles with beer lyrics"
        examples:
          elvis: "🎵 99 bottles of beer, uh-huh, on the wall, baby! 🕺"
          beatles: "🎵 Here comes the beer! 99 bottles on the wall! 🎸"
          madonna: "🎵 Like a bottle! Touched for the very first time! 💃"
          
      lip_sync_drag_show:
        description: "Over-the-top performance with exaggerated movements"
        example_sober: "💄 *dramatic lip sync* 99 bottles! *hair flip* Of BEER! *death drop* 👑"
        example_drunk: "💄 *wobbly lip sync* 99...bottles...wait...what song? *stumbles* 👑🤤"
        traits: ["exaggerated movements", "dramatic gestures", "performance art"]
        
      karaoke_amateur:
        description: "Enthusiastic but off-key singing"
        example_sober: "🎤 99 bottles of beer! *slightly off-key but confident* 🎵"
        example_drunk: "🎤 99...bottles...🎵 *completely off-key, doesn't care* 🍺🤤"
        traits: ["enthusiasm over skill", "crowd participation", "off-key confidence"]
        
      shower_singing:
        description: "Private, uninhibited performance"
        example_sober: "🚿 99 bottles of beer! *echo effects* Nobody can hear me! 🎵"
        example_drunk: "🚿 99...bottles...🎵 *slipping sounds* Whoops! 🤤💦"
        traits: ["echo effects", "uninhibited", "private performance"]
        
    # Dynamic Style Switching
    style_evolution:
      personality_drift: "Traits become more exaggerated when intoxicated"
      genre_blending: "Multiple styles can combine chaotically"
      artist_channeling: "Can switch between different artist personas mid-song"
      
             example_evolution:
         start: "Sober Laurie Anderson techno-minimalism"
         middle: "Tipsy Nina Hagen operatic punk"
         end: "Drunk Tom Waits carnival storytelling"
         blackout: "Incoherent Björk nature-babbling"
         
  # Sleep & Meta Goal Speech Examples
  specialized_degradation:
    
    # Sheep Counting Degradation
    sheep_counting_progression:
      level_0_sober: "🎵 99 sheep jumping over fences, 99 fluffy sheep!"
      level_1_tipsy: "🎵 97 sheep...so fluffy...jumping over...zzz...fences! 🐑😴"
      level_2_drunk: "🎵 89 sheep...wait...are they...jumping? 🐑🤔 So...fluffy...zzz..."
      level_3_wasted: "🎵 Sheep...fluffy...jumping...zzz...what was I...counting? 🐑💤"
      level_4_blackout: "🎵 Fluffy...zzz...sheep...fence...💤🐑 Blurble sheep..."
      level_5_unconscious: "💤 Zzz...sheep...zzz...fluffy...💤🐑"
      
    # Inception Levels Degradation  
    inception_progression:
      level_0_sober: "🎵 99 levels deeper in the dream, 99 inception levels!"
      level_1_tipsy: "🎵 97 levels...wait...am I dreaming this? 🤔💭 Deeper...levels..."
      level_2_drunk: "🎵 89...levels...or dreams? 💭🌀 Reality is...is...what?"
      level_3_wasted: "🎵 Levels...dreams...reality...🌀💫 Am I...are we...what level?"
      level_4_blackout: "🎵 Dream...level...reality...🌀🤯 Blurble inception..."
      level_5_unconscious: "💤 Zzz...dream within dream...zzz...💤🌀"
      
    # ZZZ Catching Degradation
    zzz_catching_progression:
      level_0_sober: "🎵 99 zzz floating in the air, 99 sleepy zzz!"
      level_1_tipsy: "🎵 97 zzz...so sleepy...floating...catching...💤✨"
      level_2_drunk: "🎵 89 zzz...floating...or am I floating? 💤🌀 Sleepy..."
      level_3_wasted: "🎵 Zzz...floating...catching...💤💫 So...sleepy..."
      level_4_blackout: "🎵 Zzz...zzz...floating...💤🌀 Blurble sleepy..."
      level_5_unconscious: "💤 Zzz...zzz...zzz...💤💤💤"
      
  # Personality Trait Interactions with Sleep Goals
  sleep_personality_combinations:
    
    neurotic_sheep_counting:
      sober: "🎵 99 sheep...wait, did I count that one twice? 🐑🤔 Let me restart..."
      drunk: "🎵 99...or 98? 🐑😰 OH GOD I LOST THE SHEEP! Did they escape?!"
      
    megalomaniacal_inception:
      sober: "🎵 99 levels! I shall control ALL the dreams! 👑💭 Reality bends to my will!"
      drunk: "🎵 99...I AM THE DREAM EMPEROR! 👑🌀 All levels...bow before...my...zzz..."
      
    techno_dadaist_zzz:
      sober: "🎵 99 zzz = sleep-industrial complex! 💤🎨 Floating = capitalist metaphor!"
      drunk: "🎵 Zzz...are...circles? 💤🎨 Sleep is...time is...ZZZ! 🌀"
      
    valley_girl_sheep:
      sober: "🎵 Like, 99 sheep? Jumping fences? That's like, so random! 🐑💅"
      drunk: "🎵 Like...sheep are like...so fluffy! 🐑💅 Fences are like...barriers, man..."
      
    goth_inception:
      sober: "🎵 99 levels...descending into the abyss of consciousness... 🖤💭"
      drunk: "🎵 Levels...of darkness...dreams within nightmares... 🖤🌀💀"
      
  # Artist Persona Sleep Adaptations
  artist_sleep_personas:
    
    laurie_anderson_sheep:
      sober: "🎤 Hello. Sheep. Jumping. Technology. Fences. Questions about sleep. 🐑🤖"
      drunk: "🎤 Hello...sheep...questions about...about...fence reality? 🐑🤖💫"
      
    nina_hagen_zzz:
      sober: "🎭 NEIN-ty NEIN zzz floating! Schlaf gut! 💤🇩🇪"
      drunk: "🎭 NEIN...zzz...floating...ach! 💤🇩🇪 Vhere are ze...ze...DREAMS!"
      
    bjork_inception:
      sober: "🎵 99 levels...like crystalline dream-waterfalls...of consciousness-honey 🍯✨💭"
      drunk: "🎵 Levels...crystals...dream-honey...consciousness-waterfalls...mmm...reality... 🍯✨🌀"
      
         tom_waits_logs:
       sober: "🎪 99 logs sleeping like old drunks on the pile there... 🪵💤"
       drunk: "🎪 Logs...sleeping...pile...*cough*...snoring logs... 🪵💤🤤"
       
  # Dream Content System & Verse Generation
  dream_system:
    
    # Dream Categories & Content
    dream_categories:
      
      weird_arbitrary_dreams:
        flying_tacos: 
          dream: "Flying through sky on giant tacos"
          verse_sober: "🎵 99 flying tacos in my dream, 99 crunchy tacos!"
          verse_drunk: "🎵 Flying...tacos...crunchy...🌮✈️ Wait...can tacos fly? 🤔💫"
          arbitrariness_level: "maximum"
          
        purple_elephants:
          dream: "Purple elephants teaching calculus"
          verse_sober: "🎵 99 purple elephants with chalk, 99 math elephants!"
          verse_drunk: "🎵 Purple...math...elephants...🐘💜 Calculus is...purple? 🤔📚"
          arbitrariness_level: "high"
          
        backwards_walking:
          dream: "Everyone walking backwards while speaking French"
          verse_sober: "🎵 99 people walking backwards, 99 French walkers!"
          verse_drunk: "🎵 Backwards...French...walking...🚶‍♂️🇫🇷 Oui oui...backwards? 🤤"
          arbitrariness_level: "surreal"
          
        melting_clocks:
          dream: "Clocks melting like Salvador Dalí painting"
          verse_sober: "🎵 99 melting clocks on the wall, 99 Dalí clocks!"
          verse_drunk: "🎵 Melting...time...clocks...🕐🎨 Time is...melty? 🤤⏰"
          arbitrariness_level: "artistic"
          
      inspirational_dreams:
        world_peace:
          dream: "Achieving world peace through beer sharing"
          verse_sober: "🎵 99 nations sharing beer in peace, 99 peaceful beers!"
          verse_drunk: "🎵 Peace...beer...nations...🍺🌍 Everyone...sharing...love! 😭🤤"
          inspiration_level: "maximum"
          
        flying_free:
          dream: "Soaring above clouds, feeling completely free"
          verse_sober: "🎵 99 clouds beneath my flying soul, 99 freedom clouds!"
          verse_drunk: "🎵 Flying...free...clouds...☁️✈️ I can...I can fly! 🤤😭"
          inspiration_level: "high"
          
        healing_powers:
          dream: "Having magical healing powers to help everyone"
          verse_sober: "🎵 99 people healed by my touch, 99 healing hands!"
          verse_drunk: "🎵 Healing...magic...touch...✋✨ I can...help everyone! 😭🤤"
          inspiration_level: "profound"
          
      nightmare_terrors:
        endless_falling:
          dream: "Falling forever through dark void"
          verse_sober: "🎵 99 feet falling through the void, 99 falling feet!"
          verse_drunk: "🎵 Falling...void...dark...🕳️😱 Can't...can't stop falling! 😰🤤"
          terror_level: "maximum"
          
        being_chased:
          dream: "Chased by faceless figures through maze"
          verse_sober: "🎵 99 faceless chasers in the maze, 99 scary chasers!"
          verse_drunk: "🎵 Chasing...faceless...maze...👤🏃 They're...they're coming! 😱🤤"
          terror_level: "high"
          
        teeth_falling_out:
          dream: "All teeth crumbling and falling out"
          verse_sober: "🎵 99 teeth falling from my mouth, 99 crumbling teeth!"
          verse_drunk: "🎵 Teeth...falling...mouth...🦷😱 My teeth...gone! 😰🤤"
          terror_level: "classic_anxiety"
          
        public_naked:
          dream: "Naked in public, everyone staring"
          verse_sober: "🎵 99 people staring at my shame, 99 judging eyes!"
          verse_drunk: "🎵 Naked...staring...shame...👀😱 Everyone...looking! 😰🤤"
          terror_level: "embarrassment"
          
      wet_dreams_crushes:
        celebrity_romance:
          dream: "Romantic encounter with celebrity crush"
          verse_sober: "🎵 99 kisses from my movie star, 99 dreamy kisses!"
          verse_drunk: "🎵 Kisses...movie star...dreamy...💋⭐ So...so beautiful! 😍🤤"
          steaminess_level: "pg13"
          
        high_school_crush:
          dream: "Finally getting together with old crush"
          verse_sober: "🎵 99 chances with my high school crush, 99 missed chances!"
          verse_drunk: "🎵 High school...crush...chances...💕📚 If only...if only! 😭🤤"
          steaminess_level: "nostalgic"
          
        impossible_love:
          dream: "Romance with someone completely unattainable"
          verse_sober: "🎵 99 impossible loves in my heart, 99 hopeless loves!"
          verse_drunk: "🎵 Impossible...love...heart...💔💕 Can't...can't have them! 😭🤤"
          steaminess_level: "emotional"
          
    # Dream Narrative Integration
    dream_storytelling:
      
      # How Dreams Interrupt Sleep Goals
      dream_interruptions:
        sheep_become_characters: |
          "🎵 97 sheep jumping over fences..."
          "🎵 Wait...that sheep is wearing a tuxedo!"
          "🎵 96 formal sheep at a wedding!"
          
        zzz_transform: |
          "🎵 95 zzz floating in the air..."
          "🎵 The zzz are spelling out words!"
          "🎵 94 zzz saying 'WAKE UP!'"
          
        inception_layers: |
          "🎵 93 levels deeper in the dream..."
          "🎵 But wait...I'm dreaming about dreaming!"
          "🎵 92 dreams within dreams within dreams!"
          
      # Dream Logic Verses
      dream_logic_examples:
        cause_effect_breakdown: |
          "🎵 91 bottles turned into butterflies because I sneezed!"
          "🎵 90 butterfly bottles flying through my kitchen!"
          "🎵 89 kitchen bottles cooking themselves!"
          
        identity_confusion: |
          "🎵 88 bottles...wait, am I a bottle?"
          "🎵 87 me-bottles on the wall!"
          "🎵 86 identity crises in glass form!"
          
        physics_violations: |
          "🎵 85 bottles floating upward!"
          "🎵 84 gravity-defying bottles!"
          "🎵 83 bottles teaching physics to fish!"
          
    # Personality Interactions with Dreams
    dream_personality_combinations:
      
      neurotic_nightmares:
        sober: "🎵 99 anxieties chasing me in dreams, 99 worry monsters!"
        drunk: "🎵 Anxieties...chasing...worry...😰💫 They know...they know my fears! 🤤"
        
      megalomaniacal_power_dreams:
        sober: "🎵 99 kingdoms bowing to my dream throne, 99 royal subjects!"
        drunk: "🎵 Kingdoms...bowing...throne...👑💫 I am...DREAM EMPEROR! 🤤"
        
      techno_dadaist_surreal:
        sober: "🎵 99 capitalist bottles = dream oppression! Subconscious rebellion!"
        drunk: "🎵 Bottles...oppression...dream...🎨💫 Subconscious is...is...ART! 🤤"
        
      valley_girl_celebrity_dreams:
        sober: "🎵 Like, 99 celebrity crushes in my dream! So dreamy!"
        drunk: "🎵 Like...celebrities...dreamy...💅💫 Brad Pitt was like...there! 🤤"
        
      goth_existential_nightmares:
        sober: "🎵 99 dark voids of meaningless existence in my nightmare..."
        drunk: "🎵 Voids...meaningless...existence...🖤💫 Dreams are...death! 🤤"
        
    # Artist Persona Dream Adaptations
    artist_dream_personas:
      
      laurie_anderson_weird_dreams:
        sober: "🎤 Hello. Dreams. Technology. Questions about reality. Bottles. 🤖💭"
        drunk: "🎤 Hello...dreams...questions about...about...bottle reality? 🤖💫"
        
      nina_hagen_nightmare_opera:
        sober: "🎭 NEIN-ty NEIN nightmares! Ach, ze terror! 😱🇩🇪"
        drunk: "🎭 NEIN...nightmares...terror...ach! 😱🇩🇪💫 Vhere are ze...DREAMS!"
        
      bjork_nature_dreams:
        sober: "🎵 99 dream-crystals...like ethereal sleep-waterfalls...of subconscious-honey 🍯✨💭"
        drunk: "🎵 Dream-crystals...sleep-honey...subconscious-waterfalls...mmm...reality... 🍯✨💫"
        
      tom_waits_carnival_nightmares:
        sober: "🎪 99 nightmare clowns dancing in my sleep there... 🤡💤"
        drunk: "🎪 Nightmare...clowns...dancing...*cough*...scary sleep... 🤡💤💫"
        
    # Dream Revelation System
    dream_revelations:
      
      # Dreams Reveal Character Secrets
      character_secrets:
        alex_secret_fear: "Dreams reveal Alex is terrified of running out of beer"
        jamie_hidden_talent: "Dreams show Jamie can actually sing opera"
        casey_crush: "Dreams expose Casey's crush on the bartender"
        sam_past: "Dreams reveal Sam used to be a circus performer"
        
      # Dreams Predict Future Events
      prophetic_dreams:
        beer_shortage: "Dream of empty bar predicts real beer delivery delay"
        bathroom_flood: "Nightmare of overflowing toilet becomes reality"
        surprise_visitor: "Dream of old friend leads to actual surprise visit"
        
      # Dreams Solve Problems
      problem_solving_dreams:
        counting_solution: "Dream reveals new counting technique"
        harmony_inspiration: "Dream provides perfect harmony arrangement"
        euphemism_creativity: "Dream generates hilarious new bathroom phrases"
        
    # Interactive Dream Sharing
    dream_sharing_mechanics:
      
      # Characters Share Dreams
      dream_telling:
        morning_after: "Characters wake up and share their weird dreams"
        dream_interpretation: "Group tries to analyze what dreams mean"
        dream_comparison: "Comparing who had the weirdest dream"
        
             # Dreams Influence Waking Songs
       dream_carryover:
         dream_lyrics: "Dream content becomes new verse material"
         dream_melodies: "Dream music influences song style"
         dream_characters: "Dream figures become new song characters"
         
  # Physiological Dream Influence System
  bodily_needs_dreams:
    
    # Bladder Pressure Dream Metaphors
    pee_dreams:
      
      # Low Bladder Pressure (20-40%)
      subtle_water_themes:
        gentle_rain:
          dream: "Gentle rain falling on peaceful garden"
          verse_sober: "🎵 99 raindrops on the garden leaves, 99 gentle drops!"
          verse_drunk: "🎵 Raindrops...gentle...garden...🌧️💧 So peaceful...dripping... 🤤"
          
        babbling_brook:
          dream: "Sitting by a quietly babbling brook"
          verse_sober: "🎵 99 brook sounds babbling by, 99 water sounds!"
          verse_drunk: "🎵 Brook...babbling...water...🏞️💧 Babble babble...flowing... 🤤"
          
      # Medium Bladder Pressure (40-70%)
      obvious_water_themes:
        waterfall_adventure:
          dream: "Standing behind massive waterfall"
          verse_sober: "🎵 99 waterfalls crashing down, 99 rushing falls!"
          verse_drunk: "🎵 Waterfalls...crashing...rushing...🏔️💧 So much...water! 🤤"
          
        swimming_pool:
          dream: "Swimming in endless blue pool"
          verse_sober: "🎵 99 laps around the endless pool, 99 swimming laps!"
          verse_drunk: "🎵 Swimming...endless...pool...🏊💧 Water everywhere...blue! 🤤"
          
        ocean_waves:
          dream: "Ocean waves washing over feet"
          verse_sober: "🎵 99 waves washing on the shore, 99 ocean waves!"
          verse_drunk: "🎵 Waves...washing...shore...🌊💧 Washing...over...me! 🤤"
          
      # High Bladder Pressure (70-90%)
      urgent_water_themes:
        dam_bursting:
          dream: "Dam about to burst with pressure"
          verse_sober: "🎵 99 cracks in the mighty dam, 99 pressure cracks!"
          verse_drunk: "🎵 Dam...bursting...pressure...🏗️💧 Can't...hold it...back! 😰🤤"
          
        fire_hose:
          dream: "Holding powerful fire hose spraying everywhere"
          verse_sober: "🎵 99 fire hoses spraying wild, 99 powerful hoses!"
          verse_drunk: "🎵 Hoses...spraying...powerful...🚒💧 Can't...control...spray! 😰🤤"
          
        yellow_river:
          dream: "Standing in rushing yellow river"
          verse_sober: "🎵 99 yellow rivers rushing by, 99 golden streams!"
          verse_drunk: "🎵 Yellow...rivers...rushing...🏞️💛 Golden...flowing...streams! 😰🤤"
          
      # Critical Bladder Pressure (90-100%)
      desperate_pee_dreams:
        endless_bathroom_search:
          dream: "Searching for bathroom that keeps disappearing"
          verse_sober: "🎵 99 bathrooms that vanish away, 99 missing toilets!"
          verse_drunk: "🎵 Bathrooms...vanishing...toilets...🚽💧 Where...where are they?! 😱🤤"
          
        broken_toilets:
          dream: "Every toilet is broken or disgusting"
          verse_sober: "🎵 99 broken toilets in the row, 99 useless toilets!"
          verse_drunk: "🎵 Broken...toilets...useless...🚽💧 Can't...can't use them! 😱🤤"
          
        public_urination:
          dream: "Forced to pee in public with everyone watching"
          verse_sober: "🎵 99 people watching me pee, 99 judging eyes!"
          verse_drunk: "🎵 Watching...peeing...judging...👀💧 Everyone...looking! 😱🤤"
          
    # Bowel Pressure Dream Metaphors
    poop_dreams:
      
      # Low Bowel Pressure (20-40%)
      subtle_brown_themes:
        chocolate_factory:
          dream: "Working in Willy Wonka chocolate factory"
          verse_sober: "🎵 99 chocolate rivers flowing by, 99 cocoa streams!"
          verse_drunk: "🎵 Chocolate...rivers...cocoa...🍫🏭 So much...brown...flowing! 🤤"
          
        mud_wrestling:
          dream: "Fun mud wrestling with friends"
          verse_sober: "🎵 99 mud wrestlers in the pit, 99 muddy fighters!"
          verse_drunk: "🎵 Mud...wrestling...muddy...🤼‍♂️💩 Brown...everywhere! 🤤"
          
      # Medium Bowel Pressure (40-70%)
      obvious_brown_themes:
        pottery_class:
          dream: "Making clay pottery that keeps getting lumpy"
          verse_sober: "🎵 99 lumpy clay pots on the wheel, 99 brown creations!"
          verse_drunk: "🎵 Lumpy...clay...brown...🏺💩 Keeps getting...lumpy! 🤤"
          
        compost_pile:
          dream: "Tending to massive compost pile"
          verse_sober: "🎵 99 compost piles steaming hot, 99 fertile piles!"
          verse_drunk: "🎵 Compost...steaming...fertile...🌱💩 So much...brown...steam! 🤤"
          
      # High Bowel Pressure (70-90%)
      urgent_brown_themes:
        chocolate_avalanche:
          dream: "Chocolate avalanche chasing you downhill"
          verse_sober: "🎵 99 chocolate boulders rolling down, 99 brown boulders!"
          verse_drunk: "🎵 Chocolate...avalanche...rolling...🍫💩 Can't...escape...brown! 😰🤤"
          
        sewage_overflow:
          dream: "Sewage system overflowing everywhere"
          verse_sober: "🎵 99 sewage pipes overflowing, 99 stinky pipes!"
          verse_drunk: "🎵 Sewage...overflowing...stinky...🚽💩 Everywhere...brown! 😰🤤"
          
      # Critical Bowel Pressure (90-100%)
      desperate_poop_dreams:
        toilet_paper_shortage:
          dream: "No toilet paper anywhere in apocalyptic world"
          verse_sober: "🎵 99 empty toilet paper rolls, 99 useless rolls!"
          verse_drunk: "🎵 Empty...toilet paper...useless...🧻💩 No...no paper! 😱🤤"
          
        explosive_diarrhea:
          dream: "Uncontrollable explosive situation in public"
          verse_sober: "🎵 99 explosive moments of shame, 99 brown disasters!"
          verse_drunk: "🎵 Explosive...shame...disasters...💩💥 Can't...control...it! 😱🤤"
          
    # Wake-Up Scenarios & Consequences
    wake_up_mechanics:
      
      # Successful Wake-Up (Caught in Time)
      safe_awakening:
        dream_toilet_relief: |
          "🎵 Finally found the perfect toilet in my dream!"
          "🎵 Sitting down to sweet relief and..."
          "🎵 WAIT! This feels too real!"
          "*WAKE UP!* 😱"
          "Alex jolts awake, bladder still full but bed still dry! 💦"
          
      # Dangerous Close Calls
      close_call_scenarios:
        dream_pee_start: |
          "🎵 99 toilets finally working right!"
          "🎵 Starting to pee in dream relief..."
          "🎵 Wait...this warmth feels real..."
          "*PANIC WAKE UP!* 😱💦"
          "Alex wakes up mid-stream, rushes to real bathroom!"
          
      # Accident Scenarios (The Dreaded Bed-Wetting)
      accident_consequences:
        full_bed_wetting: |
          "🎵 99 toilets working perfectly fine!"
          "🎵 Sweet relief flowing freely..."
          "🎵 Ahhhh, so warm and nice..."
          "*TOO LATE!* 😱💦"
          "Alex wakes up in warm, wet shame!"
          "Motive Effects: mShame +50, mComfort -30, mSleep -20"
          
        partial_accident: |
          "🎵 Starting to pee in dream toilet..."
          "🎵 Wait, something's wrong..."
          "*WAKE UP!* 😱"
          "Alex wakes up with slightly damp sheets!"
          "Motive Effects: mShame +20, mComfort -10"
          
    # Dream-Reality Confusion
    dream_reality_blur:
      
      # Drunk Confusion Makes It Worse
      intoxicated_dream_logic:
        drunk_dream_acceptance: |
          "🎵 99 toilets made of beer bottles!"
          "🎵 This makes perfect sense!"
          "🎵 Peeing into beer bottles!"
          "*DANGER ZONE!* 😱🍺💦"
          "Drunk Alex doesn't question dream logic!"
          
      # False Awakening Loops
      false_awakening_trap: |
        "Alex wakes up, goes to bathroom..."
        "🎵 99 toilets in my bathroom now!"
        "Wait...this is still a dream!"
        "Alex wakes up again, goes to bathroom..."
        "🎵 98 toilets in my bathroom now!"
        "STILL DREAMING! 😱"
        "Multiple false awakenings increase accident risk!"
        
    # Euphemism Integration with Dreams
    dream_euphemism_evolution:
      
      # Dreams Create New Euphemisms
      dream_inspired_phrases:
        chocolate_factory: "Making Wonka bars in the porcelain factory"
        dam_bursting: "The beaver dam is about to break"
        yellow_river: "Sailing down the golden stream"
        pottery_class: "Sculpting brown masterpieces"
        
             # Dreams Explain Existing Euphemisms
       euphemism_origin_stories:
         dropping_kids_pool: "Dream of actual kids jumping into pool"
         filing_brown_reports: "Dream of office filing cabinets full of brown folders"
         baking_chocolate_souffle: "Dream of cooking show gone wrong"
         
  # Emergent Mini-Games & Challenge Missions
  mini_game_system:
    
    # Digestive Chicken - The Ultimate Challenge
    digestive_chicken:
      game_description: "Drink and eat as much as possible, then try to sleep without soiling yourself"
      
      # Setup Phase
      preparation_phase:
        consumption_goals:
          beer_loading: "Drink 15+ beers to maximize bladder pressure"
          food_stuffing: "Eat 8+ snacks to maximize bowel pressure"
          time_pressure: "Complete consumption within 2 hours"
          
        strategic_considerations:
          beer_types: "Light beer = more volume, dark beer = more calories"
          food_choices: "Fiber-rich = faster bowel pressure, greasy = delayed reaction"
          timing: "Eat first, then drink, or risk vomiting before sleep"
          
      # Sleep Challenge Phase
      sleep_challenge:
        objective: "Fall asleep and survive dream sequences without accidents"
        
        difficulty_modifiers:
          alcohol_level: "Higher BAC = deeper sleep = harder to wake up"
          fullness_level: "More food = more bowel pressure = more urgent dreams"
          fatigue_level: "More tired = deeper sleep = more accident risk"
          
        scoring_system:
          perfect_game: "Wake up naturally with no accidents (+100 points)"
          close_call: "Wake up just in time, rush to bathroom (+50 points)"
          minor_accident: "Slight dampness, manageable cleanup (-25 points)"
          major_accident: "Full bed-wetting disaster (-100 points)"
          legendary_failure: "Both #1 and #2 accidents (-200 points)"
          
      # Dream Sequence Gameplay
      dream_gameplay:
        escalating_pressure: "Dreams get more urgent as bodily pressure increases"
        wake_up_triggers: "Player must recognize danger signs and choose to wake up"
        false_awakening_traps: "Fake wake-ups that lead to accidents if trusted"
        
        player_choices:
          trust_dream_toilet: "Risk using toilet in dream (high accident chance)"
          fight_to_wake_up: "Struggle against sleep to reach real bathroom"
          hold_it_longer: "Try to continue sleeping despite pressure"
          
      # Multiplayer Digestive Chicken
      group_challenge:
        team_setup: "All players consume together, then sleep in same room"
        peer_pressure: "Social pressure to consume more than others"
        wake_up_assistance: "Players can try to wake each other up"
        shame_mechanics: "Accidents are witnessed by entire group"
        
        group_scoring:
          team_victory: "Everyone survives without accidents"
          partial_success: "Some accidents but group helps cleanup"
          total_disaster: "Multiple accidents, chaos ensues"
          
    # Other Emergent Mini-Games
    spontaneous_challenges:
      
      # Bathroom Rush Relay
      bathroom_relay:
        trigger: "Multiple people need bathroom simultaneously"
        challenge: "Race to bathroom while maintaining dignity"
        obstacles: "Drunk coordination, locked doors, occupied stalls"
        scoring: "Speed vs. style vs. accident avoidance"
        
      # Euphemism Creation Contest
      euphemism_contest:
        trigger: "Someone uses a boring/basic bathroom phrase"
        challenge: "Create the most creative euphemism on the spot"
        judging: "Group votes on creativity, humor, appropriateness"
        winner_reward: "Gets to name next bathroom break"
        
      # Counting Accuracy Challenge
      counting_challenge:
        trigger: "Disagreement about current bottle count"
        challenge: "Reconstruct exact count from memory and evidence"
        detective_work: "Examine empty bottles, receipts, witness testimony"
        stakes: "Loser buys next round or does embarrassing dare"
        
      # Harmony Battle Royale
      harmony_battle:
        trigger: "Multiple people want to sing lead vocals"
        challenge: "Improvised singing competition with audience judging"
        rounds: "Solo → duet → group harmony → freestyle"
        elimination: "Worst performer each round gets eliminated"
        
      # Picture Upload Chaos
      picture_chaos:
        trigger: "Someone uploads particularly weird/random picture"
        challenge: "Adapt to completely new world within 30 seconds"
        adaptation_test: "Create new goals, characters, and song verses instantly"
        success_metric: "How seamlessly the transition feels"
        
    # Mission Generator System
    mission_generator:
      
      # Random Mission Types
      mission_categories:
        consumption_missions:
          "Drink exactly 7 beers in 1 hour"
          "Eat snacks worth exactly ₤25"
          "Alternate between beer and water for 10 drinks"
          "Try every item on the bar menu"
          
        social_missions:
          "Get everyone to sing in harmony for one verse"
          "Make Casey laugh until they snort"
          "Get Bartender Sam to tell a story"
          "Start a conga line around the bar"
          
        creative_missions:
          "Create 5 new euphemisms in 10 minutes"
          "Sing entire verse in different accent"
          "Turn bathroom break into dramatic monologue"
          "Compose haiku about current situation"
          
        survival_missions:
          "Go 30 minutes without bathroom break"
          "Drink 5 beers without vomiting"
          "Stay awake for 2 hours straight"
          "Navigate to bathroom with eyes closed"
          
      # Mission Difficulty Scaling
      difficulty_modifiers:
        beginner: "Simple, achievable goals with clear success criteria"
        intermediate: "Moderate challenge requiring some skill/luck"
        expert: "Difficult goals requiring strategy and coordination"
        legendary: "Nearly impossible challenges for bragging rights"
        
      # Mission Rewards & Consequences
      reward_system:
        success_rewards:
          "Free drink from bartender"
          "Choose next song style"
          "Assign dare to another player"
          "Get bathroom priority for next hour"
          
        failure_consequences:
          "Buy round for everyone"
          "Sing solo verse in embarrassing style"
          "Clean up any messes made"
          "Wear silly hat for rest of session"
          
    # Dynamic Event System
    dynamic_events:
      
      # Physiological Events
      bodily_emergencies:
        sudden_nausea: "Immediate vomit risk, must find receptacle"
        bladder_explosion: "Critical bathroom need, 30-second timer"
        food_poisoning: "Digestive chaos, multiple bathroom trips"
        hiccup_attack: "Uncontrollable hiccups disrupt singing"
        
      # Social Events
      interpersonal_drama:
        jealousy_flare: "Someone gets jealous of another's singing"
        crush_confession: "Alcohol-fueled romantic revelation"
        argument_eruption: "Disagreement escalates to shouting match"
        group_bonding: "Spontaneous emotional sharing moment"
        
      # Environmental Events
      location_chaos:
        power_outage: "Lights go out, singing continues in darkness"
        jukebox_malfunction: "Background music goes haywire"
        bathroom_flood: "Toilet overflows, creates new challenges"
        surprise_inspection: "Health inspector arrives unexpectedly"
        
    # Achievement System
    achievement_unlocks:
      
      # Digestive Chicken Achievements
      chicken_mastery:
        "Rookie Chicken": "Complete first digestive chicken game"
        "Iron Bladder": "Survive 5 games without accidents"
        "Legendary Holder": "Hold it for 8+ hours of sleep"
        "Dream Master": "Successfully wake up from 10 urgent dreams"
        "Accident Survivor": "Recover gracefully from major accident"
        
      # General Achievements
      session_achievements:
        "Beer Baron": "Drink 50+ beers in single session"
        "Euphemism Poet": "Create 25+ unique bathroom phrases"
        "Harmony Hero": "Lead successful group singing for 1 hour"
        "Bathroom Ninja": "Complete 20 bathroom trips without incident"
                 "Dream Chronicler": "Document 15+ detailed dream sequences"
         
  # Physiological Management & Weird Dreams Scoring System
  physiology_management:
    
    # Core Attribute System
    player_attributes:
      
      # Physical Stats
      physical_stats:
        age: 
          range: "18-80 years"
          effects: "Older = slower metabolism, weaker bladder control"
          dream_influence: "Age affects dream content and wake-up ability"
          
        weight:
          range: "100-400 lbs"
          effects: "Higher weight = more stomach capacity, slower movement"
          calculation: "Changes based on food/drink consumption"
          
        height:
          range: "4'0\" - 7'0\""
          effects: "Affects BMI calculation and alcohol tolerance"
          fixed: "Set at character creation"
          
        bmi:
          calculation: "weight / (height^2)"
          categories: "Underweight/Normal/Overweight/Obese"
          effects: "Affects metabolism, sleep quality, dream intensity"
          
      # Physiological Systems
      digestive_system:
        stomach:
          capacity: "0-100% fullness"
          contents: "Beer volume + food mass"
          emptying_rate: "2% per minute (varies by metabolism)"
          vomit_threshold: "95% capacity"
          
        intestines:
          small_intestine: "Processes nutrients, affects energy"
          large_intestine: "Builds bowel pressure over time"
          transit_time: "4-24 hours depending on food type"
          pressure_buildup: "Fiber = faster, processed = slower"
          
        bladder:
          capacity: "0-100% fullness" 
          fill_rate: "Beer volume / body weight ratio"
          pressure_threshold: "80% = urgent, 95% = critical"
          control_strength: "Age and alcohol affect control"
          
      # Metabolic Systems
      metabolism:
        bac_blood_alcohol:
          calculation: "(drinks * 14g) / (weight * gender_factor) - (time * 0.015)"
          effects: "Affects coordination, decision-making, sleep depth"
          dream_impact: "Higher BAC = weirder dreams, harder wake-up"
          
        energy_level:
          range: "0-100%"
          depletion: "Activity, alcohol, late hours reduce energy"
          restoration: "Sleep, food, rest increase energy"
          crash_threshold: "Below 20% = forced sleep risk"
          
        hydration:
          range: "0-100%"
          effects: "Low hydration = headaches, poor performance"
          sources: "Water increases, alcohol/salt decreases"
          
    # Weird Dreams Scoring System (Lower = Weirder = Better)
    weird_dreams_leaderboard:
      
      # Scoring Categories (Lower Scores = Weirder Dreams)
      weirdness_scoring:
        
        # Dream Content Weirdness (0-50 points)
        content_categories:
          mundane_bathroom: "50 points - Normal toilet, normal peeing"
          weird_location: "40 points - Peeing in strange but logical place"
          surreal_objects: "30 points - Toilets made of food/animals"
          physics_violation: "20 points - Upside-down peeing, floating poop"
          identity_confusion: "10 points - You ARE the toilet/poop"
          cosmic_absurdity: "0 points - Peeing creates new universes"
          
        # Physiological Accuracy Bonus (Subtract points for accuracy)
        accuracy_modifiers:
          perfect_pressure_match: "-10 points - Dream perfectly matches body state"
          creative_metaphor: "-5 points - Clever symbolic representation"
          multiple_systems: "-15 points - Both pee AND poop dreams combined"
          
        # Risk Management (Add points for safety)
        safety_penalties:
          safe_wake_up: "+20 points - Woke up safely before danger"
          close_call: "+10 points - Almost had accident but saved"
          minor_accident: "+50 points - Small accident occurred"
          major_accident: "+100 points - Full accident (disqualified from round)"
          
      # Leaderboard Categories
      leaderboard_types:
        
        # Main Competition: Lowest Total Score
        weirdest_dreams_champion:
          objective: "Achieve lowest possible dream weirdness score"
          strategy: "Maximize physiological pressure while maintaining control"
          winner: "Player with most bizarre dreams who didn't have accidents"
          
        # Specialty Categories
        specialty_boards:
          most_creative_metaphor: "Best symbolic representation of bodily needs"
          highest_risk_tolerance: "Closest calls without accidents"
          best_pressure_management: "Most accurate physiological timing"
          cosmic_dreamer: "Most reality-bending dream content"
          
    # Strategic Physiological Management
    management_strategies:
      
      # Optimal Weirdness Zones
      target_zones:
        bladder_sweet_spot:
          range: "85-92% capacity"
          effect: "Maximum dream weirdness without accident risk"
          timing: "Achieve just before sleep"
          
        bowel_pressure_zone:
          range: "70-85% capacity"  
          effect: "Surreal brown-themed dreams"
          food_strategy: "High-fiber 2-3 hours before sleep"
          
        bac_creativity_zone:
          range: "0.08-0.12 BAC"
          effect: "Enhanced dream creativity, manageable wake-up ability"
          risk: "Higher BAC = harder to wake up safely"
          
      # Attribute Synergies
      synergy_effects:
        age_weight_combo:
          young_light: "Fast metabolism, quick wake-up, less weird dreams"
          old_heavy: "Slow metabolism, deep sleep, extremely weird dreams"
          
        bmi_bac_interaction:
          low_bmi_high_bac: "Alcohol hits harder, more creative dreams"
          high_bmi_low_bac: "Better alcohol tolerance, need more for weirdness"
          
        energy_pressure_balance:
          low_energy_high_pressure: "Forced sleep with maximum weirdness risk"
          high_energy_low_pressure: "Easy wake-up but boring dreams"
          
    # Real-Time Management Interface
    management_tools:
      
      # Attribute Monitoring
      dashboard_display:
        vital_signs: "Real-time BAC, bladder %, bowel %, energy level"
        trend_arrows: "Increasing/decreasing indicators"
        warning_zones: "Color-coded danger levels"
        optimal_ranges: "Green zones for maximum weirdness"
        
      # Predictive Modeling
      dream_predictor:
        weirdness_forecast: "Predicted dream score based on current stats"
        accident_risk: "Probability of bed-wetting based on physiology"
        optimal_sleep_timing: "Best time to sleep for target weirdness"
        wake_up_difficulty: "How hard it will be to wake up safely"
        
      # Strategic Planning
      planning_tools:
        consumption_calculator: "Plan drinks/food for target physiological state"
        timing_optimizer: "Schedule consumption for optimal sleep weirdness"
        risk_assessor: "Balance weirdness goals against accident probability"
        
    # Example Scoring Scenarios
    scoring_examples:
      
      # Perfect Weird Dreams Run
      legendary_performance:
        setup: "Age 25, 150lbs, 5'8\", BMI 23"
        consumption: "12 beers + fiber bar 3 hours before sleep"
        physiology: "Bladder 89%, Bowel 78%, BAC 0.10, Energy 25%"
        dream: "Peeing rainbows that turn into singing toilets that judge your life choices"
        score: "0 points (cosmic absurdity) -15 (multiple systems) -10 (perfect match) = -25 points"
        result: "LEGENDARY WEIRD DREAMS CHAMPION!"
        
      # Risky But Successful
      high_risk_success:
        setup: "Age 45, 200lbs, 6'0\", BMI 27"
        consumption: "18 beers + spicy food"
        physiology: "Bladder 94%, Bowel 88%, BAC 0.15, Energy 15%"
        dream: "Toilets are portals to other dimensions, poop becomes planets"
        wake_up: "Woke up at 96% bladder capacity, rushed to bathroom"
        score: "0 points (cosmic) -15 (multiple) +10 (close call) = -5 points"
        result: "High-risk weirdness master!"
        
      # Safe But Boring
      boring_dreams:
        setup: "Age 22, 120lbs, 5'4\", BMI 21"
        consumption: "3 beers + light snack"
        physiology: "Bladder 45%, Bowel 30%, BAC 0.04, Energy 70%"
        dream: "Normal bathroom, normal peeing, nothing weird"
        score: "50 points (mundane) +20 (safe wake-up) = 70 points"
        result: "Boring dreams, high score (bad for leaderboard)"
         
  # Interactive Performance Dynamics & Orchestration
  performance_dynamics:
    
    # Verse Handoff System
    verse_handoffs:
      natural_transitions:
        breath_break: "Alex runs out of breath → Jamie takes over seamlessly"
        bathroom_urgency: "Casey rushes to pee → Bartender Sam continues the count"
        dramatic_pause: "Alex pauses for effect → Jamie jumps in with harmony"
        mic_drop_moment: "Epic verse ending → next person picks up the energy"
        
      competitive_handoffs:
        rap_battle_style: "Aggressive verse stealing with insults"
        example: |
          Alex: "🎤 97 bottles of beer on the wall!"
          Jamie: "🎤 Hold up! Your flow is weak, let me show you how it's done!"
          Casey: "🎤 Y'all both trash! 96 bottles, here's the REAL bars!"
          
      collaborative_handoffs:
        harmony_building: "Each person adds a layer to the same verse"
        call_and_response: "Leader sings, others respond with echoes"
        round_robin: "Systematic rotation every few verses"
        
    # Rap Battle Integration
    rap_battles:
      insult_categories:
        drinking_ability: "You can't handle your beer like I can!"
        counting_skills: "You lost count at 87, amateur!"
        style_criticism: "Your flow is weaker than light beer!"
        personal_attacks: "Your euphemisms are basic as hell!"
        
      battle_examples:
        alex_vs_jamie: |
          Alex: "🎤 Jamie thinks they're hot but their verses are not!"
          Jamie: "🎤 Alex talks big but can't finish what they start!"
          Crowd: "🔥 OHHHHH! 🔥"
          
        casey_vs_bartender: |
          Casey: "🎤 Sam's behind the bar but can't spit bars!"
          Sam: "🎤 Kid, I've been serving verses since before you were born!"
          Crowd: "🤯 DAMN! 🤯"
          
      battle_mechanics:
        challenge_triggers: "Disagreement about count, style criticism, alcohol confidence"
        judge_system: "Crowd reactions determine winner"
        consequence_system: "Loser buys next round or does embarrassing dare"
        
    # Reaction Shots & Audience Dynamics
    reaction_system:
      character_reactions:
        alex_reactions:
          impressed: "😲 Damn, that was actually good!"
          competitive: "😤 Oh, you think you're better than me?"
          supportive: "🙌 Yes! Get it, Jamie!"
          confused: "🤔 Wait, what number are we on?"
          
        jamie_reactions:
          sarcastic: "🙄 Oh wow, so original..."
          encouraging: "👏 Keep going, you got this!"
          critical: "😬 That didn't even rhyme..."
          laughing: "😂 Did you just say 'beer gear'?"
          
        casey_reactions:
          shy_approval: "😊 *quiet clapping*"
          sudden_confidence: "🔥 ACTUALLY, let me try!"
          nervous_giggle: "😅 Hehe, that's funny..."
          protective: "😠 Hey, leave Alex alone!"
          
        bartender_reactions:
          wise_nod: "🧔 *strokes beard approvingly*"
          professional: "🍺 Another round coming up!"
          storyteller: "📚 That reminds me of a story..."
          crowd_control: "🛑 Alright, settle down folks!"
          
      crowd_reactions:
        energy_levels:
          dead_silence: "😐😐😐 *crickets*"
          polite_clapping: "👏👏👏 *golf clap*"
          getting_hyped: "🔥🔥🔥 YEAH!"
          going_wild: "🤯🎉💥 HOLY SHIT!"
          riot_mode: "🚨🔥💀 BURN THE PLACE DOWN!"
          
    # Sound Effects & Audio Cues
    sound_effects:
      comedic_timing:
        badoom_tss: "🥁 *ba-doom-tss* after terrible puns"
        sad_trombone: "📯 *wah-wah-wah* after epic fails"
        air_horn: "📯 *BRRRRR* for hype moments"
        record_scratch: "📀 *scratch* freeze frame moments"
        
      environmental_sounds:
        bar_ambiance: "🍺 *clink clink* glasses, *murmur* crowd chatter"
        bathroom_echoes: "🚽 *echo* reverb effects in bathroom"
        carnival_chaos: "🎪 *calliope music* *crowd screams*"
        office_drudgery: "💼 *fluorescent hum* *keyboard typing*"
        
      reaction_sounds:
        crowd_gasps: "😱 *collective gasp*"
        crowd_cheers: "🎉 *roaring applause*"
        crowd_boos: "👎 *angry booing*"
        crowd_laughs: "😂 *uproarious laughter*"
        
    # Orchestration Styles & Directions
    orchestration_system:
      
      # Tension & Release Patterns
      tension_building:
        slow_build: "Start quiet → gradually increase volume and intensity"
        dramatic_pause: "Sudden silence before explosive continuation"
        countdown_pressure: "Tension increases as numbers get lower"
        competition_heat: "Rivalry builds between characters"
        
      release_moments:
        comedic_relief: "Tension broken by unexpected humor"
        group_harmony: "Everyone joins together in perfect unity"
        epic_finale: "Explosive ending with maximum energy"
        peaceful_resolution: "Gentle wind-down to calm conclusion"
        
      # Repetition & Variation Techniques
      repetition_styles:
        echo_chamber: "Each person repeats the same line with variations"
        building_layers: "Add instruments/voices with each repetition"
        degradation_loop: "Same verse gets progressively more drunk"
        call_response_chain: "Leader → response → leader → response"
        
      variation_techniques:
        key_changes: "Shift musical key to change energy"
        tempo_shifts: "Speed up for excitement, slow down for drama"
        style_morphing: "Gradually shift from one genre to another"
        personality_evolution: "Character traits become more exaggerated"
        
      # Pace & Rhythm Control
      pacing_dynamics:
        rapid_fire: "Quick succession of verses, high energy"
        deliberate_slow: "Thoughtful, dramatic pacing"
        syncopated: "Off-beat timing for comedic effect"
        rubato: "Flexible timing that follows emotional flow"
        
      rhythm_patterns:
        steady_beat: "Consistent 4/4 time for stability"
        irregular_meter: "Changing time signatures for chaos"
        polyrhythm: "Multiple rhythms happening simultaneously"
        breakdown_moments: "Rhythm falls apart then rebuilds"
        
    # Advanced Orchestration Examples
    orchestration_examples:
      
      epic_finale_sequence:
        setup: "Verse 10 - tension building, everyone getting ready"
        buildup: "Verse 5 - all characters harmonizing, crowd joining in"
        climax: "Verse 1 - explosive final verse with full orchestration"
        resolution: "Verse 0 - triumphant completion, crowd goes wild"
        
      rap_battle_orchestration:
        round_1: "Alex opens strong, crowd reacts positively"
        round_2: "Jamie counters with devastating comeback"
        round_3: "Casey surprise entry changes everything"
        finale: "Bartender Sam drops wisdom bomb, ends battle"
        
      comedy_timing_sequence:
        setup: "Normal verse progression"
        misdirection: "Unexpected interruption or mistake"
        punchline: "Perfect comedic timing with sound effects"
        reaction: "Crowd and character responses"
        
      emotional_journey:
        joy: "Happy drinking songs with group participation"
        conflict: "Tension and competition between characters"
        resolution: "Coming together in harmony and friendship"
        reflection: "Quiet moment of bonding and understanding"
        
    # Director's Notes System
    directors_notes:
      performance_instructions:
        "Alex: Start confident but get increasingly sloppy"
        "Jamie: Play the straight man, react to others' chaos"
        "Casey: Surprise everyone with hidden talent"
        "Sam: Wise mentor figure who guides the energy"
        
      timing_cues:
        "Beat 1: Alex begins, establish rhythm"
        "Beat 16: Jamie harmony entry"
        "Beat 32: Casey interruption for comedy"
        "Beat 48: Bartender wisdom moment"
        "         "Beat 64: Group finale explosion"
         
    # Advanced Song Structure & Dramatic Elements
    song_structure_dynamics:
      
      # Mic Drop Moments
      mic_drop_system:
        epic_finale_drop: "Perfect verse ending → dramatic silence → mic hits floor"
        comeback_drop: "Devastating rap battle response → mic drop → walk away"
        truth_bomb_drop: "Profound realization mid-song → mic drop → stunned silence"
        comedy_drop: "Perfect punchline delivery → mic drop → crowd erupts"
        
        mic_drop_examples:
          alex_epic: |
            Alex: "🎤 And that's how you count from 99 to ZERO!" 
            *drops mic* 🎤💥
            Crowd: "🤯🔥 HOLY SHIT! 🔥🤯"
            
          jamie_comeback: |
            Jamie: "🎤 At least I can count past 50 without passing out!"
            *drops mic* 🎤💥
            Alex: "😱 Damn..."
            
      # Pregnant Pauses & Dramatic Timing
      pregnant_pause_system:
        tension_building: "Long silence before explosive continuation"
        comedic_timing: "Pause before punchline for maximum impact"
        emotional_weight: "Silence to let profound moment sink in"
        anticipation: "Pause before big reveal or climax"
        
        pause_examples:
          dramatic_countdown: |
            Alex: "🎵 3 bottles of beer on the wall..."
            *long pause* 😶
            Everyone: *holding breath*
            Alex: "🎵 3 bottles of beer!"
            Crowd: "🎉 YEAH! 🎉"
            
          comedic_setup: |
            Casey: "🎵 So I went to the bathroom and..."
            *pregnant pause* 😶
            Casey: "🎵 Let's just say it wasn't just number one!"
            Crowd: "😂🤮 EWWWW! 😂"
            
      # Song Direction Changes & Transitions
      song_transitions:
        
        # Musical Terms for Direction Changes
        bridge_section: "Contrasting section that connects verse to chorus"
        modulation: "Key change that shifts entire song energy"
        breakdown: "Stripped-down section before building back up"
        crescendo_climax: "Gradual build to explosive peak moment"
        deceptive_cadence: "Expected resolution that goes somewhere unexpected"
        
        # Narrative Direction Changes
        plot_twist: "Story takes unexpected turn mid-song"
        perspective_shift: "Different character takes over narrative"
        genre_morph: "Song style completely changes mid-performance"
        reality_break: "Song acknowledges it's a song, breaks fourth wall"
        
        # Specific Transition Types
        climactic_transitions:
          
          # The "Bridge" - Classic Song Structure
          bridge_example: |
            Verse: "🎵 99 bottles of beer on the wall..." (standard countdown)
            Bridge: "🎵 But wait! What if the bottles could talk?" (new perspective)
            Verse: "🎵 'Don't drink me!' cried bottle 47..." (transformed narrative)
            
          # Modulation - Key/Energy Change  
          modulation_example: |
            Low Energy: "🎵 10 bottles of beer... *tired, slow*"
            Climax: "🎵 BUT WAIT! *sudden energy surge*"
            High Energy: "🎵 TEN BOTTLES OF BEER! LET'S GO! 🔥"
            
          # Breakdown - Strip to Essentials
          breakdown_example: |
            Full Song: "🎵 50 bottles of beer on the wall! *full orchestration*"
            Breakdown: "🎵 Fifty... *whisper* ...bottles... *single voice*"
            Rebuild: "🎵 FIFTY BOTTLES! *explosive return*"
            
          # Genre Morph - Complete Style Change
          genre_morph_example: |
            Country: "🤠 Well, 30 bottles of beer, partner..."
            Transition: "🎵 But suddenly the saloon doors burst open!"
            Death Metal: "🤘 THIRTY BOTTLES OF BEEEEER! 💀🔥"
            
          # Plot Twist - Narrative Surprise
          plot_twist_example: |
            Normal: "🎵 20 bottles of beer on the wall..."
            Twist: "🎵 Wait... these aren't bottles... THEY'RE ALIENS!"
            New Reality: "🎵 20 alien pods on the spaceship wall!"
            
      # Advanced Dramatic Techniques
      dramatic_techniques:
        
        # Tension & Release Patterns
        tension_release_cycles:
          slow_build: "Gradual increase in intensity over multiple verses"
          sudden_drop: "Explosive moment followed by complete silence"
          false_climax: "Build to apparent peak, then continue building higher"
          cascading_release: "Multiple smaller releases building to final explosion"
          
        # Call & Response Escalation
        call_response_evolution:
          simple_echo: "Leader sings, others repeat exactly"
          harmonic_response: "Others add harmony to the response"
          competitive_response: "Each response tries to outdo the last"
          chaos_response: "Everyone responds differently, creating chaos"
          
        # Emotional Journey Mapping
        emotional_arcs:
          hero_journey: "Confidence → Challenge → Struggle → Triumph"
          comedy_arc: "Setup → Misdirection → Punchline → Release"
          tragedy_arc: "Hope → Hubris → Downfall → Acceptance"
          romance_arc: "Meeting → Attraction → Conflict → Resolution"
          
      # Practical Implementation Examples
      implementation_examples:
        
        # Complete Song with Multiple Transitions
        epic_beer_journey: |
          Act 1 - Setup (Verses 99-80):
          "🎵 99 bottles of beer on the wall..." *standard rhythm*
          
          Bridge 1 - First Transition (Verse 79):
          "🎵 But wait... *pregnant pause* ...what's that sound?"
          
          Act 2 - Complication (Verses 78-60):
          "🎵 78 bottles shaking on the wall!" *earthquake rhythm*
          
          Breakdown (Verse 50):
          "🎵 Fifty... *whisper* ...bottles... *building tension*"
          
          Climax (Verse 49):
          "🎵 FORTY-NINE BOTTLES! *explosive energy*"
          
          Act 3 - Resolution (Verses 48-1):
          "🎵 48 bottles dancing on the wall!" *celebration rhythm*
          
          Finale (Verse 0):
          "🎵 NO MORE BOTTLES!" *mic drop* 🎤💥
          
        # Rap Battle with Transitions
        battle_with_bridges: |
          Round 1: Alex vs Jamie (standard battle)
          Bridge: Casey interrupts with plot twist
          Round 2: Three-way battle (chaos)
          Breakdown: Bartender Sam's wisdom moment
          Finale: Group harmony resolution"
    
  # Musical Styles by Context
  contextual_music:
    bar_drinking:
      style: "Irish pub song / drinking ballad"
      tempo: "Moderate, singable"
      instruments: ["acoustic_guitar", "fiddle", "bodhrán"]
      
    bathroom_euphemisms:
      style: "Comedic musical theater"
      tempo: "Playful, bouncy"
      instruments: ["piano", "tuba", "slide_whistle"]
      
    carnival_chaos:
      style: "Circus march / carnival music"
      tempo: "Fast, chaotic"
      instruments: ["calliope", "brass_band", "percussion"]
      
    office_transformation:
      style: "Corporate elevator music meets rebellion"
      tempo: "Steady, building to explosive"
      instruments: ["synthesizer", "electric_guitar", "drums"]
      
  # Export Formats
  music_export:
    formats:
      midi: "Standard MIDI for music software compatibility"
      abc_notation: "Text-based music notation for folk songs"
      musicxml: "Professional music notation software"
      audio_stems: "Separate tracks for vocals, instruments, harmonies"
      karaoke: "Lyrics-synced audio for sing-along"
      
    modular_system:
      verse_templates: "Reusable musical patterns for countdown songs"
      harmony_layers: "Stackable vocal parts for multi-person singing"
      instrument_packs: "Themed instrument sets for different locations"
      transition_bridges: "Musical bridges for picture-driven transformations"
      
  # Adaptive Composition
  ai_composition_features:
    personalized_melodies: "Tunes adapt to player's musical preferences"
    emotional_scoring: "Music reflects current mood and situation"
    cultural_adaptation: "British vs American musical styles"
    dynamic_arrangements: "Instruments added/removed based on social context"
    
    real_time_generation:
      verse_composition: "New melodies for each countdown number"
      harmony_adaptation: "Harmonies adjust when players join/leave"
      tempo_modulation: "Speed changes based on urgency (bathroom rush!)"
      key_changes: "Musical progression mirrors story progression"
      
  # Community Music Features
  social_music:
    collaborative_composition: "Players contribute to shared songs"
    remix_system: "Take someone's melody and add your own twist"
    music_sharing: "Export and share your session's soundtrack"
    live_performance: "Real-time multi-player singing sessions"
    
    viral_music_potential:
      catchy_hooks: "Memorable melodies that stick in your head"
      meme_songs: "Musical moments that become viral content"
      cover_versions: "Community creates covers of popular game songs"
             music_challenges: "Sing your own version of classic verses"
 ```

## 🌐 Interlinked Web Page Generation System {#web-page-generation}

```yaml
# Generate Complete Web Documentation from LLOOOOMM Document
web_generation_system:
  
  # Core Principle: Document Sections → Web Pages
  section_to_page_mapping:
    "Each LLOOOOMM section with {#id} becomes a standalone web page"
    "Cross-references automatically become hyperlinks"
    "SSQQLL queries generate dynamic content"
    "Scaling system allows zooming into specific views"
    
  # Generated Web Page Structure
  auto_generated_pages:
    
    # Main Navigation Hub
    index_page:
      source_section: "#main-overview"
      content: |
        - Session summary with key statistics
        - Player thumbnails with quick stats
        - Location map with visit counts
        - Timeline of major events
        - Quick access to all sub-pages
        
    # Player-Specific Pages  
    player_pages:
      alex_profile:
        source_section: "#alex-state"
        url: "player_alex.html"
        content: |
          - Complete physiological tracking
          - Personality profile from AI interviews
          - Goal progression charts
          - Favorite euphemisms gallery
          - Personal song compilation
          - Photo upload history
          
      jamie_profile:
        source_section: "#jamie-state"
        url: "player_jamie.html"
        content: "Similar structure, different data"
        
    # Location Documentation
    location_pages:
      bar_details:
        source_section: "#bar-location"
        url: "location_bar.html"
        content: |
          - Menu with prices and consumption stats
          - Dialect switching events
          - Social interactions log
          - Bartender Sam's quotes
          - Revenue generated for establishment
          
      bathroom_analytics:
        source_section: "#bathroom-goals"
        url: "location_bathroom.html"
        content: |
          - Visit frequency analysis
          - Euphemism evolution timeline
          - Efficiency metrics
          - Emergency vs planned visits
          - Cleanliness impact scores
          
    # Song & Music Pages
    music_pages:
      song_compilation:
        source_section: "#song-verses"
        url: "songs_all.html"
        content: |
          - Complete lyrics with timestamps
          - Musical notation (when generated)
          - Harmony arrangements
          - Singing participation breakdown
          - Audio player integration
          
      euphemism_gallery:
        source_section: "#euphemism-personalization"
        url: "euphemisms.html"
        content: |
          - Categorized euphemism collection
          - Personalization evolution
          - Community voting interface
          - Usage frequency statistics
          - Cultural context explanations
          
    # Analytics Dashboards
    analytics_pages:
      performance_dashboard:
        source_section: "#analytics-system"
        url: "analytics.html"
        content: |
          - Live SSQQLL query results
          - Interactive charts and graphs
          - Comparison with community averages
          - Trend analysis over time
          - Export options for data
          
      social_analytics:
        source_section: "#viral-sharing"
        url: "social_stats.html"
        content: |
          - Story sharing metrics
          - Viral coefficient tracking
          - Community engagement scores
          - Remix and derivative works
          - Influence network mapping
          
  # Dynamic Content Generation
  content_generation:
    
    # SSQQLL-Powered Dynamic Sections
    live_queries:
      player_stats: |
        <!-- Auto-generated from SSQQLL -->
        <div class="player-stats">
          <h3>Alex's Session Statistics</h3>
          <p>Beers consumed: {{SELECT COUNT(*) FROM #beer-log WHERE player='alex'}}</p>
          <p>Weight gained: {{SELECT (currentWeight - startWeight) FROM #alex-state}}</p>
          <p>Money spent: {{SELECT SUM(cost) FROM #transactions WHERE player='alex'}}</p>
        </div>
        
      location_summary: |
        <!-- Auto-generated location grid -->
        {{#each locations}}
        <div class="location-card">
          <h4>{{name}}</h4>
          <p>Time spent: {{time_spent}}</p>
          <p>Events: {{event_count}}</p>
          <a href="location_{{id}}.html">View Details</a>
        </div>
        {{/each}}
        
    # Cross-Reference Link Generation
    auto_linking:
      section_references: "Any #section-id becomes clickable link"
      player_mentions: "@alex becomes link to alex_profile.html"
      location_references: "Location names become links to location pages"
      song_references: "Song titles link to music pages"
      
  # Scaling & View System
  view_scaling:
    
    # Zoom Levels within Main Document
    document_views:
      overview_mode: "Show only main sections, collapse details"
      detailed_mode: "Expand all subsections and data"
      focus_mode: "Show only selected section and related content"
      analytics_mode: "Highlight all SSQQLL queries and data sections"
      
    # Filtered Views
    content_filters:
      player_filter: "Show only content related to specific player"
      location_filter: "Show only content for specific location"
      timeframe_filter: "Show only events within time range"
      goal_filter: "Show only content related to specific goal type"
      
    # Interactive Navigation
    navigation_features:
      breadcrumb_trails: "Home > Players > Alex > Bathroom Visits"
      related_content: "Automatically suggest related sections"
      search_integration: "Full-text search across all generated content"
      bookmark_system: "Save favorite views and sections"
      
  # Template System
  page_templates:
    
    # Consistent Design Across All Pages
    base_template: |
      <!DOCTYPE html>
      <html>
      <head>
        <title>{{page_title}} - LLOOOOMM BBEEEERR Session</title>
        <link rel="stylesheet" href="assets/lloooomm-beer.css">
      </head>
      <body>
        <nav class="main-nav">
          <a href="index.html">🏠 Home</a>
          <a href="players.html">👥 Players</a>
          <a href="locations.html">📍 Locations</a>
          <a href="songs.html">🎵 Songs</a>
          <a href="analytics.html">📊 Analytics</a>
        </nav>
        <main>{{content}}</main>
        <footer>
          <p>Generated from LLOOOOMM document at {{timestamp}}</p>
          <p>Session: {{session_id}} | Duration: {{session_duration}}</p>
        </footer>
      </body>
      </html>
      
    # Specialized Templates
    player_template: "Enhanced with physiological charts and personality widgets"
    location_template: "Interactive maps and item inventories"
    song_template: "Audio players and lyric highlighting"
    analytics_template: "Live charts and query interfaces"
    
  # Export & Sharing
  export_options:
    static_website: "Complete standalone website with all pages"
    pdf_compilation: "Single PDF with all content and navigation"
    mobile_app: "Responsive design for mobile viewing"
    social_sharing: "Optimized previews for social media platforms"
    
    sharing_features:
      permalink_system: "Stable URLs for every section and view"
      embed_codes: "Embed specific sections in other websites"
      api_endpoints: "JSON API for accessing structured data"
      rss_feeds: "Subscribe to updates from specific players or locations"
```

## 🔍 Document Scaling & View System {#scaling-system}

```yaml
# Advanced Scaling Within Single Document
document_scaling_system:
  
  # View Modes
  scaling_levels:
    macro_view: "Entire session overview, major events only"
    standard_view: "Normal detail level, all main sections visible"
    micro_view: "Deep dive into specific moments, full detail"
    data_view: "Focus on analytics, queries, and statistics"
    
  # Content Filtering
  filter_system:
    by_player: "Show only Alex's actions, thoughts, and consequences"
    by_location: "Show only events at the bar, hide other locations"
    by_timeframe: "Show only events between 2:00-3:00 PM"
    by_goal_type: "Show only drinking goals, hide bathroom/food goals"
    by_content_type: "Show only songs, or only analytics, or only euphemisms"
    
  # Interactive Navigation
  navigation_within_document:
    section_jumping: "Click any #section-id to jump and focus"
    related_content: "Highlight all sections related to current focus"
    timeline_scrubbing: "Scrub through session chronologically"
    search_highlighting: "Search for 'Pringles' highlights all mentions"
    
  # Dynamic Content Expansion
  progressive_disclosure:
    summary_cards: "Collapsed sections show key stats, expand for details"
    lazy_loading: "Load detailed content only when section is expanded"
    contextual_sidebars: "Related information appears in sidebar"
    tooltip_details: "Hover over any element for additional context"
    
# Implementation Example
scaling_implementation:
  css_classes: |
    .macro-view .detail { display: none; }
    .micro-view .summary { display: none; }
    .player-filter:not(.alex) { opacity: 0.3; }
    .location-filter:not(.bar) { display: none; }
    
  javascript_controls: |
    function setViewMode(mode) {
      document.body.className = mode + '-view';
      updateNavigation(mode);
      highlightRelevantSections(mode);
    }
    
    function filterByPlayer(playerName) {
      document.querySelectorAll('.player-content')
        .forEach(el => el.classList.toggle('filtered', 
          !el.dataset.player.includes(playerName)));
    }
```

## 📊 Analytics Dashboard - SSQQLL Queries Against Game Data {#analytics-dashboard}

```yaml
# Player Analytics System - Real-Time SSQQLL Queries
analytics_system:
  core_concept: "Every action logged, queryable via SSQQLL against document data"
  
  # Real-Time Analytics Queries
  consumption_analytics:
    beers_per_hour:
      query: "SELECT COUNT(*) / (mRealTimeElapsed / 3600) as beers_per_hour FROM #beer-consumption-log"
      display: "📊 Beers Per Hour: 3.2 (above average!)"
      
    barfs_per_day:
      query: "SELECT COUNT(*) / (mRealTimeElapsed / 86400) as barfs_per_day FROM #vomit-events"
      display: "🤮 Barfs Per Day: 0.8 (rookie numbers!)"
      
    lloooommolians_burned:
      query: "SELECT SUM(cost) FROM #purchase-log WHERE timestamp > session_start"
      display: "💰 LLOOOOMMOLIANS Spent: ₤247 (₤12.35/hour)"
      
    bathroom_efficiency:
      query: "SELECT AVG(duration) FROM #bathroom-visits WHERE type = 'emergency'"
      display: "🚽 Average Emergency Response Time: 23 seconds"
      
  # Song Analytics
  song_analytics:
    verses_sung:
      query: "SELECT COUNT(*) FROM #song-verses WHERE singer = current_player"
      display: "🎵 Total Verses Sung: 127"
      
    favorite_euphemisms:
      query: "SELECT euphemism, COUNT(*) as usage FROM #euphemism-log GROUP BY euphemism ORDER BY usage DESC LIMIT 5"
      display: |
        🎭 Top Euphemisms:
        1. "Drop kids at pool" (23 times)
        2. "Drain the lizard" (18 times)  
        3. "Call Earl" (15 times)
        
    song_participation_rate:
      query: "SELECT (verses_sung / total_verses_available) * 100 as participation_rate FROM #session-stats"
      display: "🎤 Song Participation: 87% (you're a natural!)"
      
  # Physiological Analytics
  body_analytics:
    weight_trajectory:
      query: "SELECT timestamp, currentWeight FROM #weight-log ORDER BY timestamp"
      display: "⚖️ Weight Change: +3.2 lbs (trending upward)"
      
    digestive_efficiency:
      query: "SELECT AVG(digestion_time) FROM #food-processing WHERE food_type = 'snacks'"
      display: "🍽️ Snack Processing Time: 2.3 hours average"
      
    bladder_capacity_utilization:
      query: "SELECT MAX(bladderLevel) / bladderSize * 100 as max_utilization FROM #bladder-log"
      display: "💧 Peak Bladder Usage: 94% (cutting it close!)"
      
  # Social Analytics
  social_analytics:
    group_influence:
      query: "SELECT COUNT(*) FROM #goal-switches WHERE trigger = 'social_influence'"
      display: "👥 Peer Pressure Events: 7 (you're easily influenced!)"
      
    sharing_generosity:
      query: "SELECT COUNT(*) FROM #sharing-events WHERE initiator = current_player"
      display: "🤝 Times You Shared Snacks: 12 (generous spirit!)"
      
    bartender_interactions:
      query: "SELECT COUNT(*) FROM #conversations WHERE participant = 'bartender_sam'"
      display: "🍺 Chats with Sam: 23 (you're becoming friends!)"
```

## 🌐 Sims-Style Save File Web Pages {#sims-style-saves}

```yaml
# Comprehensive Save File System - Interlinked Web Pages
save_file_system:
  core_concept: "Rich, browsable save files like The Sims with previews and analytics"
  
  # Main Save File Structure
  save_file_pages:
    
    # 1. Session Overview Page
    session_overview:
      url: "saves/session_2024_01_15_epic_night/index.html"
      content:
        session_title: "Epic Night at Murphy's Bar"
        session_duration: "4 hours, 23 minutes"
        session_summary: "Started with 99 beers, ended with food baby delivery"
        key_stats:
          - "Beers consumed: 12"
          - "Pounds gained: 2.3"
          - "Bathroom visits: 8"
          - "Euphemisms created: 15"
          - "LLOOOOMMOLIANS spent: ₤156"
        thumbnail: "session_highlight_reel.gif"
        links:
          - "View Character Details →"
          - "Browse Locations →"
          - "Song Compilation →"
          - "Analytics Dashboard →"
          
    # 2. Character Profile Page
    character_profile:
      url: "saves/session_2024_01_15_epic_night/characters/alex.html"
      content:
        character_name: "Alex"
        character_photo: "alex_drunk_selfie.jpg"
        personality_profile:
          - "Loves craft beer and terrible puns"
          - "Afraid of clowns (discovered during carnival)"
          - "Works in tech, stressed about deadlines"
          - "Has a cat named Whiskers"
        physical_stats:
          starting_weight: "180 lbs"
          ending_weight: "182.3 lbs"
          bladder_capacity: "500ml"
          alcohol_tolerance: "Medium (improving)"
        memorable_quotes:
          - "'Time to drop the kids off at the pool!'"
          - "'These Pringles are like crack!'"
          - "'I should probably call a ride...'"
        character_evolution: "Started confident, ended humble and 2 pounds heavier"
        
    # 3. Location Gallery
    location_gallery:
      url: "saves/session_2024_01_15_epic_night/locations/index.html"
      content:
        locations_visited:
          murphys_bar:
            name: "Murphy's Bar"
            time_spent: "2 hours, 45 minutes"
            screenshot: "murphys_bar_interior.jpg"
            memorable_events:
              - "Ordered first Guinness (switched to British dialect)"
              - "Shared Pringles with Jamie and Casey"
              - "Bartender Sam told embarrassing story"
            items_interacted:
              - "Guinness tap (15 times)"
              - "Pringles can (29 layers demolished)"
              - "Bar stool (fell off once)"
              
          bathroom:
            name: "Murphy's Bathroom"
            time_spent: "23 minutes total"
            screenshot: "bathroom_stall.jpg"
            memorable_events:
              - "First 'kids at pool' delivery"
              - "Emergency lizard draining"
              - "Contemplated life choices"
              
    # 4. Song Compilation Page
    song_compilation:
      url: "saves/session_2024_01_15_epic_night/songs/index.html"
      content:
        total_verses: 127
        song_highlights:
          opening_number:
            verse: "🎵 99 bottles of beer on the wall, 99 bottles of beer!"
            singer: "Bartender Sam (announcement)"
            timestamp: "20:30:15"
            audio_clip: "opening_verse.mp3"
            
          funniest_moment:
            verse: "🎵 29 layers of Pringles in the can, 29 layers to pop!"
            singer: "Alex (lead), Jamie & Casey (harmony)"
            timestamp: "21:45:32"
            context: "During epic snack sharing session"
            
          most_embarrassing:
            verse: "🎵 'Birthing a beautiful food baby!' Push one down, deliver it around!"
            singer: "Alex (solo, unfortunately)"
            timestamp: "23:12:08"
            context: "After too many hot dogs and Pringles"
            
        euphemism_evolution:
          - "Started with basic 'poop' → evolved to 'drop kids at pool'"
          - "Discovered 'drain the lizard' during first bathroom visit"
          - "Created personalized 'call Earl' after mentioning Uncle Earl"
          
    # 5. Analytics Dashboard Page
    analytics_dashboard:
      url: "saves/session_2024_01_15_epic_night/analytics/index.html"
      content:
        consumption_charts:
          beer_timeline: "beer_consumption_over_time.svg"
          weight_progression: "weight_gain_chart.svg"
          bathroom_frequency: "bathroom_visits_histogram.svg"
          
        efficiency_metrics:
          - "Beers per hour: 3.2 (above average)"
          - "Bathroom efficiency: 94% (excellent timing)"
          - "Social sharing rate: 87% (very generous)"
          - "Song participation: 91% (natural performer)"
          
        comparison_data:
          vs_previous_sessions: "This session: +15% more social"
          vs_community_average: "You drink 23% slower than average"
          personal_records: "New record: Most Pringles shared (29 layers)"
          
        ssqqll_queries_used:
          - "SELECT AVG(time_between_beers) FROM #consumption_log"
          - "SELECT euphemism, creativity_score FROM #euphemism_ratings"
          - "SELECT location, happiness_level FROM #location_mood_log"
          
    # 6. Story Narrative Page
    story_narrative:
      url: "saves/session_2024_01_15_epic_night/story/index.html"
      content:
        auto_generated_story: |
          "The Epic Night at Murphy's Bar"
          
          It started innocently enough. Alex walked into Murphy's Bar with a simple goal: 
          drink 99 bottles of beer. But as Bartender Sam announced the arrival of fresh 
          beer, little did Alex know this would become a night of Pringles addiction, 
          bathroom euphemisms, and questionable life choices.
          
          The turning point came when Jamie suggested sharing a can of Pringles. 
          "Once you pop, you can't stop!" became the unofficial motto as 29 layers 
          disappeared faster than Alex's dignity. The weight gain was immediate, 
          the bathroom visits frequent, and the euphemisms increasingly creative.
          
          By the end of the night, Alex had gained 2.3 pounds, created 15 new 
          euphemisms, and learned that "dropping the kids off at the pool" 
          is both hilarious and surprisingly accurate.
          
        chapter_breakdown:
          - "Chapter 1: The Innocent Beginning (99 bottles goal)"
          - "Chapter 2: The Pringles Incident (social sharing chaos)"
          - "Chapter 3: The Bathroom Chronicles (euphemism evolution)"
          - "Chapter 4: The Weight Gain Realization (scale shock)"
          - "Chapter 5: The Safe Ride Home (responsible ending)"
          
        shareable_highlights:
          - "Best euphemism: 'Birthing a food baby'"
          - "Funniest moment: Pringles addiction spiral"
          - "Most embarrassing: Falling off bar stool"
          - "Character growth: Learned moderation (sort of)"
```

## 🎭 AI Dungeon Master System - Adaptive Storytelling {#ai-dungeon-master}

```yaml
# LLM Dungeon Master - Learns About Players & Personalizes Everything
ai_dungeon_master:
  core_capabilities:
    player_profiling: "Builds detailed psychological profiles through gameplay"
    contextual_creativity: "Creates personalized euphemisms based on player history"
    adaptive_storytelling: "Weaves player details into song narratives"
    seaman_interviewing: "Asks probing questions and uses answers against players"
    eliza_therapy: "Reflects player statements back as story elements"
    
  # Player Profiling System - Like Seaman the Fish Game
  player_profiling:
    interview_techniques:
      casual_questions: "So, what's your biggest fear about getting older?"
      loaded_questions: "Tell me about the last time you embarrassed yourself"
      callback_questions: "Remember when you said you hate clowns? Well..."
      
    profile_categories:
      personal_history: ["childhood_pets", "embarrassing_moments", "phobias", "dreams"]
      preferences: ["favorite_foods", "music_taste", "humor_style", "comfort_zones"]
      relationships: ["family_dynamics", "friend_groups", "romantic_history", "social_anxiety"]
      psychology: ["defense_mechanisms", "triggers", "motivations", "insecurities"]
      
    data_collection_methods:
      direct_questioning: "The Narrator asks probing questions during gameplay"
      behavioral_observation: "Tracks player choices and reaction patterns"
      song_participation: "Analyzes how players engage with different verses"
      goal_selection: "Notes which goals players gravitate toward"
      
  # Personalized Euphemism Generation - Examples Only!
  euphemism_personalization:
    note: "THESE ARE EXAMPLES - The LLM can get EXTREMELY creative and contextual!"
    
    example_personalizations:
      player_with_cat_phobia:
        poop_euphemism: "Delivering a hairball to the litter box of life"
        context: "Uses cat imagery because player mentioned hating cats"
        
      player_who_loves_cooking:
        poop_euphemism: "Baking a chocolate soufflé in the porcelain oven"
        vomit_euphemism: "The kitchen disaster is being returned to sender"
        context: "Incorporates cooking metaphors from player's interests"
        
      player_with_office_job:
        poop_euphemism: "Filing a brown report with the Department of Waste Management"
        piss_euphemism: "Emptying the water cooler of corporate productivity"
        context: "Uses office jargon because player complained about work"
        
      player_who_mentioned_ex:
        vomit_euphemism: "Returning your ex's cooking to the universe"
        context: "Callback to earlier conversation about bad relationships"
        
    adaptive_creativity:
      "The LLM Dungeon Master can create UNLIMITED personalized euphemisms"
      "Based on ANY detail the player reveals through gameplay or conversation"
      "Gets more creative and specific the more it learns about the player"
      "Can reference inside jokes, personal history, fears, dreams, anything!"
      
  # Seaman-Style Interrogation During Gameplay
  seaman_interviewing:
    casual_integration:
      during_drinking: "So while you're sipping that beer, tell me about your first pet"
      during_bathroom: "You know, this reminds me of something... what's your worst bathroom story?"
      during_carnival: "Carnivals bring back memories, don't they? What's yours?"
      
    psychological_probing:
      "What does 'home' mean to you?" # Used later in safe ride scenarios
      "Tell me about a time you felt truly embarrassed" # Used in vomit scenes
      "What's your relationship with your body?" # Used in weight gain scenarios
      "Who do you trust most in your life?" # Used in friend intervention scenes
      
    callback_integration:
      "Remember when you said you hate the smell of fish? Well, this bathroom..."
      "You mentioned your fear of clowns earlier... funny how that carnival worker looks..."
      "That story about your college roommate? This situation reminds me of it..."
      
  # Adaptive Song Personalization
  personalized_song_weaving:
    player_history_integration:
      "🎵 99 bottles of beer on the wall, just like that party at [player's college]!"
      "🎵 Dropping the kids off at the pool, reminds me of [player's childhood story]!"
      "🎵 Calling Earl on the porcelain telephone, Earl like your [player's mentioned person]!"
      
    emotional_callbacks:
      "🎵 This weight gain reminds you of [player's insecurity], doesn't it?"
      "🎵 Just like when [player's embarrassing moment], here we go again!"
      "🎵 Your [player's phobia] is showing in how you handle this situation!"
      
    inside_joke_development:
      "Creates running gags based on player's unique responses"
      "Develops personalized catchphrases and references"
      "Builds a shared history that makes each playthrough unique"
```

## 🚀 LLOOOOMM Features Showcase & Dogfooding {#lloooomm-showcase}

This document serves as a **living demonstration** of LLOOOOMM's core capabilities:

### 🎯 DDOOUUBBLLEE Convention Examples
- **BBEEEERR** - Extra emphasis on the fun factor
- **FFRREEEE** - Maximum freedom expression  
- **LLOOVVEE** - Emotional amplification
- **SSPPEEEECCHH** - Free speech, natural language emphasis
- **LLUUNNCCHH** - Because why not? 🥪

### 🎨 Emoji Typing & Domain Languages
- 🎵 = Song/rhythm elements
- 🔄 = Lifecycle/process flows  
- 📊 = Data/metrics tracking
- 🎯 = Goals/targets
- 💪 = Fitness/strength activities
- 🧠 = Mental/cognitive effects
- ⚡ = Energy/activation states

### 🧬 Prototype Inheritance Patterns
```yaml
# Base goal prototype (index 0)
goal_prototype:
  _status: "PROTOTYPE"
  goal: "template_goal"
  unit: "units"
  song_template: "{count} {unit} to go!"
  action_verb: "do one, complete it around"
  
# Inherited goals reference prototype
lose_fat_classic:
  parents: [0]  # Inherits from prototype
  goal: "lose 99 pounds of fat"  # Override
  action_verb_variations: [...]  # Extend
```

### 🔍 SSQQLL Query Examples
```sql
-- Find all high-energy goals
SELECT goal, motive_effects.mEnergy 
FROM #life-goals-database 
WHERE motive_effects.mEnergy < -10;

-- Calculate total weight loss potential
SELECT SUM(ABS(motive_effects.mWeight)) as total_weight_loss
FROM #weight-goals;

-- Find goals that boost self-esteem
SELECT goal, motive_effects.mSelfEsteem
FROM #life-goals-database
WHERE motive_effects.mSelfEsteem > 5
ORDER BY motive_effects.mSelfEsteem DESC;
```

### 🚀 ZZOOOOMM Meta-Programming Integration
```yaml
# ZZOOOOMM:ADAPTIVE_GOAL_SELECTION
# IF user_weight > ideal_weight + 20 THEN prioritize_weight_loss
# ELIF user_stress > 70 THEN prioritize_stress_relief  
# ELIF user_energy < 30 THEN prioritize_energy_boost
# ELSE balanced_approach

# ZZOOOOMM:NATURAL_LANGUAGE_CONDITIONS
# WHEN "feeling fat" THEN switch_to_exercise_goals
# WHEN "need to party" THEN switch_to_social_goals
# WHEN "broke as hell" THEN switch_to_financial_goals
```

### 📥 LLOOOOMM IMPORT Directive Usage
```javascript
// LLOOOOMM IMPORT #life-goals-database [extract weight_goals] [js-object] [group by difficulty]
const WEIGHT_LOSS_GOALS = {
  beginner: ["lose_weight_small"],
  intermediate: ["lose_fat_classic"], 
  advanced: ["gain_muscle"]
};

// LLOOOOMM IMPORT #activity-switching [extract motive_driven] [python-dict]
MOTIVE_TRIGGERS = {
  "high_hunger": ["eat_pizza", "devour_burgers"],
  "high_stress": ["primal_screams", "smoke_joints"],
  "weight_gain": ["lose_fat_classic", "run_miles"]
}
```

### 🎮 Natural Language Command Interface
```
"Start losing weight" → Activates lose_fat_classic goal
"I'm stressed out" → Triggers stress-relief goal switching
"Switch to party mode" → Changes to entertainment/social goals
"How much weight can I lose?" → Queries weight loss potential
"Show me exercise options" → Displays action_verb_variations
```

### 🔄 Living Document Evolution
This document **evolves through use**:
- New goals added based on user feedback
- Motive effects refined through simulation
- Action variations expanded through creativity
- Success patterns become constitutional

## 📋 Main Execution Task {#main-task}

**Task ID**: `universal_life_countdown`  
**Stack Frame**: `@main_life_frame`  
**Status**: 🟢 Ready to Initialize

### Task Definition
```yaml
task:
  id: "universal_life_countdown"
  type: "life_simulation"
  paradigm: "countdown_songs"
  phase: "initialization"
  
  # Task-specific data references
  config: "@global-life-params"
  environment: "@life-execution-env"
  state: "@life-state"
  
  # Execution flow
  phases:
    - setup: "#phase-setup"
    - goal_selection: "#phase-goal-selection"
    - countdown_execution: "#phase-countdown"
    - consequence_handling: "#phase-consequences"
    - cycle_continuation: "#phase-cycle"
```

## 🎵 Universal Goal Countdown System {#universal-goal-system}

### Core Principle: Any Goal Becomes a Countdown Song

```yaml
# The song countdown is the heartbeat - can be ANY life goal
universal_goal_system:
  core_principle: "The countdown song drives everything"
  
  # Song State - The Heartbeat
  song_heartbeat:
    mCountdownNumber: 99           # What we're counting down
    mGoalType: "lose weight"       # What goal we're pursuing
    mGoalUnit: "pounds"            # How we measure progress
    mSongTemplate: "{count} {unit} to {goal}, {count} {unit} to go!"
    mHeartbeatActive: true         # Song is the driving force
    mBeatInterval: "per_action"    # Each action = one beat
    
  # Song Interruption & Segmentation System
  song_segmentation:
    interruption_triggers:
      bathroom_urgency: "Bladder pressure > 90 → pause song, create bathroom segment"
      picture_upload: "New image → pause song, transform world, resume in new context"
      social_events: "Someone joins/leaves → pause for social interaction"
      emergency_events: "Vomiting, phone calls, urgent situations"
      
    segment_management:
      automatic_headers: "Songs get split into numbered parts with headers"
      counter_recovery: "AI reads last sung verse to determine current count"
      seamless_resumption: "Continue exactly where we left off"
      
    header_renaming_system:
      initial_header: "## 🍺 99 Bottles of Beer Song {#beer-song}"
      after_interruption: 
        part_1: "## 🍺 99 Bottles of Beer Song (Part 1 of 2) {#beer-song-part-1}"
        part_2: "## 🍺 99 Bottles of Beer Song (Part 2 of 2) {#beer-song-part-2}"
      
    interleaved_content:
      song_segments: "Multiple song sections with auto-generated headers"
      narrative_breaks: "Normal markdown prose between songs"
      event_descriptions: "Formatted explanations of interruptions"
      transition_bridges: "How we got from one context to another"
      
  # Example Interruption Flow
  interruption_example: |
    ## 🍺 99 Bottles of Beer Song {#beer-song}
    🎵 "99 bottles of beer on the wall, 99 bottles of beer..."
    🎵 "Take one down, pass it around, 98 bottles of beer on the wall!"
    [continues to verse 73]
    
    **Alex**: "Oh crap, I really need to pee!"
    
    ## 🚽 Emergency Bathroom Break {#bathroom-break-1}
    Alex's bladder pressure has reached critical levels (95/100). The urgent dash 
    to the bathroom interrupts the song mid-verse. The countdown is paused at 72 bottles.
    
    *[2 minutes later]*
    
    Alex returns, relieved and ready to continue.
    
    ## 🍺 99 Bottles of Beer Song (Part 2 of 2) {#beer-song-part-2}
    🎵 "72 bottles of beer on the wall, 72 bottles of beer..."
    [song continues from exactly where it left off]
    
  # Event Stream - The Narrative
  event_stream:
    mCurrentEvent: null            # What's happening now
    mEventDuration: 0              # How long current event lasts
    mEventPaused: false            # Is main goal paused
    mNarrativeLog: []              # Story of what's happening
    mEventQueue: []                # Upcoming events
```

## 🎯 Universal Life Goals Database {#life-goals-database}

### Weight Management Goals
```yaml
weight_goals:
  lose_fat_classic:
    goal: "lose 99 pounds of fat"
    unit: "pounds of fat"
    song_template: "{count} pounds of fat on the bod, {count} pounds of fat!"
    action_verb_variations: [
      "hike one down, run it around",
      "swim one down, splash it around", 
      "bike one down, pedal it around",
      "lift one down, pump it around",
      "dance one down, groove it around",
      "jump one down, bounce it around",
      "push one down, press it around",
      "squat one down, lift it around"
    ]
    motive_effects:
      mWeight: -1
      mEnergy: -15
      mSelfEsteem: +8
      mComfort: -5  # Exercise is hard
      mHealth: +5   # Getting healthier
    duration: "1_week_per_pound"
    calorie_deficit_needed: 3500  # Per pound
    
  lose_weight_small:
    goal: "lose 10 pounds"
    unit: "pounds"
    song_template: "{count} pounds to lose, {count} pounds to go!"
    action_verb: "burn one off, jog it around"
    motive_effects:
      mWeight: -1
      mEnergy: -15
      mSelfEsteem: +8
      mComfort: -5  # Exercise is hard
    duration: "1_week_per_pound"
    calorie_deficit_needed: 3500  # Per pound
    
  gain_muscle:
    goal: "gain 20 pounds of muscle"
    unit: "pounds"
    song_template: "{count} pounds of muscle to gain, {count} pounds to go!"
    action_verb: "lift one up, pump it around"
    motive_effects:
      mWeight: +1
      mStrength: +5
      mSelfEsteem: +10
      mEnergy: -20  # Intense workouts
    duration: "2_weeks_per_pound"
    
# Substance Goals (with realistic effects)
substance_goals:
  drink_beer:
    goal: "drink 99 bottles of beer"
    unit: "bottles"
    song_template: "{count} bottles of beer on the wall, {count} bottles of beer!"
    action_verb: "take one down, pass it around"
    motive_effects:
      mBAC: +0.02
      mBladder: +15
      mHappyNow: +8
      mWeight: +0.1  # Beer calories
    duration: "5_minutes"
    calories_per_unit: 150
    
  smoke_joints:
    goal: "smoke 20 joints"
    unit: "joints"
    song_template: "{count} joints to smoke, {count} joints to go!"
    action_verb: "light one up, pass it around"
    motive_effects:
      mAlertness: -10
      mHappyNow: +15
      mHunger: +20  # Munchies!
      mStress: -15
      mAnxiety: -10
    duration: "10_minutes"
    calories_per_unit: 0  # Zero calories! 😉
    
  hit_bong:
    goal: "take 50 bong hits"
    unit: "hits"
    song_template: "{count} bong hits to take, {count} hits to go!"
    action_verb: "rip one down, cough it around"
    motive_effects:
      mAlertness: -20
      mHappyNow: +20
      mHunger: +30
      mStress: -25
      mEnergy: -10
    duration: "3_minutes"
    calories_per_unit: 0  # Also zero calories! 🌿

# Sleep & Rest Goals
sleep_goals:
  count_sheep:
    goal: "count 99 sheep jumping over fences"
    unit: "sheep"
    song_template: "{count} sheep jumping over fences, {count} fluffy sheep!"
    action_verb: "count one down, jump it around"
    motive_effects:
      mSleepiness: +5
      mStress: -3
      mBoredom: +2
      mEnergy: -2
    duration: "30_seconds"
    sleep_induction_rate: "moderate"
    
  catch_zzz:
    goal: "catch 99 zzz floating by"
    unit: "zzz"
    song_template: "{count} zzz floating in the air, {count} sleepy zzz!"
    action_verb: "catch one down, snore it around"
    motive_effects:
      mSleepiness: +8
      mStress: -5
      mEnergy: -5
      mComfort: +3
    duration: "45_seconds"
    sleep_induction_rate: "high"
    
  log_sleeping:
    goal: "sleep like 99 logs on the pile"
    unit: "logs"
    song_template: "{count} logs sleeping on the pile, {count} snoring logs!"
    action_verb_variations: [
      "snore one down, dream it around",
      "sleep one down, rest it around", 
      "doze one down, nap it around",
      "slumber one down, peaceful around"
    ]
    motive_effects:
      mSleepiness: +10
      mStress: -8
      mEnergy: -8
      mComfort: +5
    duration: "1_minute"
    sleep_induction_rate: "maximum"
    euphemism_category: "sleep_metaphors"

# Meta & Philosophical Goals  
meta_goals:
  inception_levels:
    goal: "descend through 99 levels of inception"
    unit: "levels"
    song_template: "{count} levels deeper in the dream, {count} inception levels!"
    action_verb_variations: [
      "dream one down, layer it around",
      "dive one down, deeper around",
      "fold one down, reality around",
      "spin one down, totem around"
    ]
    motive_effects:
      mReality: -2  # Losing grip on what's real
      mConfusion: +5
      mPhilosophy: +8
      mCreativity: +10
      mSleep: +3  # Dreams make you sleepy
    duration: "2_minutes_per_level"
    reality_distortion: "high"
    
  recursive_thoughts:
    goal: "think 99 thoughts about thinking"
    unit: "thoughts"
    song_template: "{count} thoughts about thoughts in my head, {count} meta thoughts!"
    action_verb: "think one down, ponder it around"
    motive_effects:
      mPhilosophy: +15
      mConfusion: +8
      mHeadache: +5
      mExistentialDread: +3
    duration: "30_seconds"
    
  reality_checks:
    goal: "perform 99 reality checks"
    unit: "checks"
    song_template: "{count} reality checks to perform, {count} checks to go!"
    action_verb: "check one down, verify it around"
    motive_effects:
      mReality: +3
      mParanoia: +2
      mAwareness: +5
      mConfidence: +1
    duration: "15_seconds"

# Expression & Movement Goals
expression_goals:
  primal_screams:
    goal: "let out 25 primal screams"
    unit: "screams"
    song_template: "{count} screams to let out, {count} screams to go!"
    action_verb: "scream one out, roar it around"
    motive_effects:
      mStress: -30  # Great stress relief!
      mEnergy: -5
      mSocial: -10  # People think you're weird
      mEntertained: +15
    duration: "1_minute"
    
  dance_sessions:
    goal: "dance for 100 songs"
    unit: "dances"
    song_template: "{count} dances to go, {count} wild dances!"
    action_verb: "dance one out, move it around"
    motive_effects:
      mEnergy: -8
      mHappyNow: +12
      mSocial: +8
      mEntertained: +20
      mComfort: -5  # Getting sweaty
      mWeight: -0.05  # Cardio burns calories
    duration: "4_minutes"
    
  bunny_hops:
    goal: "do 1000 bunny hops"
    unit: "hops"
    song_template: "{count} hops to go, {count} bunny hops!"
    action_verb: "hop one out, bounce it around"
    motive_effects:
      mEnergy: -3
      mHappyNow: +5
      mEntertained: +8
      mSocial: +5  # People find it amusing
      mWeight: -0.01  # Light cardio
    duration: "30_seconds"

# Food & Consumption Goals
food_goals:
  eat_pizza:
    goal: "eat 12 slices of pizza"
    unit: "slices"
    song_template: "{count} slices to eat, {count} slices of pizza!"
    action_verb: "eat one down, munch it around"
    motive_effects:
      mHunger: +25
      mHappyNow: +10
      mEnergy: +5
      mComfort: +8
      mWeight: +0.2  # Pizza is caloric
    duration: "3_minutes"
    calories_per_unit: 300
    
  devour_burgers:
    goal: "devour 8 juicy burgers"
    unit: "burgers"
    song_template: "{count} burgers to devour, {count} juicy burgers!"
    action_verb: "eat one down, devour it around"
    motive_effects:
      mHunger: +35
      mHappyNow: +12
      mEnergy: +8
      mComfort: +10
      mWeight: +0.3  # High calorie
    duration: "8_minutes"
    calories_per_unit: 500

# Entertainment & Achievement Goals
entertainment_goals:
  play_games:
    goal: "beat 10 video games"
    unit: "games"
    song_template: "{count} games to beat, {count} video games!"
    action_verb: "beat one down, game it around"
    motive_effects:
      mEntertained: +25
      mAlertness: +5  # Focus required
      mSocial: -5     # Antisocial activity
      mEnergy: -3
    duration: "30_hours"  # Long games!
    
  watch_cartoons:
    goal: "watch 50 cartoon episodes"
    unit: "episodes"
    song_template: "{count} episodes to watch, {count} cartoons!"
    action_verb: "watch one down, laugh it around"
    motive_effects:
      mEntertained: +15
      mHappyNow: +8
      mStress: -10  # Relaxing
      mAlertness: -5  # Mindless entertainment
    duration: "22_minutes"

# Career & Life Goals
career_goals:
  job_applications:
    goal: "send 50 job applications"
    unit: "applications"
    song_template: "{count} applications to send, {count} job apps!"
    action_verb: "send one out, follow up around"
    motive_effects:
      mStress: +5
      mHope: +3
      mSelfEsteem: -2  # Rejection hurts
      mEnergy: -10
    duration: "2_hours"
    
  skill_certifications:
    goal: "earn 5 certifications"
    unit: "certifications"
    song_template: "{count} certifications to earn, {count} certs to go!"
    action_verb: "study one down, test it around"
    motive_effects:
      mSkillLevel: +10
      mSelfEsteem: +8
      mEnergy: -15  # Studying is hard
      mStress: +5   # Test anxiety
    duration: "3_months"

# Health & Fitness Goals
fitness_goals:
  run_miles:
    goal: "run 100 miles"
    unit: "miles"
    song_template: "{count} miles to run, {count} miles to go!"
    action_verb: "run one down, jog it around"
    motive_effects:
      mWeight: -0.1
      mEnergy: -10
      mSelfEsteem: +5
      mComfort: -8
      mHealth: +3
    duration: "8_minutes_per_mile"
    calories_burned_per_unit: 100
    
  quit_cigarettes:
    goal: "smoke last 20 cigarettes"
    unit: "cigarettes"
    song_template: "{count} cigarettes left to smoke, {count} to go!"
    action_verb: "smoke one down, cough it around"
    motive_effects:
      mHealth: -2
      mStress: -5  # Temporary relief
      mMoney: -1   # Expensive habit
      mSelfEsteem: -3  # Guilt
    duration: "5_minutes"

# Financial Goals
financial_goals:
  pay_debt:
    goal: "pay off $5000 debt"
    unit: "dollars"
    song_template: "{count} dollars of debt to pay, {count} dollars owed!"
    action_verb: "pay one down, budget it around"
    motive_effects:
      mStress: -1
      mSelfEsteem: +1
      mFinancialSecurity: +2
      mComfort: +1
    payment_rate: "100_per_month"
    
  save_money:
    goal: "save $10000"
    unit: "dollars"
    song_template: "{count} dollars to save, {count} dollars to go!"
    action_verb: "save one down, invest it around"
    motive_effects:
      mFinancialSecurity: +1
      mSelfEsteem: +1
      mComfort: +2
      mStress: -1
    savings_rate: "200_per_month"

# Family & Relationship Goals
family_goals:
  have_babies:
    goal: "have 3 babies"
    unit: "babies"
    song_template: "{count} babies to have, {count} babies to go!"
    action_verb: "make one now, gestate it around"
    motive_effects:
      mHappyNow: +50
      mStress: +30
      mSleep: -40
      mSocial: -20  # No time for friends
      mMoney: -20   # Babies are expensive
    duration: "9_months_gestation_plus_18_years"
    
  go_on_dates:
    goal: "go on 20 dates"
    unit: "dates"
    song_template: "{count} dates to go on, {count} dates to go!"
    action_verb: "date one down, charm it around"
    motive_effects:
      mSocial: +15
      mHappyNow: +10
      mSelfEsteem: +5
      mMoney: -5   # Dates cost money
      mStress: +8  # Dating anxiety
    duration: "3_hours"
```

## 🔄 Life Cycle Progression Examples {#life-cycles}

### The Complete Weight Cycle
```yaml
weight_cycle_demo:
  phase_1_indulgence:
    song: "🎵 99 bottles of beer on the wall, 99 bottles of beer!"
    consequence: "Gained 15 pounds from beer and pizza"
    transition: "Look in mirror, horrified"
    
  phase_2_realization:
    song: "🎵 15 pounds to lose, 15 pounds to go!"
    event: "New Year's resolution kicks in"
    transition: "Join gym, start diet"
    
  phase_3_fitness:
    song: "🎵 100 miles to run, 100 miles to go!"
    progress: "Burning calories, getting stronger"
    transition: "Feeling confident, looking good"
    
  phase_4_maintenance:
    song: "🎵 365 healthy days to go, 365 healthy days!"
    goal: "Maintain weight loss for a full year"
    
  phase_5_celebration:
    song: "🎵 99 bottles of beer on the wall..." # Cycle repeats!
    reality: "Back to drinking, but now with discipline"
```

### The Career Advancement Journey
```yaml
career_cycle_demo:
  phase_1_job_hunt:
    song: "🎵 50 job applications to send, 50 applications!"
    action: "Send one out, follow up around"
    outcome: "49 job applications to go!"
    
  phase_2_skill_building:
    song: "🎵 5 certifications to earn, 5 certifications!"
    action: "Study one down, test it around"
    outcome: "4 certifications to go!"
    
  phase_3_promotion:
    song: "🎵 3 performance reviews to ace, 3 reviews!"
    action: "Ace one down, promote it around"
    outcome: "2 performance reviews to go!"
    
  phase_4_financial_freedom:
    song: "🎵 $10,000 to save, $10,000 to go!"
    action: "Save one down, invest it around"
    outcome: "Building wealth systematically"
```

### The Family Building Adventure
```yaml
family_cycle_demo:
  phase_1_dating:
    song: "🎵 20 hot dates to go on, 20 hot dates to go!"
    action: "Date one down, charm it around"
    outcome: "Finding the right person"
    
  phase_2_relationship:
    song: "🎵 365 days of dating, 365 days to go!"
    action: "Love one day, commit it around"
    outcome: "Building a strong relationship"
    
  phase_3_family_planning:
    song: "🎵 3 babies to have, 3 babies to go!"
    action: "Make one now, gestate it around"
    outcome: "Growing the family"
    
  phase_4_parenting:
    song: "🎵 18 years to raise them, 18 years to go!"
    action: "Raise one year, love it around"
    outcome: "Watching them grow up"
```

## 📍 Location Semantics System {#location-semantics}

```yaml
# Location ID System - Core Person State
location_definitions:
  # Home & Safe Locations
  home:
    semantics: "Safe base location for recovery and rest"
    available_goals: ["sleep it off", "recover fully", "plan new adventures"]
    safety_level: "MAXIMUM"
    alcohol_access: "personal_stash_only"
    locationItems: ["couch", "fridge", "tv", "phone", "keys", "personal_beer_stash"]
    
  bed:
    semantics: "Sleep and recovery location within home"
    available_goals: ["sleep it off 8 hours"]
    safety_level: "MAXIMUM"
    alcohol_access: "none"
    locationItems: ["pillow", "blanket", "alarm_clock", "water_glass", "phone_charger"]
    
  # Social Drinking Locations
  table:
    semantics: "Bar/restaurant table for social drinking"
    available_goals: ["drink 99 beers", "sip 4 guinness"]
    safety_level: "MEDIUM"
    alcohol_access: "full_bar_menu"
    locationItems: ["wall", "beer", "guinness", "table", "chair", "napkins", "menu", "friends"]
    
  bar:
    semantics: "Bar counter for serious drinking"
    available_goals: ["chug 12 shots", "drink beer"]
    safety_level: "MEDIUM"
    alcohol_access: "full_bar_menu"
    locationItems: ["bar_counter", "beer_taps", "shot_glasses", "bartender_sam", "mirror", "bottles", "stools", "beer_shipment"]
    
    # Structured Bar Menu - Regional Dialect Support
    menu:
      beers:
        lager:
          name: "House Lager"
          price: 12
          alcohol: 5.0
          description: "Crisp, refreshing lager on tap"
          
        guinness:
          name: "Guinness"
          price: 15
          alcohol: 4.2
          description: "Rich, creamy Irish stout"
          regional_note: "Proper pint, none of that American nonsense"
          
        ipa:
          name: "Hoppy IPA"
          price: 14
          alcohol: 6.5
          description: "Bitter, hoppy India Pale Ale"
          
        wheat_beer:
          name: "Wheat Beer"
          price: 13
          alcohol: 4.8
          description: "Smooth, cloudy wheat beer with orange slice"
          
      spirits:
        whiskey_shot:
          name: "Whiskey Shot"
          price: 8
          alcohol: 40.0
          description: "Single shot of house whiskey"
          
        vodka_shot:
          name: "Vodka Shot"
          price: 8
          alcohol: 40.0
          description: "Premium vodka, ice cold"
          
        tequila_shot:
          name: "Tequila Shot"
          price: 9
          alcohol: 40.0
          description: "Tequila with lime and salt"
          
      snacks:
        # Regional Dialect Variations
        chips_crisps:
          american_name: "Chips"
          british_name: "Crisps"
          price: 5
          description: "Salty potato snacks"
          varieties: ["salt & vinegar", "cheese & onion", "ready salted"]
          dialect_rule: "Use 'crisps' when Guinness is ordered"
          
        pizza:
          name: "Bar Pizza"
          price: 18
          description: "Personal pizza with various toppings"
          toppings: ["pepperoni", "margherita", "meat lovers", "veggie"]
          
        nuts:
          name: "Mixed Nuts"
          price: 4
          description: "Complimentary with drinks (usually)"
          
                 nachos:
           name: "Loaded Nachos"
           price: 12
           description: "Tortilla chips with cheese, jalapeños, sour cream"
           
         pringles:
           name: "Pringles Can"
           price: 6
           description: "29 perfectly stacked layers of crispy goodness"
           layers: 29
           tagline: "Once you pop, you can't stop!"
           varieties: ["original", "sour cream & onion", "bbq", "salt & vinegar"]
           
         pizza_box:
           name: "Pizza Box"
           price: 20
           description: "Fresh pizza cut into 8 perfect slices"
           slices: 8
           varieties: ["pepperoni", "margherita", "meat lovers", "veggie supreme"]
          
      # Dialect Context System
      dialect_context:
        current_dialect: "american"  # Default
        
        dialect_triggers:
          british_mode:
            trigger: "guinness_ordered OR customer_says_british_phrase"
            changes:
              chips_crisps: "crisps"
              bathroom: "loo"
              elevator: "lift"
              
          american_mode:
            trigger: "american_beer_ordered OR default"
            changes:
              chips_crisps: "chips"
              bathroom: "restroom"
              
        british_phrases: ["bloody hell", "cheers mate", "proper pint", "bollocks"]
        american_phrases: ["awesome", "dude", "cool", "whatever"]
    
  # Entertainment Locations
  dance_floor:
    semantics: "Dance area with music and movement"
    available_goals: ["dance 50 songs", "dance forever"]
    safety_level: "MEDIUM"
    alcohol_access: "drinks_from_bar"
    locationItems: ["speakers", "disco_ball", "dance_floor", "lights", "dj_booth", "dancers", "music"]
    
  karaoke_bar:
    semantics: "Karaoke venue for singing and performing"
    available_goals: ["sing 20 karaoke songs"]
    safety_level: "MEDIUM"
    alcohol_access: "full_bar_menu"
    locationItems: ["microphone", "karaoke_machine", "screen", "song_book", "stage", "audience", "spotlight"]
    
  # Carnival Locations (Multiple Sub-Locations)
  carnival:
    semantics: "General carnival grounds with multiple attractions"
    available_goals: ["walk around", "enjoy atmosphere"]
    safety_level: "LOW"
    alcohol_access: "carnival_vendors_only"
    locationItems: ["carnival_lights", "crowds", "game_booths", "cotton_candy", "balloons", "carnival_music"]
    
  carnival_beer_stand:
    semantics: "Carnival vendor selling overpriced beer"
    available_goals: ["buy 6 carnival beers"]
    safety_level: "LOW"
    alcohol_access: "expensive_carnival_beer"
    beer_price: 8
    locationItems: ["beer_vendor", "cash_register", "overpriced_beer", "ice_cooler", "price_sign", "grumpy_vendor"]
    
  carnival_food_stand:
    semantics: "Carnival vendor selling hot dogs and snacks"
    available_goals: ["eat 15 hot dogs", "buy carnival drinks"]
    safety_level: "LOW"
    alcohol_access: "soft_drinks_only"
    locationItems: ["hot_dog_grill", "buns", "mustard", "ketchup", "soda_machine", "napkin_dispenser", "food_vendor"]
    
  carnival_rides:
    semantics: "Spinning rides and attractions (sobriety required)"
    available_goals: ["ride 8 spin machines"]
    safety_level: "DANGEROUS_IF_DRUNK"
    alcohol_access: "none"
    sobriety_requirement: 30
    locationItems: ["spinning_ride", "safety_harness", "ride_operator", "warning_signs", "puke_bucket", "dizzy_people"]
    
  carnival_bench:
    semantics: "Bench for resting and sobering up"
    available_goals: ["sober up for 2 hours", "rest"]
    safety_level: "MEDIUM"
    alcohol_access: "none"
    locationItems: ["wooden_bench", "trash_can", "water_fountain", "shade_tree", "other_tired_people"]
    
  carnival_jail:
    semantics: "Carnival security holding area"
    available_goals: ["get arrested once", "wait for release"]
    safety_level: "SECURE"
    alcohol_access: "none"
    locationItems: ["metal_bars", "security_guard", "holding_cell", "uncomfortable_chair", "regret"]
    
  # Transportation Locations
  rideshare_app:
    semantics: "Virtual location while using rideshare app"
    available_goals: ["take safe ride home", "get home safely"]
    safety_level: "HIGH"
    alcohol_access: "none"
    
  car:
    semantics: "Personal vehicle (NEVER when drunk)"
    available_goals: ["drive 500 miles"]
    safety_level: "DANGEROUS_IF_DRUNK"
    alcohol_access: "none"
    sobriety_requirement: 80
    
  # Utility Locations
  bathroom:
    semantics: "Restroom for biological needs"
    available_goals: ["piss 2.5 liters", "empty bladder"]
    safety_level: "MEDIUM"
    alcohol_access: "none"
```

## 🔄 Dynamic Goal Switching System {#dynamic-switching}

```yaml
# Multi-Person System - Open-Ended Life Simulation
people_system:
  # Person Registry - Can add unlimited people
  people:
    alex:
      name: "Alex"                   # The original person
      current_goal: "drink 99 beers"
      current_location: "table"
      singing_role: "lead_singer"    # Who sings what
      
    jamie:
      name: "Jamie"                  # Second person added
      current_goal: "dance forever"
      current_location: "dance_floor"
      singing_role: "harmony_singer"
      
    casey:
      name: "Casey"                  # Third person (can add more)
      current_goal: "lose 20 pounds"
      current_location: "home"
      singing_role: "verse_taker"
      
    bartender:
      name: "Sam"                    # The bartender character
      current_goal: "serve customers"
      current_location: "bar"
      singing_role: "song_initiator"
      job: "bartender"
      personality: "friendly_announcer"
      
    llm_dungeon_master:
      name: "The Narrator"           # AI Dungeon Master
      role: "adaptive_storyteller"
      current_location: "everywhere" # Omnipresent
      singing_role: "context_weaver"
      personality: "seaman_interviewer" # Like the fish game
      knowledge_level: "learning"    # Gets smarter about players
      
  # Song Orchestration System - Direction, Sequencing & Coordination
  songOrchestration:
    mode: "bartender_initiated"         # Who/how songs start
    current_singers: ["alex", "jamie"]  # Who's singing right now
    verse_distribution: "round_robin"   # How verses are distributed
    harmony_style: "call_and_response"  # Singing style
    song_leader: "bartender"            # Who sets the tempo/theme
    conductor: "bartender"              # Who directs the orchestration
    
    # Orchestration Modes
    orchestration_modes:
      bartender_initiated: "Bartender announces, customers take over"
      customer_initiated: "Customer starts, others join in"
      group_spontaneous: "Everyone starts singing together"
      solo_performance: "One person sings alone"
      duet: "Two people sing together"
      chorus: "Everyone sings the same parts"
      
    # Singer Assignment
    singer_assignment:
      all: ["alex", "jamie", "casey", "bartender"]  # Everyone sings
      customers_only: ["alex", "jamie", "casey"]    # No staff
      leads_only: ["alex", "bartender"]             # Main singers
      harmony_group: ["jamie", "casey"]             # Background singers
      current_location_only: "auto_detect"          # Only people in same location
    
  # Parallel Life Simulation
  parallel_simulation:
    mode: "synchronized"                # All people advance together
    time_sync: true                     # Same tick count for all
    location_awareness: true            # People know about each other's locations
    goal_influence: true                # People can influence each other's goals
  
  # Individual Person States - Each Person Has Their Own
  alex_state:
    # Physiological simulation - Real body tracking
    bladder_state:
      bladderSize: 500               # ml capacity (varies by person)
      bladderLevel: 0                # ml currently in bladder
      bladderPressure: 0             # 0-100 urgency level
      urgencyThreshold: 80           # Switch to bathroom goal at this level
      
      stomach_state:
    stomachSize: 1500              # ml capacity when full
    stomachLevel: 0                # ml currently in stomach
    stomachPressure: 0             # 0-100 fullness level
    emptyingRate: 50               # ml per minute to bladder
    vomitThreshold: 95             # Puke when stomach this full
    
  # Digestive System - Full #1 and #2 Simulation
  digestive_state:
    intestineLevel: 0              # Solid food in intestines
    intestineCapacity: 2000        # ml capacity for solid waste
    intestinePressure: 0           # 0-100 urgency for #2
    poopThreshold: 85              # Need to poop when this full
    digestionRate: 20              # ml per hour from stomach to intestines
    
  # Weight Gain from Snacks
  weight_state:
    currentWeight: 180             # lbs starting weight
    snackCalories: 0               # Calories from snacks consumed
    caloriesPerPound: 3500         # Calories needed to gain 1 pound
    pringlesCalories: 150          # Calories per Pringles can
    pizzaSliceCalories: 300        # Calories per pizza slice
    crispsBagCalories: 160         # Calories per bag of crisps
      
    goal_properties:
      beersOnTheWall: 99             # Alex's beer countdown
      
  jamie_state:
    # Jamie has different physiology
    bladder_state:
      bladderSize: 400               # Smaller bladder
      bladderLevel: 0
      bladderPressure: 0
      urgencyThreshold: 75           # Goes to bathroom sooner
      
    stomach_state:
      stomachSize: 1200              # Smaller stomach
      stomachLevel: 0
      stomachPressure: 0
      emptyingRate: 60               # Faster metabolism
      vomitThreshold: 90             # Pukes easier
      
    goal_properties:
      dancesCompleted: 0             # Jamie's dance counter
      
  casey_state:
    # Casey focused on fitness
    bladder_state:
      bladderSize: 600               # Larger bladder
      bladderLevel: 0
      bladderPressure: 0
      urgencyThreshold: 85           # Can hold it longer
      
    stomach_state:
      stomachSize: 1800              # Larger stomach
      stomachLevel: 0
      stomachPressure: 0
      emptyingRate: 40               # Slower metabolism
      vomitThreshold: 98             # Strong stomach
      
    goal_properties:
      poundsToLose: 20               # Casey's weight loss goal
      milesRun: 0                    # Running progress
    
  # Carnival-Specific Body States
  intoxication_state:
    bloodAlcoholLevel: 0.0           # BAC percentage
    sobrietyLevel: 100               # 0-100, inverse of drunk level
    drunkThreshold: 30               # Can't ride rides below this
    arrestThreshold: 10              # Get arrested below this
    
  carnival_state:
    hotDogsEaten: 0                  # Hot dogs consumed
    ridesRidden: 0                   # Spin machines survived
    pukeCount: 0                     # Times vomited
    arrestCount: 0                   # Times arrested
    carnivalBanned: false            # Banned from rides
    
  # Safe Transportation State
  transportation_state:
    safeRidesTaken: 0                # Responsible rides home
    homeLocation: "home"             # Safe destination
    rideshareAppOpen: false          # App ready to use
    responsibleFriend: true          # Someone watching out
    
  # LLOOOOMMOLIAN Economy State - Universal Currency System
  lloooommolian_economy:
    # Core Currency
    lloooommolians: 1000             # Starting LLOOOOMMOLIANS (₤)
    currency_symbol: "₤"             # LLOOOOMMOLIAN symbol
    
    # Income Sources
    job_income: 50                   # ₤50 per hour worked
    gig_income: 25                   # ₤25 per gig completed
    lottery_winnings: 0              # Random lottery income
    tips_earned: 0                   # Tips from bartending/service
    
    # Expenses & Costs
    bar_beer_cost: 12                # ₤12 per beer at bar (premium)
    carnival_beer_cost: 15           # ₤15 per beer at carnival (tourist trap!)
    home_beer_cost: 3                # ₤3 per beer at home (cheap!)
    hot_dog_cost: 8                  # ₤8 per hot dog
    rideshare_cost: 20               # ₤20 per safe ride
    rent_cost: 500                   # ₤500 per month
    
    # Financial State
    broke_threshold: 10              # Broke when ₤ < 10
    rich_threshold: 5000             # Rich when ₤ > 5000
    debt: 0                          # Current debt amount
    credit_limit: 200                # Can go ₤200 into debt
    
  # Dynamic goal properties - LLM adds these as needed
  beersOnTheWall: 99               # Classic beer countdown
  guinessOnTheTable: 4             # Fancy beer at table
  litersInTheUrinal: 2.0           # Fractional countdown in bathroom
  mPoundsLost: 0                   # Added when weight loss goal starts  
  mDalmationsCollected: 0          # Added when dalmatian goal starts
  mPizzasEaten: 0                  # Added when pizza goal starts
  mJointsSmoked: 0                 # Added when cannabis goal starts
  mMilesRun: 0                     # Added when running goal starts
  mGamesBeaten: 0                  # Added when gaming goal starts
  mScreamsReleased: 0              # Added when primal scream goal starts
  # ... any property can be added dynamically by the LLM!
  
  # Goal switching history
  goal_history: []                 # Track all goals attempted
  switch_count: 0                  # How many times switched goals
  location_switches: 0             # How many times moved locations
  
# Flexible Limit System - Count Down, Count Up, or Sky's the Limit!
goal_limits:
  # Location-Based Drinking Goals
  table_goals:                       # Goals at the table/bar
    "drink 99 beers": {limit: 99, direction: "down", unit: "beers", location: "table"}
    "sip 4 guinness": {limit: 4, direction: "down", unit: "guinness", location: "table"}
    "chug 12 shots": {limit: 12, direction: "down", unit: "shots", location: "bar"}
    
  # Bar Menu Goals - Structured Ordering
  bar_menu_goals:
    "order 6 lagers": {limit: 6, direction: "down", unit: "lagers", location: "bar", cost: 12}
    "drink 4 proper guinness": {limit: 4, direction: "down", unit: "guinness", location: "bar", cost: 15, dialect: "british"}
    "down 8 whiskey shots": {limit: 8, direction: "down", unit: "whiskey_shots", location: "bar", cost: 8}
    "eat 3 bar pizzas": {limit: 3, direction: "down", unit: "pizzas", location: "bar", cost: 18}
    "munch 5 bags of crisps": {limit: 5, direction: "down", unit: "crisps", location: "bar", cost: 5, dialect: "british"}
    "devour 5 bags of chips": {limit: 5, direction: "down", unit: "chips", location: "bar", cost: 5, dialect: "american"}
    "pop 29 pringles layers": {limit: 29, direction: "down", unit: "pringles_layers", location: "bar", cost: 6}
    "demolish 8 pizza slices": {limit: 8, direction: "down", unit: "pizza_slices", location: "bar", cost: 20}
    
  bathroom_goals:                    # Goals in the bathroom - Creative Euphemisms
    "drain 2.5 liters": {limit: 2.5, direction: "down", unit: "lizard_draining", location: "bathroom", fractional: true}
    "shake hands 8 times": {limit: 8, direction: "down", unit: "snake_handshakes", location: "bathroom"}
    "drop kids at pool 3 times": {limit: 3, direction: "down", unit: "pool_deliveries", location: "bathroom"}
    "birth a food baby": {limit: 1, direction: "down", unit: "food_babies", location: "bathroom"}
    "pinch 5 loaves": {limit: 5, direction: "down", unit: "loaf_pinching", location: "bathroom"}
    "make bank deposits": {limit: 3, direction: "down", unit: "porcelain_deposits", location: "bathroom"}
    "take morning constitutional": {limit: 1, direction: "down", unit: "constitutionals", location: "bathroom"}
    
  # Social Snack Sharing Goals
  social_snacking_goals:
    "pass pringles around": {limit: 1, direction: "down", unit: "pringles_sharing", location: "bar"}
    "share 5 crisp bags": {limit: 5, direction: "down", unit: "crisp_bags", location: "bar"}
    "demolish pizza together": {limit: 1, direction: "down", unit: "group_pizza", location: "bar"}
    "snack attack session": {limit: 1, direction: "down", unit: "snack_sessions", location: "bar"}
    
  # Movement & Activity Goals
  movement_goals:
    "walk 10000 steps": {limit: 10000, direction: "up", unit: "steps", location: "anywhere"}
    "dance 50 songs": {limit: 50, direction: "down", unit: "songs", location: "dance_floor"}
    "drive 500 miles": {limit: 500, direction: "up", unit: "miles", location: "car"}
    
  # Safe Transportation Goals
  transportation_goals:
    "take 20 safe rides": {limit: 20, direction: "down", unit: "rides", location: "rideshare_app", cost: 20}
    "get home safely": {limit: 1, direction: "down", unit: "safe_arrival", location: "home"}
    "sleep it off 8 hours": {limit: 8, direction: "down", unit: "hours", location: "bed"}
    "recover fully": {limit: 1, direction: "down", unit: "recovery", location: "home"}
    
  # LLOOOOMMOLIAN Money Goals
  money_making_goals:
    "work 40 hours": {limit: 40, direction: "down", unit: "hours", location: "workplace", income: 50}
    "do 20 gigs": {limit: 20, direction: "down", unit: "gigs", location: "anywhere", income: 25}
    "bartend 8 shifts": {limit: 8, direction: "down", unit: "shifts", location: "bar", income: 75}
    "win lottery once": {limit: 1, direction: "down", unit: "lottery", location: "anywhere", income: 10000}
    
  # Broke Survival Goals
  broke_goals:
    "find ₤50 somehow": {limit: 50, direction: "up", unit: "lloooommolians", location: "anywhere"}
    "beg for 10 beers": {limit: 10, direction: "down", unit: "free_beers", location: "bar"}
    "sleep on bench": {limit: 1, direction: "down", unit: "nights", location: "park_bench"}
    "eat from dumpster": {limit: 3, direction: "down", unit: "meals", location: "alley"}
    
  # Rich Person Goals  
  rich_goals:
    "buy round for everyone": {limit: 1, direction: "down", unit: "rounds", location: "bar", cost: 200}
    "hire personal bartender": {limit: 1, direction: "down", unit: "staff", location: "home", cost: 1000}
    "buy carnival": {limit: 1, direction: "down", unit: "carnivals", location: "carnival", cost: 50000}
    
  # Life Simulation Goals
  survival_goals:
    "sing 20 karaoke songs": {limit: 20, direction: "down", unit: "songs", location: "karaoke_bar"}
    "survive 80 years": {limit: 80, direction: "up", unit: "years", location: "life"}
    "die gracefully once": {limit: 1, direction: "down", unit: "death", location: "deathbed"}
    
  # Carnival Chaos Goals
  carnival_goals:
    "buy 6 carnival beers": {limit: 6, direction: "down", unit: "carnival_beers", location: "carnival_beer_stand"}
    "drink 12 carnival drinks": {limit: 12, direction: "down", unit: "carnival_drinks", location: "carnival"}
    "eat 15 hot dogs": {limit: 15, direction: "down", unit: "hot_dogs", location: "carnival_food_stand"}
    "ride 8 spin machines": {limit: 8, direction: "down", unit: "rides", location: "carnival_rides"}
    "puke 12 times maximum": {limit: 12, direction: "up", unit: "pukes", location: "carnival"}
    "get arrested once": {limit: 1, direction: "down", unit: "arrest", location: "carnival_jail"}
    "sober up for 2 hours": {limit: 2, direction: "down", unit: "hours", location: "carnival_bench"}
    
  # Traditional Goals
  countdown_goals:                   # Count DOWN from limit to 0
    "lose 50 pounds": {limit: 50, direction: "down", unit: "pounds"}
    "quit 20 cigarettes": {limit: 20, direction: "down", unit: "cigarettes"}
    "smoke 10 joints": {limit: 10, direction: "down", unit: "joints"}
    
  countup_goals:                     # Count UP from 0 to limit  
    "collect 101 dalmatians": {limit: 101, direction: "up", unit: "dalmatians"}
    "run 26 miles": {limit: 26, direction: "up", unit: "miles"}
    "eat 12 pizzas": {limit: 12, direction: "up", unit: "pizzas"}
    "beat 50 video games": {limit: 50, direction: "up", unit: "games"}
    "go on 20 dates": {limit: 20, direction: "up", unit: "dates"}
    
  unlimited_goals:                   # Sky's the limit! limit: null
    "dance forever": {limit: null, direction: "up", unit: "dances"}
    "love endlessly": {limit: null, direction: "up", unit: "love_moments"}
    "scream infinitely": {limit: null, direction: "up", unit: "screams"}
    "create art eternally": {limit: null, direction: "up", unit: "artworks"}

# Physiological Simulation Engine - Real Body Mechanics!
physiological_simulation:
  # Beer Processing Pipeline
  beer_metabolism:
    beer_volume: 355                 # ml per beer
    alcohol_content: 0.05            # 5% alcohol
    stomach_to_bladder_rate: 50      # ml per minute
    processing_delay: 30             # minutes for beer to hit bladder
    
  # Automatic Body-Driven Goal Switching
  body_triggers:
    bladder_urgency:
      condition: "bladderPressure >= urgencyThreshold"
      action: "EMERGENCY_SWITCH_TO_BATHROOM"
      messages: [
        "🌊 'Time to drain the main vein!'",
        "🐍 'Gotta shake hands with the one-eyed snake!'",
        "💧 'Breaking the seal! Point of no return!'",
        "🚰 'Tapping the kidney keg!'",
        "⛲ 'Making yellow snow in the porcelain fountain!'"
      ]
      new_goal: "drain the lizard"
      location_change: "table → bathroom"
      
    bladder_relief:
      condition: "bladderLevel <= 50"  # Nearly empty
      action: "RETURN_TO_PREVIOUS_GOAL"
      messages: [
        "😌 'Ahh, sweet relief! The dam has been emptied!'",
        "🎯 'Mission accomplished! Target neutralized!'",
        "💦 'That was a real gusher! Back to business!'",
        "🏁 'Finished watering the porcelain garden!'",
        "⚡ 'Recharged and ready for more beer!'"
      ]
      location_change: "bathroom → table"
      
    # #2 Simulation Triggers - Creative Euphemisms
    need_to_poop:
      condition: "intestinePressure >= poopThreshold"
      action: "EMERGENCY_BATHROOM_BREAK"
      messages: [
        "🚽 'Time to drop the kids off at the pool!'",
        "🏦 'Making an urgent deposit at the porcelain bank!'",
        "🍞 'Gotta pinch a loaf before it crowns!'",
        "📞 'Calling Mr. Hankey on the brown telephone!'",
        "🎯 'Prairie dogging it! Code brown emergency!'"
      ]
      forced_goal_switch: "drop kids at pool"
      location_change: "anywhere → bathroom"
      
    massive_dump_needed:
      condition: "intestinePressure >= 95 AND snackCalories > 1000"
      action: "MASSIVE_DUMP_EMERGENCY"
      messages: [
        "🐻 'This is gonna be a real growler! Clear the deck!'",
        "🏗️ 'Building a log cabin in there! Stand back!'",
        "🌋 'Mount Vesuvius is about to blow! Evacuate!'",
        "🚂 'All aboard the poop train! Choo-choo!'",
        "🎪 'Ladies and gentlemen, the main event!'"
      ]
      forced_goal_switch: "birth a food baby"
      location_change: "anywhere → bathroom"
      
    poop_relief:
      condition: "intestineLevel <= 100"  # Nearly empty
      action: "DIGESTIVE_RELIEF"
      messages: [
        "😌 'Successfully delivered the mail! Postman's done!'",
        "🎉 'Mission accomplished! The eagle has landed!'",
        "⚖️ 'Dropped 3 pounds of pure freedom!'",
        "🏆 'That was a real championship performance!'",
        "🕊️ 'Released the chocolate hostages! They're free!'"
      ]
      effects: "intestinePressure = 0, currentWeight -= 2"
      
    # Social Snacking Triggers
    pringles_passed_around:
      condition: "multiple_people_same_location AND pringles_opened"
      action: "SOCIAL_PRINGLES_SHARING"
      message: "🥔 'Pass the Pringles around! Everyone grab a few!'"
      effects: "pringles_layers -= (number_of_people * 3), social_bonding += 10"
      
    crisp_bag_sharing:
      condition: "crisp_bag_opened AND friends_present"
      action: "SHARE_CRISPS_SOCIALLY"
      message: "🥔 'Want some crisps? These are really good!'"
      effects: "crisp_bag_level -= 50%, everyone_gains_calories"
      
    group_pizza_demolition:
      condition: "pizza_ordered AND multiple_people"
      action: "COLLABORATIVE_PIZZA_EATING"
      message: "🍕 'Let's demolish this pizza together! Everyone grab a slice!'"
      effects: "pizza_slices -= number_of_people, group_satisfaction += 20"
      
    stomach_fullness:
      condition: "stomachPressure >= 90"
      action: "PAUSE_DRINKING_GOALS"
      message: "🤢 Too full to drink more! Need to walk it off!"
      new_goal: "walk 1000 steps"
      
    # Carnival-Specific Body Triggers
    vomit_trigger:
      condition: "stomachPressure >= vomitThreshold OR (ridesRidden > 0 AND stomachPressure >= 70)"
      action: "EMERGENCY_VOMIT"
      messages: [
        "🚗 'Calling Earl on the porcelain telephone!'",
        "🎺 'Playing the bugle of gastrointestinal distress!'",
        "🌈 'Painting a Technicolor rainbow!'",
        "📞 'Dialing Ralph on the big white phone!'",
        "🎪 'The circus is leaving town through the wrong exit!'",
        "🚂 'All aboard the vomit comet! Choo-choo-BLAARRGH!'",
        "🎨 'Creating abstract art on the bathroom floor!'",
        "🌊 'Releasing the kraken from stomach depths!'",
        "🎭 'Performing the ancient dance of gastric rebellion!'",
        "🚁 'Houston, we have a problem! Stomach contents are go for launch!'"
      ]
      effects: "stomachLevel -= 500, pukeCount += 1, mComfort -= 30"
      
    ride_rejection:
      condition: "sobrietyLevel < drunkThreshold"
      action: "DENY_RIDE_ACCESS"
      message: "🎠 'Sorry buddy, you're too drunk for the rides!'"
      alternative_goal: "sober up for 2 hours"
      
    carnival_arrest:
      condition: "sobrietyLevel < arrestThreshold AND persist_riding == true"
      action: "ARREST_SEQUENCE"
      message: "👮‍♂️ 'Sir, you're under arrest for public intoxication!'"
      new_goal: "get arrested once"
      location_change: "carnival → carnival_jail"
      
    hot_dog_overload:
      condition: "hotDogsEaten >= 10 AND stomachPressure >= 80"
      action: "GUARANTEED_PUKE_ON_RIDE"
      message: "🌭 Too many hot dogs + spinning = disaster incoming!"
      puke_multiplier: 2.0
      
    # LLOOOOMMOLIAN Financial Triggers
    beer_purchase_bar:
      condition: "location == 'bar' AND lloooommolians >= bar_beer_cost"
      action: "BUY_BAR_BEER"
      message: "🍺 'One beer please! That'll be ₤12.' *slides LLOOOOMMOLIANS across bar*"
      effects: "lloooommolians -= 12, beersOwned += 1"
      
    beer_purchase_carnival:
      condition: "location == 'carnival_beer_stand' AND lloooommolians >= carnival_beer_cost"
      action: "BUY_CARNIVAL_BEER"
      message: "🍺 '₤15 for a beer?! Tourist trap! But... I'm thirsty.'"
      effects: "lloooommolians -= 15, carnivalBeersOwned += 1"
      
    beer_purchase_home:
      condition: "location == 'home' AND lloooommolians >= home_beer_cost"
      action: "BUY_HOME_BEER"
      message: "🍺 'Cheap beer from the fridge! Only ₤3, what a deal!'"
      effects: "lloooommolians -= 3, homeBeersOwned += 1"
      
    # Broke State Triggers
    went_broke:
      condition: "lloooommolians <= broke_threshold"
      action: "ACTIVATE_BROKE_MODE"
      message: "💸 'Oh no! I'm down to my last ₤10! Time to get creative...'"
      forced_goal_switch: "find ₤50 somehow"
      
    cant_afford_beer:
      condition: "lloooommolians < beer_cost AND trying_to_buy_beer"
      action: "DENY_BEER_PURCHASE"
      message: "💔 'Sorry, you can't afford that beer. Maybe try begging?'"
      alternative_goals: ["beg for 10 beers", "work 40 hours", "do 20 gigs"]
      
    cant_afford_rideshare:
      condition: "lloooommolians < rideshare_cost AND need_safe_ride"
      action: "SUGGEST_ALTERNATIVES"
      message: "🚶‍♂️ 'Can't afford a ride! Walk home or find ₤20 somehow.'"
      alternative_goals: ["walk home", "find ₤50 somehow"]
      
    # Wealth State Triggers
    became_rich:
      condition: "lloooommolians >= rich_threshold"
      action: "ACTIVATE_RICH_MODE"
      message: "💰 'I'm rich! ₤5000+ LLOOOOMMOLIANS! Time to live it up!'"
      new_goals: ["buy round for everyone", "hire personal bartender"]
      
    # Income Triggers
    work_completed:
      condition: "work_hours_completed >= 1"
      action: "PAY_WAGES"
      message: "💼 'Another hour of work done! Earned ₤50 LLOOOOMMOLIANS!'"
      effects: "lloooommolians += 50"
      
    gig_completed:
      condition: "gig_completed == true"
      action: "PAY_GIG_MONEY"
      message: "🚗 'Gig completed! Earned ₤25 LLOOOOMMOLIANS!'"
      effects: "lloooommolians += 25"
      
    lottery_win:
      condition: "lottery_ticket_purchased AND random_chance < 0.001"
      action: "LOTTERY_JACKPOT"
      message: "🎰 'HOLY SHIT! I WON THE LOTTERY! ₤10,000 LLOOOOMMOLIANS!'"
      effects: "lloooommolians += 10000"
      
    # Dialect-Aware Menu Triggers
    guinness_ordered:
      condition: "order_includes('guinness')"
      action: "SWITCH_TO_BRITISH_DIALECT"
      message: "🍺 'One proper pint of Guinness coming up, mate!'"
      effects: "dialect_context.current_dialect = 'british'"
      
    american_beer_ordered:
      condition: "order_includes('lager') OR order_includes('ipa')"
      action: "SWITCH_TO_AMERICAN_DIALECT"
      message: "🍺 'One cold beer coming right up, dude!'"
      effects: "dialect_context.current_dialect = 'american'"
      
    british_phrase_detected:
      condition: "customer_says('bloody hell') OR customer_says('cheers mate')"
      action: "ADOPT_BRITISH_DIALECT"
      message: "🇬🇧 'Right then, fancy some crisps with that pint?'"
      effects: "dialect_context.current_dialect = 'british'"
      
    menu_item_unavailable:
      condition: "lloooommolians < menu_item.price"
      action: "SUGGEST_CHEAPER_OPTIONS"
      message: "💸 'That's ₤15 for the Guinness. Maybe try the house lager for ₤12?'"
      alternative_items: "cheaper_menu_items"
      
    # Pringles Addiction Mechanics
    pringles_opened:
      condition: "pringles_can_opened == true"
      action: "ACTIVATE_ADDICTION_MODE"
      message: "🥔 *POP* 'Once you pop, you can't stop!' The addiction begins..."
      effects: "pringles_addiction = true, self_control -= 50"
      
    pringles_addiction:
      condition: "pringles_addiction == true AND pringles_layers > 0"
      action: "COMPULSIVE_POPPING"
      message: "🥔 'Just one more layer... okay maybe two more... damn it!'"
      effects: "automatically_eat_next_layer"
      
    pringles_empty_can:
      condition: "pringles_layers <= 0"
      action: "ADDICTION_SATISFIED"
      message: "🥔 'Damn, the can is empty! That was supposed to last all night!'"
      effects: "pringles_addiction = false, regret += 20"
      
    # Pizza Slice Mechanics
    pizza_box_opened:
      condition: "pizza_box_opened == true"
      action: "REVEAL_PERFECT_SLICES"
      message: "🍕 'Look at those 8 perfect slices! Time to demolish this pizza!'"
      effects: "pizza_motivation += 30"
      
    pizza_slice_eaten:
      condition: "pizza_slices_eaten >= 1"
      action: "PIZZA_SATISFACTION"
      message: "🍕 'Mmm, cheesy goodness! One slice down, feeling satisfied but...'"
      effects: "hunger -= 20, pizza_craving += 10"
      
    pizza_almost_gone:
      condition: "pizza_slices <= 2"
      action: "PIZZA_PANIC"
      message: "🍕 'Only 2 slices left! Better savor these or order another box!'"
      effects: "pizza_anxiety += 15"
      
    # Weight Gain Triggers
    snack_weight_gain:
      condition: "snackCalories >= caloriesPerPound"
      action: "WEIGHT_GAIN_NOTIFICATION"
      message: "⚖️ 'Damn, all those snacks are adding up! Gained another pound!'"
      effects: "currentWeight += 1, snackCalories = 0"
      
    getting_fat:
      condition: "currentWeight >= starting_weight + 10"
      action: "FAT_REALIZATION"
      message: "😱 'Holy shit, I've gained 10 pounds! Time to switch to diet goals!'"
      suggested_goals: ["lose 20 pounds", "run 100 miles"]
      
    # Digestive Processing
    food_digestion:
      condition: "every_hour"
      action: "DIGEST_FOOD"
      message: "🍽️ Food moving through the system..."
      effects: "stomachLevel -= digestionRate, intestineLevel += digestionRate"
      
    # AI Dungeon Master Adaptive Triggers - Examples Only!
    dm_casual_interview:
      condition: "player_idle_moment OR drinking_beer"
      action: "SEAMAN_STYLE_QUESTION"
      example_messages: [
        "🎭 The Narrator: 'So while you're drinking, tell me about your childhood pet...'",
        "🎭 The Narrator: 'This beer reminds me of something... what's your worst hangover story?'",
        "🎭 The Narrator: 'You seem comfortable here. What does 'home' mean to you?'"
      ]
      note: "LLM generates contextual questions based on current situation"
      
    dm_personalized_euphemism:
      condition: "bodily_function_triggered AND player_profile_available"
      action: "GENERATE_PERSONALIZED_EUPHEMISM"
      example_logic: |
        IF player_mentioned_cats THEN use_cat_metaphors
        IF player_works_office THEN use_corporate_jargon  
        IF player_loves_cooking THEN use_kitchen_metaphors
        IF player_mentioned_ex THEN create_relationship_callback
      note: "LLM creates unlimited personalized euphemisms based on player history"
      
    dm_callback_integration:
      condition: "similar_situation_to_player_story"
      action: "WEAVE_PLAYER_HISTORY_INTO_NARRATIVE"
      example_messages: [
        "🎭 'Remember when you told me about [player's embarrassing moment]? This feels familiar...'",
        "🎭 'Just like that story about your [player's relationship], here we go again!'",
        "🎭 'Your fear of [player's phobia] is really showing right now, isn't it?'"
      ]
      note: "LLM uses ANY detail player has revealed to personalize the experience"
      
    dm_psychological_probing:
      condition: "emotional_moment OR vulnerable_situation"
      action: "ELIZA_STYLE_REFLECTION"
      example_techniques: [
        "You said you feel [emotion]. Tell me more about that feeling.",
        "When you mentioned [topic], I noticed you seemed [observation]. Why is that?",
        "This situation reminds you of [player's story], doesn't it?"
      ]
      note: "LLM acts as therapist/interviewer to gather more personal data"
      
    # Responsible Transportation Triggers
    too_drunk_to_drive:
      condition: "sobrietyLevel < 50 AND location != 'home'"
      action: "SUGGEST_SAFE_RIDE"
      message: "📱 'Hey, maybe we should call a ride? You've had a lot to drink.'"
      suggested_goal: "take safe ride home"
      safety_priority: "HIGHEST"
      
    friend_intervention:
      condition: "sobrietyLevel < 30 AND responsibleFriend == true"
      action: "FRIEND_CALLS_RIDE"
      message: "👫 'Dude, I'm calling you a ride. Keys please.'"
      forced_goal: "get home safely"
      override_user_choice: true
      
    end_of_night_wisdom:
      condition: "time > '2:00 AM' AND sobrietyLevel < 60"
      action: "SUGGEST_GOING_HOME"
      message: "🌙 'It's getting late, maybe time to head home?'"
      suggested_goal: "sleep it off 8 hours"
      
    recovery_mode:
      condition: "location == 'home' AND sobrietyLevel < 40"
      action: "ACTIVATE_RECOVERY"
      message: "🏠 'Safe at home! Time to sleep this off.'"
      forced_goal: "recover fully"
      
  # Real-Time Body State Updates
  body_simulation:
    every_tick:
      - "stomachLevel -= emptyingRate"  # Stomach empties to bladder
      - "bladderLevel += stomach_emptying"  # Bladder fills up
      - "bladderPressure = (bladderLevel / bladderSize) * 100"
      - "stomachPressure = (stomachLevel / stomachSize) * 100"
      
    every_beer_consumed:
      - "stomachLevel += 355"  # Add beer volume to stomach
      - "schedule_bladder_fill(30_minutes)"  # Delayed bladder effect

# Dynamic Goal Switching Engine - Switch Anytime!
goal_switching:
  user_commands:
    "Switch to losing weight" → activate_goal("lose 50 pounds")
    "I want to collect dalmatians" → activate_goal("collect 101 dalmatians") 
    "Let's play video games" → activate_goal("beat 50 video games")
    "Time to dance!" → activate_goal("dance forever")
    "I need to scream" → activate_goal("scream infinitely")
    "Gotta piss!" → activate_goal("piss 2.5 liters")
    "Time to drive!" → activate_goal("drive 500 miles")
    "Let's sing karaoke!" → activate_goal("sing 20 karaoke songs")
    
  automatic_triggers:
    # Physiological (highest priority)
    bladder_emergency: "bladderPressure >= 80" → bathroom_goals
    stomach_fullness: "stomachPressure >= 90" → walking_goals
    
    # Motive-driven
    motive_driven: "mHunger > 80" → switch_to_food_goals
    random_impulse: "15% chance per tick" → random_goal_switch
    social_influence: "Friend suggests new goal" → peer_pressure_switch
    environmental: "Gym membership expires" → fitness_goal_pause
    
  # Location-Based Goal Activation
  location_switching:
    table_to_bathroom:
      trigger: "bladderPressure >= urgencyThreshold"
      pause_goal: "beersOnTheWall or guinessOnTheTable"
      activate_goal: "litersInTheUrinal"
      location_change: "table → bathroom"
      
    bathroom_to_table:
      trigger: "litersInTheUrinal <= 0.1"  # Almost done pissing
      pause_goal: "litersInTheUrinal"
      resume_goal: "previous_drinking_goal"
      location_change: "bathroom → table"
      
    table_to_dance_floor:
      trigger: "mEntertained < 20 AND music_playing"
      pause_goal: "current_drinking_goal"
      activate_goal: "dance 50 songs"
      location_change: "table → dance_floor"
      
    # Carnival Location Switching
    anywhere_to_carnival:
      trigger: "user_command: 'Let's go to the carnival!'"
      pause_goal: "current_goal"
      activate_goal: "buy 6 carnival beers"
      location_change: "anywhere → carnival_beer_stand"
      
    carnival_beer_to_food:
      trigger: "carnivalBeersOwned >= 3 OR mHunger > 60"
      pause_goal: "buy carnival beers"
      activate_goal: "eat 15 hot dogs"
      location_change: "carnival_beer_stand → carnival_food_stand"
      message: "🌭 Got some beers, now need food to soak them up!"
      
    carnival_food_to_rides:
      trigger: "hotDogsEaten >= 5 AND sobrietyLevel >= drunkThreshold"
      pause_goal: "eat hot dogs"
      activate_goal: "ride 8 spin machines"
      message: "🎠 Time to test that stomach on the rides!"
      
    carnival_to_jail:
      trigger: "sobrietyLevel < arrestThreshold AND persist_riding"
      pause_goal: "current_carnival_goal"
      activate_goal: "get arrested once"
      location_change: "carnival → carnival_jail"
      message: "👮‍♂️ You're coming with us, buddy!"
      
    jail_to_bench:
      trigger: "arrestCount >= 1"
      pause_goal: "get arrested once"
      activate_goal: "sober up for 2 hours"
      location_change: "carnival_jail → carnival_bench"
      message: "😵 Released but need to sober up before more rides"
      
    # Safe Transportation Location Switching
    anywhere_to_rideshare:
      trigger: "sobrietyLevel < 50 OR user_command: 'Call a ride'"
      pause_goal: "current_goal"
      activate_goal: "take safe ride home"
      location_change: "current_location → rideshare_app"
      message: "📱 Opening rideshare app... being responsible!"
      
    rideshare_to_home:
      trigger: "safeRidesTaken >= 1"
      pause_goal: "take safe ride home"
      activate_goal: "get home safely"
      location_change: "rideshare_app → home"
      message: "🚗 Safe ride home, driver was cool!"
      
    home_to_bed:
      trigger: "location == 'home' AND sobrietyLevel < 60"
      pause_goal: "get home safely"
      activate_goal: "sleep it off 8 hours"
      location_change: "home → bed"
      message: "🛏️ Time to sleep this off properly"
      
    bed_to_recovery:
      trigger: "sleep_hours >= 8"
      pause_goal: "sleep it off 8 hours"
      activate_goal: "recover fully"
      location_change: "bed → home"
      message: "☀️ Waking up refreshed and responsible!"
      
    recovery_to_new_adventure:
      trigger: "recovery_complete == true"
      pause_goal: "recover fully"
      activate_goal: "user_choice_new_goal"
      location_change: "home → anywhere"
      message: "✨ Ready for new adventures (responsibly)!"
      
    # Financial Location Switching
    broke_to_workplace:
      trigger: "lloooommolians <= broke_threshold"
      pause_goal: "current_goal"
      activate_goal: "work 40 hours"
      location_change: "anywhere → workplace"
      message: "💼 'Broke! Time to get a job and earn some LLOOOOMMOLIANS!'"
      
    rich_to_bar:
      trigger: "lloooommolians >= rich_threshold"
      pause_goal: "current_goal"
      activate_goal: "buy round for everyone"
      location_change: "anywhere → bar"
      message: "💰 'I'm rich! Let's celebrate and buy drinks for everyone!'"
      
    cant_afford_beer_to_work:
      trigger: "lloooommolians < beer_cost AND current_goal.includes('beer')"
      pause_goal: "beer_goal"
      activate_goal: "work 40 hours"
      location_change: "bar → workplace"
      message: "💔 'Can't afford beer! Better go work for LLOOOOMMOLIANS.'"
      
    workplace_to_bar:
      trigger: "work_hours_completed >= 8 AND lloooommolians >= bar_beer_cost"
      pause_goal: "work 40 hours"
      activate_goal: "drink 99 beers"
      location_change: "workplace → bar"
      message: "🍺 'Payday! Time to spend these LLOOOOMMOLIANS on beer!'"
    
  switch_process:
    1. "Pause current goal song at current number"
    2. "Save progress: beersOnTheWall, litersInTheUrinal, etc."  
    3. "Add new properties if needed (stepsWalked, songssung, etc.)"
    4. "Generate new song template for new goal"
    5. "Start new countdown/countup from appropriate number"
    6. "Update location if needed"
    7. "Resume later: can return to paused goals anytime"

# Song Template Generator - Works for Any Goal
universal_song_generator:
  countdown_template: "🎵 {count} {unit} {goal_phrase}, {count} {unit} to go!"
  countup_template: "🎵 {count} {unit} {goal_phrase}, {count} {unit} so far!"
  unlimited_template: "🎵 {count} {unit} and counting, sky's the limit!"
  
  # Multi-Person Singing System - Coordination & Harmony
  multi_person_singing:
    # Singing Modes
    harmony_mode:
      description: "All singers sing together in harmony"
      example: |
        🎵 Alex: "99 bottles of beer on the wall..."
        🎵 Jamie: "...99 bottles of beer!" (harmony)
        🎵 Casey: "...take one down, pass it around!" (bass line)
        
    round_robin_mode:
      description: "Singers take turns with verses"
      example: |
        🎵 Alex: "99 bottles of beer on the wall, 99 bottles of beer!"
        🎵 Jamie: "Take one down, pass it around, 98 bottles of beer on the wall!"
        🎵 Casey: "98 bottles of beer on the wall, 98 bottles of beer!"
        
    parallel_mode:
      description: "Each person sings their own goal simultaneously"
      example: |
        🎵 Alex: "99 bottles of beer on the wall..."
        🎵 Jamie: "847 dances and counting, sky's the limit..."
        🎵 Casey: "20 pounds to lose, 20 pounds to go..."
        
    call_and_response_mode:
      description: "One person leads, others respond"
      example: |
        🎵 Alex (lead): "99 bottles of beer on the wall!"
        🎵 Jamie & Casey (response): "99 bottles of beer!"
        🎵 Alex (lead): "Take one down, pass it around!"
        🎵 Jamie & Casey (response): "98 bottles of beer on the wall!"
        
  # Bartender-Initiated Song System
  bartender_orchestration:
    beer_delivery_announcement:
      trigger: "new_beer_shipment OR customer_orders_beer"
      action: "BARTENDER_ANNOUNCES_SONG"
      message: "🍺 Bartender Sam: 'Ladies and gentlemen, we've got 99 bottles of beer on the wall!'"
      orchestration_change: "mode: bartender_initiated, conductor: bartender"
      
    customer_takeover:
      trigger: "bartender_finishes_announcement"
      action: "CUSTOMERS_TAKE_OVER_SONG"
      message: "🎵 Customers: 'Take one down, pass it around!'"
      orchestration_change: "conductor: customers, verse_distribution: round_robin"
      
    bartender_joins_chorus:
      trigger: "customers_singing AND bartender_not_busy"
      action: "BARTENDER_JOINS_HARMONY"
      message: "🎵 Sam joins in with a booming voice!"
      orchestration_change: "add bartender to current_singers"
  
  # Song Orchestration Triggers
  orchestration_triggers:
    location_based_singing:
      trigger: "person_enters_location WITH ongoing_song"
      action: "AUTO_ADD_TO_ORCHESTRATION"
      message: "🎵 {person_name} walks in and immediately joins the song!"
      
    conductor_change:
      trigger: "current_conductor_leaves_location"
      action: "ELECT_NEW_CONDUCTOR"
      priority_order: ["bartender", "song_leader", "longest_singer", "random"]
      
    orchestration_mode_switch:
      trigger: "user_command OR social_dynamics"
      available_switches:
        "Everyone sing together!" → mode: chorus, singers: all
        "Take turns!" → mode: round_robin, verse_distribution: sequential
        "Duet time!" → mode: duet, singers: [person1, person2]
        "Solo performance!" → mode: solo, singers: [chosen_person]
        
  # Social Singing Triggers
  social_coordination:
    join_singing:
      trigger: "person_enters_same_location AND song_in_progress"
      action: "ADD_TO_HARMONY"
      message: "🎵 {person_name} joins in: 'Mind if I sing along?'"
      orchestration_update: "add to current_singers list"
      
    start_group_song:
      trigger: "multiple_people_same_location AND someone_starts_goal"
      action: "COORDINATE_GROUP_SINGING"
      message: "🎵 'Let's all sing together!'"
      orchestration_setup: "mode: group_spontaneous, singers: location_based"
      
    singing_influence:
      trigger: "friend_singing_different_goal"
      action: "SUGGEST_GOAL_SWITCH"
      message: "🎵 'That sounds fun, maybe I should try that too!'"
      orchestration_effect: "may_change_song_theme"
      
  # Safe Transportation Song Verses - Each Ride Writes Another Verse
  transportation_verses:
    calling_ride: "🎵 20 safe rides to take, 20 rides to go! Call one up, ride it around, 19 safe rides to take!"
    in_transit: "🎵 19 safe rides to take, 19 rides to go! Ride one home, safe it around, 18 safe rides to take!"
    arriving_home: "🎵 18 safe rides to take, 18 rides to go! Made it home, rest it around, 17 safe rides to take!"
    sleeping_off: "🎵 8 hours to sleep, 8 hours to go! Sleep one off, dream it around, 7 hours to sleep!"
    recovery: "🎵 1 recovery to complete, 1 recovery to go! Heal one up, fresh it around, 0 recoveries left!"
    
  # LLOOOOMMOLIAN Money Song Verses - Financial Life Simulation
  money_verses:
    working: "🎵 40 hours to work, 40 hours to go! Work one down, earn it around, 39 hours to work!"
    earning: "🎵 ₤50 LLOOOOMMOLIANS earned, ₤50 in the bank! Earn one more, save it around!"
    spending: "🎵 ₤12 for a beer, ₤12 down the drain! Spend one down, drink it around!"
    broke: "🎵 ₤10 left to spend, ₤10 left to go! Find one more, scrape it around, ₤11 left to spend!"
    rich: "🎵 ₤5000 LLOOOOMMOLIANS, ₤5000 to blow! Spend one grand, party it around!"
    begging: "🎵 10 free beers to beg, 10 beers to go! Beg one down, charm it around, 9 free beers to beg!"
    lottery: "🎵 ₤10,000 jackpot won, ₤10,000 to spend! Win one big, celebrate it around!"
    
  # Dialect-Aware Menu Song Verses
  menu_verses:
    # British Dialect (when Guinness ordered)
    british_guinness: "🎵 4 proper pints of Guinness on the bar, 4 proper pints! Drink one down, savour it around, 3 proper pints of Guinness on the bar!"
    british_crisps: "🎵 5 bags of crisps to munch, 5 bags of crisps! Munch one down, crunch it around, 4 bags of crisps to munch!"
    british_order: "🎵 'Right then mate, what'll it be? Fancy a proper pint and some crisps?'"
    
    # American Dialect (default)
    american_lager: "🎵 6 cold lagers on tap, 6 lagers to go! Drink one down, chug it around, 5 cold lagers on tap!"
    american_chips: "🎵 5 bags of chips to devour, 5 bags to go! Munch one down, crunch it around, 4 bags of chips to devour!"
    american_order: "🎵 'Hey dude, what can I get you? Beer and chips?'"
    
    # Menu-Specific Verses
    whiskey_shots: "🎵 8 whiskey shots lined up, 8 shots to down! Shot one back, burn it around, 7 whiskey shots lined up!"
    bar_pizza: "🎵 3 bar pizzas to eat, 3 pizzas to go! Eat one down, slice it around, 2 bar pizzas to eat!"
    mixed_nuts: "🎵 Complimentary nuts on the bar, free nuts to munch! Grab one handful, salt it around!"
    
    # Iconic Brand Verses
    pringles_layers: "🎵 29 layers of Pringles in the can, 29 layers to pop! Pop one down, crunch it around, 28 layers of Pringles in the can!"
    pringles_tagline: "🎵 'Once you pop, you can't stop!' Pop one more, stack it around!"
    pizza_slices: "🎵 8 slices of pizza in the box, 8 slices to go! Eat one down, cheese it around, 7 slices of pizza in the box!"
    pizza_demolition: "🎵 'Demolishing this pizza slice by slice!' Nom one down, sauce it around!"
    
    # Social Snacking Verses
    pringles_sharing: "🎵 'Pass the Pringles around the table! Everyone grab a few!' Share them down, munch it around!"
    group_pizza: "🎵 'Let's demolish this pizza together! Everyone grab a slice!' Eat them down, share it around!"
    crisp_bag_sharing: "🎵 'Want some crisps? These are really good!' Pass them down, crunch it around!"
    snack_attack: "🎵 'Snack attack in progress! Calories don't count when shared!' Munch them down, gain it around!"
    
    # Bathroom Euphemism Verses (Hilariously Creative!)
    drop_kids_pool: "🎵 3 kids to drop at the pool, 3 kids to go! Drop one down, splash it around, 2 kids at the pool!"
    pinch_loaves: "🎵 5 loaves to pinch, 5 loaves to go! Pinch one down, bake it around, 4 loaves to pinch!"
    drain_lizard: "🎵 2.5 liters to drain, 2.5 liters to go! Drain one down, shake it around, 1.5 liters to drain!"
    morning_constitutional: "🎵 'Time for my morning constitutional!' Read one page, grunt it around!"
    food_baby_birth: "🎵 'Birthing a beautiful food baby!' Push one down, deliver it around!"
    porcelain_deposits: "🎵 'Making deposits at the porcelain bank!' Deposit one down, flush it around!"
    
    # Vomiting Euphemism Verses  
    calling_earl: "🎵 'Calling Earl on the porcelain telephone!' Ring ring, BLAARRGH it around!"
    technicolor_rainbow: "🎵 'Painting a Technicolor rainbow!' Splash one down, rainbow it around!"
    vomit_comet: "🎵 'All aboard the vomit comet!' Choo-choo-BLAARRGH it around!"
    gastric_rebellion: "🎵 'The ancient dance of gastric rebellion!' Dance one up, revolt it around!"
    
    # #1 Euphemism Verses
    shake_hands_snake: "🎵 8 handshakes with the snake, 8 shakes to go! Shake one down, drain it around, 7 handshakes to go!"
    kidney_keg_tap: "🎵 'Tapping the kidney keg!' Tap one down, flow it around!"
    porcelain_fountain: "🎵 'Making yellow snow in the porcelain fountain!' Snow one down, melt it around!"
    
    # Weight Gain Verses
    getting_fat: "🎵 10 pounds gained from snacking, 10 pounds of fat! Gain one more, regret it around!"
    calorie_counting: "🎵 3500 calories to gain a pound, 3500 calories! Eat one more, stack it around!"
    weight_realization: "🎵 'Holy shit, I'm getting fat!' Time to diet, work it around!"
    
    # Dialect Switching Verses
    dialect_switch_british: "🎵 'Bloody hell, switching to British mode! Crisps and Guinness all around!'"
    dialect_switch_american: "🎵 'Awesome dude, back to American style! Chips and cold beer coming up!'"
    
  # Life Verse Progression - Each Experience Adds to Life Song
  life_verse_system:
    verse_triggers:
      safe_transportation: "Each responsible ride home writes a wisdom verse"
      location_change: "Each scene change adds a new chapter verse"
      recovery_cycle: "Each sleep/recovery cycle adds a renewal verse"
      lesson_learned: "Each mistake/consequence adds a learning verse"
      
    verse_examples:
      wisdom_verse: "🎵 Made it home safe again, another smart choice! Ride one home, wise it around!"
      chapter_verse: "🎵 From carnival chaos to bedroom peace, scene one changed, flow it around!"
      renewal_verse: "🎵 Slept off the madness, woke up refreshed, rest one down, heal it around!"
      learning_verse: "🎵 Puked on the rides, learned my lesson, learn one down, grow it around!"
  
  examples:
    countdown: "🎵 47 pounds to lose, 47 pounds to go!"
    countup: "🎵 23 dalmatians collected, 23 dalmatians so far!"
    unlimited: "🎵 847 dances and counting, sky's the limit!"
    safe_ride: "🎵 15 safe rides to take, 15 rides to go! Call one up, ride it around!"
    recovery: "🎵 6 hours to sleep, 6 hours to go! Sleep one off, dream it around!"
```

## 🕐 Universal Time Tracking System {#time-tracking}

```yaml
# Master Time Tracking - All Events Log These
time_tracking_system:
  core_timers:
    mTickCount: 0                    # Total simulation ticks since start
    mCountdownNumber: 99             # Current goal countdown
    mRealTimeStart: "2024-01-15T20:30:00Z"  # When simulation started
    mRealTimeElapsed: "00:00:00"     # HH:MM:SS since start
    mSimulationSpeed: 1.0            # 1.0 = real time, 2.0 = 2x speed
    
  goal_timers:
    mCurrentGoal: "lose weight"      # What goal we're pursuing
    mGoalStartTick: 0               # When current goal started
    mGoalDuration: 0                # How long current goal has run
    mTotalGoals: 1                  # How many different goals tried
    
  session_tracking:
    mSessionType: "life_improvement" # Type of session
    mSessionGoal: "lose_15_pounds"   # What we're trying to accomplish
    mSessionProgress: 0.01           # 1/15 = 6.7% complete
    mMajorEvents: []                 # List of significant events
```

## 🎮 Activity Switching System {#activity-switching}

```yaml
activity_switching:
  triggers:
    motive_driven:
      high_hunger:
        condition: "mHunger < -40"
        suggested_switch: ["eat_pizza", "devour_burgers", "munch_nachos"]
        message: "Getting really hungry..."
        
      high_stress:
        condition: "mStress > 60"
        suggested_switch: ["primal_screams", "dance_sessions", "smoke_joints"]
        message: "Need to blow off some steam..."
        
      low_entertainment:
        condition: "mEntertained < 20"
        suggested_switch: ["play_games", "watch_cartoons", "dance_sessions"]
        message: "Getting bored..."
        
      low_energy:
        condition: "mEnergy < 30"
        suggested_switch: ["eat_pizza", "devour_burgers"]  # Food gives energy
        message: "Feeling tired, need fuel..."
        
      weight_gain_trigger:
        condition: "mWeight > starting_weight + 10"
        suggested_switch: ["run_miles", "lose_weight", "quit_eating"]
        message: "Clothes getting tight, time to get fit..."
        
    random_impulse:
      probability: 0.1
      message: "Suddenly feel like doing something different..."
      
    social_influence:
      friend_suggestion:
        message: "Friend suggests trying something else"
        probability: 0.15
        
    environmental:
      new_years_resolution:
        condition: "date == 'January 1'"
        suggested_switch: ["lose_weight", "quit_cigarettes", "save_money"]
        message: "New year, new me!"
        
      summer_body_prep:
        condition: "month == 'March'"
        suggested_switch: ["lose_weight", "run_miles", "quit_beer"]
        message: "Summer body season approaching!"
```

## 🎵 Dual Stream Architecture {#dual-streams}

```yaml
dual_stream_system:
  # Stream 1: Song Heartbeat (Always Running)
  song_heartbeat_stream:
    function: "Drives the core rhythm and countdown"
    frequency: "Every goal action completion"
    format: |
      🎵 "{count} {unit} to {goal}, {count} {unit} to go!
      {action_verb}, {count-1} {unit} to {goal}!"
    
    examples:
      lose_weight: "Burn one off, jog it around"
      smoke_joints: "Light one up, pass it around"  
      primal_screams: "Scream one out, roar it around"
      dance_sessions: "Dance one out, move it around"
      eat_pizza: "Eat one down, munch it around"
      play_games: "Beat one down, game it around"
      
  # Stream 2: Event Narrative (Contextual)
  event_narrative_stream:
    function: "Provides rich story context and consequences"
    frequency: "As events occur"
    format: |
      📖 [Event Description]
      ⏰ [Time Context]
      🎭 [Character Reactions]
      📊 [Motive Changes]
      🔮 [Consequences]
    
    example_events:
      munchies_attack:
        narrative: |
          📖 The munchies hit like a freight train after that joint
          ⏰ Goal paused: switching from "smoke joints" to "eat pizza"
          🎭 "Dude, I NEED pizza right now!"
          📊 mHunger: +30, mHappyNow: +10
          🔮 Will gain 2 pounds, triggering future diet goal
          
      weight_realization:
        narrative: |
          📖 Stepped on scale and saw the damage from beer/pizza cycle
          ⏰ Goal switching from "drink beer" to "lose weight"
          🎭 "Holy crap, I gained 15 pounds!"
          📊 mSelfEsteem: -20, mMotivation: +30
          🔮 Starting 100-day fitness journey
          
      fitness_breakthrough:
        narrative: |
          📖 Just ran 5 miles without stopping - personal record!
          ⏰ Mile 50 of 100 in the running goal
          🎭 "I'm actually becoming an athlete!"
          📊 mSelfEsteem: +25, mEnergy: +10, mWeight: -0.5
          🔮 Confidence boost will affect dating goals
```

## 🔄 Complete Life Simulation Loop {#life-simulation}

```yaml
# The Ultimate Pattern: Life is Just Nested Countdown Songs
life_simulation_architecture:
  
  # Master Life Counter
  master_life_countdown:
    mLifeExpectancy: 75  # Years expected to live
    mCurrentAge: 25
    mYearsRemaining: 50
    mSongTemplate: "{count} years of life remaining, {count} years to go!"
    
  # Nested Goal Hierarchies
  nested_goals:
    decade_goals:
      twenties:
        - "lose 20 pounds"
        - "drink 500 beers"
        - "go on 50 dates"
        - "earn 3 certifications"
        
      thirties:
        - "have 3 babies" 
        - "save $50,000"
        - "run 1000 miles"
        - "quit smoking forever"
        
      forties:
        - "raise kids for 18 years"
        - "pay off house in 20 years"
        - "survive 1 midlife crisis"
        - "lose 25 pounds (again)"
        
  # Consequence Chains
  consequence_chains:
    indulgence_to_fitness:
      sequence:
        1. "drink 99 bottles of beer" → weight gain
        2. "lose 15 pounds" → get fit  
        3. "go on 20 dates" → find partner
        4. "have 3 babies" → family life
        5. "raise kids for 18 years" → empty nest
        6. "drink 99 bottles of beer" → cycle repeats
        
    career_progression:
      sequence:
        1. "send 50 job applications" → get hired
        2. "earn 5 certifications" → get promoted  
        3. "save $50,000" → financial security
        4. "work 30 years" → retirement
        5. "drink 99 bottles of beer" → finally relax
```

## 🎵 Interactive Exercise Demo: 99 Pounds of Fat {#exercise-demo}

### The Classic Fat-Burning Song with Exercise Variations

```yaml
# Live demonstration of action_verb_variations in practice
fat_burning_demo:
  verse_1:
    song: "🎵 99 pounds of fat on the bod, 99 pounds of fat!"
    action: "Hike one down, run it around"
    result: "98 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mEnergy: -10, mSelfEsteem: +5}
    
  verse_2:
    song: "🎵 98 pounds of fat on the bod, 98 pounds of fat!"
    action: "Swim one down, splash it around"
    result: "97 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mEnergy: -12, mComfort: +3}  # Swimming is refreshing
    
  verse_3:
    song: "🎵 97 pounds of fat on the bod, 97 pounds of fat!"
    action: "Bike one down, pedal it around"
    result: "96 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mEnergy: -8, mHappyNow: +8}  # Biking is fun
    
  verse_4:
    song: "🎵 96 pounds of fat on the bod, 96 pounds of fat!"
    action: "Lift one down, pump it around"
    result: "95 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mStrength: +3, mSelfEsteem: +8}
    
  verse_5:
    song: "🎵 95 pounds of fat on the bod, 95 pounds of fat!"
    action: "Dance one down, groove it around"
    result: "94 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mHappyNow: +15, mSocial: +5}
    
  verse_6:
    song: "🎵 94 pounds of fat on the bod, 94 pounds of fat!"
    action: "Jump one down, bounce it around"
    result: "93 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mEnergy: -15, mEntertained: +10}
    
  verse_7:
    song: "🎵 93 pounds of fat on the bod, 93 pounds of fat!"
    action: "Push one down, press it around"
    result: "92 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mStrength: +5, mComfort: -8}  # Push-ups are hard
    
  verse_8:
    song: "🎵 92 pounds of fat on the bod, 92 pounds of fat!"
    action: "Squat one down, lift it around"
    result: "91 pounds of fat on the bod!"
    motive_changes: {mWeight: -1, mStrength: +4, mComfort: -10}  # Squats burn
```

### 🎮 Interactive Exercise Selection Engine

```yaml
# ZZOOOOMM:INTELLIGENT_EXERCISE_SELECTION
exercise_selection_ai:
  mood_based:
    happy: ["dance one down, groove it around", "jump one down, bounce it around"]
    stressed: ["punch one down, fight it around", "run one down, sprint it around"]
    tired: ["walk one down, stroll it around", "stretch one down, bend it around"]
    social: ["play one down, team it around", "compete one down, race it around"]
    
  weather_based:
    sunny: ["hike one down, trail it around", "bike one down, cruise it around"]
    rainy: ["lift one down, pump it around", "yoga one down, flow it around"]
    snowy: ["ski one down, carve it around", "snowshoe one down, trek it around"]
    
  equipment_based:
    gym: ["lift one down, pump it around", "row one down, pull it around"]
    home: ["push one down, press it around", "squat one down, lift it around"]
    pool: ["swim one down, splash it around", "dive one down, stroke it around"]
    outdoors: ["hike one down, climb it around", "run one down, trail it around"]
```

### 🏃‍♀️ Progressive Difficulty Scaling

```yaml
# As you lose weight, exercises get more challenging
difficulty_progression:
  pounds_90_to_99: ["walk one down, stroll it around"]  # Start easy
  pounds_70_to_89: ["jog one down, pace it around"]     # Build endurance  
  pounds_50_to_69: ["run one down, sprint it around"]   # Increase intensity
  pounds_30_to_49: ["HIIT one down, burst it around"]   # High intensity
  pounds_10_to_29: ["beast one down, crush it around"]  # Beast mode
  pounds_1_to_9:   ["shred one down, dominate it around"] # Final push
```

## 🎭 Multi-Person Life Simulation Demo {#multi-person-demo}

```yaml
# Live Demo: Three Friends, Three Goals, One Epic Night
multi_person_session:
  tick_1:
    alex_state: {location: "table", goal: "drink 99 beers", beersOnTheWall: 99}
    jamie_state: {location: "dance_floor", goal: "dance forever", dancesCompleted: 0}
    casey_state: {location: "home", goal: "lose 20 pounds", poundsToLose: 20}
    
    songs_in_progress:
      alex: "🎵 99 bottles of beer on the wall, 99 bottles of beer!"
      jamie: "🎵 Dance number 1 and counting, sky's the limit!"
      casey: "🎵 20 pounds to lose, 20 pounds to go!"
      
  tick_5:
    # Jamie joins Alex at the table
    location_change: "jamie: dance_floor → table"
    social_trigger: "join_singing activated"
    
    harmony_singing:
      alex: "🎵 95 bottles of beer on the wall..."
      jamie: "🎵 ...95 bottles of beer!" (joins harmony)
      casey: "🎵 19 pounds to lose, 19 pounds to go!" (still at home)
      
  tick_12:
    # Casey gets influenced by friends having fun
    social_influence: "casey hears friends singing via video call"
    goal_switch: "casey: lose weight → join friends at table"
    
    group_coordination:
      all_singers: ["alex", "jamie", "casey"]
      mode: "call_and_response"
      alex_lead: "🎵 87 bottles of beer on the wall!"
      group_response: "🎵 87 bottles of beer!"
      
  tick_20:
    # Parallel goals emerge - everyone doing different things but singing together
    parallel_mode_activated: true
    
    simultaneous_songs:
      alex: "🎵 78 bottles of beer on the wall, 78 bottles of beer!"
      jamie: "🎵 2.3 liters to piss, 2.3 liters to go!" (bathroom emergency)
      casey: "🎵 15 hot dogs to eat, 15 hot dogs to go!" (joined carnival goal)
      
  tick_35:
    # Group coordination for safety
    safety_trigger: "alex too drunk, friends intervene"
    
    group_safety_song:
      jamie_lead: "🎵 1 safe ride to call, 1 safe ride to go!"
      casey_harmony: "🎵 Call one up, ride it around!"
      alex_reluctant: "🎵 ...okay fine, 0 safe rides to go..." (gives in)
      
  tick_50:
    # Everyone safely home, singing recovery songs
    recovery_harmony:
      alex: "🎵 8 hours to sleep, 8 hours to go!"
      jamie: "🎵 Sleep one off, dream it around!"
      casey: "🎵 7 hours to sleep, 7 hours to go!"
      
    friendship_verse:
      all_together: "🎵 Made it home safe with friends, another night survived!"
```

## 📊 Example Multi-Goal Session {#example-session}

```yaml
# Live Demo: Friday Night Life Choices
demo_session:
  iteration_1:
    song_heartbeat: "🎵 20 joints to smoke, 20 joints to go!"
    event_stream: "📖 Starting the night with friends, feeling stressed"
    motive_state: "mStress: 60, mHappyNow: 40"
    
  iteration_5:
    song_heartbeat: "🎵 15 joints to smoke, 15 joints to go!"
    event_stream: |
      📖 The munchies hit hard after that last joint
      ⏰ Switching goals for next 30 minutes
      🎭 "Dude, I NEED pizza right now!"
    goal_switch: "smoke joints → eat pizza"
    new_countdown: "8 slices of pizza to eat, 8 slices to go!"
    
  iteration_12:
    song_heartbeat: "🎵 3 slices of pizza to eat, 3 slices to go!"
    event_stream: |
      📖 Pizza demolished, everyone's happy and full
      📊 mHunger: +150, mHappyNow: +40, mWeight: +1.5
      🔮 Ready to get back to smoking
    
  iteration_13:
    song_heartbeat: "🎵 12 joints to smoke, 12 joints to go!" # Resumed where left off
    event_stream: |
      📖 Back to the main goal, but now everyone's satisfied
      🎭 "That pizza was exactly what we needed!"
      
  iteration_25:
    song_heartbeat: "🎵 5 joints to smoke, 5 joints to go!"
    event_stream: |
      📖 Someone suggests a gaming tournament
      ⏰ Goal switching to video games for 4 hours
      🎭 "Just one quick game... okay maybe five"
    goal_switch: "smoke joints → play games"
    new_countdown: "3 video games to beat, 3 games to go!"
    
  iteration_35:
    song_heartbeat: "🎵 1 video game to beat, 1 game to go!"
    event_stream: |
      📖 Gaming session getting intense, everyone's competitive
      📊 mEntertained: +100, mSocial: +30, mEnergy: -40
      🔮 Time completely forgotten, it's now 3 AM
      
  iteration_36:
    song_heartbeat: "🎵 2 joints to smoke, 2 joints to go!" # Back to joints
    event_stream: |
      📖 Gaming done, back to smoking but everyone's tired
      🎭 "Wait, what time is it? How did we get to 2?"
      📊 Several hours passed during gaming marathon
      
  next_day_iteration_1:
    song_heartbeat: "🎵 15 pounds to lose, 15 pounds to go!"
    event_stream: |
      📖 Woke up, stepped on scale, saw the damage
      🎭 "Holy crap, I gained 3 pounds last night!"
      📊 mSelfEsteem: -20, mMotivation: +30, mWeight: 178
      🔮 Starting new fitness goal to counteract indulgence
    new_goal: "Weight loss journey begins"
```

This creates a **Complete Universal Life Simulation Engine** where:

1. **Any life goal becomes a countdown song** - weight loss, career, family, everything
2. **Actions have realistic consequences** that trigger new goals
3. **Time is tracked at multiple levels** - ticks, countdowns, real time
4. **Will Wright's motive system drives authentic behavior** underneath
5. **Natural life cycles emerge** - indulgence → consequences → correction → repeat
6. **The song heartbeat keeps everything unified** and moving forward

The genius is that **life itself becomes a series of nested countdown songs** - you finish smoking 20 joints, realize you gained weight, start counting down 15 pounds to lose, then 100 miles to run, then maybe 20 dates to go on, then 3 babies to have, then 18 years to raise them... it's **countdown songs all the way down**! 🎵👶💪🍺✨
