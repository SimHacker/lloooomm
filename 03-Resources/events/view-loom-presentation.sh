#!/bin/bash
# View the LOOM methodology presentation

echo "🎨 LOOM Methodology Presentation Viewer"
echo "========================================"
echo ""
echo "Available formats:"
echo "1) Interactive HTML presentation (recommended)"
echo "2) Technical markdown document"
echo "3) Both in split terminal (requires tmux)"
echo "4) Start presentation server (share with team)"
echo ""
read -p "Select option (1-4): " choice

case $choice in
    1)
        echo "Opening HTML presentation..."
        if command -v open &> /dev/null; then
            open webbie-problem-solving-manifesto.html
        elif command -v xdg-open &> /dev/null; then
            xdg-open webbie-problem-solving-manifesto.html
        else
            echo "Please open webbie-problem-solving-manifesto.html manually"
        fi
        ;;
    2)
        echo "Viewing markdown document..."
        if command -v glow &> /dev/null; then
            glow -p webbie-loom-methodology.md
        elif command -v mdcat &> /dev/null; then
            mdcat webbie-loom-methodology.md | less -R
        else
            less webbie-loom-methodology.md
        fi
        ;;
    3)
        if command -v tmux &> /dev/null; then
            echo "Opening split view in tmux..."
            tmux new-session -d -s loom
            tmux send-keys -t loom "open webbie-problem-solving-manifesto.html" C-m
            tmux split-window -h -t loom
            tmux send-keys -t loom "glow -p webbie-loom-methodology.md" C-m
            tmux attach -t loom
        else
            echo "tmux not found. Please install tmux for split view."
        fi
        ;;
    4)
        echo "Starting presentation server..."
        echo "Share this URL with your team: http://$(hostname):8888"
        echo ""
        echo "Files available:"
        echo "- http://$(hostname):8888/webbie-problem-solving-manifesto.html"
        echo "- http://$(hostname):8888/webbie-loom-methodology.md"
        echo "- http://$(hostname):8888/tailscale-oauth-visualization.html"
        echo ""
        echo "Press Ctrl+C to stop the server"
        python3 -m http.server 8888
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac 