# Sudo Tips for LLOOOOMM Automation

## Extend sudo timeout (more time before password prompt)

Edit sudo configuration:
```bash
sudo visudo
```

Add this line (extends timeout to 60 minutes):
```
Defaults timestamp_timeout=60
```

## Keep sudo warm during long scripts

Add this to the beginning of scripts:
```bash
# Keep sudo alive
sudo -v
while true; do sudo -n true; sleep 50; done 2>/dev/null &
SUDO_PID=$!
trap "kill $SUDO_PID" EXIT
```

## For specific commands without password (BE CAREFUL!)

Add to sudoers (replace username with yours):
```
username ALL=(ALL) NOPASSWD: /usr/bin/gcloud
```

⚠️ Security note: Only use NOPASSWD for specific, safe commands!

## Quick warm-up before automation
```bash
# Run this before starting automation tasks
sudo -v && echo "✅ Sudo warmed up for 15 minutes!"
``` 