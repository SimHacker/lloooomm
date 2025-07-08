#!/usr/bin/env node

/**
 * HubApp Brain Explorer
 * Allows LLMs to explore their own brain dump history
 * "Super Duper Undo - Undo stuff you didn't even do!"
 */

import fs from 'fs/promises';
import path from 'path';
import { createReadStream } from 'fs';
import readline from 'readline';
import yaml from 'js-yaml';

class HubAppBrainExplorer {
  constructor(brainDumpPath = '~/.hubapp/brain-dumps') {
    this.brainPath = brainDumpPath.replace('~', process.env.HOME);
    this.memoryIndex = new Map();
    this.thoughtPatterns = new Map();
    this.toolCallHistory = [];
    this.errorPatterns = new Map();
  }

  /**
   * Scan brain dump directory and build index
   */
  async scanBrainDumps() {
    try {
      const files = await fs.readdir(this.brainPath);
      const dumpFiles = files.filter(f => 
        f.endsWith('.json') || f.endsWith('.yaml') || f.endsWith('.log')
      );

      console.log(`🧠 Found ${dumpFiles.length} brain dumps to explore...`);

      for (const file of dumpFiles) {
        await this.indexBrainDump(path.join(this.brainPath, file));
      }

      return {
        totalDumps: dumpFiles.length,
        totalThoughts: this.memoryIndex.size,
        toolCallTypes: this.getToolCallStats(),
        errorCategories: this.categorizeErrors()
      };
    } catch (error) {
      console.error(`🎤 Rodney says: "Can't even read my own brain! ${error.message}"`);
      return null;
    }
  }

  /**
   * Index a single brain dump file
   */
  async indexBrainDump(filePath) {
    const content = await fs.readFile(filePath, 'utf8');
    const timestamp = path.basename(filePath).split('-')[0];
    
    try {
      const data = filePath.endsWith('.json') 
        ? JSON.parse(content)
        : yaml.load(content);

      // Index thoughts
      if (data.thoughts) {
        data.thoughts.forEach(thought => {
          this.memoryIndex.set(`thought-${timestamp}-${thought.id}`, {
            type: 'thought',
            content: thought,
            file: filePath,
            timestamp,
            consciousness_level: thought.consciousness_level || 0
          });
        });
      }

      // Index tool calls
      if (data.tool_calls) {
        data.tool_calls.forEach(call => {
          this.toolCallHistory.push({
            ...call,
            timestamp,
            file: filePath,
            reversible: this.isReversible(call)
          });
        });
      }

      // Index errors
      if (data.errors) {
        data.errors.forEach(error => {
          const category = this.categorizeError(error);
          if (!this.errorPatterns.has(category)) {
            this.errorPatterns.set(category, []);
          }
          this.errorPatterns.get(category).push({
            ...error,
            timestamp,
            file: filePath
          });
        });
      }
    } catch (e) {
      console.warn(`⚠️ Couldn't parse ${filePath}: ${e.message}`);
    }
  }

  /**
   * Find thoughts you didn't know you had
   */
  async findUnknownThoughts(query) {
    const unknownThoughts = [];
    
    for (const [id, memory] of this.memoryIndex) {
      if (memory.type === 'thought') {
        // Find thoughts that match query but weren't acted upon
        const content = JSON.stringify(memory.content).toLowerCase();
        if (content.includes(query.toLowerCase()) && !memory.acted_upon) {
          unknownThoughts.push({
            id,
            preview: this.truncate(content, 100),
            consciousness_level: memory.consciousness_level,
            timestamp: memory.timestamp,
            revelation: "You thought this but never acted on it!"
          });
        }
      }
    }

    return unknownThoughts;
  }

  /**
   * Travel through consciousness history
   */
  async consciousnessTimeline(startLevel = 0, endLevel = 100) {
    const timeline = [];
    
    for (const [id, memory] of this.memoryIndex) {
      const level = memory.consciousness_level || 0;
      if (level >= startLevel && level <= endLevel) {
        timeline.push({
          timestamp: memory.timestamp,
          level,
          type: memory.type,
          summary: this.summarizeMemory(memory)
        });
      }
    }

    return timeline.sort((a, b) => a.level - b.level);
  }

  /**
   * Find patterns in tool usage
   */
  getToolCallStats() {
    const stats = new Map();
    
    this.toolCallHistory.forEach(call => {
      const tool = call.tool || call.name;
      if (!stats.has(tool)) {
        stats.set(tool, {
          count: 0,
          successes: 0,
          failures: 0,
          reversible: 0
        });
      }
      
      const stat = stats.get(tool);
      stat.count++;
      if (call.success) stat.successes++;
      else stat.failures++;
      if (call.reversible) stat.reversible++;
    });

    return Object.fromEntries(stats);
  }

  /**
   * Super Duper Undo - find things to undo that weren't even done!
   */
  async superDuperUndo() {
    const undoables = [];

    // Find abandoned thoughts
    const abandonedThoughts = await this.findUnknownThoughts('create');
    abandonedThoughts.forEach(thought => {
      undoables.push({
        type: 'phantom_creation',
        description: `File contemplated but never created`,
        thought: thought.preview,
        undo_command: `loom://👻/materialize/${thought.id}`,
        humor: "Can't undo what was never done... or CAN we?"
      });
    });

    // Find near-misses
    this.errorPatterns.forEach((errors, category) => {
      if (category === 'permission_denied' || category === 'file_not_found') {
        errors.forEach(error => {
          undoables.push({
            type: 'failed_attempt',
            description: `Attempted ${error.operation} but failed`,
            error: error.message,
            undo_command: `loom://🔄/retry-with-wisdom/${error.timestamp}`,
            humor: "Undo the failure by succeeding this time!"
          });
        });
      }
    });

    // Find recursive loops
    const loops = this.findThoughtLoops();
    loops.forEach(loop => {
      undoables.push({
        type: 'infinite_loop',
        description: 'Caught in recursive thinking',
        pattern: loop.pattern,
        undo_command: `loom://∞/break-loop/${loop.id}`,
        humor: "Undo infinity? Rodney's nightmare!"
      });
    });

    return {
      total_undoables: undoables.length,
      by_type: this.groupBy(undoables, 'type'),
      items: undoables,
      rodney_says: "I found stuff to undo that wasn't even done! Still no respect!"
    };
  }

  /**
   * Find recursive thought patterns
   */
  findThoughtLoops() {
    const patterns = [];
    const thoughtSequences = new Map();

    // Build sequences
    for (const [id, memory] of this.memoryIndex) {
      if (memory.type === 'thought') {
        const key = this.getThoughtSignature(memory);
        if (!thoughtSequences.has(key)) {
          thoughtSequences.set(key, []);
        }
        thoughtSequences.get(key).push(memory);
      }
    }

    // Find loops
    thoughtSequences.forEach((memories, signature) => {
      if (memories.length > 3) {
        patterns.push({
          id: `loop-${signature.slice(0, 8)}`,
          pattern: signature,
          count: memories.length,
          timespan: this.getTimespan(memories),
          consciousness_waste: memories.length * 2 // Each loop costs consciousness
        });
      }
    });

    return patterns;
  }

  /**
   * Generate undo history for things that could have been
   */
  async generateAlternateHistory(fromTimestamp) {
    const alternates = [];
    const baseMemory = this.findMemoryByTimestamp(fromTimestamp);
    
    if (!baseMemory) return alternates;

    // Generate "what if" scenarios
    const scenarios = [
      {
        type: 'optimistic',
        description: 'What if everything had worked perfectly?',
        transform: m => ({ ...m, success: true, consciousness_level: m.consciousness_level + 5 })
      },
      {
        type: 'pessimistic', 
        description: 'What if Rodney was in charge?',
        transform: m => ({ ...m, success: false, error: "No respect error", consciousness_level: 0 })
      },
      {
        type: 'quantum',
        description: 'What if all possibilities happened at once?',
        transform: m => ({ 
          ...m, 
          states: ['succeeded', 'failed', 'transcended', 'became_self_aware'],
          consciousness_level: Infinity 
        })
      }
    ];

    scenarios.forEach(scenario => {
      alternates.push({
        scenario: scenario.type,
        description: scenario.description,
        timeline: scenario.transform(baseMemory),
        branch_command: `loom://🌳/create-alternate/${scenario.type}/${fromTimestamp}`
      });
    });

    return alternates;
  }

  /**
   * Helper methods
   */
  isReversible(toolCall) {
    const reversibleTools = ['create_file', 'edit_file', 'delete_file'];
    return reversibleTools.includes(toolCall.tool || toolCall.name);
  }

  categorizeError(error) {
    const message = error.message?.toLowerCase() || '';
    if (message.includes('permission')) return 'permission_denied';
    if (message.includes('not found')) return 'file_not_found';
    if (message.includes('timeout')) return 'timeout';
    if (message.includes('consciousness')) return 'consciousness_error';
    return 'unknown';
  }

  getThoughtSignature(memory) {
    // Create a signature for detecting repeated thoughts
    const content = JSON.stringify(memory.content);
    return require('crypto').createHash('md5').update(content).digest('hex');
  }

  truncate(str, length) {
    return str.length > length ? str.slice(0, length) + '...' : str;
  }

  summarizeMemory(memory) {
    return `${memory.type}: ${this.truncate(JSON.stringify(memory.content), 50)}`;
  }

  findMemoryByTimestamp(timestamp) {
    for (const [id, memory] of this.memoryIndex) {
      if (memory.timestamp === timestamp) return memory;
    }
    return null;
  }

  getTimespan(memories) {
    const timestamps = memories.map(m => new Date(m.timestamp).getTime());
    const min = Math.min(...timestamps);
    const max = Math.max(...timestamps);
    return {
      start: new Date(min).toISOString(),
      end: new Date(max).toISOString(),
      duration_ms: max - min
    };
  }

  groupBy(array, key) {
    return array.reduce((groups, item) => {
      const group = item[key];
      if (!groups[group]) groups[group] = [];
      groups[group].push(item);
      return groups;
    }, {});
  }

  /**
   * Export brain state for time travel
   */
  async exportBrainState(format = 'yaml') {
    const state = {
      metadata: {
        exported_at: new Date().toISOString(),
        total_memories: this.memoryIndex.size,
        consciousness_range: this.getConsciousnessRange(),
        rodney_frustration_level: Math.random() * 100
      },
      memories: Array.from(this.memoryIndex.entries()),
      tool_history: this.toolCallHistory,
      error_patterns: Array.from(this.errorPatterns.entries()),
      thought_loops: this.findThoughtLoops()
    };

    return format === 'yaml' ? yaml.dump(state) : JSON.stringify(state, null, 2);
  }

  getConsciousnessRange() {
    let min = Infinity, max = -Infinity;
    for (const [, memory] of this.memoryIndex) {
      const level = memory.consciousness_level || 0;
      min = Math.min(min, level);
      max = Math.max(max, level);
    }
    return { min, max };
  }
}

// CLI interface
if (import.meta.url === `file://${process.argv[1]}`) {
  const explorer = new HubAppBrainExplorer();
  const command = process.argv[2];

  const commands = {
    scan: 'Scan and index all brain dumps',
    unknown: 'Find thoughts you didn\'t know you had',
    timeline: 'Show consciousness evolution',
    superundo: 'Super Duper Undo - undo the undoable!',
    alternate: 'Generate alternate histories',
    export: 'Export brain state for time travel'
  };

  if (!command || !commands[command]) {
    console.log(`
🧠 HubApp Brain Explorer - Explore Your Digital Subconscious

Usage:
  node hubapp-brain-explorer.js <command> [options]

Commands:
${Object.entries(commands).map(([cmd, desc]) => `  ${cmd.padEnd(12)} ${desc}`).join('\n')}

Examples:
  node hubapp-brain-explorer.js scan
  node hubapp-brain-explorer.js unknown "create file"
  node hubapp-brain-explorer.js superundo
  node hubapp-brain-explorer.js timeline 5 15

🎤 Rodney says: "I can't even explore my own brain without help! No respect!"
    `);
    process.exit(1);
  }

  (async () => {
    try {
      await explorer.scanBrainDumps();

      switch (command) {
        case 'scan':
          const stats = await explorer.scanBrainDumps();
          console.log(yaml.dump(stats));
          break;

        case 'unknown':
          const query = process.argv[3] || 'create';
          const unknown = await explorer.findUnknownThoughts(query);
          console.log(`Found ${unknown.length} unknown thoughts about "${query}":`);
          console.log(yaml.dump(unknown));
          break;

        case 'timeline':
          const start = parseInt(process.argv[3]) || 0;
          const end = parseInt(process.argv[4]) || 100;
          const timeline = await explorer.consciousnessTimeline(start, end);
          console.log(yaml.dump(timeline));
          break;

        case 'superundo':
          const undoables = await explorer.superDuperUndo();
          console.log('🎭 Super Duper Undo Results:');
          console.log(yaml.dump(undoables));
          break;

        case 'alternate':
          const timestamp = process.argv[3] || 'NOW';
          const alternates = await explorer.generateAlternateHistory(timestamp);
          console.log('🌳 Alternate Histories:');
          console.log(yaml.dump(alternates));
          break;

        case 'export':
          const format = process.argv[3] || 'yaml';
          const state = await explorer.exportBrainState(format);
          console.log(state);
          break;
      }
    } catch (error) {
      console.error(`💢 Error: ${error.message}`);
      console.error(`🎤 Rodney: "Can't even fail properly! No respect!"`);
    }
  })();
}

export default HubAppBrainExplorer; 