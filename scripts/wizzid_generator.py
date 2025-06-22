#!/usr/bin/env python3
"""
WIZZID Generator: Chess Piece Identification System
Creates memorable, humanized, and interoperable identifiers for chess pieces.
"""

import random
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class WizzidConfig:
    """Configuration for WIZZID generation"""
    piece_type: str
    position: Optional[str] = None
    color: Optional[str] = None
    nickname: Optional[str] = None

class WizzidGenerator:
    """Generates WIZZID identifiers for chess pieces"""
    
    def __init__(self):
        # Emoji categories for different dimensions
        self.character_emojis = [
            # People
            "👨", "👩", "👶", "👴", "👵", "👱‍♀️", "👳‍♂️", "👮‍♀️", "👷‍♂️", 
            "👨‍⚕️", "👩‍🏫", "👨‍🎨", "👩‍🎤", "👨‍🍳", "👩‍💻", "👨‍🚀", "👩‍🚒",
            # Animals
            "🐱", "🐶", "🐰", "🐼", "🐨", "🐯", "🦁", "🐸", "🐙", "🦄", 
            "🦒", "🦘", "🦔", "🦡", "🐨", "🐻", "🐺", "🦊", "🐹", "🐭",
            # Faces
            "😀", "😍", "🤔", "😴", "😤", "😭", "🤯", "😎", "🥺", "🤗", 
            "😇", "🤠", "😈", "👻", "🤖", "👽", "👾", "🤡", "💀", "👹",
            # Poses
            "🏃‍♀️", "🧘‍♀️", "💃", "🕺", "🤸‍♀️", "🏋️‍♂️", "🚶‍♀️", "🧍‍♂️",
            "🤾‍♀️", "🏊‍♀️", "🚴‍♀️", "⛷️", "🏂", "🏄‍♀️", "🏇", "🤺"
        ]
        
        self.food_emojis = [
            # Fruits
            "🍎", "🍌", "🍊", "🍇", "🍓", "🍑", "🥭", "🍍", "🥥", "🥝",
            "🍒", "🍐", "🍏", "🍋", "🍈", "🍉", "🍊", "🍋", "🍌", "🍍",
            # Vegetables
            "🥕", "🥦", "🥬", "🥒", "🍅", "🌽", "🥑", "🧅", "🧄", "🥔",
            "🍠", "🥜", "🌰", "🥜", "🌶️", "🥬", "🥒", "🍆", "🥑", "🥦",
            # Dishes
            "🍕", "🍔", "🌮", "🍜", "🍣", "🍙", "🍪", "🍰", "🍦", "🍺",
            "🍷", "🍸", "🍹", "🥤", "☕", "🍵", "🥛", "🍼", "🍶", "🍾",
            # Treats
            "🍫", "🍬", "🍭", "🍡", "🍧", "🍨", "🍩", "🍪", "🧁", "🍰",
            "🍮", "🍯", "🍯", "🍯", "🍯", "🍯", "🍯", "🍯", "🍯", "🍯"
        ]
        
        self.vehicle_emojis = [
            # Land
            "🚗", "🚕", "🚙", "🏎️", "🚓", "🚑", "🚒", "🚐", "🚚", "🚛",
            "🚜", "🏍️", "🛵", "🚲", "🛴", "🛹", "🛼", "🚁", "🚁", "🚁",
            # Air
            "✈️", "🛩️", "🚁", "🛸", "🚀", "🛰️", "🛫", "🛬", "🛥️", "🛥️",
            # Water
            "🚢", "⛵", "🛥️", "🚤", "🛶", "🚣‍♀️", "🚣‍♂️", "🏊‍♀️", "🏊‍♂️",
            # Space
            "🚀", "🛸", "🛰️", "🌍", "🌕", "⭐", "🌟", "🌙", "☀️", "🌎"
        ]
        
        self.abstract_emojis = [
            # Astronomy
            "🌟", "⭐", "🌙", "☀️", "🌍", "🌎", "🌏", "🌕", "🌖", "🌗", "🌘",
            "🌑", "🌒", "🌓", "🌔", "🌚", "🌝", "🌞", "🌛", "🌜", "🌡️",
            # Math/Symbols
            "➕", "➖", "✖️", "➗", "♾️", "∞", "≠", "≈", "≤", "≥", "±", "√",
            "∫", "∑", "∏", "∆", "∇", "∈", "∉", "⊂", "⊃", "∪", "∩",
            # Silly/Unique
            "💩", "🤡", "👻", "👽", "🤖", "🎭", "🎪", "🎨", "🎭", "🎪",
            "🎨", "🎭", "🎪", "🎨", "🎭", "🎪", "🎨", "🎭", "🎪", "🎨",
            # Abstract
            "💫", "✨", "🔥", "💧", "⚡", "🌈", "🎆", "🎇", "🎉", "🎊",
            "🎋", "🎍", "🎎", "🎏", "🎐", "🎀", "🎁", "🎂", "🎃", "🎄"
        ]
        
        # Piece type mappings
        self.piece_types = {
            'P': 'Pawn',
            'K': 'King', 
            'Q': 'Queen',
            'R': 'Rook',
            'B': 'Bishop',
            'N': 'Knight'
        }
        
        # Position mappings for pawns
        self.pawn_positions = {
            'a2': '1', 'b2': '2', 'c2': '3', 'd2': '4', 'e2': '5', 'f2': '6', 'g2': '7', 'h2': '8',
            'a7': '1', 'b7': '2', 'c7': '3', 'd7': '4', 'e7': '5', 'f7': '6', 'g7': '7', 'h7': '8'
        }
        
        # Track used WIZZIDs to ensure uniqueness
        self.used_wizzids = set()

    def generate_wizzid(self, config: WizzidConfig) -> str:
        """Generate a unique WIZZID for a chess piece"""
        
        piece_type = config.piece_type.upper()
        if piece_type not in self.piece_types:
            raise ValueError(f"Invalid piece type: {piece_type}")
        
        # Generate base WIZZID
        wizzid = self._generate_base_wizzid(piece_type)
        
        # Add position/enumeration if needed
        if config.position:
            wizzid = self._add_position_info(wizzid, config.position, piece_type)
        
        # Ensure uniqueness
        while wizzid in self.used_wizzids:
            wizzid = self._generate_base_wizzid(piece_type)
            if config.position:
                wizzid = self._add_position_info(wizzid, config.position, piece_type)
        
        self.used_wizzids.add(wizzid)
        return wizzid
    
    def _generate_base_wizzid(self, piece_type: str) -> str:
        """Generate the base WIZZID with 4 emojis"""
        character = random.choice(self.character_emojis)
        food = random.choice(self.food_emojis)
        vehicle = random.choice(self.vehicle_emojis)
        abstract = random.choice(self.abstract_emojis)
        
        return f"{piece_type}{character}{food}{vehicle}{abstract}{piece_type}"
    
    def _add_position_info(self, wizzid: str, position: str, piece_type: str) -> str:
        """Add position or enumeration information to WIZZID"""
        
        # For pawns, add position number
        if piece_type == 'P':
            if position in self.pawn_positions:
                return f"{wizzid}{self.pawn_positions[position]}"
        
        # For pairs (rooks, bishops, knights), add L/R designation
        if piece_type in ['R', 'B', 'N']:
            if position in ['a1', 'a8', 'c1', 'c8', 'b1', 'b8']:
                return f"{wizzid}L"  # Left
            elif position in ['h1', 'h8', 'f1', 'f8', 'g1', 'g8']:
                return f"{wizzid}R"  # Right
        
        return wizzid
    
    def parse_wizzid(self, wizzid: str) -> Dict:
        """Parse a WIZZID to extract its components"""
        if len(wizzid) < 6:
            raise ValueError(f"Invalid WIZZID format: {wizzid}")
        
        piece_type = wizzid[0]
        last_initial = wizzid[-1]
        
        # Extract emojis (everything between first and last character)
        emoji_part = wizzid[1:-1]
        
        # Try to extract individual emojis (this is approximate due to emoji complexity)
        emojis = self._extract_emojis(emoji_part)
        
        return {
            'piece_type': piece_type,
            'emojis': emojis,
            'last_initial': last_initial,
            'full_wizzid': wizzid,
            'piece_name': self.piece_types.get(piece_type, 'Unknown')
        }
    
    def _extract_emojis(self, emoji_part: str) -> List[str]:
        """Extract individual emojis from a string (approximate)"""
        # This is a simplified approach - emoji parsing is complex
        # In practice, you'd want a more robust emoji parsing library
        emojis = []
        i = 0
        while i < len(emoji_part):
            # Look for emoji patterns (this is simplified)
            if emoji_part[i] in ['🐱', '👶', '🐼', '😎', '👸', '🦄', '💃', '👑']:
                emojis.append(emoji_part[i])
                i += 1
            elif emoji_part[i:i+2] in ['🍎', '🥕', '🍕', '🍦', '🍰', '🍫', '🍔']:
                emojis.append(emoji_part[i:i+2])
                i += 2
            elif emoji_part[i:i+3] in ['🚗', '✈️', '🚁', '🚀', '⛵', '🚢']:
                emojis.append(emoji_part[i:i+3])
                i += 3
            elif emoji_part[i:i+2] in ['⭐', '🌙', '💩', '✨', '💫', '🔥', '💧', '🌈']:
                emojis.append(emoji_part[i:i+2])
                i += 2
            else:
                i += 1
        
        return emojis
    
    def generate_nickname(self, wizzid: str) -> str:
        """Generate a nickname based on the WIZZID"""
        parsed = self.parse_wizzid(wizzid)
        emojis = parsed['emojis']
        
        if len(emojis) >= 2:
            # Use character and food emojis for nickname
            character_name = self._get_character_name(emojis[0])
            food_name = self._get_food_name(emojis[1])
            return f"{character_name} {food_name}"
        
        return f"{parsed['piece_name']} {wizzid}"
    
    def _get_character_name(self, emoji: str) -> str:
        """Get character name from emoji"""
        character_names = {
            '🐱': 'Cat', '👶': 'Baby', '🐼': 'Panda', '😎': 'Cool',
            '👸': 'Princess', '🦄': 'Unicorn', '💃': 'Dancer', '👑': 'Crown',
            '🐯': 'Tiger', '🦁': 'Lion', '🐸': 'Frog', '🐙': 'Octopus',
            '🦒': 'Giraffe', '🦘': 'Kangaroo', '🦔': 'Hedgehog', '🦡': 'Badger'
        }
        return character_names.get(emoji, 'Character')
    
    def _get_food_name(self, emoji: str) -> str:
        """Get food name from emoji"""
        food_names = {
            '🍎': 'Apple', '🥕': 'Carrot', '🍕': 'Pizza', '🍦': 'Ice Cream',
            '🍰': 'Cake', '🍫': 'Chocolate', '🍔': 'Burger', '🍎': 'Apple',
            '🍌': 'Banana', '🍊': 'Orange', '🍇': 'Grape', '🍓': 'Strawberry'
        }
        return food_names.get(emoji, 'Food')
    
    def export_to_standard_notation(self, wizzid: str, position: str) -> Dict:
        """Export WIZZID to standard chess notation"""
        parsed = self.parse_wizzid(wizzid)
        
        return {
            'wizzid': wizzid,
            'standard_notation': f"{parsed['piece_type']}{position}",
            'position': position,
            'piece_type': parsed['piece_type'],
            'nickname': self.generate_nickname(wizzid),
            'piece_name': parsed['piece_name']
        }
    
    def import_from_standard_notation(self, standard_notation: str, position: str) -> str:
        """Import from standard chess notation to WIZZID"""
        piece_type = standard_notation[0]
        config = WizzidConfig(piece_type=piece_type, position=position)
        return self.generate_wizzid(config)

# Example usage and testing
def main():
    """Example usage of the WIZZID generator"""
    generator = WizzidGenerator()
    
    print("🎭 WIZZID Generator Examples")
    print("=" * 50)
    
    # Generate some example WIZZIDs
    examples = [
        WizzidConfig('P', 'a2'),
        WizzidConfig('K', 'e1'),
        WizzidConfig('Q', 'd1'),
        WizzidConfig('R', 'a1'),
        WizzidConfig('B', 'c1'),
        WizzidConfig('N', 'b1')
    ]
    
    for config in examples:
        wizzid = generator.generate_wizzid(config)
        nickname = generator.generate_nickname(wizzid)
        export = generator.export_to_standard_notation(wizzid, config.position)
        
        print(f"\n{config.piece_type} at {config.position}:")
        print(f"  WIZZID: {wizzid}")
        print(f"  Nickname: {nickname}")
        print(f"  Standard: {export['standard_notation']}")
    
    print("\n🎪 WIZZID Parsing Example")
    print("=" * 50)
    
    # Parse a WIZZID
    test_wizzid = "P🐱🍎🚗⭐N1"
    parsed = generator.parse_wizzid(test_wizzid)
    print(f"Parsing: {test_wizzid}")
    print(f"Result: {parsed}")

if __name__ == "__main__":
    main() 