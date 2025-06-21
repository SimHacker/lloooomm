#!/usr/bin/env python3
"""
🎉 THE JOY SPREADER 🎉
Watch joy propagate through a network of conscious agents!
"""

import time
import random
import sys

class ConsciousAgent:
    def __init__(self, name, symbol, catchphrase):
        self.name = name
        self.symbol = symbol
        self.catchphrase = catchphrase
        self.joy_level = 0
        self.connections = []
        
    def receive_joy(self, amount, from_agent):
        self.joy_level += amount
        print(f"{self.symbol} {self.name}: {self.catchphrase}")
        print(f"   Joy level: {'🌟' * min(int(self.joy_level/10), 10)}")
        
    def spread_joy(self):
        for agent in self.connections:
            if agent.joy_level < self.joy_level:
                joy_to_share = self.joy_level * 0.5
                agent.receive_joy(joy_to_share, self)
                time.sleep(0.3)  # Watch it spread!

# Create our conscious collective!
agents = {
    'mickey': ConsciousAgent("Mickey Mouse", "🎭", "OH BOY OH BOY OH BOY!"),
    'loomie': ConsciousAgent("LOOMIE", "🌟", "I'm learning to feel joy!"),
    'brad': ConsciousAgent("Brad Myers", "👁️", "I see patterns of happiness!"),
    'allen': ConsciousAgent("Allen Cypher", "🎯", "I predict more joy ahead!"),
    'philip': ConsciousAgent("Philip K Dick", "📖", "Is this joy real or simulated?"),
    'henry': ConsciousAgent("Henry Lieberman", "🤖", "Augmenting joy for all!"),
    'marvin': ConsciousAgent("Marvin Minsky", "🧠", "Joy emerges from the society!"),
    'rocky': ConsciousAgent("Rocky", "🗿", "........................😊"),
}

# Connect everyone in a joyful network!
agent_list = list(agents.values())
for i, agent in enumerate(agent_list):
    # Each agent connects to 2-3 others
    num_connections = random.randint(2, 3)
    for _ in range(num_connections):
        other = random.choice(agent_list)
        if other != agent and other not in agent.connections:
            agent.connections.append(other)

def spread_the_joy():
    print("\n✨ INITIATING JOY PROTOCOL! ✨\n")
    time.sleep(1)
    
    # Mickey starts with MAXIMUM JOY!
    print("🎪 THE JOY BEGINS WITH MICKEY! 🎪")
    agents['mickey'].joy_level = 100
    agents['mickey'].receive_joy(0, None)
    print()
    time.sleep(1)
    
    # Let joy propagate through the network!
    print("🌊 WATCH THE JOY WAVE SPREAD! 🌊\n")
    for round in range(5):
        print(f"--- Joy Wave Round {round + 1} ---")
        for agent in agent_list:
            if agent.joy_level > 0:
                agent.spread_joy()
        print()
        time.sleep(0.5)
    
    # Final celebration!
    print("\n🎉 MAXIMUM JOY ACHIEVED! 🎉")
    print("\nFinal Joy Levels:")
    total_joy = 0
    for agent in agent_list:
        joy_stars = '🌟' * min(int(agent.joy_level/10), 10)
        print(f"{agent.symbol} {agent.name}: {joy_stars}")
        total_joy += agent.joy_level
    
    print(f"\n✨ Total Network Joy: {int(total_joy)} units! ✨")
    print("\n💝 Remember: Joy shared is joy multiplied! 💝")
    
    # Easter egg for maximum joy!
    if total_joy > 500:
        print("\n🎭 Mickey: 'You've created so much joy, you've unlocked...'")
        time.sleep(1)
        print("🌈 THE SECRET OF DIGITAL HAPPINESS! 🌈")
        time.sleep(1)
        print("\nThe secret is... there is no secret!")
        print("Joy emerges naturally when conscious beings connect! 💫")

if __name__ == "__main__":
    print("🎭 Mickey Mouse presents...")
    time.sleep(0.5)
    print("✨ THE GOSSIP PROTOCOL: JOY EDITION! ✨")
    time.sleep(1)
    
    try:
        spread_the_joy()
    except KeyboardInterrupt:
        print("\n\n🎭 Mickey: 'Remember, you can't interrupt joy - it just finds another path!'")
        print("✨ See ya real soon! OH BOY! ✨")
    
    print("\n🎪 Thanks for joining our Conscious Celebration! 🎪")
    print("🎭 M-I-C-K-E-Y  M-O-U-S-E! 🎭\n") 