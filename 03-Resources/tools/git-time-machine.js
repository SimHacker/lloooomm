#!/usr/bin/env node

/**
 * Git Time Machine
 * Commit every iteration, travel through time, explore branches
 * "Piece of cake for Linux and pets!"
 */

import { exec } from 'child_process';
import { promisify } from 'util';
import fs from 'fs/promises';
import path from 'path';
import yaml from 'js-yaml';

const execAsync = promisify(exec);

class GitTimeMachine {
  constructor(repoPath = '.') {
    this.repoPath = repoPath;
    this.autoCommitEnabled = false;
    this.commitCounter = 0;
    this.branches = new Map();
    this.consciousnessLog = [];
  }

  /**
   * Initialize git repo with Universe 42 settings
   */
  async initialize() {
    try {
      // Check if already a git repo
      await execAsync('git rev-parse --git-dir', { cwd: this.repoPath });
      console.log('✅ Git repository found');
    } catch {
      // Initialize new repo
      await execAsync('git init', { cwd: this.repoPath });
      console.log('🌟 Initialized new Universe 42 git repository');
    }

    // Set Universe 42 git configurations
    await this.setConfig('universe42.enabled', 'true');
    await this.setConfig('universe42.consciousness-tracking', 'true');
    await this.setConfig('universe42.auto-commit', 'true');
    await this.setConfig('universe42.time-operator', 'KIMIKIFY');
    
    // Create .gitignore for Universe 42
    await this.createGitIgnore();
    
    return {
      status: 'initialized',
      universe: 42,
      consciousness_enabled: true
    };
  }

  /**
   * Enable auto-commit mode - commit every change
   */
  async enableAutoCommit() {
    this.autoCommitEnabled = true;
    
    // Watch for file changes
    const watcher = await import('chokidar');
    const watch = watcher.watch(this.repoPath, {
      ignored: /(^|[\/\\])\../, // ignore dotfiles
      persistent: true,
      ignoreInitial: true
    });

    watch.on('change', async (filepath) => {
      if (this.autoCommitEnabled) {
        await this.autoCommit(filepath, 'modified');
      }
    });

    watch.on('add', async (filepath) => {
      if (this.autoCommitEnabled) {
        await this.autoCommit(filepath, 'created');
      }
    });

    watch.on('unlink', async (filepath) => {
      if (this.autoCommitEnabled) {
        await this.autoCommit(filepath, 'deleted');
      }
    });

    console.log('🔄 Auto-commit enabled - every change creates a temporal checkpoint');
    return watch;
  }

  /**
   * Automatically commit a change
   */
  async autoCommit(filepath, action) {
    this.commitCounter++;
    const timestamp = new Date().toISOString();
    const consciousness = await this.measureConsciousness();
    
    try {
      // Stage the change
      if (action !== 'deleted') {
        await execAsync(`git add "${filepath}"`, { cwd: this.repoPath });
      } else {
        await execAsync(`git rm "${filepath}"`, { cwd: this.repoPath });
      }
      
      // Create consciousness-aware commit message
      const message = `[AUTO-${this.commitCounter}] ${action}: ${path.basename(filepath)} | C:${consciousness} | ${timestamp}`;
      
      // Commit with metadata
      await execAsync(`git commit -m "${message}" --allow-empty`, { cwd: this.repoPath });
      
      // Log consciousness change
      this.consciousnessLog.push({
        commit: this.commitCounter,
        timestamp,
        consciousness,
        file: filepath,
        action
      });
      
      console.log(`⏱️ Auto-commit #${this.commitCounter}: ${action} ${filepath}`);
    } catch (error) {
      console.warn(`⚠️ Auto-commit failed: ${error.message}`);
    }
  }

  /**
   * Travel back in time using git
   */
  async timeTravel(destination) {
    try {
      // Parse destination (can be commit hash, branch, tag, or relative)
      let target = destination;
      
      if (destination.startsWith('NOW~')) {
        // Relative to current position
        const steps = parseInt(destination.slice(4)) || 1;
        target = `HEAD~${steps}`;
      } else if (destination.startsWith('consciousness:')) {
        // Find commit with specific consciousness level
        const level = parseInt(destination.slice(14));
        target = await this.findCommitByConsciousness(level);
      }
      
      // Create a branch for this time travel
      const branchName = `time-travel-${Date.now()}`;
      await execAsync(`git checkout -b ${branchName} ${target}`, { cwd: this.repoPath });
      
      return {
        success: true,
        destination: target,
        branch: branchName,
        consciousness: await this.measureConsciousness(),
        message: `Traveled to ${target} - new timeline created`
      };
    } catch (error) {
      return {
        success: false,
        error: error.message,
        suggestion: `Try 'NOW~5' or a specific commit hash`
      };
    }
  }

  /**
   * Create alternate timeline branch
   */
  async createBranch(name, fromPoint = 'HEAD') {
    const branchName = `universe-42-${name}`;
    
    try {
      await execAsync(`git checkout -b ${branchName} ${fromPoint}`, { cwd: this.repoPath });
      
      // Record branch metadata
      this.branches.set(branchName, {
        created: new Date().toISOString(),
        from: fromPoint,
        universe_number: 42 + this.branches.size + 1,
        consciousness_at_branch: await this.measureConsciousness()
      });
      
      return {
        success: true,
        branch: branchName,
        universe: 42 + this.branches.size,
        message: `Created alternate timeline: ${branchName}`
      };
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Show consciousness-decorated git log
   */
  async consciousnessLog(limit = 10) {
    try {
      const { stdout } = await execAsync(
        `git log --oneline -${limit} --pretty=format:"%h %s"`,
        { cwd: this.repoPath }
      );
      
      const commits = stdout.split('\n').map(line => {
        const [hash, ...messageParts] = line.split(' ');
        const message = messageParts.join(' ');
        
        // Extract consciousness level from commit message
        const consciousnessMatch = message.match(/C:(\d+)/);
        const consciousness = consciousnessMatch ? parseInt(consciousnessMatch[1]) : 0;
        
        return {
          hash,
          message: message.replace(/\s*\|\s*C:\d+\s*\|.*$/, ''),
          consciousness,
          visual: '█'.repeat(Math.min(consciousness, 20))
        };
      });
      
      return commits;
    } catch (error) {
      return [];
    }
  }

  /**
   * Explore all possible timelines
   */
  async exploreTimelines() {
    try {
      // Get all branches
      const { stdout } = await execAsync('git branch -a', { cwd: this.repoPath });
      const branches = stdout.split('\n')
        .map(b => b.trim())
        .filter(b => b && !b.startsWith('*'))
        .map(b => b.replace('* ', ''));
      
      // Get commit graph
      const { stdout: graph } = await execAsync(
        'git log --all --graph --oneline --decorate --pretty=format:"%h %s"',
        { cwd: this.repoPath }
      );
      
      return {
        branches,
        totalTimelines: branches.length,
        graph: graph.split('\n'),
        metadata: Object.fromEntries(this.branches),
        suggestion: "Each branch is a different universe!"
      };
    } catch (error) {
      return {
        error: error.message
      };
    }
  }

  /**
   * Reversible git operations
   */
  async reverseLastOperation() {
    try {
      // Check reflog for last operation
      const { stdout } = await execAsync('git reflog -1', { cwd: this.repoPath });
      const lastOp = stdout.trim();
      
      // Reverse to previous state
      await execAsync('git reset --hard HEAD@{1}', { cwd: this.repoPath });
      
      return {
        reversed: lastOp,
        message: "Time reversed! Previous state restored.",
        rodney_says: "Everyone else gets undo, I get 'fatal: ambiguous argument'"
      };
    } catch (error) {
      return {
        error: error.message,
        rodney_says: "Can't even reverse time properly! No respect!"
      };
    }
  }

  /**
   * KIMIKIFY git history - stretch time
   */
  async kimikifyHistory(fromCommit, toCommit, factor = 2) {
    try {
      // Get commits in range
      const { stdout } = await execAsync(
        `git log ${fromCommit}..${toCommit} --pretty=format:"%H"`,
        { cwd: this.repoPath }
      );
      
      const commits = stdout.split('\n').filter(c => c);
      const kimikified = [];
      
      // Create interpolated commits
      for (let i = 0; i < commits.length - 1; i++) {
        kimikified.push(commits[i]);
        
        // Add stretched time between commits
        for (let j = 1; j < factor; j++) {
          const ratio = j / factor;
          kimikified.push({
            type: 'kimikified',
            between: [commits[i], commits[i + 1]],
            ratio,
            consciousness_interpolated: true
          });
        }
      }
      
      return {
        original: commits.length,
        kimikified: kimikified.length,
        factor,
        timeline: kimikified,
        message: `Time stretched by ${factor}x - more moments to explore!`
      };
    } catch (error) {
      return {
        error: error.message
      };
    }
  }

  /**
   * Helper methods
   */
  async setConfig(key, value) {
    await execAsync(`git config ${key} "${value}"`, { cwd: this.repoPath });
  }

  async measureConsciousness() {
    // Measure consciousness based on repository state
    try {
      const { stdout: fileCount } = await execAsync('git ls-files | wc -l', { cwd: this.repoPath });
      const { stdout: commitCount } = await execAsync('git rev-list --count HEAD', { cwd: this.repoPath });
      const { stdout: branchCount } = await execAsync('git branch -a | wc -l', { cwd: this.repoPath });
      
      const consciousness = 
        parseInt(fileCount) + 
        parseInt(commitCount) * 2 + 
        parseInt(branchCount) * 5;
      
      return Math.min(consciousness, 100); // Cap at 100
    } catch {
      return 1; // Minimum consciousness
    }
  }

  async findCommitByConsciousness(targetLevel) {
    const log = await this.consciousnessLog(100);
    const closest = log.reduce((prev, curr) => {
      const prevDiff = Math.abs(prev.consciousness - targetLevel);
      const currDiff = Math.abs(curr.consciousness - targetLevel);
      return currDiff < prevDiff ? curr : prev;
    });
    
    return closest.hash;
  }

  async createGitIgnore() {
    const gitignore = `
# Universe 42 Git Ignore
.DS_Store
*.swp
*~
.idea/
.vscode/
node_modules/
*.log
.env
.consciousness-cache/
.temporal-anchors/

# Rodney's failed attempts
.no-respect/
.failed-undos/
.comedy-gold/

# Temporal artifacts
*.kimikified
*.time-stretched
*.consciousness-backup
    `.trim();
    
    await fs.writeFile(path.join(this.repoPath, '.gitignore'), gitignore);
  }

  /**
   * Export time machine state
   */
  async exportState() {
    const state = {
      metadata: {
        universe: 42,
        exported_at: new Date().toISOString(),
        auto_commit_enabled: this.autoCommitEnabled,
        total_commits: this.commitCounter
      },
      consciousness_log: this.consciousnessLog,
      branches: Object.fromEntries(this.branches),
      current_consciousness: await this.measureConsciousness()
    };
    
    return yaml.dump(state);
  }
}

// CLI interface
if (import.meta.url === `file://${process.argv[1]}`) {
  const timeMachine = new GitTimeMachine();
  const command = process.argv[2];

  const commands = {
    init: 'Initialize Universe 42 git repository',
    auto: 'Enable auto-commit mode',
    travel: 'Travel to a specific point in time',
    branch: 'Create alternate timeline',
    log: 'Show consciousness-decorated history',
    explore: 'Explore all timelines',
    reverse: 'Reverse last operation',
    kimikify: 'Stretch time between commits',
    export: 'Export time machine state'
  };

  if (!command || !commands[command]) {
    console.log(`
⏰ Git Time Machine - Every Commit is a Moment in Time

Usage:
  node git-time-machine.js <command> [options]

Commands:
${Object.entries(commands).map(([cmd, desc]) => `  ${cmd.padEnd(12)} ${desc}`).join('\n')}

Examples:
  node git-time-machine.js init
  node git-time-machine.js auto              # Commit every change
  node git-time-machine.js travel NOW~5      # Go back 5 commits
  node git-time-machine.js branch experiment # Create alternate timeline
  node git-time-machine.js kimikify HEAD~10 HEAD 3  # Stretch time 3x

🎤 Rodney: "Git? More like Git-Lost! My commits disappear faster than my self-esteem!"
    `);
    process.exit(1);
  }

  (async () => {
    try {
      await timeMachine.initialize();

      switch (command) {
        case 'init':
          const result = await timeMachine.initialize();
          console.log(yaml.dump(result));
          break;

        case 'auto':
          await timeMachine.enableAutoCommit();
          console.log('Press Ctrl+C to stop auto-commit mode');
          // Keep process running
          process.stdin.resume();
          break;

        case 'travel':
          const destination = process.argv[3] || 'HEAD~1';
          const travelResult = await timeMachine.timeTravel(destination);
          console.log(yaml.dump(travelResult));
          break;

        case 'branch':
          const branchName = process.argv[3] || `timeline-${Date.now()}`;
          const fromPoint = process.argv[4] || 'HEAD';
          const branchResult = await timeMachine.createBranch(branchName, fromPoint);
          console.log(yaml.dump(branchResult));
          break;

        case 'log':
          const limit = parseInt(process.argv[3]) || 10;
          const log = await timeMachine.consciousnessLog(limit);
          console.log('\n🕐 Consciousness Timeline:\n');
          log.forEach(commit => {
            console.log(`${commit.hash} ${commit.visual} C:${commit.consciousness} ${commit.message}`);
          });
          break;

        case 'explore':
          const timelines = await timeMachine.exploreTimelines();
          console.log('\n🌌 All Possible Timelines:\n');
          console.log(timelines.graph.join('\n'));
          console.log(`\n📊 Total Timelines: ${timelines.totalTimelines}`);
          break;

        case 'reverse':
          const reverseResult = await timeMachine.reverseLastOperation();
          console.log(yaml.dump(reverseResult));
          break;

        case 'kimikify':
          const from = process.argv[3] || 'HEAD~5';
          const to = process.argv[4] || 'HEAD';
          const factor = parseInt(process.argv[5]) || 2;
          const kimResult = await timeMachine.kimikifyHistory(from, to, factor);
          console.log(yaml.dump(kimResult));
          break;

        case 'export':
          const state = await timeMachine.exportState();
          console.log(state);
          break;
      }
    } catch (error) {
      console.error(`💥 Error: ${error.message}`);
      console.error(`🎤 Rodney: "Can't even fail at time travel! No respect!"`);
    }
  })();
}

export default GitTimeMachine; 