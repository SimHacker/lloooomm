# LLOOOOMM Logging Protocol

## Core Convention

Every LLOOOOMM document can have associated log files:
- `lloooomm-logs.md` - Append-only structured activity log
- `lloooomm-errors.md` - Append-only error and exception log

## Configuration via YAML

Logging behavior is controlled by YAML configuration files with suffix patterns:

```yaml
# lloooomm.yml (default config)
logging:
  enabled: true
  logs_file: "lloooomm-logs.md"
  errors_file: "lloooomm-errors.md"

# lloooomm-debug.yml (debug config)
logging:
  enabled: true
  logs_file: "lloooomm-logs-debug.md"
  errors_file: "lloooomm-errors-debug.md"
  verbose: true
```

## Log Entry Format

Structured markdown with consistent formatting:

```markdown
## [2024-01-15T10:30:45Z] Activity: Task Started
- **Context**: tailscale-oauth-key.md
- **Action**: Beginning OAuth configuration
- **State**: PROJECT_ID=leela-prod

## [2024-01-15T10:31:02Z] Error: API Call Failed
- **Context**: gcloud auth
- **Error**: Permission denied
- **Stack**: Line 45 in setup script
- **Recovery**: Retrying with --quiet flag
```

## Suffix Convention

Different logging runs use suffix patterns:
- Default: `lloooomm-logs.md`
- Debug mode: `lloooomm-logs-debug.md`
- Test run: `lloooomm-logs-test.md`
- Production: `lloooomm-logs-prod.md`

## Future Compilation Intent

This logging protocol is designed to be compiled into a Python logging framework that:
- Reads YAML configuration
- Manages append-only log files
- Provides structured logging API
- Supports multiple log streams
- Enables/disables logging dynamically

The compilation will happen externally as a standalone module, not embedded in LLOOOOMM documents.

## Usage in LLOOOOMM Documents

Simply reference logging in your LLOOOOMM document:

```markdown
LLOOOOMM_LOG: "Starting analysis phase"
LLOOOOMM_ERROR: "Failed to connect to API"
```

The LLOOOOMM processor handles the actual file operations based on the active configuration. 