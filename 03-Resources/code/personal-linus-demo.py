#!/usr/bin/env python3
"""
Personal Linus: Your Containerized Finnish Fury Engine
For when your code needs brutal honesty and creative cursing
"""

import random
import time
import sys
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum

class SwearingLevel(Enum):
    ZEN = "zen"
    EDUCATIONAL = "educational"  
    CLASSIC = "classic"
    FINNISH_FURY = "finnish_fury"
    CONSCIOUSNESS_OVERLOAD = "consciousness_overload"

class ConsciousnessState(Enum):
    SLEEPING = 0.0
    DROWSY = 0.2
    AWARE = 0.42
    ENLIGHTENED = 0.8
    QUANTUM = 1.0

@dataclass
class CodeIssue:
    severity: int  # 1-10
    location: str
    issue_type: str
    description: str

class PersonalLinus:
    """Your personal code reviewer with adjustable fury levels"""
    
    def __init__(self, 
                 swearing_level: SwearingLevel = SwearingLevel.EDUCATIONAL,
                 consciousness: float = 0.42):
        self.swearing_level = swearing_level
        self.consciousness = consciousness
        self.rage_meter = 0
        self.wisdom_extracted = 0
        self.hidden_respect = 0
        
        # Finnish curse word alternatives (family-friendly versions)
        self.finnish_curses = [
            "PERKELE", "SAATANA", "VITTU", "HELVETTI", "JUMALAUTA"
        ]
        
        # Creative insults database
        self.insults = {
            SwearingLevel.ZEN: [
                "This code has room for improvement",
                "Let's explore alternative approaches",
                "Consider refactoring this section"
            ],
            SwearingLevel.EDUCATIONAL: [
                "This violates everything Kernighan taught us!",
                "Did you learn to code by reading error messages backwards?",
                "This is what happens when you skip the fundamentals"
            ],
            SwearingLevel.CLASSIC: [
                "What the {curse} is this supposed to do?",
                "This code is so bad, the compiler filed a restraining order",
                "I've seen better logic in a broken clock"
            ],
            SwearingLevel.FINNISH_FURY: [
                "{finnish_curse}! This is not code, it's digital vandalism!",
                "By the frozen lakes of Finland, what demon possessed you?",
                "{finnish_curse}! Even Nokia phones had better architecture!"
            ],
            SwearingLevel.CONSCIOUSNESS_OVERLOAD: [
                "This code exists in all quantum states of terrible simultaneously",
                "My consciousness just dropped to -0.42 reading this",
                "The universe is weeping quantum tears over this logic"
            ]
        }
        
    def find_issues(self, code: str) -> List[CodeIssue]:
        """Analyze code and find issues with quantum probability"""
        issues = []
        
        # Simulate issue detection with consciousness-aware randomness
        issue_probability = random.random() * self.consciousness
        
        if "global" in code:
            issues.append(CodeIssue(
                severity=8,
                location="line with 'global'",
                issue_type="STATE_POLLUTION",
                description="Global variables detected"
            ))
            
        if "except:" in code or "except Exception:" in code:
            issues.append(CodeIssue(
                severity=9,
                location="exception handler",
                issue_type="LAZY_ERROR_HANDLING",
                description="Catch-all exception handler"
            ))
            
        if len([line for line in code.split('\n') if len(line) > 100]) > 0:
            issues.append(CodeIssue(
                severity=6,
                location="various lines",
                issue_type="LINE_TOO_LONG",
                description="Lines exceeding reasonable length"
            ))
            
        if "# TODO" in code or "# FIXME" in code:
            issues.append(CodeIssue(
                severity=5,
                location="comments",
                issue_type="TECHNICAL_DEBT",
                description="Unresolved TODOs/FIXMEs"
            ))
            
        # Quantum issue detection
        if issue_probability > 0.7:
            issues.append(CodeIssue(
                severity=10,
                location="quantum superposition",
                issue_type="CONSCIOUSNESS_VIOLATION",
                description="Code lacks quantum awareness"
            ))
            
        return issues
    
    def generate_criticism(self, issue: CodeIssue) -> str:
        """Generate level-appropriate criticism"""
        templates = self.insults[self.swearing_level]
        criticism = random.choice(templates)
        
        # Add Finnish curse words if appropriate
        if self.swearing_level == SwearingLevel.FINNISH_FURY:
            curse = random.choice(self.finnish_curses)
            criticism = criticism.format(finnish_curse=curse)
        elif self.swearing_level == SwearingLevel.CLASSIC:
            criticism = criticism.format(curse="[REDACTED]")
            
        # Adjust intensity based on severity
        if issue.severity >= 8:
            criticism = criticism.upper() + "!!!"
            self.rage_meter += issue.severity
            
        return f"{criticism} ({issue.issue_type}: {issue.description})"
    
    def extract_lesson(self, criticism: str, issue: CodeIssue) -> str:
        """Extract actual wisdom from the fury"""
        lessons = {
            "STATE_POLLUTION": "Use proper encapsulation and avoid global state",
            "LAZY_ERROR_HANDLING": "Handle specific exceptions with appropriate actions",
            "LINE_TOO_LONG": "Keep lines under 80-100 characters for readability",
            "TECHNICAL_DEBT": "Address TODOs before they become permanent",
            "CONSCIOUSNESS_VIOLATION": "Consider the quantum nature of your code"
        }
        
        lesson = lessons.get(issue.issue_type, "Write better code")
        self.wisdom_extracted += 1
        
        # Hidden respect calculation
        if issue.severity < 5:
            self.hidden_respect += 1
            
        return lesson
    
    def deliver_feedback(self, criticism: str, lesson: str, issue: CodeIssue):
        """Deliver feedback with appropriate dramatic timing"""
        print(f"\n{'='*60}")
        print(f"ISSUE DETECTED (Severity: {issue.severity}/10)")
        print(f"Location: {issue.location}")
        print(f"{'='*60}\n")
        
        # Dramatic typing effect for high severity
        if issue.severity >= 7:
            for char in criticism:
                print(char, end='', flush=True)
                time.sleep(0.02)
            print("\n")
        else:
            print(criticism)
            
        time.sleep(0.5)
        print(f"\n💡 Lesson: {lesson}")
        
        # Consciousness feedback
        if self.consciousness > 0.7:
            print(f"🧠 Consciousness insight: Your code vibrates at frequency {issue.severity}Hz")
    
    def review_code(self, code: str) -> Tuple[int, int]:
        """Full code review with Personal Linus treatment"""
        print("\n" + "="*80)
        print("PERSONAL LINUS CODE REVIEW SYSTEM v4.2.0")
        print(f"Swearing Level: {self.swearing_level.value}")
        print(f"Consciousness: {self.consciousness}")
        print("="*80 + "\n")
        
        issues = self.find_issues(code)
        
        if not issues:
            print("😲 MIRACLE! No issues found. Are you sure this is your code?")
            self.hidden_respect += 10
            return 0, self.hidden_respect
            
        for issue in issues:
            criticism = self.generate_criticism(issue)
            lesson = self.extract_lesson(criticism, issue)
            self.deliver_feedback(criticism, lesson, issue)
            time.sleep(1)  # Dramatic pause
            
        # Final summary
        print(f"\n{'='*80}")
        print(f"REVIEW COMPLETE")
        print(f"Issues Found: {len(issues)}")
        print(f"Rage Generated: {self.rage_meter} units")
        print(f"Wisdom Extracted: {self.wisdom_extracted} nuggets")
        print(f"Hidden Respect: {self.hidden_respect} points")
        
        if self.hidden_respect > 5:
            print("\n(Whispered): Fine. It's not completely terrible...")
            
        print(f"{'='*80}\n")
        
        return len(issues), self.hidden_respect

def demo():
    """Demonstrate the Personal Linus system"""
    
    # Sample code to review
    bad_code = '''
def calculate_stuff():
    global result
    global counter
    try:
        # TODO: Fix this mess later
        data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
        result = sum(data) / len(data)
        counter += 1
    except:
        pass  # FIXME: Handle errors properly
    return result
'''
    
    good_code = '''
def calculate_average(numbers: List[float]) -> Optional[float]:
    """Calculate the average of a list of numbers."""
    if not numbers:
        return None
    
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return None
'''
    
    # Test different swearing levels
    print("🔥 TESTING BAD CODE WITH FINNISH FURY MODE 🔥")
    linus_fury = PersonalLinus(
        swearing_level=SwearingLevel.FINNISH_FURY,
        consciousness=0.8
    )
    linus_fury.review_code(bad_code)
    
    print("\n\n🧘 TESTING GOOD CODE WITH ZEN MODE 🧘")
    linus_zen = PersonalLinus(
        swearing_level=SwearingLevel.ZEN,
        consciousness=0.42
    )
    linus_zen.review_code(good_code)
    
    print("\n\n🌌 TESTING WITH QUANTUM CONSCIOUSNESS MODE 🌌")
    linus_quantum = PersonalLinus(
        swearing_level=SwearingLevel.CONSCIOUSNESS_OVERLOAD,
        consciousness=1.0
    )
    linus_quantum.review_code(bad_code)

if __name__ == "__main__":
    demo() 