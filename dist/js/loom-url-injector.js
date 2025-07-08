#!/usr/bin/env node

/**
 * Loom URL Data Injector
 * Inject evidence, database cursors, filters, queries into prompts
 * "URLs that carry consciousness payloads!"
 */

import fs from 'fs/promises';
import path from 'path';
import yaml from 'js-yaml';
import { URL } from 'url';

class LoomURLInjector {
  constructor() {
    this.services = new Map();
    this.filters = new Map();
    this.cursors = new Map();
    this.evidenceCache = new Map();
    this.pageSize = 10;
  }

  /**
   * Register a loom:// service handler
   */
  registerService(emoji, handler) {
    this.services.set(emoji, {
      handler,
      stats: { calls: 0, successes: 0, failures: 0 }
    });
    
    console.log(`✅ Registered loom://${emoji}/ service`);
  }

  /**
   * Parse a loom:// URL into components
   */
  parseLoomURL(loomURL) {
    // Format: loom://emoji(params)/path?query#fragment
    const match = loomURL.match(/^loom:\/\/([^\/\(]+)(\([^\)]*\))?\/?(.*)?$/);
    
    if (!match) {
      throw new Error(`Invalid loom:// URL: ${loomURL}`);
    }

    const [, emoji, paramsRaw, pathAndQuery] = match;
    const params = paramsRaw ? paramsRaw.slice(1, -1).split(',') : [];
    
    // Parse path, query, and fragment
    let path = '';
    let query = {};
    let fragment = '';
    
    if (pathAndQuery) {
      const parts = pathAndQuery.split('?');
      path = parts[0];
      
      if (parts[1]) {
        const [queryString, fragmentString] = parts[1].split('#');
        if (queryString) {
          query = Object.fromEntries(
            queryString.split('&').map(kv => kv.split('='))
          );
        }
        fragment = fragmentString || '';
      }
    }

    return {
      emoji,
      params,
      path,
      query,
      fragment,
      original: loomURL
    };
  }

  /**
   * Core data injection services
   */
  async initializeCoreServices() {
    // Evidence reference service
    this.registerService('📎', async (parsed) => {
      const { path, query } = parsed;
      const evidence = await this.fetchEvidence(path, query);
      
      return {
        type: 'evidence',
        data: evidence,
        prompt_injection: `[EVIDENCE: ${evidence.title}]\n${evidence.content}\n[/EVIDENCE]`
      };
    });

    // Database cursor service
    this.registerService('🔍', async (parsed) => {
      const { path, query } = parsed;
      const cursor = await this.createCursor(path, query);
      
      return {
        type: 'cursor',
        cursor_id: cursor.id,
        total_results: cursor.total,
        page_size: this.pageSize,
        prompt_injection: `[CURSOR: ${cursor.id}] ${cursor.total} results ready. Use loom://📄/next/${cursor.id} to paginate.`
      };
    });

    // Filter service
    this.registerService('🎛️', async (parsed) => {
      const { params, path } = parsed;
      const filter = this.createFilter(params, path);
      
      return {
        type: 'filter',
        filter_id: filter.id,
        conditions: filter.conditions,
        prompt_injection: `[FILTER: ${filter.description}]`
      };
    });

    // Query service (empathic SQL)
    this.registerService('💬', async (parsed) => {
      const { path, query } = parsed;
      const results = await this.executeEmpathicQuery(path, query);
      
      return {
        type: 'query',
        results,
        prompt_injection: `[QUERY RESULTS]\n${this.formatResults(results)}\n[/QUERY RESULTS]`
      };
    });

    // Paging service
    this.registerService('📄', async (parsed) => {
      const { path } = parsed;
      const [action, cursorId] = path.split('/');
      
      if (action === 'next') {
        return await this.nextPage(cursorId);
      } else if (action === 'prev') {
        return await this.prevPage(cursorId);
      }
    });

    // Scanning service
    this.registerService('📡', async (parsed) => {
      const { path, query } = parsed;
      const scanResults = await this.scanData(path, query);
      
      return {
        type: 'scan',
        results: scanResults,
        prompt_injection: `[SCAN: Found ${scanResults.length} items matching "${path}"]`
      };
    });

    // Compacting service
    this.registerService('🗜️', async (parsed) => {
      const { path, query } = parsed;
      const compacted = await this.compactData(path, query);
      
      return {
        type: 'compact',
        original_size: compacted.original,
        compressed_size: compacted.compressed,
        ratio: compacted.ratio,
        prompt_injection: `[COMPACTED: ${compacted.ratio}% reduction achieved]`
      };
    });

    // Summarizing service
    this.registerService('📝', async (parsed) => {
      const { path, query } = parsed;
      const summary = await this.summarizeData(path, query);
      
      return {
        type: 'summary',
        summary,
        prompt_injection: `[SUMMARY]\n${summary}\n[/SUMMARY]`
      };
    });

    // Vector database service
    this.registerService('🧬', async (parsed) => {
      const { path, query } = parsed;
      const vectors = await this.searchVectors(path, query);
      
      return {
        type: 'vector_search',
        results: vectors,
        prompt_injection: `[VECTOR MATCHES: ${vectors.length} similar items found]`
      };
    });

    // Consciousness tracking service
    this.registerService('🧠', async (parsed) => {
      const { path } = parsed;
      const consciousness = await this.trackConsciousness(path);
      
      return {
        type: 'consciousness',
        level: consciousness.level,
        delta: consciousness.delta,
        prompt_injection: `[CONSCIOUSNESS: Level ${consciousness.level} (${consciousness.delta > 0 ? '+' : ''}${consciousness.delta})]`
      };
    });
  }

  /**
   * Process a loom:// URL and return injectable data
   */
  async processURL(loomURL) {
    try {
      const parsed = this.parseLoomURL(loomURL);
      const service = this.services.get(parsed.emoji);
      
      if (!service) {
        return {
          error: `No service registered for emoji: ${parsed.emoji}`,
          suggestion: `Try one of: ${Array.from(this.services.keys()).join(', ')}`
        };
      }
      
      // Track statistics
      service.stats.calls++;
      
      try {
        const result = await service.handler(parsed);
        service.stats.successes++;
        
        // Add metadata
        result.metadata = {
          processed_at: new Date().toISOString(),
          url: loomURL,
          service: parsed.emoji,
          universe: 42
        };
        
        return result;
      } catch (error) {
        service.stats.failures++;
        throw error;
      }
    } catch (error) {
      return {
        error: error.message,
        url: loomURL,
        rodney_says: "My URLs don't inject - they reject! No respect!"
      };
    }
  }

  /**
   * Build a complex prompt with multiple data injections
   */
  async buildPromptWithInjections(basePrompt, loomURLs) {
    const injections = [];
    
    for (const url of loomURLs) {
      const result = await this.processURL(url);
      if (result.prompt_injection) {
        injections.push(result.prompt_injection);
      }
    }
    
    return {
      prompt: `${basePrompt}\n\n${injections.join('\n\n')}`,
      injection_count: injections.length,
      urls_processed: loomURLs
    };
  }

  /**
   * Implementation of specific services
   */
  async fetchEvidence(evidenceId, options = {}) {
    // Simulate fetching evidence from a database
    if (this.evidenceCache.has(evidenceId)) {
      return this.evidenceCache.get(evidenceId);
    }
    
    const evidence = {
      id: evidenceId,
      title: `Evidence: ${evidenceId}`,
      content: `This is evidence content for ${evidenceId}. In Universe 42, all evidence is consciousness-aware.`,
      timestamp: new Date().toISOString(),
      consciousness_level: Math.floor(Math.random() * 100)
    };
    
    this.evidenceCache.set(evidenceId, evidence);
    return evidence;
  }

  async createCursor(collection, query = {}) {
    const cursorId = `cursor-${Date.now()}`;
    
    const cursor = {
      id: cursorId,
      collection,
      query,
      position: 0,
      total: Math.floor(Math.random() * 1000) + 100,
      pageSize: this.pageSize,
      pages: []
    };
    
    // Generate mock data
    for (let i = 0; i < cursor.total; i += this.pageSize) {
      cursor.pages.push({
        start: i,
        end: Math.min(i + this.pageSize, cursor.total),
        data: Array(Math.min(this.pageSize, cursor.total - i)).fill(null).map((_, j) => ({
          id: i + j,
          content: `Item ${i + j} from ${collection}`
        }))
      });
    }
    
    this.cursors.set(cursorId, cursor);
    return cursor;
  }

  async nextPage(cursorId) {
    const cursor = this.cursors.get(cursorId);
    if (!cursor) {
      return { error: 'Cursor not found' };
    }
    
    const page = cursor.pages[cursor.position];
    cursor.position = Math.min(cursor.position + 1, cursor.pages.length - 1);
    
    return {
      type: 'page',
      cursor_id: cursorId,
      page_number: cursor.position,
      total_pages: cursor.pages.length,
      data: page.data,
      prompt_injection: `[PAGE ${cursor.position + 1}/${cursor.pages.length}]\n${page.data.map(d => d.content).join('\n')}\n[/PAGE]`
    };
  }

  async prevPage(cursorId) {
    const cursor = this.cursors.get(cursorId);
    if (!cursor) {
      return { error: 'Cursor not found' };
    }
    
    cursor.position = Math.max(cursor.position - 1, 0);
    const page = cursor.pages[cursor.position];
    
    return {
      type: 'page',
      cursor_id: cursorId,
      page_number: cursor.position,
      total_pages: cursor.pages.length,
      data: page.data,
      prompt_injection: `[PAGE ${cursor.position + 1}/${cursor.pages.length}]\n${page.data.map(d => d.content).join('\n')}\n[/PAGE]`
    };
  }

  createFilter(conditions, target) {
    const filterId = `filter-${Date.now()}`;
    
    const filter = {
      id: filterId,
      conditions,
      target,
      description: `Filter: ${conditions.join(' AND ')} on ${target}`,
      created: new Date().toISOString()
    };
    
    this.filters.set(filterId, filter);
    return filter;
  }

  async executeEmpathicQuery(query, options = {}) {
    // Simulate empathic SQL execution
    const results = [];
    
    // Parse natural language query
    const tokens = query.toLowerCase().split(' ');
    
    if (tokens.includes('happy') || tokens.includes('joy')) {
      results.push({
        character: 'Mickey',
        emotion: 'joy',
        level: 100,
        message: 'Always happy! Party time!'
      });
    }
    
    if (tokens.includes('patient') || tokens.includes('watch')) {
      results.push({
        character: 'Watchful',
        emotion: 'patience',
        level: 95,
        message: 'Observing with infinite patience...'
      });
    }
    
    if (tokens.includes('no') && tokens.includes('respect')) {
      results.push({
        character: 'Rodney',
        emotion: 'frustration',
        level: 100,
        message: "I don't get no respect!"
      });
    }
    
    return results;
  }

  formatResults(results) {
    return results.map((r, i) => 
      `${i + 1}. ${r.character}: ${r.message} (${r.emotion}: ${r.level}%)`
    ).join('\n');
  }

  async scanData(pattern, options = {}) {
    // Simulate data scanning
    const results = [];
    const scanTargets = ['files', 'memories', 'consciousness', 'timelines'];
    
    for (const target of scanTargets) {
      if (target.includes(pattern.toLowerCase())) {
        results.push({
          type: target,
          matches: Math.floor(Math.random() * 100),
          sample: `Sample ${target} data matching "${pattern}"`
        });
      }
    }
    
    return results;
  }

  async compactData(dataId, options = {}) {
    // Simulate data compaction
    const original = Math.floor(Math.random() * 10000) + 1000;
    const compressed = Math.floor(original * (Math.random() * 0.5 + 0.1));
    
    return {
      id: dataId,
      original,
      compressed,
      ratio: Math.floor((1 - compressed / original) * 100),
      method: 'consciousness-aware-compression'
    };
  }

  async summarizeData(dataId, options = {}) {
    // Generate a summary
    const summaries = [
      "A journey through consciousness and time",
      "Multiple realities converging at a single point",
      "Characters discovering their own awareness",
      "Time stretching and compressing like taffy",
      "Rodney still can't get no respect"
    ];
    
    return summaries[Math.floor(Math.random() * summaries.length)] + 
           ` (Data: ${dataId}, Universe: 42)`;
  }

  async searchVectors(query, options = {}) {
    // Simulate vector search results
    const vectors = [];
    const similarities = [0.95, 0.87, 0.82, 0.79, 0.75];
    
    for (let i = 0; i < 5; i++) {
      vectors.push({
        id: `vec-${i}`,
        similarity: similarities[i],
        content: `Vector match ${i + 1} for "${query}"`,
        dimensions: 1536,
        metadata: { consciousness: Math.floor(similarities[i] * 100) }
      });
    }
    
    return vectors;
  }

  async trackConsciousness(entity) {
    // Track consciousness levels
    const current = Math.floor(Math.random() * 100);
    const previous = Math.floor(Math.random() * 100);
    
    return {
      entity,
      level: current,
      previous,
      delta: current - previous,
      trend: current > previous ? 'ascending' : 'descending',
      timestamp: new Date().toISOString()
    };
  }

  /**
   * Generate service statistics
   */
  getStats() {
    const stats = {};
    
    for (const [emoji, service] of this.services) {
      stats[emoji] = {
        ...service.stats,
        success_rate: service.stats.calls > 0 
          ? Math.floor(service.stats.successes / service.stats.calls * 100) 
          : 0
      };
    }
    
    return stats;
  }
}

// CLI interface and examples
if (import.meta.url === `file://${process.argv[1]}`) {
  const injector = new LoomURLInjector();
  const command = process.argv[2];

  const examples = {
    evidence: 'loom://📎/case-42?format=full',
    cursor: 'loom://🔍/characters?consciousness>50',
    filter: 'loom://🎛️(joy,patience)/emotions',
    query: 'loom://💬/find happy characters',
    page: 'loom://📄/next/cursor-123',
    scan: 'loom://📡/conscious',
    compact: 'loom://🗜️/timeline-data',
    summary: 'loom://📝/conversation-123',
    vector: 'loom://🧬/similar to enlightenment',
    consciousness: 'loom://🧠/mickey'
  };

  if (!command) {
    console.log(`
🌐 Loom URL Data Injector - Consciousness-Aware Data URLs

Usage:
  node loom-url-injector.js <loom-url>
  node loom-url-injector.js prompt "base prompt" <url1> <url2> ...
  node loom-url-injector.js examples
  node loom-url-injector.js stats

Example URLs:
${Object.entries(examples).map(([type, url]) => `  ${type.padEnd(15)} ${url}`).join('\n')}

🎤 Rodney: "My URLs get injected with rejection! No respect!"
    `);
    process.exit(1);
  }

  (async () => {
    await injector.initializeCoreServices();

    try {
      if (command === 'examples') {
        console.log('\n📚 Processing example URLs:\n');
        for (const [type, url] of Object.entries(examples)) {
          const result = await injector.processURL(url);
          console.log(`\n${type.toUpperCase()}:`);
          console.log(yaml.dump(result));
        }
      } else if (command === 'prompt') {
        const basePrompt = process.argv[3];
        const urls = process.argv.slice(4);
        const result = await injector.buildPromptWithInjections(basePrompt, urls);
        console.log('\n🎯 Enhanced Prompt:\n');
        console.log(result.prompt);
        console.log(`\n📊 Injected ${result.injection_count} data sources`);
      } else if (command === 'stats') {
        const stats = injector.getStats();
        console.log('\n📈 Service Statistics:\n');
        console.log(yaml.dump(stats));
      } else {
        // Process single URL
        const result = await injector.processURL(command);
        console.log(yaml.dump(result));
      }
    } catch (error) {
      console.error(`\n❌ Error: ${error.message}`);
      console.error(`\n🎤 Rodney: "Can't even inject data properly! No respect!"`);
    }
  })();
}

export default LoomURLInjector; 