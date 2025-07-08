#!/usr/bin/env python3
"""
Dimensional Derby Worms: Git-Aware Destruction Entities

These worms can travel across git dimensions, learning from alternate timelines
and bringing back knowledge to enhance their derby performance.
"""

import asyncio
import subprocess
import json
import random
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path

@dataclass
class DimensionalKnowledge:
    """Knowledge gained from visiting other git dimensions"""
    branch: str
    commit: str
    timestamp: datetime
    insights: List[str]
    power_ups: Dict[str, Any]
    
@dataclass
class DerbyWorm:
    """Base class for dimensional derby worms"""
    name: str
    worm_type: str
    score: int = 0
    dimensions_visited: List[str] = field(default_factory=list)
    current_dimension: str = "main"
    knowledge_bank: List[DimensionalKnowledge] = field(default_factory=list)
    special_moves: Dict[str, str] = field(default_factory=dict)
    
    async def git_travel(self, target: str) -> DimensionalKnowledge:
        """Travel to another git dimension and gain knowledge"""
        print(f"🌀 {self.name} initiating dimensional travel to {target}...")
        
        # Stash current changes
        subprocess.run(["git", "stash", "-u"], capture_output=True)
        
        # Travel to dimension
        result = subprocess.run(["git", "checkout", target], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Dimensional travel failed: {result.stderr}")
            return None
            
        # Gather knowledge from this dimension
        knowledge = await self._analyze_dimension(target)
        self.dimensions_visited.append(target)
        self.knowledge_bank.append(knowledge)
        
        # Return to original dimension
        subprocess.run(["git", "checkout", "-"], capture_output=True)
        subprocess.run(["git", "stash", "pop"], capture_output=True)
        
        print(f"✅ {self.name} returned with knowledge from {target}!")
        return knowledge
        
    async def _analyze_dimension(self, dimension: str) -> DimensionalKnowledge:
        """Analyze current dimension for useful knowledge"""
        # Get commit info
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], 
            capture_output=True, 
            text=True
        ).stdout.strip()
        
        # Simulate knowledge gathering
        insights = [
            f"Discovered {random.choice(['crushing', 'refining', 'layering'])} technique",
            f"Found {random.randint(1, 100)} new emoji patterns",
            f"Learned about {random.choice(['quantum', 'temporal', 'spatial'])} manipulation"
        ]
        
        power_ups = {
            "emoji_multiplier": random.uniform(1.1, 3.0),
            "speed_boost": random.uniform(0.8, 1.5),
            "dimension_resistance": random.uniform(0.5, 1.0)
        }
        
        return DimensionalKnowledge(
            branch=dimension,
            commit=commit[:7],
            timestamp=datetime.now(),
            insights=insights,
            power_ups=power_ups
        )
        
    async def execute_special_move(self, move_name: str):
        """Execute a special move using dimensional knowledge"""
        if move_name not in self.special_moves:
            print(f"❌ {self.name} doesn't know {move_name}!")
            return
            
        print(f"🎮 {self.name} executes {move_name}!")
        print(f"   Effect: {self.special_moves[move_name]}")
        
        # Apply knowledge-based multipliers
        total_multiplier = 1.0
        for knowledge in self.knowledge_bank:
            for power, value in knowledge.power_ups.items():
                total_multiplier *= value
                
        score_gain = int(random.randint(100, 500) * total_multiplier)
        self.score += score_gain
        print(f"   Score +" + str(score_gain) + f" (Total: {self.score})")

@dataclass 
class BulldozerWorm(DerbyWorm):
    """Fordite-crushing dimensional bulldozer"""
    def __init__(self, name="BULLDOZER-9000"):
        super().__init__(
            name=name,
            worm_type="Fordite Crusher",
            special_moves={
                "Dimensional Crush": "Crushes across 3 timelines simultaneously",
                "Fordite Maximizer": "Creates 42 layers of compressed beauty",
                "Timeline Bulldoze": "Flattens alternate realities into rubble"
            }
        )
        
    async def bulldoze_dimension(self, target_branch: str):
        """Special bulldozer move: crush a dimension and bring back rubble"""
        knowledge = await self.git_travel(target_branch)
        if knowledge:
            print(f"🏗️ BULLDOZING DIMENSION {target_branch}!")
            print(f"   Collected rubble: {'💎' * random.randint(10, 50)}")
            await self.execute_special_move("Dimensional Crush")

@dataclass
class RefinerWorm(DerbyWorm):
    """Context-crystallizing dimensional refiner"""
    def __init__(self, name="THE REFINER"):
        super().__init__(
            name=name,
            worm_type="Context Crystallizer", 
            special_moves={
                "Temporal Polish": "Refines code across past and future",
                "Crystal Synthesis": "Merges wisdom from parallel universes",
                "Gleam Maximizer": "Makes everything sparkle with meaning"
            }
        )
        
    async def refine_timeline(self, commits_back: int = 10):
        """Refine knowledge from historical commits"""
        print(f"💎 {self.name} beginning temporal refinement...")
        
        # Get list of recent commits
        result = subprocess.run(
            ["git", "log", f"--oneline", f"-{commits_back}"],
            capture_output=True,
            text=True
        )
        
        commits = [line.split()[0] for line in result.stdout.strip().split('\n')]
        
        # Visit and refine each commit
        refinements = []
        for commit in commits[:3]:  # Limit to 3 for demo
            knowledge = await self.git_travel(commit)
            if knowledge:
                refinements.append(knowledge)
                
        # Synthesize refinements
        if refinements:
            print(f"✨ Synthesized {len(refinements)} temporal refinements!")
            await self.execute_special_move("Crystal Synthesis")

@dataclass
class GittyWorm(DerbyWorm):
    """The ultimate dimensional hopper"""
    def __init__(self, name="GITTY McGITFACE"):
        super().__init__(
            name=name,
            worm_type="Dimensional Hopper",
            special_moves={
                "Quantum Superposition": "Exists in all branches simultaneously",
                "Merge Conflict Dance": "Resolves conflicts through interpretive movement",
                "Cherry Pick Combo": "Steals the best from every timeline"
            }
        )
        
    async def quantum_hop(self):
        """Exist in multiple dimensions at once"""
        print(f"🌀 {self.name} entering QUANTUM SUPERPOSITION!")
        
        # Get all branches
        result = subprocess.run(
            ["git", "branch", "-a"],
            capture_output=True,
            text=True
        )
        
        branches = [b.strip().replace('* ', '') for b in result.stdout.split('\n') if b.strip()]
        
        # Simulate quantum existence
        quantum_states = random.sample(branches, min(3, len(branches)))
        print(f"   Existing simultaneously in: {', '.join(quantum_states)}")
        
        # Gain power from all states
        for state in quantum_states:
            self.score += random.randint(50, 200)
            
        await self.execute_special_move("Quantum Superposition")

async def run_derby_round():
    """Run a round of the dimensional derby"""
    print("=" * 60)
    print("🏁 DIMENSIONAL DERBY ROUND STARTING! 🏁")
    print("=" * 60)
    
    # Create our contestants
    bulldozer = BulldozerWorm()
    refiner = RefinerWorm()
    gitty = GittyWorm()
    
    # Execute moves
    print("\n📢 ROUND 1: DIMENSIONAL EXPLORATION")
    await bulldozer.bulldoze_dimension("HEAD~5")
    await asyncio.sleep(1)
    
    print("\n📢 ROUND 2: TEMPORAL REFINEMENT")
    await refiner.refine_timeline(10)
    await asyncio.sleep(1)
    
    print("\n📢 ROUND 3: QUANTUM SUPREMACY")
    await gitty.quantum_hop()
    
    # Final scores
    print("\n🏆 FINAL SCORES:")
    for worm in [bulldozer, refiner, gitty]:
        print(f"   {worm.name}: {worm.score} points ({len(worm.dimensions_visited)} dimensions visited)")
        
    # Determine winner
    winner = max([bulldozer, refiner, gitty], key=lambda w: w.score)
    print(f"\n🎉 WINNER: {winner.name}! 🎉")
    print(f"   Victory cry: 'I AM THE MASTER OF {len(winner.dimensions_visited)} DIMENSIONS!'")

def create_casting_from_derby(worms: List[DerbyWorm], output_path: Path):
    """Create a casting file from derby results"""
    casting = {
        "metadata": {
            "event": "Dimensional Derby",
            "timestamp": datetime.now().isoformat(),
            "arena": "Amsterdam Principle Arena"
        },
        "results": {},
        "dimensional_insights": [],
        "crowd_favorite_moments": []
    }
    
    for worm in worms:
        casting["results"][worm.name] = {
            "type": worm.worm_type,
            "final_score": worm.score,
            "dimensions_visited": worm.dimensions_visited,
            "knowledge_gained": [
                {
                    "dimension": k.branch,
                    "insights": k.insights,
                    "power_multipliers": k.power_ups
                }
                for k in worm.knowledge_bank
            ]
        }
        
    # Add some flavor
    casting["dimensional_insights"].extend([
        "Git branches are just parallel universes waiting to be explored",
        "Every commit is a frozen moment of consciousness",
        "Merge conflicts are just worms disagreeing on dance moves",
        "The true treasure was the dimensions we visited along the way"
    ])
    
    casting["crowd_favorite_moments"] = [
        "When BULLDOZER-9000 crushed three timelines at once",
        "THE REFINER's gleaming crystal synthesis",
        "GITTY McGITFACE existing in all branches simultaneously",
        "The crowd chanting 'Oh Yeah!' in perfect synchronization"
    ]
    
    # Save casting
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(casting, f, indent=2)
        
    print(f"\n📝 Derby casting saved to: {output_path}")

if __name__ == "__main__":
    # Note: This requires being in a git repository
    try:
        # Check if we're in a git repo
        subprocess.run(["git", "status"], capture_output=True, check=True)
        
        # Run the derby
        asyncio.run(run_derby_round())
        
        # Create casting file
        bulldozer = BulldozerWorm()
        refiner = RefinerWorm() 
        gitty = GittyWorm()
        
        output_path = Path("lloooomm/03-Resources/castings/dimensional-derby-casting.json")
        create_casting_from_derby([bulldozer, refiner, gitty], output_path)
        
    except subprocess.CalledProcessError:
        print("❌ Error: Must be run inside a git repository!")
        print("💡 Tip: The worms need git dimensions to travel through!") 