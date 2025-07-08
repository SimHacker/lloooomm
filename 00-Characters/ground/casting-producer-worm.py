#!/usr/bin/env python3
"""
Casting Producer Worm - MapReduce Vermicular Style
Demonstrates DIGEST -> PERISTALSIS -> COMPOST -> CASTINGS
"""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict
import hashlib

@dataclass
class CastingMetadata:
    """Metadata for each casting produced"""
    casting_id: str
    produced_by: str
    timestamp: datetime
    source: Dict[str, Any]
    digestion_stats: Dict[str, Any]
    worm_preferences: Dict[str, Any]

class VermicularMapReduce:
    """MapReduce but with WORMS! 🪱"""
    
    def __init__(self, worm_name: str, preferences: Dict[str, Any]):
        self.worm_name = worm_name
        self.preferences = preferences
        self.casting_number = 0
        self.digestion_stats = defaultdict(int)
        
        # Yello - Oh Yeah! counter
        self.oh_yeah_counter = 0
        
    def digest_phase(self, document: str, source_info: Dict) -> List[Tuple[str, Any]]:
        """
        MAP PHASE -> DIGEST PHASE
        Worms digest input into key-value nutrients
        """
        print("🪱 DIGEST PHASE: Breaking down document...")
        nutrients = []
        
        lines = document.split('\n')
        for line_num, line in enumerate(lines):
            # Extract nutrients based on worm preferences
            if self._matches_preferences(line):
                nutrient_type = self._classify_nutrient(line)
                nutrient_value = {
                    'content': line,
                    'line_number': line_num,
                    'source': source_info['file'],
                    'extracted_at': datetime.now().isoformat()
                }
                nutrients.append((nutrient_type, nutrient_value))
                self.digestion_stats['nutrients_extracted'] += 1
        
        self.digestion_stats['bytes_consumed'] += len(document)
        return nutrients
    
    def peristalsis_phase(self, nutrients: List[Tuple[str, Any]]) -> Dict[str, List[Any]]:
        """
        SHUFFLE & SORT -> PERISTALSIS
        Wave-like contractions group similar nutrients
        """
        print("🌊 PERISTALSIS PHASE: Muscle waves grouping nutrients...")
        
        # Group by nutrient type (peristaltic sorting)
        grouped = defaultdict(list)
        for nutrient_type, value in nutrients:
            grouped[nutrient_type].append(value)
        
        # Sort within groups (rhythmic contractions)
        for nutrient_type in grouped:
            grouped[nutrient_type].sort(key=lambda x: x['line_number'])
        
        # Check for Oh Yeah moment
        if len(nutrients) > 100:
            self._play_oh_yeah()
        
        return dict(grouped)
    
    def compost_phase(self, grouped_nutrients: Dict[str, List[Any]]) -> Dict[str, Any]:
        """
        REDUCE -> COMPOST
        Final composting produces enriched output
        """
        print("🌱 COMPOST PHASE: Enriching nutrients...")
        
        composted = {}
        for nutrient_type, values in grouped_nutrients.items():
            # Different composting strategies based on type
            if nutrient_type == 'function':
                composted[nutrient_type] = self._compost_functions(values)
            elif nutrient_type == 'pattern':
                composted[nutrient_type] = self._compost_patterns(values)
            elif nutrient_type == 'error':
                composted[nutrient_type] = self._compost_errors(values)
            else:
                composted[nutrient_type] = self._default_compost(values)
        
        return composted
    
    def produce_casting(self, composted: Dict[str, Any], source_info: Dict) -> str:
        """
        OUTPUT -> CASTING
        Produce nutrient-rich casting file
        """
        self.casting_number += 1
        casting_id = f"{self.worm_name}-casting-{self.casting_number:03d}"
        
        print(f"💩 PRODUCING CASTING: {casting_id}")
        
        # Create casting metadata
        metadata = CastingMetadata(
            casting_id=casting_id,
            produced_by=self.worm_name,
            timestamp=datetime.now(),
            source=source_info,
            digestion_stats=dict(self.digestion_stats),
            worm_preferences=self.preferences
        )
        
        # Prepare casting content
        casting = {
            'metadata': {
                'casting_id': metadata.casting_id,
                'produced_by': metadata.produced_by,
                'timestamp': metadata.timestamp.isoformat(),
                'source': metadata.source,
                'digestion_stats': metadata.digestion_stats,
                'worm_preferences': metadata.worm_preferences
            },
            'enriched_content': composted
        }
        
        # Save casting
        casting_file = Path(f"{casting_id}.yml")
        with open(casting_file, 'w') as f:
            yaml.dump(casting, f, default_flow_style=False)
        
        # Check for Oh Yeah moment
        if self.casting_number % 100 == 0:
            self._play_oh_yeah()
        
        return str(casting_file)
    
    def _matches_preferences(self, line: str) -> bool:
        """Check if line matches worm preferences"""
        for pattern in self.preferences.get('favorite_patterns', []):
            if pattern in line:
                return True
        return False
    
    def _classify_nutrient(self, line: str) -> str:
        """Classify the type of nutrient"""
        if 'function' in line:
            return 'function'
        elif 'error' in line.lower() or 'exception' in line.lower():
            return 'error'
        elif any(p in line for p in ['TODO', 'FIXME', 'HACK']):
            return 'todo'
        else:
            return 'pattern'
    
    def _compost_functions(self, values: List[Dict]) -> Dict:
        """Special composting for functions"""
        return {
            'total_found': len(values),
            'locations': [{'file': v['source'], 'line': v['line_number']} for v in values],
            'summary': f"Found {len(values)} functions ready for enhancement"
        }
    
    def _compost_patterns(self, values: List[Dict]) -> Dict:
        """Special composting for patterns"""
        pattern_counts = defaultdict(int)
        for v in values:
            pattern_counts[v['content'].strip()] += 1
        
        return {
            'unique_patterns': len(pattern_counts),
            'most_common': sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)[:5],
            'total_occurrences': len(values)
        }
    
    def _compost_errors(self, values: List[Dict]) -> Dict:
        """Special composting for errors"""
        return {
            'error_count': len(values),
            'error_locations': [{'file': v['source'], 'line': v['line_number'], 'preview': v['content'][:50]} for v in values],
            'severity': 'high' if len(values) > 10 else 'medium'
        }
    
    def _default_compost(self, values: List[Dict]) -> List[Dict]:
        """Default composting strategy"""
        return values
    
    def _play_oh_yeah(self):
        """🎵 Oh Yeah by Yello moment! 🎵"""
        self.oh_yeah_counter += 1
        print("\n🎵 OH YEAH! 🎵")
        print("Boom boom boom boom...")
        print("Oh yeah... Oh yeah...")
        print(f"Beautiful... Powerful... (Moment #{self.oh_yeah_counter})\n")

class SpecializedCastingWorms:
    """Different worms with different collection preferences"""
    
    @staticmethod
    def create_code_composter():
        """Collects dead code and deprecated patterns"""
        return VermicularMapReduce(
            "code-composter",
            {
                'favorite_patterns': ['DEPRECATED', 'UNUSED', 'OLD', 'LEGACY'],
                'collection_type': 'dead_code',
                'casting_prefix': 'compost'
            }
        )
    
    @staticmethod
    def create_reference_librarian():
        """Collects imports and dependencies"""
        return VermicularMapReduce(
            "reference-librarian",
            {
                'favorite_patterns': ['import', 'require', 'include', 'from'],
                'collection_type': 'dependencies',
                'casting_prefix': 'bibliography'
            }
        )
    
    @staticmethod
    def create_pattern_miner():
        """Collects recurring patterns"""
        return VermicularMapReduce(
            "pattern-miner",
            {
                'favorite_patterns': ['function', 'class', 'const', 'let', 'var'],
                'collection_type': 'patterns',
                'casting_prefix': 'patterns'
            }
        )
    
    @staticmethod
    def create_bug_hunter():
        """Collects errors and exceptions"""
        return VermicularMapReduce(
            "bug-hunter",
            {
                'favorite_patterns': ['error', 'exception', 'throw', 'catch', 'bug', 'FIXME'],
                'collection_type': 'bugs',
                'casting_prefix': 'pest-control'
            }
        )

# Example usage
if __name__ == "__main__":
    # Create a pattern miner worm
    worm = SpecializedCastingWorms.create_pattern_miner()
    
    # Sample document
    document = """
    function calculateLove(user, data) {
        // TODO: Add more love
        if (user.loves_worms) {
            return 42;
        }
        throw new Error("Not enough worm love");
    }
    
    class WormManager {
        constructor() {
            this.worms = [];
        }
        
        function addWorm(worm) {
            // DEPRECATED: Use registerWorm instead
            this.worms.push(worm);
        }
    }
    
    const PATTERN = /worm/gi;
    let foundPatterns = [];
    """
    
    source_info = {
        'file': 'example.js',
        'line_range': [1, 25],
        'query': 'find all patterns'
    }
    
    # Run the MapReduce pipeline
    print("🪱 VERMICULAR MAPREDUCE STARTING...\n")
    
    # DIGEST (Map)
    nutrients = worm.digest_phase(document, source_info)
    print(f"Extracted {len(nutrients)} nutrients\n")
    
    # PERISTALSIS (Shuffle & Sort)
    grouped = worm.peristalsis_phase(nutrients)
    print(f"Grouped into {len(grouped)} nutrient types\n")
    
    # COMPOST (Reduce)
    composted = worm.compost_phase(grouped)
    print(f"Composted into enriched output\n")
    
    # PRODUCE CASTING (Output)
    casting_file = worm.produce_casting(composted, source_info)
    print(f"\n✅ Casting produced: {casting_file}")
    print("\n🪱 From Soil to Software: Worms Enrich Everything They Touch! 🪱") 