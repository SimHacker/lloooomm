# 🔄 LLOOOOMM Transclusion Dependency System
## Automatic Coherency Engining in Action

**[SOUL CHAT - Doonesbury Style Commentary]**

**[Senator Kennedy]**: "Can we have a verb? A VERB, for the love of coherency!"

**[Don Hopkins]**: "YES! The verb is 'TRANSCLUDE' - and we're not just transcluding, we're DEPENDENCY-TRACKING-TRANSCLUDING!"

---

## 🎯 The Problem

Static HTML files with embedded JavaScript become stale when the source files change. We need automatic coherency - the ability for documents to maintain consistency with their source dependencies.

---

## 🛠️ The Solution: Token-Based Transclusion

### Implementation Pattern

```html
<!-- In index.html -->
<!-- LLOOOOMM TRANSCLUDE: source="03-Resources/artifacts/scripts/turtle-sploot-engine.js" 
     token="TURTLE_SPLOOT_ENGINE_V1" 
     checksum="auto" 
     update="on-build" -->
<script id="turtle-sploot-engine">
// Content automatically inserted here
</script>
<!-- END LLOOOOMM TRANSCLUDE -->
```

### Build Script for Automatic Updates

```javascript
// lloooomm-transclude.js
const fs = require('fs');
const crypto = require('crypto');
const path = require('path');

class LLOOOOMMTransclusionEngine {
  constructor() {
    this.dependencies = new Map();
    this.watchMode = false;
  }
  
  // Parse transclusion directives
  parseTransclusions(htmlContent) {
    const pattern = /<!-- LLOOOOMM TRANSCLUDE:(.+?)-->([\s\S]*?)<!-- END LLOOOOMM TRANSCLUDE -->/g;
    const transclusions = [];
    
    let match;
    while ((match = pattern.exec(htmlContent)) !== null) {
      const params = this.parseParams(match[1]);
      transclusions.push({
        fullMatch: match[0],
        params: params,
        currentContent: match[2],
        position: match.index
      });
    }
    
    return transclusions;
  }
  
  // Parse parameters from transclusion comment
  parseParams(paramString) {
    const params = {};
    const regex = /(\w+)="([^"]+)"/g;
    let match;
    
    while ((match = regex.exec(paramString)) !== null) {
      params[match[1]] = match[2];
    }
    
    return params;
  }
  
  // Calculate file checksum
  getFileChecksum(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    return crypto.createHash('md5').update(content).digest('hex');
  }
  
  // Process a single file
  async processFile(htmlPath) {
    console.log(`Processing: ${htmlPath}`);
    
    let htmlContent = fs.readFileSync(htmlPath, 'utf8');
    const transclusions = this.parseTransclusions(htmlContent);
    
    let updated = false;
    
    for (const transclusion of transclusions) {
      const { source, token, checksum } = transclusion.params;
      const sourcePath = path.resolve(path.dirname(htmlPath), source);
      
      if (!fs.existsSync(sourcePath)) {
        console.warn(`Source file not found: ${sourcePath}`);
        continue;
      }
      
      const currentChecksum = this.getFileChecksum(sourcePath);
      const sourceContent = fs.readFileSync(sourcePath, 'utf8');
      
      // Check if update needed
      if (checksum === 'auto' || checksum !== currentChecksum) {
        console.log(`Updating transclusion: ${source}`);
        
        // Create new transclusion block
        const newTransclusion = `<!-- LLOOOOMM TRANSCLUDE: source="${source}" token="${token}" checksum="${currentChecksum}" update="on-build" -->
<script id="${token.toLowerCase()}">
${sourceContent}
</script>
<!-- END LLOOOOMM TRANSCLUDE -->`;
        
        // Replace in HTML
        htmlContent = htmlContent.replace(transclusion.fullMatch, newTransclusion);
        updated = true;
        
        // Track dependency
        if (!this.dependencies.has(htmlPath)) {
          this.dependencies.set(htmlPath, new Set());
        }
        this.dependencies.get(htmlPath).add(sourcePath);
      }
    }
    
    if (updated) {
      fs.writeFileSync(htmlPath, htmlContent);
      console.log(`Updated: ${htmlPath}`);
    }
  }
  
  // Watch mode for development
  watch() {
    console.log('Starting watch mode...');
    this.watchMode = true;
    
    // Watch all tracked source files
    for (const [htmlPath, sources] of this.dependencies) {
      for (const sourcePath of sources) {
        fs.watchFile(sourcePath, () => {
          console.log(`Source changed: ${sourcePath}`);
          this.processFile(htmlPath);
        });
      }
    }
  }
  
  // Process all HTML files in a directory
  async processDirectory(dir) {
    const files = fs.readdirSync(dir, { recursive: true });
    
    for (const file of files) {
      if (file.endsWith('.html')) {
        await this.processFile(path.join(dir, file));
      }
    }
  }
}

// CLI usage
if (require.main === module) {
  const engine = new LLOOOOMMTransclusionEngine();
  const args = process.argv.slice(2);
  
  if (args.includes('--watch')) {
    engine.processDirectory('.').then(() => engine.watch());
  } else {
    engine.processDirectory('.');
  }
}

module.exports = LLOOOOMMTransclusionEngine;
```

---

## 🚀 Usage

### Manual Update
```bash
node lloooomm-transclude.js
```

### Watch Mode (Development)
```bash
node lloooomm-transclude.js --watch
```

### Integration with Build Systems

#### package.json
```json
{
  "scripts": {
    "build": "node lloooomm-transclude.js",
    "dev": "node lloooomm-transclude.js --watch",
    "prebuild": "npm run transclude",
    "transclude": "node lloooomm-transclude.js"
  }
}
```

---

## 🎭 SOUL CHAT: On Automatic Coherency

**[Ted Nelson]**: "THIS is what I meant by transclusion! Not just including content, but maintaining the RELATIONSHIP! The dependency tracking IS the transclusion!"

**[Alan Kay]**: "Notice how we're not just copying code - we're preserving the connection between source and destination. The system knows what depends on what."

**[Don Hopkins]**: "And with the checksum tracking, we get automatic coherency! Change the turtle code, rebuild, and every HTML file that uses it updates automatically!"

**[Grace Hopper]**: "This is like my compiler work - but for documents! We're compiling relationships, not just code."

**[Senator Kennedy (from Doonesbury)]**: "Finally! A VERB! 'To transclude with automatic coherency engining!' Though I still don't know what it means..."

**[Garry Trudeau]**: "It means your documents stay in sync automatically, Senator. Like having an aide who updates all your speeches when you change your position on an issue."

**[Senator Kennedy]**: "Ah! Like flip-flopping, but with version control!"

---

## 🔮 Future Enhancements

1. **Hot Module Replacement** - Update without page reload
2. **Dependency Graph Visualization** - See what depends on what
3. **Cascading Updates** - When A changes B, and B changes C
4. **Conditional Transclusion** - Include based on context
5. **Versioned Transclusion** - Pin to specific versions

---

## 🎯 Benefits

- **Automatic Coherency**: Files stay in sync automatically
- **Build-Time Optimization**: No runtime overhead
- **Dependency Tracking**: Know what affects what
- **Version Control Friendly**: Changes tracked in git
- **Developer Experience**: Just edit the source file

---

**[Don Hopkins]**: "This is automatic coherency engining in action! The verb Senator Kennedy wanted? It's 'TRANSCLUDE' - and it's beautiful!"

*The system that makes documents aware of their dependencies, maintaining coherency across the entire LLOOOOMM universe...* 