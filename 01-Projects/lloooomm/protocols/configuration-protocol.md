# LLOOOOMM Configuration Protocol - "Just Work"

## Heisenbergian Configuration

**The act of observing configuration changes the system's behavior.**

When you load `lloooomm-debug.yml`, you're not just reading settings - you're transforming the entire system into debug mode. The configuration file you observe determines the reality you experience.

## Core Principles

### 1. Suffix-Based Configuration Selection
```
lloooomm.yml         → Default mode
lloooomm-debug.yml   → Debug mode (verbose logging)
lloooomm-test.yml    → Test mode (isolated state)
lloooomm-prod.yml    → Production mode (optimized)
```

### 2. Configuration Cascading
- Base configuration provides defaults
- Suffix configurations override selectively
- Environment determines active configuration
- "Just Work" - the right config loads automatically

### 3. Mode-Aware Logging
```yaml
# Normal mode (lloooomm.yml)
logging:
  enabled: true
  logs_file: "lloooomm-logs.md"
  level: "INFO"  # Only important events

# Debug mode (lloooomm-debug.yml)
logging:
  enabled: true
  logs_file: "lloooomm-logs-debug.md"  # Separate file!
  level: "DEBUG"  # Everything logged
  verbose: true
```

## The "Just Work" Philosophy

1. **Zero Configuration**: Defaults that make sense
2. **Progressive Enhancement**: Add configs as needed
3. **Mode Isolation**: Debug logs don't pollute production
4. **Automatic Selection**: System picks right config
5. **Observable Effects**: Config changes are immediately visible

## Configuration Naming Convention

```
{base}-{mode}.{ext}
```

Examples:
- `lloooomm-debug.yml`
- `tailscale-oauth-key-test.yaml`
- `vm-state-prod.yml`

## Logging Optimization Tips

### For LLMs and Tools

**Prefer Append Operations:**
- Use append-only tools when available
- Avoid read-modify-write cycles for logs
- Stream writes for efficiency

**Addressing Modes:**
- `append:` - Add to end of file
- `prepend:` - Add to beginning (rare)
- `insert:line:` - Insert at specific line
- `replace:pattern:` - Pattern-based replacement

## Mode Switching

When switching modes:
1. Save current state if needed
2. Load new configuration
3. Redirect logs to mode-specific files
4. Adjust verbosity and behavior
5. Continue with isolated state

Example:
```
LLOOOOMM_MODE: debug
# Now writing to lloooomm-logs-debug.md
# Verbose output enabled
# Stack traces included

LLOOOOMM_MODE: normal
# Back to lloooomm-logs.md
# Only important events logged
```

## The Beauty of Separation

Debug logs stay in debug files. Production logs stay clean. Test runs don't contaminate real data. Each mode has its own universe of files, perfectly isolated yet easily accessible.

## Future Compilation

This protocol will compile to:
- Automatic configuration loaders
- Mode-aware file routers
- Dynamic behavior switching
- State isolation managers

But for now, it's beautifully simple documentation that "Just Works". 