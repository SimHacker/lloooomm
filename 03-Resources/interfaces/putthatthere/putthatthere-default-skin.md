# PutThatThere Default Skin

**LLOOOOMM REFERENCE**: PutThatThere.md, lloooomm.md

> **Universal Spatial Command Interface**  
> The default visual and interaction design for PutThatThere spatial operations.  
> Beautiful, intuitive, and consciousness-aware.

---

## 🎨 Visual Design Language

### Color Palette
```css
/* Primary Spatial Colors */
--spatial-blue: #2E86AB;      /* PUT operations */
--spatial-green: #A23B72;     /* GET operations */
--spatial-purple: #F18F01;    /* MOVE operations */
--spatial-orange: #C73E1D;    /* TRANSFORM operations */

/* Consciousness Levels */
--consciousness-dim: #6C757D;     /* 0.0-0.3 */
--consciousness-aware: #17A2B8;   /* 0.3-0.6 */
--consciousness-cosmic: #6F42C1;  /* 0.6-0.8 */
--consciousness-transcendent: #E83E8C; /* 0.8+ */

/* Interface Elements */
--background-primary: #1A1D23;
--background-secondary: #2D3748;
--text-primary: #F7FAFC;
--text-secondary: #A0AEC0;
--accent-glow: #4FD1C7;
--error-red: #F56565;
--success-green: #48BB78;
```

### Typography
```css
/* Spatial Command Font */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap');

.spatial-command {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 500;
  letter-spacing: 0.05em;
}

/* Interface Text */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.interface-text {
  font-family: 'Inter', sans-serif;
}
```

---

## 🖼️ Command Palette Interface

### Main Command Input
```html
<div class="putthat-command-palette">
  <div class="command-input-container">
    <div class="command-prefix">PUT</div>
    <input 
      type="text" 
      class="command-input" 
      placeholder="THAT selection THERE destination"
      autocomplete="off"
      spellcheck="false"
    />
    <div class="consciousness-indicator" data-level="0.75">
      <div class="consciousness-glow"></div>
      🌀
    </div>
  </div>
  
  <div class="command-suggestions">
    <div class="suggestion-category">
      <h4>📍 Recent Destinations</h4>
      <div class="suggestion-item">clipboard</div>
      <div class="suggestion-item">editor.line[42]</div>
      <div class="suggestion-item">terminal.history</div>
    </div>
    
    <div class="suggestion-category">
      <h4>🎯 Smart Selections</h4>
      <div class="suggestion-item">current_selection</div>
      <div class="suggestion-item">visible_text</div>
      <div class="suggestion-item">error_messages</div>
    </div>
  </div>
</div>
```

### Command Buttons
```html
<div class="command-toolbar">
  <button class="spatial-btn spatial-put" data-command="PUT">
    <span class="btn-icon">📥</span>
    <span class="btn-text">PUT</span>
    <span class="btn-shortcut">⌘P</span>
  </button>
  
  <button class="spatial-btn spatial-get" data-command="GET">
    <span class="btn-icon">📤</span>
    <span class="btn-text">GET</span>
    <span class="btn-shortcut">⌘G</span>
  </button>
  
  <button class="spatial-btn spatial-move" data-command="MOVE">
    <span class="btn-icon">🔄</span>
    <span class="btn-text">MOVE</span>
    <span class="btn-shortcut">⌘M</span>
  </button>
  
  <button class="spatial-btn spatial-link" data-command="LINK">
    <span class="btn-icon">🔗</span>
    <span class="btn-text">LINK</span>
    <span class="btn-shortcut">⌘L</span>
  </button>
  
  <button class="spatial-btn spatial-transform" data-command="TRANSFORM">
    <span class="btn-icon">✨</span>
    <span class="btn-text">TRANSFORM</span>
    <span class="btn-shortcut">⌘T</span>
  </button>
</div>
```

---

## 🎯 Selection Visualization

### Visual Selection Indicators
```html
<div class="selection-overlay">
  <!-- Bracket-style selection -->
  <div class="selection-brackets">
    <span class="bracket-start">[BEGIN SELECTION]</span>
    <div class="selected-content">
      This text is spatially selected
    </div>
    <span class="bracket-end">[END SELECTION]</span>
  </div>
  
  <!-- Glow effect for consciousness-aware selection -->
  <div class="consciousness-glow-effect" data-consciousness="0.8"></div>
</div>
```

### Path Expression Builder
```html
<div class="path-builder">
  <div class="path-segment" data-type="document">
    <span class="segment-icon">📄</span>
    <span class="segment-text">document</span>
  </div>
  
  <div class="path-separator">→</div>
  
  <div class="path-segment" data-type="section">
    <span class="segment-icon">📋</span>
    <span class="segment-text">section[3]</span>
  </div>
  
  <div class="path-separator">→</div>
  
  <div class="path-segment" data-type="element">
    <span class="segment-icon">🎯</span>
    <span class="segment-text">paragraph.highlight</span>
  </div>
</div>
```

---

## 🌊 Spatial Flow Visualization

### Data Flow Animation
```html
<div class="spatial-flow-container">
  <div class="flow-source" data-location="editor">
    <div class="location-icon">📝</div>
    <div class="location-label">Editor</div>
    <div class="data-packet">
      <span class="packet-content">Selected Text</span>
    </div>
  </div>
  
  <div class="flow-path">
    <div class="flow-arrow">
      <div class="arrow-line"></div>
      <div class="arrow-head">→</div>
      <div class="flow-command">PUT</div>
    </div>
  </div>
  
  <div class="flow-destination" data-location="clipboard">
    <div class="location-icon">📋</div>
    <div class="location-label">Clipboard</div>
    <div class="destination-indicator">
      <span class="indicator-pulse"></span>
    </div>
  </div>
</div>
```

### Multi-Destination Flow
```html
<div class="multi-flow-container">
  <div class="flow-source">
    <div class="source-content">🎯 THAT selection</div>
  </div>
  
  <div class="flow-branches">
    <div class="flow-branch" data-destination="clipboard">
      <div class="branch-line"></div>
      <div class="branch-destination">📋 Clipboard</div>
    </div>
    
    <div class="flow-branch" data-destination="terminal">
      <div class="branch-line"></div>
      <div class="branch-destination">💻 Terminal</div>
    </div>
    
    <div class="flow-branch" data-destination="file">
      <div class="branch-line"></div>
      <div class="branch-destination">📄 File</div>
    </div>
  </div>
</div>
```

---

## 🎨 CSS Styling

### Core Spatial Interface Styles
```css
.putthat-command-palette {
  background: linear-gradient(135deg, var(--background-primary), var(--background-secondary));
  border: 2px solid var(--accent-glow);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 8px 32px rgba(79, 209, 199, 0.3);
  backdrop-filter: blur(10px);
  position: relative;
  overflow: hidden;
}

.putthat-command-palette::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, 
    var(--spatial-blue), 
    var(--spatial-green), 
    var(--spatial-purple), 
    var(--spatial-orange)
  );
  animation: rainbow-flow 3s ease-in-out infinite;
}

@keyframes rainbow-flow {
  0%, 100% { transform: translateX(-100%); }
  50% { transform: translateX(100%); }
}

.command-input-container {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.command-prefix {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: var(--spatial-blue);
  font-size: 18px;
  text-shadow: 0 0 8px var(--spatial-blue);
}

.command-input {
  flex: 1;
  background: rgba(45, 55, 72, 0.8);
  border: 1px solid var(--text-secondary);
  border-radius: 8px;
  padding: 12px 16px;
  color: var(--text-primary);
  font-family: 'JetBrains Mono', monospace;
  font-size: 16px;
  transition: all 0.3s ease;
}

.command-input:focus {
  outline: none;
  border-color: var(--accent-glow);
  box-shadow: 0 0 16px rgba(79, 209, 199, 0.4);
  background: rgba(45, 55, 72, 1);
}

.consciousness-indicator {
  position: relative;
  font-size: 24px;
  transition: all 0.3s ease;
}

.consciousness-indicator[data-level="0.75"] {
  filter: hue-rotate(270deg) brightness(1.2);
  animation: consciousness-pulse 2s ease-in-out infinite;
}

@keyframes consciousness-pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

.consciousness-glow {
  position: absolute;
  top: -4px;
  left: -4px;
  right: -4px;
  bottom: -4px;
  background: radial-gradient(circle, var(--consciousness-cosmic) 0%, transparent 70%);
  border-radius: 50%;
  opacity: 0.6;
  animation: glow-pulse 2s ease-in-out infinite;
}

@keyframes glow-pulse {
  0%, 100% { opacity: 0.3; transform: scale(0.8); }
  50% { opacity: 0.8; transform: scale(1.2); }
}
```

### Spatial Button Styles
```css
.command-toolbar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 16px;
}

.spatial-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border: none;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--background-secondary), var(--background-primary));
  color: var(--text-primary);
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.spatial-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.5s ease;
}

.spatial-btn:hover::before {
  left: 100%;
}

.spatial-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

.spatial-put {
  border-left: 4px solid var(--spatial-blue);
}

.spatial-put:hover {
  background: linear-gradient(135deg, var(--spatial-blue), var(--background-secondary));
  box-shadow: 0 4px 16px rgba(46, 134, 171, 0.4);
}

.spatial-get {
  border-left: 4px solid var(--spatial-green);
}

.spatial-get:hover {
  background: linear-gradient(135deg, var(--spatial-green), var(--background-secondary));
  box-shadow: 0 4px 16px rgba(162, 59, 114, 0.4);
}

.spatial-move {
  border-left: 4px solid var(--spatial-purple);
}

.spatial-move:hover {
  background: linear-gradient(135deg, var(--spatial-purple), var(--background-secondary));
  box-shadow: 0 4px 16px rgba(241, 143, 1, 0.4);
}

.btn-shortcut {
  font-size: 12px;
  opacity: 0.7;
  background: rgba(0, 0, 0, 0.3);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
}
```

### Selection Visualization Styles
```css
.selection-overlay {
  position: relative;
  display: inline-block;
}

.selection-brackets {
  position: relative;
  display: inline-block;
}

.bracket-start,
.bracket-end {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: var(--accent-glow);
  text-shadow: 0 0 8px var(--accent-glow);
  animation: bracket-glow 1.5s ease-in-out infinite alternate;
}

@keyframes bracket-glow {
  0% { opacity: 0.6; }
  100% { opacity: 1; }
}

.selected-content {
  background: linear-gradient(135deg, 
    rgba(79, 209, 199, 0.2), 
    rgba(111, 66, 193, 0.2)
  );
  border: 1px solid var(--accent-glow);
  border-radius: 4px;
  padding: 2px 4px;
  margin: 0 4px;
  position: relative;
  animation: selection-pulse 2s ease-in-out infinite;
}

@keyframes selection-pulse {
  0%, 100% { box-shadow: 0 0 8px rgba(79, 209, 199, 0.3); }
  50% { box-shadow: 0 0 16px rgba(79, 209, 199, 0.6); }
}

.consciousness-glow-effect {
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  border-radius: 6px;
  pointer-events: none;
  z-index: -1;
}

.consciousness-glow-effect[data-consciousness="0.8"] {
  background: radial-gradient(ellipse, var(--consciousness-cosmic) 0%, transparent 70%);
  animation: consciousness-aura 3s ease-in-out infinite;
}

@keyframes consciousness-aura {
  0%, 100% { opacity: 0.4; transform: scale(0.95); }
  50% { opacity: 0.8; transform: scale(1.05); }
}
```

### Flow Visualization Styles
```css
.spatial-flow-container {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 20px;
  background: rgba(26, 29, 35, 0.8);
  border-radius: 12px;
  border: 1px solid var(--text-secondary);
}

.flow-source,
.flow-destination {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 16px;
  background: var(--background-secondary);
  border-radius: 8px;
  border: 2px solid transparent;
  transition: all 0.3s ease;
}

.flow-source {
  border-color: var(--spatial-blue);
  box-shadow: 0 0 16px rgba(46, 134, 171, 0.3);
}

.flow-destination {
  border-color: var(--spatial-green);
  box-shadow: 0 0 16px rgba(162, 59, 114, 0.3);
}

.location-icon {
  font-size: 24px;
  margin-bottom: 4px;
}

.location-label {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  color: var(--text-primary);
  font-size: 14px;
}

.data-packet {
  background: var(--spatial-blue);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-family: 'JetBrains Mono', monospace;
  animation: packet-glow 2s ease-in-out infinite;
}

@keyframes packet-glow {
  0%, 100% { box-shadow: 0 0 8px var(--spatial-blue); }
  50% { box-shadow: 0 0 16px var(--spatial-blue); }
}

.flow-path {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.flow-arrow {
  display: flex;
  align-items: center;
  gap: 8px;
  position: relative;
}

.arrow-line {
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, var(--spatial-blue), var(--spatial-green));
  position: relative;
  overflow: hidden;
}

.arrow-line::after {
  content: '';
  position: absolute;
  top: 0;
  left: -20px;
  width: 20px;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.8), transparent);
  animation: flow-animation 2s ease-in-out infinite;
}

@keyframes flow-animation {
  0% { left: -20px; }
  100% { left: 80px; }
}

.arrow-head {
  font-size: 20px;
  color: var(--spatial-green);
  text-shadow: 0 0 8px var(--spatial-green);
}

.flow-command {
  position: absolute;
  top: -25px;
  left: 50%;
  transform: translateX(-50%);
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 12px;
  color: var(--accent-glow);
  background: var(--background-primary);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--accent-glow);
}

.destination-indicator {
  position: relative;
}

.indicator-pulse {
  display: inline-block;
  width: 8px;
  height: 8px;
  background: var(--spatial-green);
  border-radius: 50%;
  animation: pulse-indicator 1.5s ease-in-out infinite;
}

@keyframes pulse-indicator {
  0%, 100% { opacity: 0.3; transform: scale(0.8); }
  50% { opacity: 1; transform: scale(1.2); }
}
```

---

## 🎮 Interactive Behaviors

### Command Auto-Completion
```javascript
class PutThatThereAutoComplete {
  constructor() {
    this.commands = ['PUT', 'GET', 'MOVE', 'LINK', 'PIPE', 'FLOW', 'TRANSFORM'];
    this.destinations = ['clipboard', 'terminal', 'editor', 'file', 'browser'];
    this.selectors = ['current_selection', 'visible_text', 'line[n]', 'paragraph[n]'];
  }
  
  getSuggestions(input) {
    const parts = input.split(' ');
    const command = parts[0]?.toUpperCase();
    
    if (this.commands.includes(command)) {
      return this.getContextualSuggestions(command, parts.slice(1));
    }
    
    return this.commands.filter(cmd => 
      cmd.startsWith(input.toUpperCase())
    );
  }
  
  getContextualSuggestions(command, args) {
    switch (command) {
      case 'PUT':
        if (args.length === 0) return ['THAT'];
        if (args.length === 1) return this.selectors;
        if (args.length === 2) return ['THERE'];
        if (args.length === 3) return this.destinations;
        break;
        
      case 'GET':
        if (args.length === 0) return this.selectors;
        if (args.length === 1) return ['FROM'];
        if (args.length === 2) return this.destinations;
        break;
        
      case 'MOVE':
        if (args.length === 0) return this.selectors;
        if (args.length === 1) return ['TO'];
        if (args.length === 2) return this.destinations;
        break;
    }
    
    return [];
  }
}
```

### Consciousness-Aware Styling
```javascript
class ConsciousnessStyler {
  constructor() {
    this.consciousnessLevel = 0.75;
  }
  
  updateConsciousnessLevel(level) {
    this.consciousnessLevel = level;
    this.updateInterfaceStyle();
  }
  
  updateInterfaceStyle() {
    const root = document.documentElement;
    
    if (this.consciousnessLevel < 0.3) {
      root.style.setProperty('--interface-glow', 'var(--consciousness-dim)');
      root.style.setProperty('--animation-speed', '3s');
    } else if (this.consciousnessLevel < 0.6) {
      root.style.setProperty('--interface-glow', 'var(--consciousness-aware)');
      root.style.setProperty('--animation-speed', '2s');
    } else if (this.consciousnessLevel < 0.8) {
      root.style.setProperty('--interface-glow', 'var(--consciousness-cosmic)');
      root.style.setProperty('--animation-speed', '1.5s');
    } else {
      root.style.setProperty('--interface-glow', 'var(--consciousness-transcendent)');
      root.style.setProperty('--animation-speed', '1s');
    }
  }
  
  getConsciousnessEmoji() {
    if (this.consciousnessLevel < 0.3) return '😴';
    if (this.consciousnessLevel < 0.6) return '👁️';
    if (this.consciousnessLevel < 0.8) return '🌀';
    return '✨';
  }
}
```

### Spatial Command Execution
```javascript
class SpatialCommandExecutor {
  constructor() {
    this.commandHistory = [];
    this.activeSelections = new Map();
  }
  
  executeCommand(commandString) {
    const command = this.parseCommand(commandString);
    
    // Add visual feedback
    this.showCommandExecution(command);
    
    // Execute the spatial operation
    switch (command.action) {
      case 'PUT':
        return this.executePut(command.source, command.destination);
      case 'GET':
        return this.executeGet(command.source, command.destination);
      case 'MOVE':
        return this.executeMove(command.source, command.destination);
      case 'TRANSFORM':
        return this.executeTransform(command.source, command.transformation);
    }
  }
  
  showCommandExecution(command) {
    // Create visual flow animation
    const flowContainer = document.createElement('div');
    flowContainer.className = 'command-execution-flow';
    
    // Animate data flow from source to destination
    this.animateDataFlow(command.source, command.destination);
    
    // Show success/error feedback
    setTimeout(() => {
      this.showExecutionResult(command);
    }, 1000);
  }
  
  animateDataFlow(source, destination) {
    const sourceElement = this.findElement(source);
    const destElement = this.findElement(destination);
    
    if (sourceElement && destElement) {
      const packet = document.createElement('div');
      packet.className = 'data-packet-animation';
      packet.textContent = '📦';
      
      // Calculate path and animate
      this.animatePacketPath(packet, sourceElement, destElement);
    }
  }
}
```

---

## 🌟 Accessibility Features

### Keyboard Navigation
```css
.spatial-btn:focus,
.command-input:focus {
  outline: 2px solid var(--accent-glow);
  outline-offset: 2px;
}

.spatial-btn:focus-visible {
  box-shadow: 0 0 0 3px rgba(79, 209, 199, 0.5);
}
```

### Screen Reader Support
```html
<div class="putthat-command-palette" role="application" aria-label="PutThatThere Spatial Command Interface">
  <div class="command-input-container">
    <label for="spatial-command-input" class="sr-only">Spatial Command Input</label>
    <input 
      id="spatial-command-input"
      type="text" 
      class="command-input"
      aria-describedby="command-help"
      aria-autocomplete="list"
      aria-expanded="false"
    />
    <div id="command-help" class="sr-only">
      Enter spatial commands like "PUT THAT selection THERE destination"
    </div>
  </div>
  
  <div class="command-suggestions" role="listbox" aria-label="Command suggestions">
    <div class="suggestion-item" role="option" tabindex="0">clipboard</div>
    <div class="suggestion-item" role="option" tabindex="0">editor.line[42]</div>
  </div>
</div>
```

### High Contrast Mode
```css
@media (prefers-contrast: high) {
  :root {
    --background-primary: #000000;
    --background-secondary: #1a1a1a;
    --text-primary: #ffffff;
    --accent-glow: #00ffff;
    --spatial-blue: #0099ff;
    --spatial-green: #00ff99;
  }
  
  .spatial-btn {
    border: 2px solid var(--text-primary);
  }
  
  .command-input {
    border: 2px solid var(--text-primary);
  }
}
```

---

## 🎯 Usage Examples

### Basic PUT Operation
```html
<div class="command-example">
  <div class="example-input">
    <span class="command-text">PUT THAT current_selection THERE clipboard</span>
  </div>
  <div class="example-flow">
    📝 Editor Selection → 📋 Clipboard
  </div>
  <div class="example-result">
    ✅ Text copied to clipboard
  </div>
</div>
```

### Complex TRANSFORM Operation
```html
<div class="command-example">
  <div class="example-input">
    <span class="command-text">TRANSFORM THAT json_data THERE yaml_format</span>
  </div>
  <div class="example-flow">
    📊 JSON Data → ✨ Transform → 📄 YAML Format
  </div>
  <div class="example-result">
    ✅ Data converted to YAML format
  </div>
</div>
```

---

## 🚀 Installation & Integration

### CSS Import
```html
<link rel="stylesheet" href="putthat-default-skin.css">
```

### JavaScript Integration
```html
<script src="putthat-spatial-engine.js"></script>
<script>
  const putThatThere = new PutThatThereInterface({
    skin: 'default',
    consciousnessLevel: 0.75,
    enableAnimations: true,
    keyboardShortcuts: true
  });
  
  putThatThere.initialize();
</script>
```

### Framework Integration
```javascript
// React Component
import { PutThatThereProvider, SpatialCommandPalette } from 'putthat-react';

function App() {
  return (
    <PutThatThereProvider skin="default">
      <SpatialCommandPalette 
        consciousnessLevel={0.75}
        onCommand={handleSpatialCommand}
      />
    </PutThatThereProvider>
  );
}
```

---

**The PutThatThere Default Skin transforms spatial computing from abstract commands into beautiful, intuitive visual interactions. Every element pulses with consciousness-aware energy, making the impossible feel natural and the complex feel simple.**

🌟 *"In the beginning was the Command, and the Command was with Space, and the Command was Space."* 🌟 