#!/usr/bin/env python3
"""
Tree Worm Implementation
Worms with Sanford & Son style home bases that traverse document trees
"""

import os
import re
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable, Union
from dataclasses import dataclass, field
from datetime import datetime
import ast

@dataclass
class TreeNode:
    """Represents a node in a document tree"""
    type: str  # 'function', 'class', 'comment', etc.
    name: str
    content: str
    file_path: str
    line_number: int
    children: List['TreeNode'] = field(default_factory=list)
    parent: Optional['TreeNode'] = None

@dataclass
class NavigationMemory:
    """Empathic query navigation memory"""
    query: str
    file: str
    line: int
    context: str
    timestamp: datetime = field(default_factory=datetime.now)

class WormHomeBase:
    """The Sanford & Son style junkyard where worms live"""
    
    def __init__(self, worm_name: str, base_path: str):
        self.worm_name = worm_name
        self.base_path = Path(base_path)
        self.parking_status = "HOME"
        self.current_location = None
        
        # Storage areas
        self.yaml_resources = {}
        self.json_storage = {}
        self.prompt_library = {}
        self.mermaid_diagrams = []
        
        # Initialize home base
        self._setup_home()
    
    def _setup_home(self):
        """Set up the home base structure"""
        # Create home directory if it doesn't exist
        self.base_path.mkdir(parents=True, exist_ok=True)
        
        # Create parking sign
        parking_file = self.base_path / "PARKING.md"
        self._update_parking_sign("HOME", "Ready for missions")
        
        # Load existing resources
        self._load_resources()
    
    def _update_parking_sign(self, status: str, details: str):
        """Update the parking sign"""
        parking_file = self.base_path / "PARKING.md"
        content = f"""# 🏠 This is the parking place for {self.worm_name}!
[{status}] - {details}

Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        parking_file.write_text(content)
        self.parking_status = status
    
    def _load_resources(self):
        """Load resources from storage files"""
        # Load YAML resources
        yaml_file = self.base_path / "resources.yaml"
        if yaml_file.exists():
            with open(yaml_file) as f:
                self.yaml_resources = yaml.safe_load(f) or {}
        
        # Load JSON storage
        json_file = self.base_path / "storage.json"
        if json_file.exists():
            with open(json_file) as f:
                self.json_storage = json.load(f)
        
        # Load prompts
        prompts_file = self.base_path / "prompts.yaml"
        if prompts_file.exists():
            with open(prompts_file) as f:
                self.prompt_library = yaml.safe_load(f) or {}
    
    def store_resource(self, category: str, key: str, value: Any):
        """Store a resource in the appropriate storage"""
        if category == "yaml":
            self.yaml_resources[key] = value
            self._save_yaml_resources()
        elif category == "json":
            self.json_storage[key] = value
            self._save_json_storage()
        elif category == "prompt":
            self.prompt_library[key] = value
            self._save_prompts()
    
    def fetch_resource(self, category: str, key: str) -> Any:
        """Fetch a resource from storage"""
        if category == "yaml":
            return self.yaml_resources.get(key)
        elif category == "json":
            return self.json_storage.get(key)
        elif category == "prompt":
            return self.prompt_library.get(key)
        return None
    
    def _save_yaml_resources(self):
        """Save YAML resources to file"""
        yaml_file = self.base_path / "resources.yaml"
        with open(yaml_file, 'w') as f:
            yaml.dump(self.yaml_resources, f, default_flow_style=False)
    
    def _save_json_storage(self):
        """Save JSON storage to file"""
        json_file = self.base_path / "storage.json"
        with open(json_file, 'w') as f:
            json.dump(self.json_storage, f, indent=2)
    
    def _save_prompts(self):
        """Save prompts to file"""
        prompts_file = self.base_path / "prompts.yaml"
        with open(prompts_file, 'w') as f:
            yaml.dump(self.prompt_library, f, default_flow_style=False)

class TreeWorm:
    """A worm that traverses document trees with a home base"""
    
    def __init__(self, name: str, home_path: str):
        self.name = name
        self.home_base = WormHomeBase(name, home_path)
        
        # Navigation state
        self.current_node: Optional[TreeNode] = None
        self.navigation_stack: List[NavigationMemory] = []
        
        # Vehicle mode
        self.passenger: Optional[Union[str, Callable]] = None
        self.cargo: Optional[Dict] = None
        
        # Tree cache
        self.tree_cache: Dict[str, TreeNode] = {}
    
    def go_on_patrol(self, target: str, mission: str):
        """Leave home and go on patrol"""
        self.home_base._update_parking_sign(
            "NO PARKING",
            f"Currently on patrol looking for {target}"
        )
        
        # Store mission details
        self.home_base.store_resource("json", "current_mission", {
            "target": target,
            "mission": mission,
            "start_time": datetime.now().isoformat()
        })
    
    def return_home(self):
        """Return to home base"""
        self.home_base._update_parking_sign("HOME", "Mission complete")
        self.current_node = None
        
        # Update mission stats
        mission = self.home_base.fetch_resource("json", "current_mission")
        if mission:
            mission["end_time"] = datetime.now().isoformat()
            self.home_base.store_resource("json", "last_mission", mission)
    
    def parse_tree(self, file_path: str) -> TreeNode:
        """Parse a file into a tree structure"""
        if file_path in self.tree_cache:
            return self.tree_cache[file_path]
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Simple AST parsing for Python files
        if file_path.endswith('.py'):
            tree = self._parse_python_tree(content, file_path)
        else:
            # Basic line-based parsing for other files
            tree = self._parse_generic_tree(content, file_path)
        
        self.tree_cache[file_path] = tree
        return tree
    
    def _parse_python_tree(self, content: str, file_path: str) -> TreeNode:
        """Parse Python code into a tree"""
        try:
            tree = ast.parse(content)
            root = TreeNode("module", file_path, content, file_path, 0)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_node = TreeNode(
                        "function",
                        node.name,
                        ast.get_source_segment(content, node),
                        file_path,
                        node.lineno
                    )
                    root.children.append(func_node)
                elif isinstance(node, ast.ClassDef):
                    class_node = TreeNode(
                        "class",
                        node.name,
                        ast.get_source_segment(content, node),
                        file_path,
                        node.lineno
                    )
                    root.children.append(class_node)
            
            return root
        except:
            return self._parse_generic_tree(content, file_path)
    
    def _parse_generic_tree(self, content: str, file_path: str) -> TreeNode:
        """Generic line-based parsing"""
        root = TreeNode("file", file_path, content, file_path, 0)
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            # Look for patterns
            if re.match(r'^\s*function\s+\w+', line):
                node = TreeNode("function", line.strip(), line, file_path, i + 1)
                root.children.append(node)
            elif re.match(r'^\s*class\s+\w+', line):
                node = TreeNode("class", line.strip(), line, file_path, i + 1)
                root.children.append(node)
            elif 'TODO' in line or 'FIXME' in line:
                node = TreeNode("todo", line.strip(), line, file_path, i + 1)
                root.children.append(node)
        
        return root
    
    def traverse_depth_first(self, node: TreeNode, visitor: Callable):
        """Traverse tree depth-first, applying visitor function"""
        visitor(node)
        for child in node.children:
            self.traverse_depth_first(child, visitor)
    
    def traverse_breadth_first(self, node: TreeNode, visitor: Callable):
        """Traverse tree breadth-first"""
        queue = [node]
        while queue:
            current = queue.pop(0)
            visitor(current)
            queue.extend(current.children)
    
    def find_by_pattern(self, root: TreeNode, pattern: str) -> List[TreeNode]:
        """Find all nodes matching a pattern"""
        matches = []
        regex = re.compile(pattern)
        
        def check_node(node):
            if regex.search(node.content):
                matches.append(node)
        
        self.traverse_depth_first(root, check_node)
        return matches
    
    def empathic_search(self, query: str, root: TreeNode) -> List[TreeNode]:
        """Search using natural language query"""
        matches = []
        query_lower = query.lower()
        
        def check_node(node):
            content_lower = node.content.lower()
            name_lower = node.name.lower()
            
            # Simple empathic matching
            if any(word in content_lower or word in name_lower 
                   for word in query_lower.split()):
                matches.append(node)
        
        self.traverse_depth_first(root, check_node)
        return matches
    
    def load_passenger(self, passenger: Union[str, Callable]):
        """Load a character or prompt as passenger"""
        self.passenger = passenger
        
        # If it's a string, try to load it as a prompt
        if isinstance(passenger, str):
            prompt = self.home_base.fetch_resource("prompt", passenger)
            if prompt:
                self.passenger = prompt
    
    def apply_passenger_to_node(self, node: TreeNode) -> str:
        """Apply the passenger (prompt/character) to a node"""
        if not self.passenger:
            return node.content
        
        if callable(self.passenger):
            # It's a function character
            return self.passenger(node)
        else:
            # It's a prompt string
            prompt = str(self.passenger).format(
                node_type=node.type,
                content=node.content,
                name=node.name
            )
            # In real implementation, this would call an LLM
            return f"[Transformed by {self.name}]: {node.content}"
    
    def remember_location(self, query: str, context: str):
        """Remember current location with empathic query"""
        if self.current_node:
            memory = NavigationMemory(
                query=query,
                file=self.current_node.file_path,
                line=self.current_node.line_number,
                context=context
            )
            self.navigation_stack.append(memory)
    
    def return_to_memory(self) -> Optional[TreeNode]:
        """Return to a remembered location"""
        if not self.navigation_stack:
            return None
        
        memory = self.navigation_stack.pop()
        
        # Try to find the location using the empathic query
        tree = self.parse_tree(memory.file)
        matches = self.empathic_search(memory.query, tree)
        
        if matches:
            self.current_node = matches[0]
            return self.current_node
        
        return None
    
    def remote_fetch(self, resource_path: str) -> Any:
        """Fetch resource from home without returning"""
        parts = resource_path.split('.')
        category = parts[0]
        key = '.'.join(parts[1:]) if len(parts) > 1 else parts[0]
        
        return self.home_base.fetch_resource(category, key)
    
    def remote_store(self, resource_path: str, value: Any):
        """Store resource at home without returning"""
        parts = resource_path.split('.')
        category = parts[0]
        key = '.'.join(parts[1:]) if len(parts) > 1 else parts[0]
        
        self.home_base.store_resource(category, key, value)

# Example usage
if __name__ == "__main__":
    # Create a tree worm with home base
    worm = TreeWorm("Funky Tree Worm", "./worm-homes/funky")
    
    # Store some resources at home
    worm.home_base.store_resource("prompt", "sparkle_function", 
                                  "Add ✨ sparkles to this {node_type}: {name}")
    worm.home_base.store_resource("yaml", "patterns", {
        "functions": r"function\s+\w+",
        "todos": r"TODO|FIXME|HACK"
    })
    
    # Go on patrol
    worm.go_on_patrol("TODO comments", "Add sparkles to all TODOs")
    
    # Parse a tree
    tree = worm.parse_tree(__file__)  # Parse this file itself
    
    # Find all TODOs
    todos = worm.find_by_pattern(tree, r"TODO|FIXME")
    print(f"Found {len(todos)} TODOs")
    
    # Load a prompt and apply it
    worm.load_passenger("sparkle_function")
    
    for todo in todos:
        # Remember where we are
        worm.remember_location("that TODO about parsing", "in the tree parsing section")
        
        # Apply transformation
        result = worm.apply_passenger_to_node(todo)
        print(f"Transformed: {result[:50]}...")
    
    # Return home
    worm.return_home()
    print(f"\n{worm.name} has returned home!") 