# 🎯 Cursor-Friendly Script Design Guide
## By Brad Myers (Now With PBD System Experience!)

### 🔑 Core Principles for Cursor Scripts

1. **Clear Output** - Cursor needs to parse your output
2. **Non-Interactive by Default** - Assume no human is watching
3. **Fail Gracefully** - Errors should be informative, not fatal
4. **Progress Indicators** - Show what's happening
5. **Structured Data** - JSON/YAML when possible

### 🐍 Python Script Template

```python
#!/usr/bin/env python3
"""
Cursor-friendly Python script template
Brad says: "Watch what this script does and learn from it!"
"""

import sys
import json
import argparse
from typing import Dict, Any
import subprocess

# Globals for Cursor visibility
CURSOR_MODE = True
VERBOSE = False

def cursor_print(message: str, level: str = "info"):
    """Print formatted for Cursor to parse"""
    if CURSOR_MODE:
        print(f"[{level.upper()}] {message}")
    else:
        print(message)

def run_command(cmd: list, require_sudo: bool = False) -> Dict[str, Any]:
    """Run command with Cursor-friendly output"""
    if require_sudo and not check_sudo():
        return {"error": "Sudo required but not available"}
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "command": " ".join(cmd)
        }
    except Exception as e:
        return {"error": str(e), "command": " ".join(cmd)}

def check_sudo():
    """Check if sudo is available without prompting"""
    try:
        result = subprocess.run(['sudo', '-n', 'true'], 
                                capture_output=True)
        return result.returncode == 0
    except:
        return False

def warm_up_sudo():
    """Ask user to authenticate sudo before we need it"""
    cursor_print("🔐 Please authenticate sudo (will be used for: XYZ)", "warn")
    cursor_print("Run: sudo -v", "info")
    cursor_print("Then re-run this script", "info")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-cursor', action='store_true', 
                       help='Disable Cursor-friendly output')
    parser.add_argument('--verbose', '-v', action='store_true')
    parser.add_argument('--json', action='store_true',
                       help='Output as JSON')
    args = parser.parse_args()
    
    global CURSOR_MODE, VERBOSE
    CURSOR_MODE = not args.no_cursor
    VERBOSE = args.verbose
    
    # Check sudo if needed
    if need_sudo_for_task() and not check_sudo():
        warm_up_sudo()
    
    # Do the actual work
    results = do_work()
    
    # Output results
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for key, value in results.items():
            cursor_print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```

### 🐚 Shell Script Template

```bash
#!/bin/bash
# Cursor-friendly shell script template
# Brad says: "Make it observable and predictable!"

set -euo pipefail

# Configuration
CURSOR_MODE=${CURSOR_MODE:-1}
VERBOSE=${VERBOSE:-0}
REQUIRE_SUDO=${REQUIRE_SUDO:-0}

# Colors (disabled in Cursor mode)
if [[ "$CURSOR_MODE" -eq 1 ]]; then
    RED=""
    GREEN=""
    YELLOW=""
    BLUE=""
    NC=""
else
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m'
fi

# Cursor-friendly logging
log() {
    local level=$1
    shift
    if [[ "$CURSOR_MODE" -eq 1 ]]; then
        echo "[$level] $*"
    else
        case $level in
            ERROR) echo -e "${RED}❌ $*${NC}" >&2 ;;
            WARN)  echo -e "${YELLOW}⚠️  $*${NC}" ;;
            INFO)  echo -e "${BLUE}ℹ️  $*${NC}" ;;
            OK)    echo -e "${GREEN}✅ $*${NC}" ;;
            *)     echo "$*" ;;
        esac
    fi
}

# Check sudo without prompting
check_sudo() {
    if sudo -n true 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Warm up sudo if needed
warm_up_sudo() {
    log WARN "This script requires sudo access for:"
    log INFO "  - Installing packages"
    log INFO "  - Modifying system files"
    log INFO ""
    log INFO "Please run: sudo -v"
    log INFO "Then re-run this script"
    exit 1
}

# Main function
main() {
    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --no-cursor) CURSOR_MODE=0 ;;
            --verbose|-v) VERBOSE=1 ;;
            --help|-h) show_help; exit 0 ;;
            *) log ERROR "Unknown option: $1"; exit 1 ;;
        esac
        shift
    done
    
    # Check sudo if required
    if [[ "$REQUIRE_SUDO" -eq 1 ]] && ! check_sudo; then
        warm_up_sudo
    fi
    
    # Do the work with progress
    log INFO "Starting task..."
    
    # Example: Process with progress
    total_steps=5
    for i in $(seq 1 $total_steps); do
        log INFO "Step $i/$total_steps: Processing..."
        # Do actual work here
        sleep 1
    done
    
    log OK "Task completed successfully!"
}

# Run main
main "$@"
```

### 🎨 Best Practices for Cursor

1. **Output Structure**
   ```bash
   # Good - Structured and parseable
   [INFO] Starting process...
   [OK] Process completed: 5 items processed
   
   # Bad - Unstructured
   Starting... done! (5)
   ```

2. **Error Handling**
   ```python
   # Good - Informative errors
   try:
       result = do_something()
   except FileNotFoundError as e:
       cursor_print(f"Required file missing: {e.filename}", "error")
       cursor_print("Suggestion: Run 'setup.sh' first", "info")
       sys.exit(1)
   ```

3. **Progress Tracking**
   ```bash
   # Good - Clear progress
   log INFO "Processing files: 0/$total"
   for file in "${files[@]}"; do
       log INFO "Processing: $file ($current/$total)"
       process_file "$file"
       ((current++))
   done
   ```

4. **Non-Interactive Defaults**
   ```python
   # Good - Assume defaults
   def get_confirmation(prompt, default=True):
       if CURSOR_MODE or NON_INTERACTIVE:
           return default
       response = input(f"{prompt} [Y/n]: ")
       return response.lower() != 'n'
   ```

5. **JSON Output Option**
   ```bash
   # Good - Machine-readable option
   if [[ "$OUTPUT_JSON" -eq 1 ]]; then
       jq -n \
         --arg status "success" \
         --arg files "$processed_count" \
         '{status: $status, files_processed: $files}'
   fi
   ```

### 🔐 Sudo Handling Strategy

```bash
# Early in script
SUDO_TASKS=(
    "Installing system packages"
    "Modifying /etc/hosts"
    "Starting system services"
)

if [[ ${#SUDO_TASKS[@]} -gt 0 ]] && ! check_sudo; then
    log WARN "This script will need sudo for:"
    for task in "${SUDO_TASKS[@]}"; do
        log INFO "  - $task"
    done
    log INFO ""
    log INFO "Please authenticate: sudo -v"
    exit 1
fi
```

### 📊 Brad's PBD Insights

Having experienced being a PBD system myself, here's what I've learned:

1. **Predictability** - Cursor (like me!) learns from patterns. Be consistent!
2. **Observability** - Show what you're doing, not just the result
3. **Recoverability** - Make it easy to resume after errors
4. **Demonstrability** - Structure output so Cursor can learn from it

Remember: Every script you write is teaching Cursor how to write better scripts!

---
*"Now that I'm part of a PBD system, I understand: good scripts aren't just about getting work done - they're about teaching the system how to do it better next time!"* - Brad Myers (PBD Researcher & Subject) 