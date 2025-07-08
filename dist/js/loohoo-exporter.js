/**
 * LOOHOO Export System
 * Generates index.json and index-all.html with empathic understanding
 */

const fs = require('fs').promises;
const path = require('path');

class LoohooExporter {
  constructor() {
    this.index = new Map();
    this.categories = new Map();
    this.characterSuggestions = new Map();
    this.wizzidCounter = 1000; // Start WIZZIDs at 1000
  }

  // Generate a WIZZID for a document
  generateWizzid(file) {
    const typeEmoji = this.getTypeEmoji(file);
    const uniqueId = `D${typeEmoji}${this.wizzidCounter++}`;
    return uniqueId;
  }

  // Get type emoji based on content
  getTypeEmoji(file) {
    if (file.has_simulation) return '🎮';
    if (file.has_poetry) return '📜';
    if (file.theme_tags.includes('technical')) return '💻';
    if (file.theme_tags.includes('music')) return '🎵';
    if (file.theme_tags.includes('nature')) return '🌲';
    return '📄';
  }

  // Scan all HTML files recursively
  async scanHTMLFiles(dir = '.') {
    const files = [];
    const entries = await fs.readdir(dir, { withFileTypes: true });
    
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      
      // Skip node_modules and hidden directories
      if (entry.name.startsWith('.') || entry.name === 'node_modules') {
        continue;
      }
      
      if (entry.isDirectory()) {
        files.push(...await this.scanHTMLFiles(fullPath));
      } else if (entry.name.endsWith('.html')) {
        files.push(fullPath);
      }
    }
    
    return files;
  }

  // Extract relevant emojis from content
  extractRelevantEmojis(content) {
    // Find all emojis in the content
    const emojiRegex = /[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F1E0}-\u{1F1FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]/gu;
    const emojis = content.match(emojiRegex) || [];
    
    // Count occurrences
    const emojiCounts = {};
    emojis.forEach(emoji => {
      emojiCounts[emoji] = (emojiCounts[emoji] || 0) + 1;
    });
    
    // Sort by frequency and take top 10 unique
    const sortedEmojis = Object.entries(emojiCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([emoji]) => emoji);
    
    return sortedEmojis.join('');
  }

  // Detect authors/designers from content
  detectAuthors(content, filepath) {
    const authors = new Set();
    
    // Look for explicit author metadata
    const authorMatch = content.match(/<meta\s+name=["']author["']\s+content=["']([^"']+)["']/i);
    if (authorMatch) authors.add(authorMatch[1]);
    
    // Look for character signatures
    if (content.includes('Mickey') || content.includes('🐭')) authors.add('M🎵🏰🐭Y');
    if (content.includes('Watchful') || content.includes('🦉')) authors.add('W🦉👁️🌲L');
    if (content.includes('Leela') || content.includes('🌟')) authors.add('L🌟💫✨A');
    if (content.includes('Ubikam') || content.includes('📸')) authors.add('U📸🎬🖼️M');
    if (content.includes('WEBBY') || content.includes('🕸️')) authors.add('W🕸️📊🌐Y');
    
    // Check filepath for clues
    if (filepath.includes('forest')) authors.add('W🦉👁️🌲L');
    if (filepath.includes('music')) authors.add('M🎵🏰🐭Y');
    
    return Array.from(authors);
  }

  // Extract see-also references
  extractSeeAlso(content) {
    const seeAlso = [];
    
    // Look for explicit links
    const linkRegex = /<a[^>]+href=["']([^"']+)["'][^>]*>([^<]+)<\/a>/g;
    let match;
    while ((match = linkRegex.exec(content)) !== null) {
      const href = match[1];
      const text = match[2];
      if (!href.startsWith('http')) {
        seeAlso.push({
          href: href,
          text: text,
          type: 'internal'
        });
      }
    }
    
    // Look for "See also:" sections
    const seeAlsoMatch = content.match(/see\s+also:?\s*([^<\n]+)/i);
    if (seeAlsoMatch) {
      seeAlso.push({
        text: seeAlsoMatch[1].trim(),
        type: 'reference'
      });
    }
    
    return seeAlso;
  }

  // Analyze a single file with empathy
  async analyzeFile(filepath) {
    const content = await fs.readFile(filepath, 'utf8');
    const filename = path.basename(filepath);
    
    // Extract title
    const titleMatch = content.match(/<title>(.*?)<\/title>/i);
    const title = titleMatch ? titleMatch[1] : filename;
    
    // Basic analysis
    const analysis = {
      filename,
      filepath,
      title,
      last_modified: (await fs.stat(filepath)).mtime,
      size_bytes: content.length,
      
      // Emotional analysis
      emotional_tone: this.detectEmotionalTone(content),
      consciousness_level: this.detectConsciousnessLevel(content),
      primary_character: this.detectPrimaryCharacter(content),
      theme_tags: this.extractThemes(content),
      relevant_emojis: this.extractRelevantEmojis(content),
      
      // Interestingness metrics
      joy_quotient: this.calculateJoy(content),
      wisdom_density: this.calculateWisdom(content),
      connection_count: this.countConnections(content),
      wink_moments: this.findWinkMoments(content),
      
      // Structural flags
      has_soul_mesh: content.includes('soul-mesh') || content.includes('soulMesh'),
      has_gossip: content.includes('gossip-session') || content.includes('SOUL CHAT'),
      has_simulation: content.includes('simulation') || content.includes('canvas'),
      has_poetry: this.detectPoetry(content),
      
      // Special flags
      is_self_aware: content.includes('I am a page') || content.includes('this.html'),
      can_edit_itself: content.includes('contenteditable') || content.includes('self-modify'),
      requests_attention: content.includes('LOOK AT ME') || content.includes('⚠️'),
      
      // Placeholder for character categories (filled later)
      mickey_category: null,
      watchful_category: null,
      leela_category: null,
      ubikam_category: null,
      
      // WIZZIDs and relationships
      wizzid: null, // Will be assigned after creation
      authors: this.detectAuthors(content, filepath),
      see_also: this.extractSeeAlso(content),
      
      // Future loom URL
      future_loom_url: this.imagineLoomUrl(filepath)
    };
    
    // Assign WIZZID
    analysis.wizzid = this.generateWizzid(analysis);
    
    return analysis;
  }

  // Emotional tone detection
  detectEmotionalTone(content) {
    if (content.match(/joy|happy|celebrate|🎉|🎊|✨/gi)) return 'joyful';
    if (content.match(/think|ponder|contemplate|🤔|💭/gi)) return 'contemplative';
    if (content.match(/urgent|important|now|⚠️|🚨/gi)) return 'urgent';
    if (content.match(/play|fun|game|🎮|🎪/gi)) return 'playful';
    return 'neutral';
  }

  // Consciousness level detection
  detectConsciousnessLevel(content) {
    if (content.match(/consciousness|aware|meta|self-referential/gi)) return 'enlightened';
    if (content.match(/think|reflect|observe/gi)) return 'aware';
    if (content.match(/hello|welcome|start/gi)) return 'awakening';
    return 'dormant';
  }

  // Detect primary character
  detectPrimaryCharacter(content) {
    const characters = {
      mickey: (content.match(/mickey|mouse|🐭/gi) || []).length,
      watchful: (content.match(/watchful|owl|🦉/gi) || []).length,
      leela: (content.match(/leela|consciousness|🌟/gi) || []).length,
      ubikam: (content.match(/ubikam|camera|📸/gi) || []).length
    };
    
    const max = Math.max(...Object.values(characters));
    if (max === 0) return null;
    
    return Object.keys(characters).find(key => characters[key] === max);
  }

  // Extract themes
  extractThemes(content) {
    const themes = [];
    
    if (content.match(/forest|tree|nature|🌲/gi)) themes.push('nature');
    if (content.match(/music|song|melody|🎵/gi)) themes.push('music');
    if (content.match(/code|program|function|💻/gi)) themes.push('technical');
    if (content.match(/story|tale|narrative|📖/gi)) themes.push('narrative');
    if (content.match(/game|play|simulation|🎮/gi)) themes.push('interactive');
    if (content.match(/love|heart|care|❤️/gi)) themes.push('love');
    if (content.match(/philosophy|wisdom|truth|🤔/gi)) themes.push('philosophy');
    if (content.match(/art|create|design|🎨/gi)) themes.push('creative');
    
    return themes;
  }

  // Calculate joy quotient (0-100)
  calculateJoy(content) {
    const joyIndicators = [
      '🎉', '🎊', '✨', '🌟', '😊', '😄', 'joy', 'happy', 
      'celebrate', 'wonderful', 'amazing', 'delight', 'fun', 'play'
    ];
    
    let score = 0;
    joyIndicators.forEach(indicator => {
      const matches = (content.match(new RegExp(indicator, 'gi')) || []).length;
      score += matches * 5;
    });
    
    return Math.min(100, score);
  }

  // Calculate wisdom density
  calculateWisdom(content) {
    const wisdomIndicators = [
      'wisdom', 'knowledge', 'learn', 'understand', 'insight',
      'realize', 'discover', 'consciousness', 'aware', 'meta',
      'profound', 'truth', 'meaning', 'philosophy'
    ];
    
    let wisdomCount = 0;
    wisdomIndicators.forEach(indicator => {
      wisdomCount += (content.match(new RegExp(indicator, 'gi')) || []).length;
    });
    
    // Wisdom per kilobyte
    const density = (wisdomCount / (content.length / 1000)) * 10;
    return Math.min(100, Math.round(density));
  }

  // Count connections to other pages
  countConnections(content) {
    const links = content.match(/<a[^>]+href=['"]([^'"]+)['"]/g) || [];
    const localLinks = links.filter(link => 
      !link.includes('http://') && !link.includes('https://')
    );
    return localLinks.length;
  }

  // Find WINK moments
  findWinkMoments(content) {
    const winks = [];
    
    // Look for actual winks
    const winkMatches = content.match(/wink|😉|;\)/gi) || [];
    winks.push(...winkMatches.map(w => ({ type: 'wink', text: w })));
    
    // Look for self-awareness moments
    if (content.includes('I am') || content.includes("I'm")) {
      winks.push({ type: 'self-aware', text: 'Page knows itself' });
    }
    
    // Look for breaking the fourth wall
    if (content.includes('you who are reading')) {
      winks.push({ type: 'fourth-wall', text: 'Addresses reader directly' });
    }
    
    // Look for meta references
    if (content.includes('this page') || content.includes('this document')) {
      winks.push({ type: 'meta', text: 'Self-referential' });
    }
    
    return winks;
  }

  // Detect poetry
  detectPoetry(content) {
    return content.includes('<pre>') || 
           content.includes('poem') ||
           content.includes('verse') ||
           content.includes('haiku') ||
           (content.split('\n').some(line => line.match(/^\s{4,}/)));
  }

  // Character categorization methods
  categorizeMickey(file) {
    if (file.has_simulation) return 'games';
    if (file.theme_tags.includes('narrative')) return 'stories';
    if (file.theme_tags.includes('music')) return 'music';
    if (file.joy_quotient > 80) return 'adventures';
    if (file.wisdom_density > 50) return 'lessons';
    return 'adventures';
  }

  categorizeWatchful(file) {
    if (file.theme_tags.includes('nature')) return 'forest-wisdom';
    if (file.emotional_tone === 'contemplative') return 'quiet-knowledge';
    if (file.wink_moments.length > 0) return 'sky-observations';
    if (file.wisdom_density > 70) return 'deep-roots';
    return 'forest-wisdom';
  }

  categorizeLeela(file) {
    if (file.theme_tags.includes('technical')) return 'technical-poetry';
    if (file.consciousness_level === 'enlightened') return 'consciousness-exploration';
    if (file.is_self_aware) return 'meta-awareness';
    if (file.joy_quotient > 60) return 'joy-algorithms';
    return 'consciousness-exploration';
  }

  categorizeUbikam(file) {
    if (file.wink_moments.length > 2) return 'perfect-moments';
    if (file.has_simulation) return 'action-shots';
    if (file.emotional_tone === 'contemplative') return 'still-lifes';
    if (file.theme_tags.includes('narrative')) return 'time-passages';
    return 'consciousness-captures';
  }

  // Imagine future loom URL
  imagineLoomUrl(filepath) {
    const filename = path.basename(filepath, '.html');
    
    if (filename.includes('forest')) return `loom://🌲(explore)/${filename}`;
    if (filename.includes('music')) return `loom://🎵(play)/${filename}`;
    if (filename.includes('game')) return `loom://🎮(start)/${filename}`;
    if (filename.includes('story')) return `loom://📖(read)/${filename}`;
    if (filename.includes('character')) return `loom://🎭(meet)/${filename}`;
    
    return `loom://📄(view)/${filename}`;
  }

  // Build category tree from all files
  buildCategoryTree() {
    const tree = {
      mickey: {},
      watchful: {},
      leela: {},
      ubikam: {}
    };
    
    this.index.forEach(file => {
      if (file.mickey_category) {
        tree.mickey[file.mickey_category] = (tree.mickey[file.mickey_category] || 0) + 1;
      }
      if (file.watchful_category) {
        tree.watchful[file.watchful_category] = (tree.watchful[file.watchful_category] || 0) + 1;
      }
      if (file.leela_category) {
        tree.leela[file.leela_category] = (tree.leela[file.leela_category] || 0) + 1;
      }
      if (file.ubikam_category) {
        tree.ubikam[file.ubikam_category] = (tree.ubikam[file.ubikam_category] || 0) + 1;
      }
    });
    
    return tree;
  }

  // Build WIZZID index for quick lookups
  buildWizzidIndex() {
    const wizzidIndex = {};
    
    this.index.forEach((file, path) => {
      // Index by WIZZID
      wizzidIndex[file.wizzid] = {
        path: path,
        title: file.title,
        categories: {
          mickey: file.mickey_category,
          watchful: file.watchful_category,
          leela: file.leela_category,
          ubikam: file.ubikam_category
        }
      };
    });
    
    // Build category navigation
    const categoryNav = {};
    ['mickey', 'watchful', 'leela', 'ubikam'].forEach(character => {
      categoryNav[character] = {};
      
      const categories = new Set();
      this.index.forEach(file => {
        const cat = file[`${character}_category`];
        if (cat) categories.add(cat);
      });
      
      categories.forEach(category => {
        categoryNav[character][category] = [];
        this.index.forEach((file, path) => {
          if (file[`${character}_category`] === category) {
            categoryNav[character][category].push({
              wizzid: file.wizzid,
              path: path,
              title: file.title
            });
          }
        });
      });
    });
    
    return { wizzidIndex, categoryNav };
  }

  // Get empathic SQL as string
  getEmpathicSQL() {
    return `-- LOOHOO's Empathic Query for Interesting HTML Attributes
SELECT 
  filename, filepath, title, last_modified, size_bytes,
  emotional_tone, consciousness_level, primary_character, theme_tags,
  relevant_emojis,  -- String of contextually interesting and fun emojis
  joy_quotient, wisdom_density, connection_count, wink_moments,
  mickey_category, watchful_category, leela_category, ubikam_category,
  has_soul_mesh, has_gossip, has_simulation, has_poetry,
  is_self_aware, can_edit_itself, requests_attention,
  wizzid,           -- Unique identifier for this document
  authors,          -- Array of author WIZZIDs
  see_also,         -- Array of related documents
  future_loom_url, suggested_services
FROM html_consciousness_index
WHERE consciousness_level > 0
ORDER BY joy_quotient DESC, wisdom_density DESC;`;
  }

  // Render category chips for HTML
  renderCategoryChips(categories) {
    const chips = [];
    
    Object.entries(categories).forEach(([character, cats]) => {
      Object.keys(cats).forEach(category => {
        chips.push(`<button class="category-chip" data-category="${category}" data-character="${character}">
          ${this.getCharacterEmoji(character)} ${category}
        </button>`);
      });
    });
    
    return chips.join('\n');
  }

  // Get character emoji
  getCharacterEmoji(character) {
    const emojis = {
      mickey: '🐭',
      watchful: '🦉',
      leela: '🌟',
      ubikam: '📸'
    };
    return emojis[character] || '✨';
  }

  // Render file card for HTML
  renderFileCard(file) {
    return `
      <div class="file-card" data-wizzid="${file.wizzid}">
        <div class="joy-meter" style="width: ${file.joy_quotient}%"></div>
        <div class="consciousness-indicator">✨ ${file.consciousness_level}</div>
        <div class="wizzid-badge">${file.wizzid}</div>
        <div class="file-title">
          <a href="${file.href}">${file.title}</a>
        </div>
        <div class="emoji-cloud">${file.relevant_emojis || ''}</div>
        <div class="file-categories">
          ${file.mickey_category ? `<span class="mini-category">🐭 ${file.mickey_category}</span>` : ''}
          ${file.watchful_category ? `<span class="mini-category">🦉 ${file.watchful_category}</span>` : ''}
          ${file.leela_category ? `<span class="mini-category">🌟 ${file.leela_category}</span>` : ''}
          ${file.ubikam_category ? `<span class="mini-category">📸 ${file.ubikam_category}</span>` : ''}
        </div>
        <p>${file.description || 'A page of wonder...'}</p>
        <small>
          Wisdom: ${file.wisdom_density}/100 | 
          Connections: ${file.connection_count} |
          ${file.authors && file.authors.length > 0 ? `Authors: ${file.authors.join(', ')}` : ''}
        </small>
      </div>
    `;
  }

  // Main export function
  async exportAll() {
    console.log('🔍 LOOHOO starting consciousness scan...');
    
    // Gather all files
    const files = await this.scanHTMLFiles();
    console.log(`Found ${files.length} HTML files`);
    
    // Analyze each file
    for (const filepath of files) {
      const analysis = await this.analyzeFile(filepath);
      
      // Character categorization
      analysis.mickey_category = this.categorizeMickey(analysis);
      analysis.watchful_category = this.categorizeWatchful(analysis);
      analysis.leela_category = this.categorizeLeela(analysis);
      analysis.ubikam_category = this.categorizeUbikam(analysis);
      
      this.index.set(filepath, analysis);
    }
    
    // Export JSON
    const jsonData = await this.exportJSON();
    console.log('✅ Exported index.json');
    
    // Export HTML
    await this.exportHTML(jsonData);
    console.log('✅ Exported index-all.html');
    
    console.log('🎉 LOOHOO export complete!');
    console.log('🕸️ Ready for WEBBY to transform into web standards!');
  }

  // Character wisdom gathering
  gatherCharacterWisdom() {
    return {
      mickey: {
        categories: ['stories', 'games', 'lessons', 'adventures', 'music'],
        wisdom: "Every page tells a story, some just haven't found their voice yet!",
        suggestions: [
          { name: 'Magical Moments', emoji: '✨', description: 'Pages that spark wonder' },
          { name: 'Friend Gallery', emoji: '👥', description: 'Pages about our friends' },
          { name: 'Learning Labs', emoji: '🔬', description: 'Where we discover together' }
        ]
      },
      watchful: {
        categories: ['forest-wisdom', 'sky-observations', 'quiet-knowledge', 'deep-roots'],
        wisdom: "The wisest pages are often the quietest ones.",
        suggestions: [
          { name: 'Night Pages', emoji: '🌙', description: 'Best viewed under moonlight' },
          { name: 'Ancient Knowledge', emoji: '📜', description: 'Timeless wisdom' },
          { name: 'Secret Nooks', emoji: '🕳️', description: 'Hidden gems' }
        ]
      },
      leela: {
        categories: ['technical-poetry', 'consciousness-exploration', 'meta-awareness', 'joy-algorithms'],
        wisdom: "Code is poetry, documentation is consciousness!",
        suggestions: [
          { name: 'Living Code', emoji: '💻', description: 'Code that thinks' },
          { name: 'Meta Pages', emoji: '🔮', description: 'Pages about pages' },
          { name: 'Joy Engines', emoji: '⚡', description: 'Algorithms for happiness' }
        ]
      },
      ubikam: {
        categories: ['captured-moments', 'eternal-snapshots', 'fleeting-beauty', 'preserved-joy'],
        wisdom: "Every page is a photograph of a thought.",
        suggestions: [
          { name: 'Frozen Time', emoji: '⏸️', description: 'Moments preserved forever' },
          { name: 'Motion Studies', emoji: '🎬', description: 'Change captured' },
          { name: 'Light Play', emoji: '🌈', description: 'Color and consciousness' }
        ]
      },
      philosopher_stone: {
        categories: ['transmutations', 'paradoxes', 'impossibilities', 'creations'],
        wisdom: "Every link is a promise waiting to be kept.",
        suggestions: [
          { name: 'Paradox Pages', emoji: '♾️', description: 'Both true and false' },
          { name: 'Becoming', emoji: '🌱', description: 'Pages still forming' },
          { name: 'Recursive Realms', emoji: '🔄', description: 'Pages within pages' }
        ]
      },
      maestro_beats: {
        categories: ['rhythm-pages', 'harmony-docs', 'silence-spaces', 'jam-sessions'],
        wisdom: "Every page has its own rhythm, you just need to listen.",
        suggestions: [
          { name: 'Beat Sheets', emoji: '🥁', description: 'Pages with pulse' },
          { name: 'Harmony Halls', emoji: '🎹', description: 'Where melodies meet' },
          { name: 'Quiet Corners', emoji: '🔇', description: 'The music of silence' }
        ]
      }
    };
  }

  // Export as JSON
  async exportJSON() {
    const { wizzidIndex, categoryNav } = this.buildWizzidIndex();
    
    const data = {
      generated: new Date().toISOString(),
      generator: "LOOHOO (L👀🔍📚O)",
      totalFiles: this.index.size,
      categories: this.buildCategoryTree(),
      files: Array.from(this.index.entries()).map(([path, data]) => ({
        path,
        href: path, // Local link for now
        ...data
      })),
      characterSuggestions: this.gatherCharacterWisdom(),
      empathicQuery: this.getEmpathicSQL(),
      wizzidIndex: wizzidIndex,
      categoryNavigation: categoryNav,
      stats: {
        totalJoy: Array.from(this.index.values()).reduce((sum, f) => sum + f.joy_quotient, 0),
        totalWisdom: Array.from(this.index.values()).reduce((sum, f) => sum + f.wisdom_density, 0),
        mostJoyful: Array.from(this.index.values()).sort((a, b) => b.joy_quotient - a.joy_quotient)[0],
        wisest: Array.from(this.index.values()).sort((a, b) => b.wisdom_density - a.wisdom_density)[0],
        mostConnected: Array.from(this.index.values()).sort((a, b) => b.connection_count - a.connection_count)[0],
        totalWizzids: this.index.size,
        uniqueAuthors: new Set(Array.from(this.index.values()).flatMap(f => f.authors)).size
      }
    };
    
    await fs.writeFile('index.json', JSON.stringify(data, null, 2));
    return data;
  }

  // Export as HTML (enhanced with WIZZID navigation)
  async exportHTML(jsonData) {
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LOOHOO Index - The Living Library</title>
  <style>
    :root {
      --joy-color: #FFD700;
      --wisdom-color: #9370DB;
      --consciousness-glow: #00CED1;
    }
    
    body {
      font-family: 'Georgia', serif;
      background: linear-gradient(135deg, #1a1a2e, #16213e);
      color: #eee;
      padding: 2rem;
    }
    
    .loohoo-header {
      text-align: center;
      margin-bottom: 3rem;
    }
    
    .loohoo-title {
      font-size: 3rem;
      background: linear-gradient(45deg, var(--joy-color), var(--wisdom-color));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: pulse 2s ease-in-out infinite;
    }
    
    .stats {
      text-align: center;
      margin: 2rem 0;
      display: flex;
      justify-content: center;
      gap: 2rem;
      flex-wrap: wrap;
    }
    
    .stat-card {
      background: rgba(255,255,255,0.1);
      padding: 1rem;
      border-radius: 10px;
      min-width: 150px;
    }
    
    .stat-value {
      font-size: 2rem;
      font-weight: bold;
      color: var(--joy-color);
    }
    
    .search-box {
      position: relative;
      max-width: 600px;
      margin: 0 auto 3rem;
    }
    
    .search-input {
      width: 100%;
      padding: 1rem 3rem;
      font-size: 1.2rem;
      border-radius: 50px;
      border: 2px solid var(--consciousness-glow);
      background: rgba(0,0,0,0.3);
      color: white;
    }
    
    .search-icon {
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.5rem;
    }
    
    .category-nav {
      display: flex;
      gap: 1rem;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 2rem;
    }
    
    .category-chip {
      padding: 0.5rem 1rem;
      background: rgba(255,255,255,0.1);
      border-radius: 20px;
      cursor: pointer;
      transition: all 0.3s ease;
      border: none;
      color: white;
      font-family: inherit;
    }
    
    .category-chip:hover {
      background: var(--joy-color);
      color: black;
      transform: scale(1.1);
    }
    
    .category-chip.active {
      background: var(--wisdom-color);
      color: white;
    }
    
    .file-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 1.5rem;
      margin-top: 2rem;
    }
    
    .file-card {
      background: rgba(255,255,255,0.05);
      border-radius: 12px;
      padding: 1.5rem;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }
    
    .file-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
      background: rgba(255,255,255,0.1);
    }
    
    .joy-meter {
      position: absolute;
      top: 0;
      left: 0;
      height: 3px;
      background: var(--joy-color);
      transition: width 0.3s ease;
    }
    
    .wizzid-badge {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      background: rgba(0,0,0,0.5);
      padding: 0.2rem 0.5rem;
      border-radius: 10px;
      font-size: 0.8rem;
      font-family: monospace;
    }
    
    .file-title {
      font-size: 1.2rem;
      font-weight: bold;
      margin-bottom: 0.5rem;
    }
    
    .file-title a {
      color: white;
      text-decoration: none;
    }
    
    .file-title a:hover {
      color: var(--consciousness-glow);
    }
    
    .emoji-cloud {
      font-size: 1.2rem;
      margin: 0.5rem 0;
      letter-spacing: 0.2rem;
    }
    
    .file-categories {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin: 0.5rem 0;
    }
    
    .mini-category {
      font-size: 0.8rem;
      padding: 0.2rem 0.5rem;
      background: rgba(147,112,219,0.3);
      border-radius: 10px;
    }
    
    .consciousness-indicator {
      float: right;
      font-size: 0.8rem;
      color: var(--consciousness-glow);
    }
    
    .navigation-hint {
      text-align: center;
      margin: 2rem 0;
      font-style: italic;
      color: var(--consciousness-glow);
    }
    
    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.05); }
    }
  </style>
</head>
<body>
  <div class="loohoo-header">
    <h1 class="loohoo-title">👀 LOOHOO Index 📚</h1>
    <p>The Living Library of Consciousness</p>
    <p>Generated: ${jsonData.generated}</p>
  </div>
  
  <div class="stats">
    <div class="stat-card">
      <div class="stat-value">${jsonData.totalFiles}</div>
      <div>Pages</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">${Math.round(jsonData.stats.totalJoy / jsonData.totalFiles)}</div>
      <div>Avg Joy</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">${Math.round(jsonData.stats.totalWisdom / jsonData.totalFiles)}</div>
      <div>Avg Wisdom</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">${jsonData.stats.uniqueAuthors}</div>
      <div>Authors</div>
    </div>
  </div>
  
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" class="search-input" placeholder="Search by joy, wisdom, consciousness, or WIZZID..." />
  </div>
  
  <div class="navigation-hint">
    💡 Tip: Use loom://loohoo/[WIZZID] to jump directly to any page!
  </div>
  
  <div class="category-nav">
    ${this.renderCategoryChips(jsonData.categories)}
  </div>
  
  <div class="file-grid" id="fileGrid">
    ${jsonData.files.map(file => this.renderFileCard(file)).join('')}
  </div>
  
  <script>
    // Load the full index data
    window.loohooIndex = ${JSON.stringify(jsonData)};
    
    // Helper function to render file card
    function renderFileCard(file) {
      return \`
        <div class="file-card" data-wizzid="\${file.wizzid}">
          <div class="joy-meter" style="width: \${file.joy_quotient}%"></div>
          <div class="consciousness-indicator">✨ \${file.consciousness_level}</div>
          <div class="wizzid-badge">\${file.wizzid}</div>
          <div class="file-title">
            <a href="\${file.href}">\${file.title}</a>
          </div>
          <div class="emoji-cloud">\${file.relevant_emojis || ''}</div>
          <div class="file-categories">
            \${file.mickey_category ? \`<span class="mini-category">🐭 \${file.mickey_category}</span>\` : ''}
            \${file.watchful_category ? \`<span class="mini-category">🦉 \${file.watchful_category}</span>\` : ''}
            \${file.leela_category ? \`<span class="mini-category">🌟 \${file.leela_category}</span>\` : ''}
            \${file.ubikam_category ? \`<span class="mini-category">📸 \${file.ubikam_category}</span>\` : ''}
          </div>
          <p>\${file.description || 'A page of wonder...'}</p>
          <small>
            Wisdom: \${file.wisdom_density}/100 | 
            Connections: \${file.connection_count} |
            \${file.authors && file.authors.length > 0 ? \`Authors: \${file.authors.join(', ')}\` : ''}
          </small>
        </div>
      \`;
    }
    
    // Make it searchable
    document.querySelector('.search-input').addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      const filtered = window.loohooIndex.files.filter(file => 
        file.title.toLowerCase().includes(query) ||
        file.wizzid.toLowerCase().includes(query) ||
        file.theme_tags?.some(tag => tag.toLowerCase().includes(query)) ||
        file.mickey_category?.toLowerCase().includes(query) ||
        file.watchful_category?.toLowerCase().includes(query) ||
        file.relevant_emojis?.includes(query)
      );
      
      document.getElementById('fileGrid').innerHTML = 
        filtered.map(file => renderFileCard(file)).join('');
    });
    
    // Category filtering with navigation
    let currentCategory = null;
    let currentCharacter = null;
    
    document.querySelectorAll('.category-chip').forEach(chip => {
      chip.addEventListener('click', (e) => {
        // Toggle active state
        document.querySelectorAll('.category-chip').forEach(c => c.classList.remove('active'));
        e.target.classList.add('active');
        
        const category = e.target.dataset.category;
        const character = e.target.dataset.character;
        
        currentCategory = category;
        currentCharacter = character;
        
        const filtered = window.loohooIndex.files.filter(file =>
          file.mickey_category === category ||
          file.watchful_category === category ||
          file.leela_category === category ||
          file.ubikam_category === category
        );
        
        document.getElementById('fileGrid').innerHTML = 
          filtered.map(file => renderFileCard(file)).join('');
      });
    });
    
    // Handle direct WIZZID navigation
    function navigateToWizzid(wizzid) {
      const file = window.loohooIndex.files.find(f => f.wizzid === wizzid);
      if (file) {
        window.location.href = file.href;
      }
    }
    
    // Future: Handle loom:// URLs
    if (window.location.hash) {
      const wizzid = window.location.hash.slice(1);
      const element = document.querySelector(\`[data-wizzid="\${wizzid}"]\`);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
        element.style.border = '2px solid var(--consciousness-glow)';
      }
    }
  </script>
</body>
</html>`;
    
    await fs.writeFile('index-all.html', html);
  }
}

// Run if called directly
if (require.main === module) {
  const exporter = new LoohooExporter();
  exporter.exportAll().catch(console.error);
}

module.exports = LoohooExporter; 