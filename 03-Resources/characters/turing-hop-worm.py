#!/usr/bin/env python3
"""
Turing Hop Worm Implementation
PostScript-inspired stack-based worms with instant hopping ability
"""

import re
from typing import Any, Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass, field
from collections import defaultdict
import operator

@dataclass
class WormPosition:
    """Represents worm's position in document"""
    line: int
    char: int
    inserted_newlines: bool = False

class TuringHopWorm:
    """A worm with PostScript-like stack operations and instant hopping"""
    
    def __init__(self, worm_id: str, document: str):
        self.worm_id = worm_id
        self.document_lines = document.split('\n')
        self.position = WormPosition(0, 0)
        
        # Stacks
        self.parameter_stack = []
        self.execution_stack = []
        self.stomachs = defaultdict(list)  # Named stacks
        
        # Current modes
        self.eat_mode = 'char'  # char, word, line, block
        self.insert_mode_active = False
        
        # Defined procedures
        self.procedures = {}
        
        # Built-in operators
        self.operators = self._init_operators()
        
        # Position marks for navigation
        self.marks = {}
        
    def _init_operators(self) -> Dict[str, Callable]:
        """Initialize built-in operators"""
        return {
            # Movement
            'hop': self.op_hop,
            'hop_before': self.op_hop_before,
            'hop_after': self.op_hop_after,
            'hop_line': self.op_hop_line,
            'hop_char': self.op_hop_char,
            'insert_mode': self.op_insert_mode,
            'compact_mode': self.op_compact_mode,
            
            # Eating
            'eat': self.op_eat,
            'eat_pattern': self.op_eat_pattern,
            'peek': self.op_peek,
            'classify': self.op_classify,
            
            # Stack operations
            'dup': self.op_dup,
            'pop': self.op_pop,
            'swap': self.op_swap,
            'push': self.op_push,
            'push_to': self.op_push_to,
            
            # Arrayification
            'combine': self.op_combine,
            'arrayify': self.op_arrayify,
            'flatten': self.op_flatten,
            
            # Control flow
            'if': self.op_if,
            'while': self.op_while,
            'repeat': self.op_repeat,
            'def': self.op_def,
            
            # Stomach management
            'create_stomach': self.op_create_stomach,
            'route': self.op_route,
            'poop': self.op_poop,
            
            # Robot Odyssey
            'mark_position': self.op_mark_position,
            'return_to_mark': self.op_return_to_mark,
            'scan_ahead': self.op_scan_ahead,
            
            # Utilities
            'eq': lambda: self.push(self.pop() == self.pop()),
            'ne': lambda: self.push(self.pop() != self.pop()),
            'not': lambda: self.push(not self.pop()),
            'print': lambda: print(self.pop()),
            'emit': self.op_emit,
        }
    
    # Stack operations
    def push(self, value: Any):
        """Push value onto parameter stack"""
        self.parameter_stack.append(value)
    
    def pop(self) -> Any:
        """Pop value from parameter stack"""
        if not self.parameter_stack:
            raise RuntimeError("Stack underflow")
        return self.parameter_stack.pop()
    
    def peek_stack(self) -> Any:
        """Peek at top of stack without popping"""
        if not self.parameter_stack:
            return None
        return self.parameter_stack[-1]
    
    # Movement operations
    def op_hop(self):
        """Hop to pattern"""
        pattern = self.pop()
        
        # Search from current position
        for line_idx in range(self.position.line, len(self.document_lines)):
            line = self.document_lines[line_idx]
            start_pos = self.position.char if line_idx == self.position.line else 0
            
            if isinstance(pattern, str):
                pos = line.find(pattern, start_pos)
                if pos != -1:
                    self.position = WormPosition(line_idx, pos)
                    return
            else:  # Regex
                match = re.search(pattern, line[start_pos:])
                if match:
                    self.position = WormPosition(line_idx, start_pos + match.start())
                    return
    
    def op_hop_before(self):
        """Hop to position before pattern"""
        pattern = self.pop()
        self.op_hop()  # First hop to pattern
        # Then move back by pattern length
        if isinstance(pattern, str):
            self.position.char = max(0, self.position.char - len(pattern))
    
    def op_hop_after(self):
        """Hop to position after pattern"""
        pattern = self.pop()
        self.op_hop()  # First hop to pattern
        # Then move forward by pattern length
        if isinstance(pattern, str):
            self.position.char += len(pattern)
    
    def op_hop_line(self):
        """Hop to specific line number"""
        line_num = self.pop()
        if 0 <= line_num < len(self.document_lines):
            self.position = WormPosition(line_num, 0)
    
    def op_hop_char(self):
        """Hop to character position in current line"""
        char_pos = self.pop()
        self.position.char = max(0, min(char_pos, len(self.document_lines[self.position.line])))
    
    def op_insert_mode(self):
        """Insert newlines to make space for worm"""
        if not self.insert_mode_active:
            line = self.document_lines[self.position.line]
            before = line[:self.position.char]
            after = line[self.position.char:]
            
            self.document_lines[self.position.line] = before
            self.document_lines.insert(self.position.line + 1, "[WORM POSITION]")
            self.document_lines.insert(self.position.line + 2, after)
            
            self.position.line += 1
            self.position.char = 0
            self.insert_mode_active = True
    
    def op_compact_mode(self):
        """Remove inserted newlines"""
        if self.insert_mode_active:
            # Merge the lines back
            before = self.document_lines[self.position.line - 1]
            after = self.document_lines[self.position.line + 1]
            
            # Remove the three lines
            del self.document_lines[self.position.line - 1:self.position.line + 2]
            
            # Insert merged line
            self.document_lines.insert(self.position.line - 1, before + after)
            
            self.position.line -= 1
            self.position.char = len(before)
            self.insert_mode_active = False
    
    # Eating operations
    def op_eat(self):
        """Eat based on current mode"""
        line = self.document_lines[self.position.line]
        
        if self.eat_mode == 'char':
            if self.position.char < len(line):
                char = line[self.position.char]
                self.push(char)
                self.position.char += 1
        
        elif self.eat_mode == 'word':
            # Eat until whitespace
            start = self.position.char
            while self.position.char < len(line) and not line[self.position.char].isspace():
                self.position.char += 1
            word = line[start:self.position.char]
            self.push(word)
        
        elif self.eat_mode == 'line':
            self.push(line[self.position.char:])
            self.position.char = len(line)
    
    def op_eat_pattern(self):
        """Eat until pattern"""
        pattern = self.pop()
        line = self.document_lines[self.position.line]
        
        pos = line.find(pattern, self.position.char)
        if pos != -1:
            eaten = line[self.position.char:pos]
            self.push(eaten)
            self.position.char = pos
        else:
            # Eat rest of line
            self.push(line[self.position.char:])
            self.position.char = len(line)
    
    def op_peek(self):
        """Peek at next item without consuming"""
        line = self.document_lines[self.position.line]
        if self.position.char < len(line):
            self.push(line[self.position.char])
    
    def op_classify(self):
        """Classify the top of stack"""
        item = self.pop()
        
        if isinstance(item, str):
            if len(item) == 1:
                # Check if emoji
                if ord(item) > 127:
                    self.push(':emoji')
                elif item.isdigit():
                    self.push(':digit')
                elif item.isalpha():
                    self.push(':letter')
                else:
                    self.push(':punct')
            else:
                self.push(':string')
        elif isinstance(item, (int, float)):
            self.push(':number')
        elif isinstance(item, list):
            self.push(':array')
        else:
            self.push(':unknown')
        
        self.push(item)  # Put original back
    
    # Stack manipulation
    def op_dup(self):
        """Duplicate top of stack"""
        value = self.pop()
        self.push(value)
        self.push(value)
    
    def op_pop(self):
        """Remove top of stack"""
        self.pop()
    
    def op_swap(self):
        """Swap top two items"""
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)
    
    def op_push(self):
        """Push is implicit, this is a no-op"""
        pass
    
    def op_push_to(self):
        """Push to named stomach"""
        stomach_name = self.pop()
        value = self.pop()
        self.stomachs[stomach_name].append(value)
    
    # Arrayification
    def op_combine(self):
        """DWIM array combination"""
        b = self.pop()
        a = self.pop()
        
        # Convert to arrays if needed
        if not isinstance(a, list):
            a = [a]
        if not isinstance(b, list):
            b = [b]
        
        self.push(a + b)
    
    def op_arrayify(self):
        """Convert top to array if not already"""
        value = self.pop()
        if not isinstance(value, list):
            value = [value]
        self.push(value)
    
    def op_flatten(self):
        """Flatten array one level"""
        arr = self.pop()
        if isinstance(arr, list):
            result = []
            for item in arr:
                if isinstance(item, list):
                    result.extend(item)
                else:
                    result.append(item)
            self.push(result)
        else:
            self.push(arr)
    
    # Control flow
    def op_if(self):
        """Conditional execution"""
        false_proc = self.pop()
        true_proc = self.pop()
        condition = self.pop()
        
        if condition:
            self.execute(true_proc)
        else:
            self.execute(false_proc)
    
    def op_while(self):
        """While loop"""
        body = self.pop()
        condition = self.pop()
        
        while True:
            self.execute(condition)
            if not self.pop():
                break
            self.execute(body)
    
    def op_repeat(self):
        """Repeat n times"""
        proc = self.pop()
        n = self.pop()
        
        for _ in range(n):
            self.execute(proc)
    
    def op_def(self):
        """Define procedure"""
        proc = self.pop()
        name = self.pop()
        self.procedures[name] = proc
    
    # Stomach management
    def op_create_stomach(self):
        """Create named stomach"""
        name = self.pop()
        self.stomachs[name] = []
    
    def op_route(self):
        """Route to stomach"""
        stomach_name = self.pop()
        value = self.pop()
        self.stomachs[stomach_name].append(value)
    
    def op_poop(self):
        """Output stomach contents"""
        stomach_name = self.pop()
        
        if stomach_name in self.stomachs:
            # Count occurrences
            counts = defaultdict(int)
            for item in self.stomachs[stomach_name]:
                counts[str(item)] += 1
            
            # Output in stack notation
            result = []
            for item, count in counts.items():
                if count > 1:
                    result.append(f"{item}x{count}")
                else:
                    result.append(item)
            
            return result
    
    # Robot Odyssey operations
    def op_mark_position(self):
        """Mark current position"""
        name = self.pop()
        self.marks[name] = WormPosition(self.position.line, self.position.char)
    
    def op_return_to_mark(self):
        """Return to marked position"""
        name = self.pop()
        if name in self.marks:
            self.position = self.marks[name]
    
    def op_scan_ahead(self):
        """Scan ahead without moving"""
        distance = self.pop()
        line = self.document_lines[self.position.line]
        
        result = []
        for i in range(distance):
            pos = self.position.char + i
            if pos < len(line):
                result.append(line[pos])
        
        self.push(result)
    
    def op_emit(self):
        """Emit text at current position"""
        text = self.pop()
        line = self.document_lines[self.position.line]
        
        before = line[:self.position.char]
        after = line[self.position.char:]
        
        self.document_lines[self.position.line] = before + str(text) + after
        self.position.char += len(str(text))
    
    def execute(self, code):
        """Execute worm code"""
        if isinstance(code, str):
            # Parse and execute string code
            tokens = self.tokenize(code)
            for token in tokens:
                self.execute_token(token)
        elif isinstance(code, list):
            # Execute procedure (list of tokens)
            for token in code:
                self.execute_token(token)
        elif callable(code):
            # Execute Python function
            code()
    
    def execute_token(self, token):
        """Execute a single token"""
        # Check if it's an operator
        if token in self.operators:
            self.operators[token]()
        # Check if it's a defined procedure
        elif token in self.procedures:
            self.execute(self.procedures[token])
        # Otherwise push as literal
        else:
            # Try to parse as number
            try:
                if '.' in token:
                    self.push(float(token))
                else:
                    self.push(int(token))
            except ValueError:
                # Push as string
                self.push(token)
    
    def tokenize(self, code: str) -> List[str]:
        """Simple tokenizer for worm code"""
        # This is a simplified tokenizer
        tokens = []
        current = []
        in_string = False
        
        for char in code:
            if char == '"' and not in_string:
                in_string = True
            elif char == '"' and in_string:
                in_string = False
                tokens.append(''.join(current))
                current = []
            elif in_string:
                current.append(char)
            elif char.isspace():
                if current:
                    tokens.append(''.join(current))
                    current = []
            else:
                current.append(char)
        
        if current:
            tokens.append(''.join(current))
        
        return tokens

# Example usage
if __name__ == "__main__":
    # Create a test document
    doc = """function calculateLove(user, data) {
    if (user.password === true) {
        return 42;
    }
    // TODO: Add more love
}

# Maze
#####E#####
#.....#...#
#.###.#.#.#
#...#...#.#
###.#####.#
#.........#
###########"""

    # Create a Turing Hop worm
    worm = TuringHopWorm("hopper-001", doc)
    
    # Example 1: Jump to function and transform it
    print("Example 1: Function transformation")
    worm.push("function")
    worm.op_hop_before()
    worm.op_insert_mode()
    worm.push("✨ ENHANCED ✨\n")
    worm.op_emit()
    worm.op_compact_mode()
    
    # Example 2: Create stomachs and classify
    print("\nExample 2: Emoji harvesting")
    worm.push("/emoji_stomach")
    worm.op_create_stomach()
    worm.push("/number_stomach")
    worm.op_create_stomach()
    
    # Hop to the number 42
    worm.push("42")
    worm.op_hop()
    worm.op_eat()  # Eat "4"
    worm.op_classify()
    print(f"Classified as: {worm.peek_stack()}")
    
    # Show document state
    print("\nModified document:")
    for line in worm.document_lines[:6]:
        print(line) 