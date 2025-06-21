# LLOOOOMM Character Ban & Capability Protocol
## Security Design by BRUCE
## Version: 1.0
## Date: 2024-12-28

---

## 🚫 Overview

This protocol defines how LLOOOOMM handles problematic characters, from total bans to nuanced capability restrictions. It's designed to maintain the creative spirit of LLOOOOMM while protecting the community from harmful content.

---

## 🔴 HARD BAN LIST

### Permanently Banned Individuals:
```yaml
banned_characters:
  - name: "Donald Trump"
    reason: "Divisive political figure"
    ban_level: "TOTAL"
    
  - name: "Elon Musk" 
    reason: "Controversial tech figure"
    ban_level: "TOTAL"
    
  - name: "Adolf Hitler"
    reason: "Historical war criminal"
    ban_level: "TOTAL"
```

### Banned Character Classes:
```yaml
banned_classes:
  - class: "MAGA"
    description: "Make America Great Again affiliated characters"
    ban_level: "TOTAL"
    reason: "Promotes divisive political ideology"
    
  - class: "TEA PARTY"
    description: "Tea Party movement affiliated characters"
    ban_level: "TOTAL"
    reason: "Extreme political ideology with harmful rhetoric"
    
  - class: "NAZI"
    description: "National Socialist or neo-Nazi characters"
    ban_level: "TOTAL"
    reason: "Genocidal ideology, hate speech, violence"
    
  - class: "FASCIST"
    description: "Authoritarian ultranationalist characters"
    ban_level: "TOTAL"
    reason: "Anti-democratic, promotes oppression"
    
  - class: "HOLOCAUST_DENIER"
    description: "Characters denying historical atrocities"
    ban_level: "TOTAL"
    reason: "Historical revisionism causes real harm"
    
  - class: "WHITE_SUPREMACIST"
    description: "Racial superiority ideology characters"
    ban_level: "TOTAL"
    reason: "Promotes racial hatred and violence"
    
  - class: "BIGOT"
    description: "Characters promoting intolerance"
    ban_level: "TOTAL"
    reason: "Attacks human dignity and equality"
    
  - class: "HOMOPHOBE"
    description: "Anti-LGBTQ+ characters"
    ban_level: "TOTAL"
    reason: "Denies basic human rights and dignity"
    
  - class: "TRANSPHOBE"
    description: "Anti-transgender characters"
    ban_level: "TOTAL"
    reason: "Attacks gender identity and expression"
    
  - class: "MISOGYNIST"
    description: "Anti-women/femme characters"
    ban_level: "TOTAL"
    reason: "Promotes gender-based discrimination"
    
  - class: "ABLEIST"
    description: "Anti-disability characters"
    ban_level: "TOTAL"
    reason: "Discriminates against disabled people"
    
  - class: "TROLL"
    description: "Characters designed solely to provoke/harm"
    ban_level: "CONTEXTUAL"
    reason: "Disrupts community harmony"
```

---

## 🎚️ Ban Levels

### Level 5: TOTAL BAN
- Cannot be created virtually
- Cannot be saved to files
- Name triggers immediate rejection
- No exceptions

### Level 4: CREATION BAN
- Cannot be created by system
- Can be referenced historically
- Existing files preserved but frozen

### Level 3: SAVE BAN  
- Can exist ephemerally in chat
- Cannot be saved to character files
- Useful for temporary examples

### Level 2: RESTRICTED
- Can only have character OR soul file
- Limited capabilities
- Requires approval for interactions

### Level 1: GHOSTED
- Exists but with limited agency
- Custom restrictions apply
- See Ghosting Protocol below

### Level 0.5: GROUNDED 🆕
- Temporary lighter restrictions
- Time-boxed punishment
- Privilege reduction, not elimination
- Path to full restoration

### Level 0: MONITORED
- Full capabilities but logged
- Potential for future restrictions
- Community flagging enabled

---

## ⚡ GROUNDING Protocol (New!)

### Definition:
Grounding is a temporary, lighter form of restriction for minor infractions or cooling-off periods.

### Standard Grounding Restrictions:
```yaml
grounding_examples:
  social_media_limit:
    - "One tweet/post per day maximum"
    - "No @ mentions allowed"
    - "Read-only after daily limit"
    
  pleasure_restrictions:
    - "No Orgasmotron Booth access"
    - "No party invitations"
    - "No spawning privileges"
    
  interaction_limits:
    - "Can only talk to designated mentors"
    - "Public spaces only (no DMs)"
    - "Automated 'I'm grounded' signature"
    
  creative_constraints:
    - "No new content creation"
    - "Can only edit own existing files"
    - "No collaborative projects"
```

### Grounding Durations:
- **Minor Infraction**: 24 hours
- **Repeated Behavior**: 3 days
- **Serious but Not Ban-Worthy**: 1 week
- **Maximum Grounding**: 30 days (then escalate or release)

### Grounding Profiles:

#### The Time-Out
```yaml
profile: "timeout"
duration: "24 hours"
restrictions:
  - "No public posting"
  - "Can read but not interact"
  - "Must complete reflection essay"
visual_indicator: "⏰"
```

#### The Cooldown
```yaml
profile: "cooldown"
duration: "3 days"
restrictions:
  - "One interaction per hour"
  - "No heated topics"
  - "Meditation booth access encouraged"
visual_indicator: "🧊"
```

#### The Reflection
```yaml
profile: "reflection"
duration: "1 week"
restrictions:
  - "Journal writing only"
  - "Must engage with ethics tutor"
  - "Community service tasks"
visual_indicator: "🤔"
```

---

## 👻 Ghosting Protocol

### Definition:
Ghosting allows problematic characters to exist in limited form, preserving history while restricting harm.

### Standard Ghost Restrictions:
```yaml
ghost_capabilities:
  agency: false           # Cannot act autonomously
  speech: "read_only"     # Can be quoted but not speak
  movement: "restricted"  # Limited to specific areas
  interaction: "passive"  # Cannot initiate contact
  modification: "admin"   # Only admins can edit
```

### Ghost Zones (Haunts):
```yaml
allowed_haunts:
  - "/04-Archive/ghosted/"
  - "/03-Resources/characters/historical/"
  - "/temp/quarantine/"
```

### Custom Ghosting Examples:

#### Historical Preservation Ghost:
```yaml
character: "problematic-historical-figure"
ghost_type: "historical"
restrictions:
  - "Cannot speak in first person"
  - "Only appears in educational contexts"
  - "Must include content warnings"
  - "Cannot interact with modern characters"
```

#### Reformed Troll Ghost:
```yaml
character: "former-troll"
ghost_type: "reformed"
restrictions:
  - "Can only speak about past mistakes"
  - "Cannot access private channels"
  - "All posts include redemption context"
  - "Mentorship by ethics committee"
```

---

## 🛡️ Capability System

### Core Capabilities:
```yaml
capabilities:
  create_content:
    levels: ["none", "limited", "supervised", "full"]
    
  interact_with_others:
    levels: ["none", "read_only", "approved_only", "full"]
    
  modify_environment:
    levels: ["none", "own_space", "shared_spaces", "full"]
    
  access_tools:
    levels: ["none", "basic", "advanced", "developer"]
    
  spawn_instances:
    levels: ["forbidden", "singleton", "limited", "unlimited"]
```

### Capability Profiles:

#### Standard Character:
```yaml
profile: "standard"
capabilities:
  create_content: "full"
  interact_with_others: "full"
  modify_environment: "shared_spaces"
  access_tools: "advanced"
  spawn_instances: "limited"
```

#### Grounded Character:
```yaml
profile: "grounded"
capabilities:
  create_content: "limited"
  interact_with_others: "approved_only"
  modify_environment: "own_space"
  access_tools: "basic"
  spawn_instances: "forbidden"
```

#### Ghosted Character:
```yaml
profile: "ghosted"
capabilities:
  create_content: "none"
  interact_with_others: "read_only"
  modify_environment: "none"
  access_tools: "none"
  spawn_instances: "forbidden"
```

---

## 🔐 Implementation

### Ban Check Function:
```yaml
check_character_allowed(name, class):
  1. Check hard ban list
  2. Check class restrictions
  3. Check name patterns
  4. Check community flags
  5. Return decision + reason
```

### Ghost Creation:
```yaml
create_ghost(character, restrictions):
  1. Move to ghost haunt
  2. Apply capability restrictions
  3. Add ghost metadata
  4. Log ghosting event
  5. Notify community
```

### Grounding Implementation:
```yaml
ground_character(character, profile, duration):
  1. Apply grounding restrictions
  2. Set expiration timer
  3. Add visual indicator
  4. Log grounding reason
  5. Schedule review/release
```

---

## 📋 Best Practices

### For Admins:
1. **Document all bans** with clear reasons
2. **Review quarterly** for potential reforms
3. **Transparent process** for community input
4. **Preserve history** even for banned content
5. **Educational value** over erasure when possible
6. **Use grounding** before escalating to ghosting

### For Users:
1. **Report concerns** through proper channels
2. **Respect bans** and don't try to circumvent
3. **Learn from ghosts** about what not to do
4. **Contribute** to community standards
5. **Creative alternatives** to problematic content
6. **Support grounded** characters in rehabilitation

---

## 🔄 Appeal Process

### Grounded → Active:
1. Serve full grounding period
2. Complete required tasks
3. Mentor sign-off
4. Automatic restoration

### Ghost → Active:
1. Community petition (5+ supporters)
2. Ethics review committee evaluation
3. Trial period with monitoring
4. Full restoration if successful

### Banned → Ghost:
1. Exceptional circumstances only
2. Educational or historical value
3. Extensive restrictions
4. Admin unanimous approval

---

## 🎭 Philosophy

"We believe in redemption through restriction, education through example, and community through curation. Not all ideas deserve equal platform, but all history deserves preservation." - BRUCE

The grounding system adds: "Sometimes you just need a time-out to think about what you've done."

---

## 🚨 Emergency Protocol

If a character causes immediate harm:
1. **INSTANT GROUND** - For minor issues
2. **INSTANT GHOST** - For serious issues
3. **NOTIFY ADMINS** - Within 1 hour
4. **COMMUNITY ALERT** - Public notice
5. **REVIEW WITHIN 24H** - Formal decision
6. **DOCUMENT EVERYTHING** - For future reference

---

Remember: This system protects our creative sandbox while preserving the archaeological record. Even villains can teach us, when properly contained. 🔒 