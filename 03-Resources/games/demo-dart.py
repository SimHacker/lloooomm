#!/usr/bin/env python3
"""
🎯 TIME DART GAME - QUICK DEMO
Shows the dart game throwing a dart and creating a James Burke story
"""

from time_dart_game import TimeDartGame
from temporal_anchor_adventure import TemporalAnchorAdventure

def demo_dart_game():
    print('🎯 TIME DART GAME - QUICK DEMO')
    print('='*50)

    # Initialize
    adventure = TemporalAnchorAdventure()
    dart_game = TimeDartGame(adventure)

    print('\n🎯 Available targets:')
    dart_game.list_available_targets()

    print('\n🎯 Throwing dart at "stranger"...')
    dart_hit = dart_game.throw_dart('stranger')

    if dart_hit:
        print('\n🎭 Creating James Burke story...')
        journey = dart_game.create_burke_story(dart_hit)
        
        print(f'\n📊 Journey Summary:')
        print(f'Path: {" → ".join(journey.dart_hit.target_path)}')
        print(f'Final Target: {journey.dart_hit.final_target}')
        print(f'Depth: {journey.dart_hit.depth} levels')
        print(f'Score: {journey.dart_hit.score:,} points')
        print(f'Burke Factor: {journey.burke_factor:.2f}')
        
        print('\n🎭 Story Preview (first element):')
        if journey.story_elements:
            print(journey.story_elements[0][:200] + "...")
            
        print('\n🔗 Connection Preview:')
        if journey.connections:
            print(journey.connections[0][:200] + "...")

if __name__ == "__main__":
    demo_dart_game() 