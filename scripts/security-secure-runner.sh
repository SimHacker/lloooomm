#!/bin/bash
# Secure runner for MCP servers using 1Password CLI

# --- Configuration ---
# The 1Password account to use. Can be overridden by the OP_ACCOUNT env var.
ACCOUNT_NAME=${OP_ACCOUNT:-"Ground Up Software"}
# The name of the Secure Note/API Credentials item in 1Password. Can be overridden by OP_SECRET_ITEM_TITLE.
SECRET_ITEM_TITLE=${OP_SECRET_ITEM_TITLE:-"LLOOOOMM Secrets"}

# --- Script Logic ---
set -e

# Collect secret names until we hit '--'
secret_keys=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --)
      shift
      break
      ;;
    *)
      secret_keys+=("$1")
      shift
      ;;
  esac
done

# The rest of the arguments are the command to run
command_to_run=("$@")
if [ ${#command_to_run[@]} -eq 0 ]; then
  echo "Error: No command provided to secure_runner.sh" >&2
  exit 1
fi

# Fetch the secrets from 1Password as JSON
# This requires the user to be logged in via `op signin`
secrets_json=$(op item get "$SECRET_ITEM_TITLE" --format json --account "$ACCOUNT_NAME" 2>/dev/null)
if [ -z "$secrets_json" ]; then
  echo "Error: Could not fetch secrets from 1Password. Is the item named '$SECRET_ITEM_TITLE' in the '$ACCOUNT_NAME' account correct? Are you signed in with 'op signin'?" >&2
  exit 1
fi

# Parse the JSON and export the requested secrets
for key in "${secret_keys[@]}"; do
  # Use jq to find the field with the matching label and get its value
  value=$(echo "$secrets_json" | jq -r --arg KEY "$key" '.fields[] | select(.label == $KEY) | .value')
  
  if [ -n "$value" ]; then
    # Export the variable so the child process inherits it
    export "$key=$value"
    echo "Exported secret: $key" >&2
  else
    echo "Warning: Secret key '$key' not found in '$SECRET_ITEM_TITLE' item in the '$ACCOUNT_NAME' account." >&2
  fi
done

# Execute the actual command
exec "${command_to_run[@]}" 