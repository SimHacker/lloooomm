#!/bin/bash
# Simple script to view the Tailscale OAuth analysis

echo "🎮 Opening Tailscale OAuth Analysis..."
echo ""
echo "Choose viewing method:"
echo "1) Open HTML visualization in browser (requires local file access)"
echo "2) View markdown analysis in terminal"
echo "3) Start local web server (Python required)"
echo ""
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        if command -v open &> /dev/null; then
            # macOS
            open tailscale-oauth-visualization.html
        elif command -v xdg-open &> /dev/null; then
            # Linux
            xdg-open tailscale-oauth-visualization.html
        else
            echo "Please open tailscale-oauth-visualization.html in your browser manually"
        fi
        ;;
    2)
        if command -v mdcat &> /dev/null; then
            mdcat tailscale-oauth-analysis.md
        elif command -v glow &> /dev/null; then
            glow tailscale-oauth-analysis.md
        else
            cat tailscale-oauth-analysis.md
        fi
        ;;
    3)
        echo "Starting local web server on http://localhost:8080"
        echo "Press Ctrl+C to stop"
        if command -v python3 &> /dev/null; then
            python3 -m http.server 8080
        elif command -v python &> /dev/null; then
            python -m SimpleHTTPServer 8080
        else
            echo "Python not found. Please install Python to use this option."
        fi
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac 