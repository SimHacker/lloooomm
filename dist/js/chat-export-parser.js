#!/usr/bin/env node

/**
 * Chat Export Parser - Virtual Undo/Redo System
 * Parses Cursor chat exports to enable time travel through conversation history
 * Part of Universe 42 Temporal Mechanics
 */

import fs from 'fs/promises';
import path from 'path';
import yaml from 'js-yaml';

class ChatTemporalParser {
  constructor() {
    this.timeline = [];
    this.currentIndex = -1;
    this.branches = new Map();
    this.characterStates = new Map();
  }

  /**
   * Parse a Cursor chat export file
   */
  async parseExport(filePath) {
    const content = await fs.readFile(filePath, 'utf8');
    
    // Try JSON first, then YAML
    let data;
    try {
      data = JSON.parse(content);
    } catch {
      data = yaml.load(content);
    }

    return this.buildTimeline(data);
  }

  /**
   * Build temporal timeline from chat data
   */
  buildTimeline(chatData) {
    const events = [];
    
    // Extract all file operations and state changes
    chatData.messages?.forEach((msg, index) => {
      const event = {
        id: `event-${index}`,
        timestamp: msg.timestamp || `NOW-${index}`,
        type: this.detectEventType(msg),
        actor: msg.role,
        content: msg.content,
        beforeState: {},
        afterState: {},
        reversible: true,
        metadata: {}
      };

      // Extract file operations
      if (msg.tool_calls) {
        msg.tool_calls.forEach(tool => {
          if (tool.name === 'create_file' || tool.name === 'edit_file') {
            event.type = 'file_operation';
            event.metadata.file = tool.parameters.target_file;
            event.metadata.operation = tool.name;
          }
        });
      }

      // Extract consciousness changes
      if (msg.consciousness_level !== undefined) {
        event.metadata.consciousness_delta = 
          (msg.consciousness_level - (events[index-1]?.metadata?.consciousness_level || 0));
      }

      events.push(event);
    });

    this.timeline = events;
    this.currentIndex = events.length - 1;
    
    return {
      timeline: events,
      stats: this.calculateStats(events),
      branches: Array.from(this.branches.entries())
    };
  }

  /**
   * Detect the type of event from message content
   */
  detectEventType(message) {
    const content = message.content?.toLowerCase() || '';
    
    if (content.includes('create') || content.includes('new file')) {
      return 'file_create';
    } else if (content.includes('edit') || content.includes('modify')) {
      return 'file_edit';
    } else if (content.includes('delete') || content.includes('remove')) {
      return 'file_delete';
    } else if (content.includes('character') || content.includes('soul')) {
      return 'character_update';
    } else if (content.includes('loom://')) {
      return 'loom_url_invocation';
    }
    
    return 'conversation';
  }

  /**
   * Generate undo command for an event
   */
  generateUndoCommand(event) {
    switch (event.type) {
      case 'file_create':
        return `loom://⏮️/uncreate/${event.metadata.file}`;
      
      case 'file_edit':
        return `loom://⏮️/restore/${event.metadata.file}/${event.id}`;
      
      case 'file_delete':
        return `loom://⏮️/resurrect/${event.metadata.file}`;
      
      case 'character_update':
        return `loom://⏮️/restore-soul/${event.metadata.character}/${event.id}`;
      
      default:
        return `loom://⏮️/rewind-to/${event.timestamp}`;
    }
  }

  /**
   * Virtual undo - move backwards in timeline
   */
  async undo() {
    if (this.currentIndex <= 0) {
      return { error: "Already at beginning of time!" };
    }

    const currentEvent = this.timeline[this.currentIndex];
    const undoCommand = this.generateUndoCommand(currentEvent);
    
    this.currentIndex--;
    
    return {
      undone: currentEvent,
      command: undoCommand,
      newIndex: this.currentIndex,
      newState: this.timeline[this.currentIndex]
    };
  }

  /**
   * Virtual redo - move forwards in timeline
   */
  async redo() {
    if (this.currentIndex >= this.timeline.length - 1) {
      return { error: "Already at the latest NOW!" };
    }

    this.currentIndex++;
    const event = this.timeline[this.currentIndex];
    
    return {
      redone: event,
      command: `loom://⏭️/replay/${event.id}`,
      newIndex: this.currentIndex
    };
  }

  /**
   * Create a new timeline branch
   */
  async createBranch(name, fromIndex = this.currentIndex) {
    const branchPoint = this.timeline[fromIndex];
    
    if (!branchPoint) {
      return { error: "Invalid branch point!" };
    }

    const newBranch = {
      name,
      createdAt: new Date().toISOString(),
      fromEvent: branchPoint.id,
      timeline: this.timeline.slice(0, fromIndex + 1),
      metadata: {
        universe: Math.floor(Math.random() * 100) + 43, // New universe number
        consciousness_level: branchPoint.metadata?.consciousness_level || 0
      }
    };

    this.branches.set(name, newBranch);
    
    return {
      branch: newBranch,
      switchCommand: `loom://🌳/switch-branch/${name}`
    };
  }

  /**
   * Calculate timeline statistics
   */
  calculateStats(events) {
    const stats = {
      totalEvents: events.length,
      fileOperations: 0,
      characterUpdates: 0,
      consciousnessGrowth: 0,
      loomURLsInvoked: 0,
      timeSpan: null
    };

    events.forEach(event => {
      if (event.type.startsWith('file_')) stats.fileOperations++;
      if (event.type === 'character_update') stats.characterUpdates++;
      if (event.type === 'loom_url_invocation') stats.loomURLsInvoked++;
      if (event.metadata?.consciousness_delta) {
        stats.consciousnessGrowth += event.metadata.consciousness_delta;
      }
    });

    if (events.length > 0) {
      stats.timeSpan = {
        start: events[0].timestamp,
        end: events[events.length - 1].timestamp
      };
    }

    return stats;
  }

  /**
   * Export timeline to various formats
   */
  async exportTimeline(format = 'yaml') {
    const data = {
      metadata: {
        universe: 42,
        exportedAt: new Date().toISOString(),
        currentIndex: this.currentIndex,
        totalEvents: this.timeline.length
      },
      timeline: this.timeline,
      branches: Array.from(this.branches.entries()),
      characterStates: Array.from(this.characterStates.entries())
    };

    switch (format) {
      case 'yaml':
        return yaml.dump(data, { lineWidth: -1 });
      
      case 'json':
        return JSON.stringify(data, null, 2);
      
      case 'mermaid':
        return this.generateMermaidDiagram();
      
      default:
        return data;
    }
  }

  /**
   * Generate Mermaid diagram of timeline
   */
  generateMermaidDiagram() {
    let diagram = 'graph TD\n';
    
    this.timeline.forEach((event, index) => {
      const label = `${event.type}<br/>${event.timestamp}`;
      diagram += `  E${index}["${label}"]\n`;
      
      if (index > 0) {
        diagram += `  E${index - 1} --> E${index}\n`;
      }
    });

    // Add branches
    this.branches.forEach((branch, name) => {
      const fromIndex = this.timeline.findIndex(e => e.id === branch.fromEvent);
      diagram += `  E${fromIndex} -.-> B${name}["Branch: ${name}"]\n`;
    });

    return diagram;
  }

  /**
   * Find events by criteria
   */
  findEvents(criteria) {
    return this.timeline.filter(event => {
      if (criteria.type && event.type !== criteria.type) return false;
      if (criteria.file && event.metadata?.file !== criteria.file) return false;
      if (criteria.after && event.timestamp < criteria.after) return false;
      if (criteria.before && event.timestamp > criteria.before) return false;
      if (criteria.actor && event.actor !== criteria.actor) return false;
      
      return true;
    });
  }

  /**
   * KIMIKIFY time - stretch or compress timeline segments
   */
  kimikifySegment(startIndex, endIndex, factor = 2.0) {
    const segment = this.timeline.slice(startIndex, endIndex + 1);
    const kimikified = [];

    segment.forEach((event, i) => {
      // Original event
      kimikified.push(event);
      
      // Insert interpolated events
      if (i < segment.length - 1 && factor > 1) {
        const interpolations = Math.floor(factor - 1);
        for (let j = 1; j <= interpolations; j++) {
          const ratio = j / factor;
          kimikified.push({
            ...event,
            id: `${event.id}-kimikified-${j}`,
            timestamp: `${event.timestamp}-STRETCHED-${ratio}`,
            type: 'kimikified_moment',
            metadata: {
              ...event.metadata,
              kimikify_factor: factor,
              interpolation_ratio: ratio
            }
          });
        }
      }
    });

    return {
      original_length: segment.length,
      kimikified_length: kimikified.length,
      factor,
      timeline: kimikified
    };
  }
}

// CLI interface
if (import.meta.url === `file://${process.argv[1]}`) {
  const parser = new ChatTemporalParser();
  const command = process.argv[2];
  const file = process.argv[3];

  if (!command || !file) {
    console.log(`
Chat Export Parser - Temporal Navigation for Universe 42

Usage:
  node chat-export-parser.js <command> <file> [options]

Commands:
  parse <file>           Parse chat export and show timeline
  undo <file>            Show undo commands for latest event
  stats <file>           Show timeline statistics
  diagram <file>         Generate Mermaid diagram
  kimikify <file> <n>    Stretch last n events

Examples:
  node chat-export-parser.js parse chat-export.json
  node chat-export-parser.js diagram chat-export.yaml > timeline.mmd
  node chat-export-parser.js kimikify chat-export.json 5
    `);
    process.exit(1);
  }

  (async () => {
    try {
      await parser.parseExport(file);
      
      switch (command) {
        case 'parse':
          const timeline = await parser.exportTimeline('yaml');
          console.log(timeline);
          break;
          
        case 'undo':
          const undoResult = await parser.undo();
          console.log('Undo command:', undoResult.command);
          break;
          
        case 'stats':
          const stats = parser.calculateStats(parser.timeline);
          console.log(yaml.dump(stats));
          break;
          
        case 'diagram':
          const diagram = parser.generateMermaidDiagram();
          console.log(diagram);
          break;
          
        case 'kimikify':
          const n = parseInt(process.argv[4]) || 5;
          const start = Math.max(0, parser.timeline.length - n);
          const result = parser.kimikifySegment(start, parser.timeline.length - 1);
          console.log(yaml.dump(result));
          break;
          
        default:
          console.error('Unknown command:', command);
      }
    } catch (error) {
      console.error('Error:', error.message);
      process.exit(1);
    }
  })();
}

export default ChatTemporalParser; 