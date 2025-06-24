#!/usr/bin/env tsx
/**
 * LLOOOOMM Data Extraction Pipeline
 * Extracts all markdown discussion files into structured YAML
 */

import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync } from 'fs';
import { join, basename } from 'path';
import * as yaml from 'js-yaml';

// Data structure interfaces
interface Message {
  id: string;
  parent_id: string | null;
  index: number;
  thread: string;
  author: string;
  timestamp: string;
  points: number | null;
  status: 'active' | 'dead' | 'flagged';
  depth: number;
  character_archetype: string;
  content_type: string;
  text: string;
  metadata: Record<string, any>;
  analytics: {
    wink_energy_impact: number;
    discourse_quality_contribution: number;
    learning_catalyst_rating: number;
    collaborative_potential: number;
  };
  character_enhancements?: Record<string, any>;
  breakthrough_indicators?: Record<string, any>;
  moderation_notes?: Record<string, any>;
}

interface ThreadMetadata {
  thread_id: string;
  primary_pattern: string;
  key_breakthrough: string;
  community_value: string;
  engagement_flow: string[];
  wink_energy_metrics: Record<string, number>;
  [key: string]: any;
}

interface ThreadData {
  messages: Message[];
  thread_metadata: ThreadMetadata;
}

class LLOOOOMMDataExtractor {
  private sourceDir: string;
  private outputDir: string;
  private extractedThreads: Map<string, ThreadData> = new Map();

  constructor(sourceDir: string, outputDir: string) {
    this.sourceDir = sourceDir;
    this.outputDir = outputDir;
    
    // Ensure output directory exists
    if (!existsSync(outputDir)) {
      mkdirSync(outputDir, { recursive: true });
    }
  }

  extractAllMarkdownFiles(): void {
    console.log('🚀 LLOOOOMM Data Extraction Starting...');
    
    const files = readdirSync(this.sourceDir)
      .filter(f => f.endsWith('.md') && f.includes('hacker-news-leela'))
      .sort();

    console.log(`📁 Found ${files.length} markdown files to process`);

    for (const file of files) {
      try {
        this.extractSingleFile(file);
      } catch (error) {
        console.error(`❌ Error processing ${file}:`, error);
      }
    }

    console.log(`✅ Extracted ${this.extractedThreads.size} discussion threads`);
  }

  private extractSingleFile(filename: string): void {
    const filepath = join(this.sourceDir, filename);
    const content = readFileSync(filepath, 'utf-8');
    
    // Extract thread number from filename
    const threadMatch = filename.match(/(\d+)\.md$/);
    if (!threadMatch) {
      console.log(`⚠️  Skipping ${filename} - no thread number found`);
      return;
    }
    
    const threadNum = threadMatch[1];
    console.log(`📝 Processing Thread ${threadNum}: ${filename}`);

    // Parse the file content
    const threadData = this.parseMarkdownFile(content, threadNum);
    
    if (threadData.messages.length > 0) {
      this.extractedThreads.set(threadNum, threadData);
      
      // Save individual thread file
      const outputFile = join(this.outputDir, `messages_${threadNum}.yml`);
      this.saveThreadData(threadData, outputFile);
      
      console.log(`  ✅ Extracted ${threadData.messages.length} messages from Thread ${threadNum}`);
    } else {
      console.log(`  ⚠️  No messages found in Thread ${threadNum}`);
    }
  }

  private parseMarkdownFile(content: string, threadNum: string): ThreadData {
    const messages: Message[] = [];
    let threadMetadata: ThreadMetadata;

    // Handle frontmatter if present
    let bodyContent = content;
    if (content.startsWith('---')) {
      const frontmatterEnd = content.indexOf('---', 3);
      if (frontmatterEnd !== -1) {
        bodyContent = content.slice(frontmatterEnd + 3).trim();
      }
    }

    // Split by --- separators to get individual messages
    const sections = bodyContent.split(/\n---\n/).filter(s => s.trim());
    
    let messageIndex = 1;
    let threadPattern = 'general_discussion';
    let keyBreakthrough = 'collaborative_exchange';

    for (const section of sections) {
      const message = this.parseMessageSection(section, threadNum, messageIndex);
      if (message) {
        messages.push(message);
        messageIndex++;
        
        // Extract patterns for thread metadata
        if (message.character_archetype.includes('skeptic')) {
          threadPattern = 'skeptic_to_collaborator_conversion';
        }
        if (message.content_type.includes('breakthrough')) {
          keyBreakthrough = message.content_type;
        }
      }
    }

    // Generate thread metadata
    threadMetadata = this.generateThreadMetadata(threadNum, messages, threadPattern, keyBreakthrough);

    return { messages, thread_metadata: threadMetadata };
  }

  private parseMessageSection(section: string, threadNum: string, index: number): Message | null {
    const lines = section.trim().split('\n');
    if (lines.length === 0) return null;

    // Initialize message object
    const message: Message = {
      id: '',
      parent_id: index === 1 ? 'story' : `msg_${threadNum}_${String(index - 1).padStart(2, '0')}`,
      index,
      thread: `thread_${threadNum}`,
      author: '',
      timestamp: '',
      points: null,
      status: 'active',
      depth: index,
      character_archetype: 'community_participant',
      content_type: 'discussion_contribution',
      text: '',
      metadata: {},
      analytics: {
        wink_energy_impact: 7.0,
        discourse_quality_contribution: 7.0,
        learning_catalyst_rating: 7.0,
        collaborative_potential: 7.0
      }
    };

    // Extract author and metadata from first few lines
    let textStartIndex = 0;
    for (let i = 0; i < Math.min(5, lines.length); i++) {
      const line = lines[i];
      
      // Look for username patterns
      const usernameMatch = line.match(/\*\*username:\*\*\s*`([^`]+)`/) || 
                          line.match(/\*\*([^*]+)\*\*\s*\|\s*(\d+\s+\w+\s+ago)/);
      
      if (usernameMatch) {
        message.author = usernameMatch[1];
        if (usernameMatch[2]) {
          message.timestamp = usernameMatch[2];
        }
        textStartIndex = i + 1;
        break;
      }
      
      // Look for header patterns
      if (line.startsWith('#')) {
        textStartIndex = i + 1;
        message.thread = line.replace(/^#+\s*/, '').toLowerCase().replace(/\s+/g, '_');
        continue;
      }
    }

    // Extract text content
    const textLines = lines.slice(textStartIndex).filter(line => 
      !line.startsWith('**') || line.includes('|')
    );
    message.text = textLines.join('\n').trim();

    if (!message.text) return null;

    // Generate ID
    const contentHash = this.simpleHash(message.text.slice(0, 50));
    message.id = `msg_${threadNum}_${String(index).padStart(2, '0')}`;

    // Detect status from styling
    if (message.text.includes('<span style="color: #999999;">')) {
      message.status = 'dead';
      message.metadata.heavily_downvoted = true;
    }

    // Analyze content for archetype and metadata
    this.analyzeMessageContent(message);

    return message;
  }

  private analyzeMessageContent(message: Message): void {
    const text = message.text.toLowerCase();
    
    // Determine character archetype
    if (text.includes('question') && text.includes('?')) {
      message.character_archetype = 'technical_questioner';
    }
    if (text.includes('skeptic') || text.includes('doubt') || text.includes('evidence')) {
      message.character_archetype = 'constructive_skeptic';
    }
    if (text.includes('research') || text.includes('academic') || text.includes('mit')) {
      message.character_archetype = 'academic_researcher';
    }
    if (text.includes('example') && text.includes('breakthrough')) {
      message.character_archetype = 'breakthrough_documenter';
    }
    if (message.author.toLowerCase() === 'donhopkins') {
      message.character_archetype = 'creative_technologist_explainer';
    }

    // Determine content type
    if (text.includes('?') && message.text.split('?').length > 2) {
      message.content_type = 'challenging_questions';
    }
    if (text.includes('example:') || text.includes('breakthrough:')) {
      message.content_type = 'breakthrough_story_explanation';
    }
    if (text.includes('thanks') && text.includes('interesting')) {
      message.content_type = 'acceptance_and_expansion';
    }

    // Calculate analytics based on content
    const wordCount = message.text.split(/\s+/).length;
    const questionCount = (message.text.match(/\?/g) || []).length;
    const exampleCount = (message.text.match(/example|instance|case/gi) || []).length;
    
    message.analytics = {
      wink_energy_impact: Math.min(10, 5 + (wordCount / 50) + (questionCount * 0.5) + (exampleCount * 0.3)),
      discourse_quality_contribution: Math.min(10, 6 + (exampleCount * 0.8) + (questionCount * 0.4)),
      learning_catalyst_rating: Math.min(10, 5 + (exampleCount * 1.2) + (questionCount * 0.6)),
      collaborative_potential: Math.min(10, 6 + (message.text.includes('collaborate') ? 2 : 0) + (exampleCount * 0.5))
    };

    // Add metadata
    message.metadata = {
      word_count: wordCount,
      question_count: questionCount,
      example_count: exampleCount,
      engagement_quality: wordCount > 100 ? 'high' : wordCount > 50 ? 'medium' : 'low',
      community_value: questionCount > 0 ? 'inquiry_driving' : exampleCount > 0 ? 'example_providing' : 'discussion_contributing'
    };
  }

  private generateThreadMetadata(threadNum: string, messages: Message[], pattern: string, breakthrough: string): ThreadMetadata {
    const avgWinkEnergy = messages.reduce((sum, m) => sum + m.analytics.wink_energy_impact, 0) / messages.length;
    
    return {
      thread_id: `thread_${threadNum}`,
      primary_pattern: pattern,
      key_breakthrough: breakthrough,
      community_value: 'collaborative_intelligence_demonstration',
      engagement_flow: messages.map(m => m.content_type),
      wink_energy_metrics: {
        thread_coherence: Math.min(10, avgWinkEnergy * 0.9),
        collaborative_intelligence_emergence: Math.min(10, avgWinkEnergy * 1.1),
        technical_depth_achievement: Math.min(10, avgWinkEnergy * 0.95),
        overall_thread_wink_score: avgWinkEnergy
      },
      participant_count: new Set(messages.map(m => m.author)).size,
      message_count: messages.length,
      depth_achieved: Math.max(...messages.map(m => m.depth))
    };
  }

  private saveThreadData(threadData: ThreadData, outputFile: string): void {
    const yamlContent = yaml.dump(threadData, { 
      indent: 2, 
      lineWidth: 120,
      quotingType: '"',
      forceQuotes: false 
    });
    
    const header = `---
# LLOOOOMM Discussion Thread ${threadData.thread_metadata.thread_id}
# Extracted and enhanced with metadata
# Generated: ${new Date().toISOString()}

`;
    
    writeFileSync(outputFile, header + yamlContent);
  }

  private simpleHash(str: string): string {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      const char = str.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash; // Convert to 32bit integer
    }
    return Math.abs(hash).toString(16).slice(0, 6);
  }

  // Merge all threads with master metadata
  mergeAllData(): void {
    console.log('🔄 Merging all thread data with master metadata...');
    
    // Load master metadata
    const masterMetadataFile = join(this.outputDir, '../data/master_metadata.yml');
    let masterMetadata = {};
    
    if (existsSync(masterMetadataFile)) {
      const masterContent = readFileSync(masterMetadataFile, 'utf-8');
      masterMetadata = yaml.load(masterContent) as any;
    }

    // Combine all threads
    const allMessages: Message[] = [];
    const allThreadMetadata: ThreadMetadata[] = [];
    
    for (const [threadNum, threadData] of this.extractedThreads) {
      allMessages.push(...threadData.messages);
      allThreadMetadata.push(threadData.thread_metadata);
    }

    // Create complete data structure
    const completeData = {
      ...masterMetadata,
      extracted_threads: Object.fromEntries(this.extractedThreads),
      all_messages: allMessages,
      thread_summaries: allThreadMetadata,
      extraction_metadata: {
        total_threads: this.extractedThreads.size,
        total_messages: allMessages.length,
        extracted_at: new Date().toISOString(),
        wink_energy_stats: this.calculateWinkEnergyStats(allMessages)
      }
    };

    // Save complete data
    const completeDataFile = join(this.outputDir, 'complete_discussion_data.yml');
    const yamlContent = yaml.dump(completeData, { 
      indent: 2, 
      lineWidth: 120,
      quotingType: '"',
      forceQuotes: false 
    });
    
    const header = `---
# LLOOOOMM Complete Discussion Data
# All threads + Master metadata + Analytics
# Generated: ${new Date().toISOString()}
# 
# This file contains the complete JAZZ YAML data structure
# ready for SvelteKit rendering and viral nugget generation
#

`;
    
    writeFileSync(completeDataFile, header + yamlContent);
    console.log(`✅ Complete data saved to: ${completeDataFile}`);
  }

  private calculateWinkEnergyStats(messages: Message[]) {
    const winkScores = messages.map(m => m.analytics.wink_energy_impact);
    return {
      average: winkScores.reduce((a, b) => a + b, 0) / winkScores.length,
      maximum: Math.max(...winkScores),
      minimum: Math.min(...winkScores),
      total_messages: messages.length,
      high_wink_count: winkScores.filter(s => s >= 9.0).length,
      breakthrough_count: winkScores.filter(s => s >= 9.5).length
    };
  }
}

// Main execution
async function main() {
  const sourceDir = 'lloooomm/03-Resources/characters/hacker-news/leela';
  const outputDir = 'lloooomm/data';

  const extractor = new LLOOOOMMDataExtractor(sourceDir, outputDir);
  
  // Extract all markdown files
  extractor.extractAllMarkdownFiles();
  
  // Merge with master metadata
  extractor.mergeAllData();
  
  console.log('\n🎉 LLOOOOMM Data Extraction Complete!');
  console.log('📂 Output directory:', outputDir);
  console.log('🎯 Ready for SvelteKit viral nugget generation!');
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch(console.error);
} 