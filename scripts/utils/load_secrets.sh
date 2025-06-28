#!/bin/bash
#
# Loads all secrets from a 1Password item into the current shell environment.
# This script is meant to be sourced, not executed directly.
# Usage: source scripts/utils/load_secrets.sh

# --- Configuration (with environment variable overrides) ---
ACCOUNT_NAME=${OP_ACCOUNT:-"Ground Up Software"}
SECRET_ITEM_TITLE=${OP_SECRET_ITEM_TITLE:-"LLOOOOMM Secrets"}

# --- Script Logic ---
__load_secrets() {
    echo "Attempting to load secrets from item '$SECRET_ITEM_TITLE' in account '$ACCOUNT_NAME'..." >&2

    if ! op account get >/dev/null 2>&1; then
        echo "Error: Not logged into 1Password CLI. Please run 'op signin' first." >&2
        return 1
    fi

    local secrets_json
    secrets_json=$(op item get "$SECRET_ITEM_TITLE" --format json --account "$ACCOUNT_NAME" 2>/dev/null)
    
    if [ -z "$secrets_json" ]; then
        echo "Error: Could not fetch secrets from 1Password." >&2
        echo "Please check: " >&2
        echo "1. Are you signed in with 'op signin'?" >&2
        echo "2. Is the item named '$SECRET_ITEM_TITLE' correct?" >&2
        echo "3. Is the account name '$ACCOUNT_NAME' correct?" >&2
        return 1
    fi

    # Loop through all fields, exporting them as environment variables
    # Use process substitution and null-delimited output from jq for safety
    while IFS='=' read -r -d '' key value; do
        export "$key=$value"
        echo "Exported: $key" >&2
    done < <(echo "$secrets_json" | jq -r '.fields[] | .label + "=" + .value + "\u0000"')

    echo "✅ All secrets loaded successfully into the current shell." >&2
}

# Ensure the script is sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "This script must be sourced to affect the current shell." >&2
    echo "Usage: source ${BASH_SOURCE[0]}" >&2
    exit 1
fi

__load_secrets
unset -f __load_secrets 