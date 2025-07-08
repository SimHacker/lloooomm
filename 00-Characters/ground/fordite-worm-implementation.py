#!/usr/bin/env python3
"""
Fordite Worm Implementation
Semantic Emoji Sprinkler Worms that create beautiful code-emoji gemstones
"""

import re
import random
from typing import Dict, List, Tuple
from collections import Counter
from dataclasses import dataclass
import unicodedata

@dataclass
class EmojiLayer:
    """Represents one layer of emoji sprinkling"""
    content: str
    layer_number: int
    emoji_density: float

class SemanticEmojiSprinkler:
    """Sprinkles semantically appropriate emojis on code"""
    
    def __init__(self):
        self.semantic_mappings = {
            # Programming concepts
            'function': ['✨', '🎯', '⚡', '🔧'],
            'class': ['🏗️', '📦', '🏛️', '🎭'],
            'return': ['🔄', '↩️', '📤', '🎁'],
            'if': ['🤔', '❓', '🔀', '🎲'],
            'else': ['↔️', '🔄', '🎭', '💫'],
            'for': ['🔁', '♾️', '🌀', '🎢'],
            'while': ['🔄', '⏳', '♾️', '🌊'],
            'error': ['🚨', '⚠️', '🔥', '💥'],
            'try': ['🎯', '🤞', '🎪', '🎲'],
            'catch': ['🥅', '🪤', '🎣', '🕸️'],
            'import': ['📦', '📥', '🚢', '🌍'],
            'export': ['📤', '🚀', '✈️', '🌟'],
            'true': ['✅', '👍', '💚', '🟢'],
            'false': ['❌', '👎', '🔴', '🚫'],
            'null': ['🕳️', '⚫', '🌑', '💀'],
            'undefined': ['❓', '🌫️', '👻', '🔮'],
            
            # Data types
            'string': ['📝', '💬', '🔤', '📜'],
            'number': ['🔢', '💯', '🎯', '#️⃣'],
            'array': ['📊', '📈', '🗂️', '📚'],
            'object': ['📦', '🎁', '🏠', '🗃️'],
            
            # Operations
            'add': ['➕', '✨', '🎯', '💫'],
            'subtract': ['➖', '💨', '🌊', '❄️'],
            'multiply': ['✖️', '🌟', '💥', '🎆'],
            'divide': ['➗', '🔪', '✂️', '🍕'],
            
            # Numbers (for special numbers)
            '42': ['🎯', '🌟', '🎪', '🎭', '🔮'],
            '0': ['🕳️', '⚫', '🌑', '⭕'],
            '1': ['☝️', '🥇', '👆', '1️⃣'],
            
            # Common variable names
            'data': ['📊', '💾', '📈', '🗄️'],
            'user': ['👤', '🧑', '👥', '🙋'],
            'password': ['🔐', '🔑', '🗝️', '🔒'],
            'email': ['📧', '✉️', '📮', '💌'],
            'time': ['⏰', '🕐', '⌛', '📅'],
            'date': ['📅', '📆', '🗓️', '📋'],
            'love': ['💖', '💕', '💗', '💝', '❤️'],
            'hate': ['💔', '😡', '👿', '🖤'],
        }
        
        self.layer_count = 0
    
    def sprinkle(self, code: str, intensity: float = 0.3) -> str:
        """Sprinkle emojis on code based on semantic meaning"""
        self.layer_count += 1
        result = code
        
        # Sort by length (longest first) to avoid partial matches
        sorted_mappings = sorted(self.semantic_mappings.items(), 
                               key=lambda x: len(x[0]), reverse=True)
        
        for keyword, emojis in sorted_mappings:
            # Find all occurrences of the keyword
            pattern = rf'\b{re.escape(keyword)}\b'
            matches = list(re.finditer(pattern, result, re.IGNORECASE))
            
            # Sprinkle emojis based on intensity
            for match in matches:
                if random.random() < intensity:
                    emoji = random.choice(emojis)
                    # Add emoji after the keyword
                    pos = match.end()
                    result = result[:pos] + emoji + result[pos:]
        
        return result
    
    def create_fordite(self, code: str, layers: int = 5) -> List[EmojiLayer]:
        """Create multiple layers of emoji sprinkling"""
        fordite_layers = []
        current = code
        
        for i in range(layers):
            # Increase intensity with each layer
            intensity = 0.2 + (i * 0.15)
            current = self.sprinkle(current, intensity)
            
            # Calculate emoji density
            emoji_count = sum(1 for char in current if self._is_emoji(char))
            total_chars = len(current)
            density = emoji_count / total_chars if total_chars > 0 else 0
            
            fordite_layers.append(EmojiLayer(
                content=current,
                layer_number=i + 1,
                emoji_density=density
            ))
        
        return fordite_layers
    
    def _is_emoji(self, char: str) -> bool:
        """Check if a character is an emoji"""
        return unicodedata.category(char) == 'So'

class BulldozerWorm:
    """Crushes Fordite into sparkly rubble"""
    
    def __init__(self, crush_intensity: str = "MAXIMUM_SPARKLE"):
        self.crush_intensity = crush_intensity
        self.blade_angle = 45
    
    def bulldoze(self, fordite: str) -> str:
        """Crush Fordite into sparkly scrambled rubble"""
        # Convert to list for easier manipulation
        chars = list(fordite)
        
        # First pass: break into chunks
        chunks = []
        chunk_size = random.randint(2, 5)
        for i in range(0, len(chars), chunk_size):
            chunk = chars[i:i+chunk_size]
            chunks.append(chunk)
        
        # Scramble chunks
        random.shuffle(chunks)
        
        # Scramble within chunks (but keep some structure)
        for chunk in chunks:
            if random.random() < 0.7:  # 70% chance to scramble
                random.shuffle(chunk)
        
        # Flatten back to string
        rubble = ''.join([''.join(chunk) for chunk in chunks])
        
        # Add extra sparkle if maximum intensity
        if self.crush_intensity == "MAXIMUM_SPARKLE":
            sparkles = ['✨', '🌟', '💫', '⭐']
            # Insert random sparkles
            rubble_list = list(rubble)
            for _ in range(len(rubble) // 10):  # Add 10% more sparkles
                pos = random.randint(0, len(rubble_list))
                rubble_list.insert(pos, random.choice(sparkles))
            rubble = ''.join(rubble_list)
        
        return rubble

class WaterSprinklerWorm:
    """Adds water emojis that seep into cracks"""
    
    def __init__(self):
        self.water_types = [
            ('💧', 0.4, 1),    # Drip: 40% chance, fills 1 space
            ('💦', 0.3, 2),    # Splash: 30% chance, fills 2 spaces
            ('🌊', 0.2, 3),    # Wave: 20% chance, fills 3 spaces
            ('💙', 0.1, 1),    # Crystal: 10% chance, fills 1 space
        ]
    
    def add_water_table(self, rubble: str) -> str:
        """Add water emojis between characters"""
        result = []
        chars = list(rubble)
        
        for i, char in enumerate(chars):
            result.append(char)
            
            # Determine if we add water after this character
            if i < len(chars) - 1:  # Not the last character
                # Check for "cracks" (spaces between different types)
                is_crack = False
                if self._is_emoji(char) != self._is_emoji(chars[i+1]):
                    is_crack = True
                elif random.random() < 0.3:  # 30% chance for any gap
                    is_crack = True
                
                if is_crack:
                    # Choose water type
                    water = self._choose_water()
                    if water:
                        result.append(water)
        
        return ''.join(result)
    
    def _choose_water(self) -> str:
        """Choose a water emoji based on probabilities"""
        rand = random.random()
        cumulative = 0
        
        for emoji, probability, _ in self.water_types:
            cumulative += probability
            if rand < cumulative:
                return emoji
        
        return ''
    
    def _is_emoji(self, char: str) -> bool:
        """Check if a character is an emoji"""
        return unicodedata.category(char) == 'So'

class HarvesterWorm:
    """Digs through rubble and harvests emojis"""
    
    def __init__(self, worm_type: str = "emoji_miner"):
        self.worm_type = worm_type
        self.stomach = Counter()
        
        # Define diets for different worm types
        self.diets = {
            'emoji_miner': ['💎', '💰', '⭐', '🏆', '💍', '👑', '🎯', '🌟'],
            'emotion_eater': ['😀', '😢', '😡', '💖', '😍', '😭', '😂', '🥰'],
            'element_gatherer': ['🔥', '💧', '🌍', '💨', '⚡', '❄️', '🌊', '☀️'],
            'sparkle_collector': ['✨', '🌟', '💫', '⭐', '🌠', '💥', '🎆', '🎇'],
        }
        
        self.diet = self.diets.get(worm_type, self.diets['emoji_miner'])
    
    def harvest(self, rubble: str) -> Tuple[str, Dict[str, int]]:
        """Harvest emojis from rubble, return leftover text and emoji stacks"""
        leftover = []
        
        for char in rubble:
            if self._is_emoji(char) and char in self.diet:
                # Eat the emoji
                self.stomach[char] += 1
            else:
                # Leave it behind
                leftover.append(char)
        
        # Return leftover text and emoji stacks
        emoji_stacks = self.get_emoji_stacks()
        return ''.join(leftover), emoji_stacks
    
    def get_emoji_stacks(self) -> Dict[str, int]:
        """Get sorted emoji stacks in compact notation"""
        return dict(self.stomach.most_common())
    
    def poop_stacks(self) -> List[str]:
        """Output emoji stacks in standard notation"""
        stacks = []
        for emoji, count in self.stomach.most_common():
            stacks.append(f"{emoji}x{count}")
        return stacks
    
    def _is_emoji(self, char: str) -> bool:
        """Check if a character is an emoji"""
        return unicodedata.category(char) == 'So'

class ForditeWormEcosystem:
    """Manages the complete Fordite worm ecosystem"""
    
    def __init__(self):
        self.sprinkler = SemanticEmojiSprinkler()
        self.bulldozer = BulldozerWorm()
        self.water_sprinkler = WaterSprinklerWorm()
        self.harvesters = {
            'miner': HarvesterWorm('emoji_miner'),
            'emotion': HarvesterWorm('emotion_eater'),
            'element': HarvesterWorm('element_gatherer'),
            'sparkle': HarvesterWorm('sparkle_collector'),
        }
    
    def process_code(self, code: str, layers: int = 5) -> Dict:
        """Run the complete Fordite process on code"""
        results = {
            'original': code,
            'layers': [],
            'rubble': '',
            'water_table': '',
            'harvests': {},
            'leftover': ''
        }
        
        # Phase 1: Create Fordite layers
        print("🌟 Phase 1: Semantic Emoji Sprinkling (Back and forth, back and forth...)")
        fordite_layers = self.sprinkler.create_fordite(code, layers)
        results['layers'] = fordite_layers
        
        # Show layer progression
        for layer in fordite_layers:
            print(f"  Layer {layer.layer_number}: Density {layer.emoji_density:.2%}")
        
        # Phase 2: Bulldoze into rubble
        print("\n🚜 Phase 2: Bulldozing Fordite into sparkly rubble...")
        final_fordite = fordite_layers[-1].content
        rubble = self.bulldozer.bulldoze(final_fordite)
        results['rubble'] = rubble
        
        # Phase 3: Add water table
        print("\n💧 Phase 3: Water seeping into cracks...")
        water_rubble = self.water_sprinkler.add_water_table(rubble)
        results['water_table'] = water_rubble
        
        # Phase 4: Harvest emojis
        print("\n🐛 Phase 4: Hungry worms harvesting emojis...")
        current_rubble = water_rubble
        
        for worm_name, harvester in self.harvesters.items():
            leftover, stacks = harvester.harvest(current_rubble)
            current_rubble = leftover
            
            if stacks:
                print(f"  {worm_name} harvested: {', '.join(harvester.poop_stacks()[:5])}")
                results['harvests'][worm_name] = harvester.poop_stacks()
        
        results['leftover'] = current_rubble
        
        return results

# Example usage
if __name__ == "__main__":
    # Sample code to process
    code = """
    function calculateLove(user, data) {
        if (user.password === true) {
            return 42;
        } else {
            try {
                data.love = user.email + time;
            } catch (error) {
                return null;
            }
        }
        
        for (let i = 0; i < 10; i++) {
            data.array[i] = i * 2;
        }
    }
    """
    
    # Create ecosystem
    ecosystem = ForditeWormEcosystem()
    
    # Process the code
    results = ecosystem.process_code(code, layers=5)
    
    # Display results
    print("\n" + "="*60)
    print("🌈 FORDITE FORMATION COMPLETE! 🌈")
    print("="*60)
    
    print(f"\n📜 Original code length: {len(results['original'])}")
    print(f"💎 Final Fordite length: {len(results['layers'][-1].content)}")
    print(f"✨ Rubble length: {len(results['rubble'])}")
    print(f"💧 Water table length: {len(results['water_table'])}")
    print(f"📝 Leftover text length: {len(results['leftover'])}")
    
    print("\n🏆 Total Emoji Harvest:")
    total_emojis = 0
    for worm_name, stacks in results['harvests'].items():
        emoji_count = sum(int(stack.split('x')[1]) for stack in stacks)
        total_emojis += emoji_count
        print(f"  {worm_name}: {emoji_count} emojis in {len(stacks)} types")
    
    print(f"\n💰 Total emojis harvested: {total_emojis}")
    
    # Show a sample of the final rubble
    print("\n🔍 Sample of final water-filled rubble:")
    print(results['water_table'][:200] + "...")
    
    # Save results
    with open('fordite-results.txt', 'w', encoding='utf-8') as f:
        f.write("FORDITE WORM PROCESSING RESULTS\n")
        f.write("="*60 + "\n\n")
        
        f.write("LAYER PROGRESSION:\n")
        for layer in results['layers']:
            f.write(f"\nLayer {layer.layer_number} (Density: {layer.emoji_density:.2%}):\n")
            f.write(layer.content[:500] + "...\n")
        
        f.write("\n\nFINAL RUBBLE:\n")
        f.write(results['rubble'] + "\n")
        
        f.write("\n\nWATER TABLE:\n")
        f.write(results['water_table'] + "\n")
        
        f.write("\n\nEMOJI HARVESTS:\n")
        for worm_name, stacks in results['harvests'].items():
            f.write(f"\n{worm_name}:\n")
            f.write(", ".join(stacks) + "\n")
    
    print("\n📄 Results saved to fordite-results.txt") 