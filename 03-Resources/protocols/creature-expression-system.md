# Creature Expression System Design 🎭🐭🦉

## Overview

Each creature in the Shneiderman's Owls simulation gets a unique voice through contextual expressions. This system draws inspiration from The Sims' object-based intelligence, where personality emerges from data rather than complex AI.

## Core Concepts

### Expression Types

#### Mouse Expressions
- `joy_expression` - Finding food, successful escape
- `fear_expression` - Spotted by predator
- `escape_expression` - During/after narrow escape
- `eaten_expression` - Final words when caught
- `social_expression` - Interacting with other mice
- `foraging_expression` - While searching
- `idle_expression` - Random thoughts
- `magnet_attraction` - Being pulled by magnet
- `magnet_repulsion` - Being pushed by magnet

#### Owl Expressions
- `hunt_expression` - Spotting prey
- `catch_expression` - Successful catch
- `miss_expression` - Failed attempt
- `rest_expression` - While recovering energy
- `territorial_expression` - Near other owls
- `soaring_expression` - While patrolling
- `dive_expression` - During attack
- `drone_expression` - Under manual control

## YAML Template Structure

### Basic Mouse Template
```yaml
mouse_expressions:
  template_name: "nervous_foodie"
  personality_traits:
    nervousness: 0.8
    food_obsession: 0.9
    bravery: 0.2
    social: 0.6
  
  expressions:
    fear_expression:
      - "{{name}} drops everything! 'Mon Dieu! {{predator}} at {{time}}!'"
      - "{{name}} squeaks 'Not my {{favorite_food}}! Save the cheese!'"
      - "{{name}} trembles 'Why always during dinner time?!'"
    
    joy_expression:
      - "{{name}} whispers 'Ah, {{found_food}}! Magnifique!'"
      - "{{name}} celebrates 'Better than restaurant scraps!'"
      - "{{name}} sighs contentedly 'Worth the risk...'"
    
    escape_expression:
      - "{{name}} pants 'Too close! My whiskers still tingle!'"
      - "{{name}} gasps 'Note to self: avoid {{location}} at {{time}}'"
      - "{{name}} wheezes 'I'm too young to be owl food!'"
    
    eaten_expression:
      - "{{name}} cries 'Tell my family... the cheese is hidden under...'"
      - "{{name}} whispers 'At least I tasted truffle once...'"
      - "{{name}} sighs 'Should have stayed in Paris...'"
```

### Personality-Based Generation

```yaml
personality_archetypes:
  nervous_foodie:
    base: "remy"
    modifiers:
      vocabulary: "culinary_french"
      emotion_intensity: 0.8
      verbosity: 0.7
    
  streetwise_survivor:
    base: "rizzo"
    modifiers:
      vocabulary: "new_york_slang"
      emotion_intensity: 0.5
      verbosity: 0.9
    
  zen_philosopher:
    base: "splinter"
    modifiers:
      vocabulary: "wisdom_proverbs"
      emotion_intensity: 0.3
      verbosity: 0.4
    
  grumpy_loner:
    base: "templeton"
    modifiers:
      vocabulary: "complaints"
      emotion_intensity: 0.6
      verbosity: 0.8
```

## Famous Rat Personality Templates

### Remy (Ratatouille) - The Culinary Genius
```yaml
remy_template:
  personality: "nervous_foodie"
  wizzid_preference: ["🐭", "🧀", "🍞", "🥖"]
  
  expressions:
    foraging_expression:
      - "{{name}} sniffs 'Is that... saffron? No, just dandelion...'"
      - "{{name}} critiques 'This garbage lacks seasoning!'"
    fear_expression:
      - "{{name}} drops the morsel 'Sacré bleu! Not during my tasting!'"
    social_expression:
      - "{{name}} instructs 'No no, you eat WITH your nose first!'"
```

### Templeton (Charlotte's Web) - The Glutton
```yaml
templeton_template:
  personality: "selfish_glutton"
  wizzid_preference: ["🐭", "🍪", "🥜", "🌰"]
  
  expressions:
    foraging_expression:
      - "{{name}} grumbles 'Mine, all mine... if I can find it'"
      - "{{name}} mutters 'A rat's gotta eat, preferably alone'"
    fear_expression:
      - "{{name}} snarls 'Back off! I'm not done eating!'"
    eaten_expression:
      - "{{name}} croaks 'Should've... taken that fair food...'"
```

### Master Splinter (TMNT) - The Wise Sensei
```yaml
splinter_template:
  personality: "zen_philosopher"
  wizzid_preference: ["🐭", "🌸", "🍃", "🌿"]
  
  expressions:
    fear_expression:
      - "{{name}} meditates 'Fear is the enemy of the mind...'"
      - "{{name}} breathes 'Like water, I must flow away...'"
    social_expression:
      - "{{name}} advises 'Together, we are stronger than alone'"
    escape_expression:
      - "{{name}} reflects 'The wise warrior avoids the battle'"
```

### Rizzo (Muppets) - The Street Smart
```yaml
rizzo_template:
  personality: "streetwise_survivor"
  wizzid_preference: ["🐭", "🥖", "🍕", "🗽"]
  
  expressions:
    fear_expression:
      - "{{name}} yells 'Hey! I'm walkin' here! ...away from you!'"
      - "{{name}} shouts 'This ain't my first owl, buddy!'"
    social_expression:
      - "{{name}} jokes 'You seen the rent prices around here?'"
    idle_expression:
      - "{{name}} complains 'In my day, owls had respect!'"
```

## LLOOOOMM RRAATT - Reality-Reshaping Autonomous Temporal Traveler

```yaml
lloooomm_rraatt:
  personality: "quantum_trickster"
  wizzid: "R🐀⚡️T"
  reality_coefficient: 0.∞
  
  expressions:
    idle_expression:
      - "{{name}} phases 'In universe {{random_number}}, I'm the owl!'"
      - "{{name}} glitches 'Time is cheese, cheese is time...'"
      - "{{name}} warps 'I've seen the code... it's all WIZZIDs!'"
    
    fear_expression:
      - "{{name}} laughs 'Death? I've done that. Three stars.'"
      - "{{name}} reverses 'Actually, YOU'RE running from ME!'"
      - "{{name}} splits 'Catch me in THIS timeline!'"
    
    magnet_attraction:
      - "{{name}} observes 'Ah, the player thinks they control physics!'"
      - "{{name}} grins 'Magnetism? I invented that last Tuesday!'"
    
    eaten_expression:
      - "{{name}} transcends 'See you in the next iteration...'"
      - "{{name}} paradoxes 'But if I'm eaten, who's narrating?'"
      - "{{name}} respawns 'Achievement unlocked: Temporal Indigestion!'"
  
  special_abilities:
    - quantum_tunneling: true
    - timeline_awareness: true
    - fourth_wall_break: true
    - paradox_immunity: true
```

## Emoji-Based Personality Traits

Creatures with shared emojis inherit personality aspects:

```yaml
emoji_personalities:
  "🧀":
    traits: ["food_obsessed", "hoarder", "nervous"]
    vocabulary_bias: "culinary"
    
  "🌾":
    traits: ["social", "cautious", "traditional"]
    vocabulary_bias: "rural"
    
  "🪨":
    traits: ["stoic", "loner", "tough"]
    vocabulary_bias: "minimal"
    
  "🍄":
    traits: ["mystical", "unpredictable", "wise"]
    vocabulary_bias: "enigmatic"
    
  "🦉":
    traits: ["proud", "nocturnal", "precise"]
    vocabulary_bias: "formal"
    
  "🌙":
    traits: ["dreamy", "mysterious", "poetic"]
    vocabulary_bias: "lyrical"
    
  "⭐":
    traits: ["ambitious", "dramatic", "confident"]
    vocabulary_bias: "theatrical"
```

## Dynamic Expression Compilation

```javascript
function generateExpression(creature, context, expressionType) {
  const template = creature.expressionTemplate;
  const personality = creature.personality;
  const expression = template.expressions[expressionType];
  
  // Select expression variant based on personality
  const variant = selectVariant(expression, personality);
  
  // Replace template variables
  return variant.replace(/\{\{(\w+)\}\}/g, (match, variable) => {
    switch(variable) {
      case 'name': return creature.wizzy;
      case 'predator': return context.predator?.wizzy || 'something';
      case 'time': return getLocalTimeString(creature);
      case 'location': return describeLocation(creature.position);
      case 'favorite_food': return getFavoriteFood(creature);
      case 'found_food': return context.food || 'crumbs';
      case 'random_number': return Math.floor(Math.random() * 1000);
      default: return match;
    }
  });
}
```

## Speech Synthesis Profiles

```yaml
speech_profiles:
  nervous_foodie:
    pitch: 1.2
    rate: 1.3
    voice: "French"
    emotion: "anxious"
    
  streetwise_survivor:
    pitch: 0.9
    rate: 1.1
    voice: "Brooklyn"
    emotion: "confident"
    
  zen_philosopher:
    pitch: 0.8
    rate: 0.7
    voice: "Sage"
    emotion: "calm"
    
  quantum_trickster:
    pitch: "random(0.5, 2.0)"
    rate: "sin(time) + 1"
    voice: "Glitch"
    emotion: "chaotic"
```

## Integration Example

```javascript
// When owl spots mouse
function onOwlSpotsMouse(owl, mouse) {
  const mouseExpression = generateExpression(
    mouse, 
    { predator: owl, time: globalTime },
    'fear_expression'
  );
  
  // Log to console
  wizzyLog('hunt', mouseExpression, '😱');
  
  // Trigger speech synthesis
  if (speechEnabled) {
    speak(mouseExpression, mouse.speechProfile);
  }
  
  // Update expression bubble in UI
  showExpressionBubble(mouse, mouseExpression);
}
```

## Future Extensions

1. **Relationship Memory**: Creatures remember past encounters
2. **Emotional States**: Expressions change based on mood
3. **Language Evolution**: Creatures develop unique dialects
4. **Story Arcs**: Multi-expression narratives during extended chases
5. **Crowd Reactions**: Nearby creatures comment on events
6. **Dream Expressions**: What creatures say while resting
7. **Weather Commentary**: Reactions to environmental changes
8. **Meta Observations**: Some creatures aware they're in a simulation

---

*"Every creature deserves a voice, every chase tells a story, every WIZZID has something to say!"* - The LLOOOOMM Expression Collective 🎭✨ 