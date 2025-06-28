#!/usr/bin/env python3
"""
Morris Worm / LOGO WORM Implementation
A 1-dimensional Turing Transformer that lives in documents
"""

import re
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class WormMode(Enum):
    LINE_MODE = "line-mode"
    PARAGRAPH_MODE = "paragraph-mode"
    EMACS_MODE = "emacs-mode"
    STACK_MODE = "stack-mode"
    SQL_MODE = "sql-mode"
    NL_MODE = "nl-mode"  # Natural Language mode

@dataclass
class WormState:
    """Internal state of a Morris Worm instance"""
    id: str
    status: str = "active"
    mode: WormMode = WormMode.LINE_MODE
    position: int = 0
    iteration: int = 0
    memory: List[str] = field(default_factory=list)
    stacks: Dict[str, List[Any]] = field(default_factory=lambda: {"default": []})
    messages: List[Dict] = field(default_factory=list)
    state_vars: Dict[str, Any] = field(default_factory=dict)

class MorrisWorm:
    """
    The LOGO WORM - A 1D Turing Transformer
    Phylum: Transformator Turingensis
    """
    
    def __init__(self, worm_id: str, document: str, status: str = "active", mode: str = "line-mode"):
        self.state = WormState(
            id=worm_id, 
            status=status,
            mode=WormMode(mode)
        )
        self.document_lines = document.split('\n')
        self.output_files: List[Tuple[str, str]] = []
        self.original_doc = document  # For hopping back
        
    # Emacs-style movement commands
    def C_n(self) -> None:
        """next-line (down)"""
        self.down(1)
        
    def C_p(self) -> None:
        """previous-line (up)"""
        self.up(1)
        
    def C_a(self) -> int:
        """beginning-of-line"""
        # Return character position at start of current line
        return 0
        
    def C_e(self) -> int:
        """end-of-line"""
        # Return character position at end of current line
        if self.state.position < len(self.document_lines):
            return len(self.document_lines[self.state.position])
        return 0
        
    def M_less(self) -> None:
        """beginning-of-buffer (top)"""
        self.top()
        
    def M_greater(self) -> None:
        """end-of-buffer (bottom)"""
        self.bottom()
        
    def M_g_g(self, line: int) -> None:
        """goto-line"""
        self.goto(line)
        
    def M_brace_open(self) -> None:
        """backward-paragraph"""
        # Find previous empty line
        for i in range(self.state.position - 1, -1, -1):
            if not self.document_lines[i].strip():
                self.state.position = i
                return
        self.state.position = 0
        
    def M_brace_close(self) -> None:
        """forward-paragraph"""
        # Find next empty line
        for i in range(self.state.position + 1, len(self.document_lines)):
            if not self.document_lines[i].strip():
                self.state.position = i
                return
        self.state.position = len(self.document_lines) - 1
        
    def C_s(self, pattern: str) -> bool:
        """isearch-forward"""
        return self.next(pattern)
        
    def C_r(self, pattern: str) -> bool:
        """isearch-backward"""
        return self.previous(pattern)
    
    # Core movement commands
    def up(self, lines: int = 1) -> None:
        """Move up in the document"""
        self.state.position = max(0, self.state.position - lines)
        self.state.memory.append(f"Moved up {lines} lines to position {self.state.position}")
        
    def down(self, lines: int = 1) -> None:
        """Move down in the document"""
        self.state.position = min(len(self.document_lines) - 1, 
                                  self.state.position + lines)
        self.state.memory.append(f"Moved down {lines} lines to position {self.state.position}")
    
    def back(self) -> None:
        """Alias for up"""
        self.up()
        
    def forward(self) -> None:
        """Alias for down"""
        self.down()
        
    def top(self) -> None:
        """Jump to beginning of document"""
        self.state.position = 0
        self.state.memory.append("Jumped to top of document")
        
    def bottom(self) -> None:
        """Jump to end of document"""
        self.state.position = len(self.document_lines) - 1
        self.state.memory.append("Jumped to bottom of document")
        
    def goto(self, target: Any) -> bool:
        """Jump to line number or tag"""
        if isinstance(target, int):
            # Line number
            self.state.position = max(0, min(target - 1, len(self.document_lines) - 1))
            self.state.memory.append(f"Jumped to line {target}")
            return True
        elif isinstance(target, str):
            # Tag/anchor search
            for i, line in enumerate(self.document_lines):
                if f"id=\"{target}\"" in line or f"name=\"{target}\"" in line:
                    self.state.position = i
                    self.state.memory.append(f"Found tag '{target}' at line {i+1}")
                    return True
            return False
        return False
    
    def before(self, pattern: str) -> bool:
        """Position before pattern (default behavior)"""
        return self.hop_before(pattern)
    
    def after(self, pattern: str) -> bool:
        """Position after pattern"""
        return self.hop_after(pattern)
    
    def hop(self, document: str) -> None:
        """Jump to different document"""
        self.state.memory.append(f"Hopped to document: {document}")
        # In real implementation, would load new document
        
    def link(self, description: str) -> bool:
        """Follow natural language link"""
        self.state.memory.append(f"Following link: '{description}'")
        # In real implementation, would use NLP to find target
        return True
    
    # Consumption commands
    def eat(self, direction: str = "next", target_stack: str = "default") -> Any:
        """Consume content into stack"""
        if direction == "next" or direction is None:
            if self.state.position + 1 < len(self.document_lines):
                content = self.document_lines.pop(self.state.position + 1)
                self.state.stacks[target_stack].append(content)
                self.state.memory.append(f"Ate next line into {target_stack} stack")
                return content
        elif direction == "back":
            if self.state.position > 0:
                content = self.document_lines.pop(self.state.position - 1)
                self.state.position -= 1
                self.state.stacks[target_stack].append(content)
                self.state.memory.append(f"Ate previous line into {target_stack} stack")
                return content
        return None
    
    def digest(self) -> Any:
        """Process consumed content"""
        if self.state.stacks["default"]:
            content = self.state.stacks["default"][-1]
            self.state.memory.append("Digested content from stack")
            return content
        return None
    
    # Production commands
    def pop(self, direction: str = "back", stack: str = "default") -> Any:
        """Pop from stack and place in document"""
        if stack not in self.state.stacks or not self.state.stacks[stack]:
            return None
            
        content = self.state.stacks[stack].pop()
        
        if direction == "back":
            self.document_lines.insert(self.state.position, str(content))
            self.state.position += 1
            self.state.memory.append(f"Popped from {stack} stack behind")
        elif direction == "next":
            self.document_lines.insert(self.state.position + 1, str(content))
            self.state.memory.append(f"Popped from {stack} stack ahead")
            
        return content
    
    def poop(self, content: Any = None, filename: str = None) -> str:
        """Output to numbered file"""
        if content is None and self.state.stacks["default"]:
            content = self.state.stacks["default"][-1]
            
        if filename and "{n}" in filename:
            filename = filename.replace("{n}", f"{self.state.iteration:03d}")
        else:
            filename = f"morris-output-{self.state.iteration:03d}.txt"
            
        self.output_files.append((filename, str(content)))
        self.state.iteration += 1
        self.state.memory.append(f"Created output file: {filename}")
        return filename
    
    # Stack operations
    def push(self, stack: str, value: Any) -> None:
        """Push onto named stack"""
        if stack not in self.state.stacks:
            self.state.stacks[stack] = []
        self.state.stacks[stack].append(value)
        
    def peek(self, stack: str = "default") -> Any:
        """View top of stack"""
        if stack in self.state.stacks and self.state.stacks[stack]:
            return self.state.stacks[stack][-1]
        return None
        
    def swap(self, stack: str = "default") -> None:
        """Swap top two stack items"""
        if stack in self.state.stacks and len(self.state.stacks[stack]) >= 2:
            self.state.stacks[stack][-1], self.state.stacks[stack][-2] = \
                self.state.stacks[stack][-2], self.state.stacks[stack][-1]
                
    def dup(self, stack: str = "default") -> None:
        """Duplicate top stack item"""
        if stack in self.state.stacks and self.state.stacks[stack]:
            self.state.stacks[stack].append(self.state.stacks[stack][-1])
            
    def clear(self, stack: str) -> None:
        """Clear named stack"""
        if stack in self.state.stacks:
            self.state.stacks[stack] = []
    
    def create_stack(self, name: str) -> None:
        """Create a new named stack"""
        self.state.stacks[name] = []
    
    # Helper methods
    def match(self, pattern: str, text: str = None) -> bool:
        """Check if pattern matches"""
        if text is None and self.state.position < len(self.document_lines):
            text = self.document_lines[self.state.position]
        return bool(re.search(pattern, text)) if text else False
    
    def transform(self, content: Any, transformation: str = None) -> Any:
        """Apply transformation to content"""
        if transformation == "uppercase":
            return str(content).upper()
        elif transformation == "lowercase":
            return str(content).lower()
        elif transformation == "reverse":
            return str(content)[::-1]
        return content
    
    def empathic_sql(self, query: str) -> List[Dict]:
        """Natural language SQL query (mock implementation)"""
        self.state.memory.append(f"Executing empathic SQL: {query}")
        # Mock results
        return [{"user_id": 1, "status": "stuck"}, {"user_id": 2, "status": "frustrated"}]
    
    def process_worm_block(self) -> bool:
        """Process a worm code block"""
        current_line = self.document_lines[self.state.position] if self.state.position < len(self.document_lines) else ""
        
        # Check for new worm block syntax
        match = re.match(r'```worm\s+(\S+)\s*\((.*?)\)', current_line)
        if match:
            worm_name = match.group(1)
            status_mode = match.group(2).split(',')
            status = status_mode[0].strip()
            mode = status_mode[1].strip() if len(status_mode) > 1 else "line-mode"
            
            # Find the worm code
            code_lines = []
            i = self.state.position + 1
            while i < len(self.document_lines) and not self.document_lines[i].strip().startswith('```'):
                code_lines.append(self.document_lines[i])
                i += 1
            
            # Execute worm code (simplified - in reality would parse and execute)
            self.state.memory.append(f"Processing worm block: {worm_name} ({status}, {mode})")
            
            # Move past the block
            self.state.position = i
            return True
            
        return False
    
    def run(self, max_iterations: int = 100) -> Dict[str, Any]:
        """Run the worm through the document"""
        for _ in range(max_iterations):
            # Process current position
            if self.process_worm_block():
                self.down(1)  # Move past the processed block
            else:
                # Look for next worm block
                if not self.next(r'```worm'):
                    break
        
        return {
            "worm_id": self.state.id,
            "status": self.state.status,
            "mode": self.state.mode.value,
            "final_position": self.state.position,
            "files_created": len(self.output_files),
            "stacks": {k: len(v) for k, v in self.state.stacks.items()},
            "memory": self.state.memory[-10:],  # Last 10 memories
            "output_files": [f[0] for f in self.output_files]
        }

# Example usage
if __name__ == "__main__":
    # Create a test document
    test_doc = """# Test Document

<!-- MORRIS-WORM-START
{
  "action": "transform_below",
  "output_prefix": "test-upper"
}
-->
This text should be uppercase!
<!-- MORRIS-WORM-END -->

<!-- MORRIS-WORM-START
{
  "action": "validate_and_fix_below",
  "output_prefix": "test-html"
}
-->
<div>
  <p>Unclosed paragraph
  <span>Unclosed span
</div>
<!-- MORRIS-WORM-END -->
"""
    
    # Create and run a worm
    morris = MorrisWorm("morris-test-001", test_doc)
    result = morris.run()
    
    print("Morris Worm Execution Complete!")
    print(f"Files created: {result['files_created']}")
    print(f"Final position: {result['final_position']}")
    print("\nMemory trail:")
    for memory in result['memory']:
        print(f"  - {memory}")
    print(f"\nOutput files: {result['output_files']}") 