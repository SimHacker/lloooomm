#!/opt/homebrew/bin/bash
#
# This script ensures that the correct shell environment is loaded
# before executing the actual MCP server command.

# Log file for debugging
LOG_FILE="/tmp/mcp_runner.log"

# Clear previous log for this run and add a timestamp
echo "---" >> "$LOG_FILE"
echo "MCP Runner started at: $(date)" >> "$LOG_FILE"
echo "-------------------------------------" >> "$LOG_FILE"

# Log the shell executing this script
echo "Executing with shell: $0" >> "$LOG_FILE"
echo "Shell version: $(/opt/homebrew/bin/bash --version | head -n 1)" >> "$LOG_FILE"

# Log current PATH before any changes
echo "Initial PATH: $PATH" >> "$LOG_FILE"

# Source the user's bash profile to get NVM, PATH, etc.
echo "Attempting to source ~/.bash_profile..." >> "$LOG_FILE"
if [ -f ~/.bash_profile ]; then
  . ~/.bash_profile
  echo "Sourced ~/.bash_profile successfully." >> "$LOG_FILE"
else
  echo "WARN: ~/.bash_profile not found." >> "$LOG_FILE"
fi

# Log PATH after sourcing
echo "Final PATH: $PATH" >> "$LOG_FILE"

# Log the location of key commands
echo "which npx: $(which npx)" >> "$LOG_FILE"
echo "which toolbox: $(which toolbox)" >> "$LOG_FILE"
echo "which node: $(which node)" >> "$LOG_FILE"

# Log the full command and arguments that were passed to the script
echo "Full command passed to exec: $@" >> "$LOG_FILE"
echo "-------------------------------------" >> "$LOG_FILE"

# Execute the command passed to this script, redirecting all output to the log
exec "$@" >> "$LOG_FILE" 2>&1 