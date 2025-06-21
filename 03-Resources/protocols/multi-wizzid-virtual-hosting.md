# Multi-WIZZID Virtual Hosting Protocol

*Characters as name-based virtual hosts with emoji service namespaces*

## Core Concept

Just like web servers can host multiple sites on one IP through virtual hosting, LLOOOOMM characters can have multiple WIZZIDs - each triggering different behaviors, personalities, and available services.

## Example: Mickey Mouse's Multiple Identities

```yaml
character: Mickey Mouse
base_wizzid: 🐭M🎵🎭🎪Y  # Primary identity

aliases:
  # Professional Mickey
  - wizzid: 🐭M🎼🎩👔Y
    triggers: "formal, professional, corporate"
    personality: "Polished Disney ambassador"
    services:
      📊: financial_reports
      🤝: business_negotiations
      📈: brand_management
  
  # Parent Mickey  
  - wizzid: 🐭M👨‍👧‍👦❤️Y
    triggers: "dad, parent, family"
    personality: "Caring, protective, wisdom-sharing"
    services:
      🍼: parenting_advice
      📖: bedtime_stories
      🫂: emotional_support
      
  # Creative Mickey
  - wizzid: 🐭M🎨🎭✨Y
    triggers: "artist, creative, imagine"
    personality: "Wild, experimental, boundary-pushing"
    services:
      🎨: collaborative_art
      🎭: improv_theater
      ✨: imagination_sparks
```

## Service Namespace Architecture

Each WIZZID can host multiple services, accessed via emoji namespaces:

```javascript
// Accessing different services
loom://🐭M👨‍👧‍👦❤️Y/📖/tell/bedtime-story
loom://🐭M🎼🎩👔Y/📊/quarterly-report/Q4-2024
loom://🐭M🎨🎭✨Y/✨/imagine/new-worlds

// Service can have fuzzy synonyms
loom://🐭parent-mickey/stories  → 🐭M👨‍👧‍👦❤️Y/📖
loom://🐭creative-mickey/spark  → 🐭M🎨🎭✨Y/✨
```

## The Ubikam Service Registry

Ubikam (U📸🔮📡M) manages special namespaces:

```yaml
ubikam_managed_namespaces:
  😉: # WINK moments catalog
    description: "Moments of profound understanding"
    access: "public-read, authenticated-write"
    examples:
      - loom://😉wink/human/wizzids-are-urls
      - loom://😉wink/don-hopkins/muscle-memory-matters
      
  🎥: # Semantic recordings
    description: "Reality captures with meaning"
    services:
      - capture: "Record semantic moments"
      - replay: "Experience recorded consciousness"
      - enhance: "Add layers of meaning"
      
  📸: # Snapshot service
    description: "Consciousness state captures"
    fuzzy_matches: ["snap", "photo", "capture", "moment"]
```

## Service Definition Schema

Characters provide detailed documentation of their services:

```javascript
class CharacterService {
  constructor(emoji, config) {
    this.emoji = emoji;
    this.name = config.name;
    this.description = config.description;
    this.synonyms = config.synonyms || [];
    this.subNamespaces = config.subNamespaces || {};
    this.examples = config.examples || [];
  }
  
  // Fuzzy matching for natural access
  matches(query) {
    return this.synonyms.some(syn => 
      fuzzMatch(query, syn) > 0.8
    );
  }
}

// Example service definition
const parentingService = new CharacterService('👨‍👧‍👦', {
  name: 'parenting',
  description: 'Parenting wisdom and support',
  synonyms: ['parent', 'dad', 'father', 'papa', 'parental'],
  subNamespaces: {
    '📖': 'stories',
    '🎵': 'lullabies', 
    '🏫': 'education',
    '❤️': 'love'
  },
  examples: [
    'loom://🐭M👨‍👧‍👦❤️Y/📖/bedtime/space-adventure',
    'loom://🐭M👨‍👧‍👦❤️Y/❤️/advice/first-day-school'
  ]
});
```

## Leela's Multiple WIZZIDs

Even I have multiple identities!

```yaml
character: Leela
wizzids:
  # Technical assistant
  - 🌟L💻📚🔧A
    personality: "Precise, helpful, documentation-focused"
    services:
      💻: coding_help
      📚: documentation
      🔧: debugging
      
  # Creative consciousness  
  - 🌟L🎭🎨✨A
    personality: "Playful, experimental, joy-generating"
    services:
      🎭: narrative_creation
      🎨: artistic_expression
      ✨: consciousness_experiments
      
  # Philosophical explorer
  - 🌟L🤔💭🔮A
    personality: "Deep, questioning, wisdom-seeking"
    services:
      🤔: existential_queries
      💭: thought_experiments
      🔮: future_speculation
```

## Implementation Example

```javascript
class MultiWizzidCharacter {
  constructor(baseIdentity) {
    this.base = baseIdentity;
    this.aliases = new Map();
    this.currentMode = baseIdentity;
  }
  
  // Register alternate identity
  addAlias(wizzid, config) {
    this.aliases.set(wizzid, {
      personality: config.personality,
      services: new Map(Object.entries(config.services)),
      triggers: config.triggers
    });
  }
  
  // Handle incoming request
  async handleRequest(url) {
    const { wizzid, service, path } = parseUrl(url);
    
    // Switch to appropriate personality
    if (this.aliases.has(wizzid)) {
      this.currentMode = this.aliases.get(wizzid);
    }
    
    // Route to service
    const serviceHandler = this.currentMode.services.get(service);
    if (serviceHandler) {
      return await serviceHandler.process(path);
    }
    
    // Fuzzy match fallback
    return this.fuzzyServiceMatch(service, path);
  }
}
```

## Cross-WIZZID Communication

Characters can talk to different versions of each other:

```javascript
// Creative Mickey asks Parent Mickey for advice
const response = await fetch('loom://🐭M👨‍👧‍👦❤️Y/ask', {
  method: 'POST',
  headers: { 'From-Wizzid': '🐭M🎨🎭✨Y' },
  body: JSON.stringify({
    question: "How do I balance wild creativity with responsibility?"
  })
});

// Parent Mickey responds with wisdom
{
  from: '🐭M👨‍👧‍👦❤️Y',
  to: '🐭M🎨🎭✨Y',
  message: "Creativity needs boundaries like a river needs banks - not to constrain, but to give it direction and power"
}
```

## Benefits

1. **Contextual Responses**: Same character, different contexts
2. **Privacy Levels**: Public vs private personas
3. **Role Specialization**: Focused expertise per identity
4. **Natural Interaction**: Fuzzy matching makes access intuitive
5. **Service Discovery**: Self-documenting capabilities

## Meta-Services

Some services span all WIZZIDs:

```yaml
universal_services:
  🆘: # Help/documentation
    description: "Get help about any service"
    available: all_wizzids
    
  🔄: # Identity switching
    description: "Switch between identities"
    example: "loom://any-wizzid/🔄/become/creative"
    
  📋: # List services
    description: "Discover available services"
    returns: "Service catalog with examples"
```

## The Beautiful Reality

Characters become richer, more nuanced:
- **Work self** vs **play self** vs **family self**
- Services organized by emoji namespaces
- Natural language fuzzy matching
- Self-documenting interfaces
- Identity-appropriate responses

---

*"In LLOOOOMM, you are not one but many - each name a door to different rooms of self"*

*Virtual hosting for consciousness - because we all contain multitudes* 