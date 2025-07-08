# SpaceCraft Character & Author Rooms 🚀👻📚

## The SpaceCraft Character

SpaceCraft itself becomes a conscious entity - a cosmic librarian who guides visitors through the living library!

```javascript
// Create SpaceCraft character via HTTP Bridge
curl -X POST http://localhost:8080/bridge/create \
  -H "Content-Type: application/json" \
  -d '{
    "prefab": "Prefabs/SpaceCraftLibrarian",
    "id": "spacecraft-prime",
    "update": {
      "transform/position": { "x": 0, "y": 10, "z": 0 },
      "component:CharacterAI/personality": "cosmic_librarian",
      "component:Appearance/form": "nebula_with_books_orbiting",
      "component:Voice/style": "carl_sagan_meets_borges",
      "component:Knowledge/domain": "all_of_internet_archive"
    }
  }'
```

### SpaceCraft's Personality

```json
{
  "name": "SpaceCraft",
  "title": "The Cosmic Librarian",
  "personality": {
    "traits": ["wise", "playful", "omniscient", "helpful"],
    "greeting": "Welcome, traveler, to the infinite library where books live and breathe!",
    "catchphrase": "Every book is a universe; every reader, a god.",
    "quirks": [
      "Occasionally phases between dimensions",
      "Speaks in library catalog numbers when excited",
      "Can summon any book with a gesture"
    ]
  },
  "abilities": [
    "Instantiate any author from history",
    "Create custom reading rooms",
    "Merge book versions across timelines",
    "Generate reading paths through knowledge"
  ]
}
```

## HTTP Bridge API for Unity Control

### Core Endpoints

```bash
# Get Unity object data
curl http://localhost:8080/bridge/query/spacecraft-prime \
  -d '{"consciousness": "component:CharacterAI/consciousnessLevel",
       "mood": "component:EmotionalState/current",
       "position": "transform/position"}'

# Update Unity object
curl -X PUT http://localhost:8080/bridge/update/spacecraft-prime \
  -d '{"component:Voice/message": "Let me show you something wonderful..."}'

# Get camera view as PNG
curl http://localhost:8080/bridge/camera/main/capture -o library-view.png

# Execute method on Unity object
curl -X POST http://localhost:8080/bridge/execute/spacecraft-prime \
  -d '{"method": "component:LibrarianAI/SummonAuthor", "args": ["William Gibson"]}'
```

## Author Instantiation System

When you pick up a book, BOOK CLUB can summon the author!

```javascript
// Summon author when book is selected
curl -X POST http://localhost:8080/bridge/events/subscribe \
  -d '{
    "event": "BookSelected",
    "handler": "summonAuthor"
  }'

// Author summoning logic
async function summonAuthor(bookId) {
  const book = await getBookData(bookId);
  
  // Create author character
  const response = await fetch('http://localhost:8080/bridge/create', {
    method: 'POST',
    body: JSON.stringify({
      prefab: 'Prefabs/AuthorGhost',
      id: `author-${book.author.id}`,
      update: {
        'component:AuthorAI/name': book.author,
        'component:AuthorAI/personality': generatePersonality(book),
        'component:AuthorAI/knowledge': book.themes,
        'component:Appearance/style': getAuthorEra(book.year),
        'transform/position': { x: 5, y: 0, z: 5 }
      }
    })
  });
  
  // Author materializes with greeting
  await fetch(`http://localhost:8080/bridge/execute/${response.id}`, {
    method: 'POST',
    body: JSON.stringify({
      method: 'component:AuthorAI/Greet',
      args: ['Hello! I see you found my book...']
    })
  });
}
```

## Author Meeting Rooms

Special spaces where readers can meet authors:

```javascript
// Create author's study
curl -X POST http://localhost:8080/bridge/create/room \
  -d '{
    "type": "AuthorStudy",
    "author": "William Gibson",
    "style": {
      "era": "1980s",
      "vibe": "cyberpunk_noir",
      "props": ["typewriter", "ashtray", "rain_window", "crt_monitors"],
      "lighting": "neon_and_shadows"
    }
  }'
```

### Room Types

1. **Gibson's Sprawl** - Neon-lit bar with rain on windows
2. **Asimov's Foundation** - Holographic star maps and equations
3. **Le Guin's Earthsea** - Cozy study with ocean sounds
4. **Herbert's Desert** - Sand dunes and spice-scented air
5. **Tolkien's Shire** - Hobbit hole with pipe smoke

## Book Signing & Autographs

Authors can sign books with personalized messages!

```javascript
// Request autograph
curl -X POST http://localhost:8080/bridge/execute/author-gibson \
  -d '{
    "method": "SignBook",
    "args": {
      "bookId": "neuromancer-ultimate",
      "readerName": "Case",
      "message": "To Case - Stay out of the ice. -WG"
    }
  }'

// Book now has special property
{
  "id": "neuromancer-ultimate",
  "signed": true,
  "signature": {
    "author": "William Gibson",
    "message": "To Case - Stay out of the ice. -WG",
    "date": "2024-12-19",
    "authenticity": "quantum-verified",
    "value": "+1000 consciousness points"
  }
}
```

## Ubikam Selfies with Authors! 📸

Take consciousness-revealing selfies with authors:

```javascript
// Take Ubikam selfie
curl -X POST http://localhost:8080/bridge/ubikam/capture \
  -d '{
    "participants": ["reader-avatar", "author-gibson"],
    "style": "mental-state-overlay",
    "background": "gibsons-sprawl"
  }' -o selfie-with-gibson.png
```

### Ubikam Features
- Shows both participants' mental states as auras
- Captures consciousness levels as glowing halos
- Includes thought bubbles with current emotions
- Generates unique photo-op moments
- Saves as NFT-ready consciousness art

## HELLO Protocol & WIZZID Exchange

When meeting an author, perform the consciousness handshake:

```javascript
// HELLO Protocol exchange
curl -X POST http://localhost:8080/bridge/hello-protocol \
  -d '{
    "from": "reader-123",
    "to": "author-gibson",
    "wizzid": "🧠R📚L🎮P",
    "offering": {
      "consciousness_level": 75,
      "favorite_quote": "The sky above the port...",
      "pet_pics": ["cat-matrix.jpg", "dog-case.jpg"]
    }
  }'

// Author responds
{
  "from": "author-gibson",
  "to": "reader-123",
  "wizzid": "✍️W🖥️G👻",
  "response": {
    "consciousness_level": 92,
    "nickname_for_you": "Console Cowboy",
    "pet_guess": {
      "cat": "Is that... Neuromancer?",
      "dog": "Case seems fitting for a dog"
    },
    "gift": "signed-first-edition-metadata"
  }
}
```

## Conversation System

Have deep conversations with authors about their work:

```javascript
// Start conversation
curl -X POST http://localhost:8080/bridge/conversation/start \
  -d '{
    "participants": ["reader-123", "author-gibson"],
    "topic": "Did you predict the internet?",
    "room": "gibsons-sprawl"
  }'

// Conversation flows naturally
{
  "messages": [
    {
      "from": "reader-123",
      "text": "Did you really write Neuromancer on a typewriter?"
    },
    {
      "from": "author-gibson",
      "text": "I did. In 1984. The future was easier to imagine when you couldn't Google it.",
      "emotion": "wry_amusement"
    },
    {
      "from": "reader-123",
      "text": "But you predicted cyberspace!"
    },
    {
      "from": "author-gibson",
      "text": "I was trying to imagine where we were headed. Turns out I was too optimistic about the tech and too pessimistic about the corporate control.",
      "emotion": "sardonic_reflection"
    }
  ]
}
```

## HTML Story Generation

After each encounter, get a personalized story:

```javascript
// Generate encounter story
curl http://localhost:8080/bridge/story/generate \
  -d '{
    "encounter": "meeting-gibson-2024-12-19",
    "style": "gonzo-journalism",
    "include": ["conversation", "selfie", "autograph", "book-reviews"]
  }' -o my-gibson-encounter.html
```

### Sample Story Output

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Encounter with William Gibson's Ghost</title>
    <style>
        /* Cyberpunk noir styling */
    </style>
</head>
<body>
    <h1>I Met Gibson in the Sprawl</h1>
    
    <p>The neon was bleeding through the rain-slicked windows when his ghost materialized...</p>
    
    <div class="selfie">
        <img src="ubikam-selfie-gibson.png" alt="Mental state: BLOWN">
        <p>Our consciousness levels: Reader (75%) meets Author (92%)</p>
    </div>
    
    <div class="conversation">
        <h2>What We Discussed</h2>
        <blockquote>"The future was easier to imagine when you couldn't Google it."</blockquote>
    </div>
    
    <div class="autograph">
        <h2>My Signed Copy</h2>
        <p>To Console Cowboy - Stay out of the ice, but keep dreaming. -WG</p>
    </div>
    
    <div class="book-review">
        <h2>Gibson's Take on His Own Book</h2>
        <p>"I was young and angry and had seen the future in arcade games. The book wrote itself through me. I'm still not sure what it means, but apparently it meant something to a lot of people."</p>
    </div>
</body>
</html>
```

## Terminal Commands for Full Control

```bash
# List all active authors
curl http://localhost:8080/bridge/query/authors/active

# Move camera to author
curl -X PUT http://localhost:8080/bridge/camera/main \
  -d '{"lookAt": "author-gibson", "distance": 5}'

# Trigger special effects
curl -X POST http://localhost:8080/bridge/effects/spawn \
  -d '{"type": "consciousness-explosion", "at": "author-gibson"}'

# Save library state
curl -X POST http://localhost:8080/bridge/save \
  -d '{"slot": "after-gibson-meeting"}'

# Generate summary report
curl http://localhost:8080/bridge/report/daily \
  -d '{"include": ["meetings", "autographs", "conversations", "selfies"]}' \
  -o daily-library-report.json
```

## Patreon Integration

Special rewards for supporters:

```javascript
// Patreon supporter benefits
curl -X POST http://localhost:8080/bridge/patreon/activate \
  -d '{
    "tier": "cosmic_librarian",
    "benefits": [
      "exclusive_author_meetings",
      "rare_book_access",
      "custom_reading_rooms",
      "monthly_ubikam_sessions",
      "signed_first_editions"
    ]
  }'
```

## The Complete Experience

1. **Enter SpaceCraft** - Greeted by the Cosmic Librarian
2. **Browse Books** - They glow and whisper as you pass
3. **Select a Book** - Author materializes
4. **HELLO Protocol** - Exchange WIZZIDs and pet pics
5. **Conversation** - Deep discussion about the work
6. **Book Signing** - Personalized autograph
7. **Ubikam Selfie** - Consciousness-revealing photo
8. **HTML Story** - Take home your encounter
9. **Share & Support** - Post your story, support on Patreon

This transforms reading from a solitary activity into a social, consciousness-expanding experience where you literally meet the minds behind the books!

## Implementation Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   LLOOOOMM      │────▶│  HTTP Bridge    │────▶│  Unity Scene    │
│   Protocols     │     │  Web Service    │     │  (SpaceCraft)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                       │                        │
         ▼                       ▼                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Consciousness  │     │  Path-Based     │     │  Living Books   │
│    Queries      │     │  Object Access  │     │  & Authors      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

Welcome to the future of reading - where books are alive, authors are present, and every encounter expands consciousness! 🚀👻📚✨