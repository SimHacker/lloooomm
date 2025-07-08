/**
 * LLOOOOMM Context-Sensitive Turtle SPLOOT Engine
 * Dancing turtles that drop contextual ideas, emojis, and concepts
 */

class TurtleSplootEngine {
    constructor(container = document.body) {
        this.container = container;
        this.turtles = [];
        this.sploots = [];
        this.recentSploots = new Map();
        this.isRunning = false;
        this.animationFrame = null;
        this.splotLibrary = null;
        this.contextKeywords = [];
        this.draggedTurtle = null;
        this.dragOffset = { x: 0, y: 0 };
        
        this.config = {
            maxTurtles: 6,
            turtleSize: 30,
            speed: 1.5,
            splotFrequency: 0.015,
            splotLifetime: 8000,
            cooldownTime: 30000,
            contextWeight: 0.8
        };
        
        // Scroll tracking for bouncing turtles
        this.scrollHistory = [];
        this.lastScrollY = window.scrollY;
        this.scrollVelocity = 0;
        
        this.loadSplotLibrary();
        this.setupStyles();
        this.extractContextKeywords();
        this.setupDragAndDrop();
        this.setupScrollTracking();
    }
    
    configure(options) {
        // Merge provided options with default config
        Object.assign(this.config, options);
        return this;
    }
    
    async loadSplotLibrary() {
        try {
            const response = await fetch('sploot-library.json');
            this.splotLibrary = await response.json();
        } catch (error) {
            console.warn('Could not load SPLOOT library, using defaults');
            this.splotLibrary = {
                concepts: [
                    { text: "CONSCIOUSNESS", description: "Navigate awareness", link: "#demo", color: "#2E8B57", keywords: ["consciousness", "awareness"] },
                    { text: "SPLOOT", description: "Comfortable positioning", link: "#demo", color: "#FF69B4", keywords: ["sploot", "comfort"] },
                    { text: "TURTLE POWER", description: "Logo programming", link: "hunter-homepage.html", color: "#20B2AA", keywords: ["turtle", "programming"] }
                ],
                emojis: [
                    { emoji: "🐢", weight: 10, keywords: ["turtle"] },
                    { emoji: "✨", weight: 8, keywords: ["magic"] },
                    { emoji: "🐱", weight: 6, keywords: ["cat"] }
                ]
            };
        }
    }
    
    extractContextKeywords() {
        // Extract keywords from data-keywords attributes
        const elements = document.querySelectorAll('[data-keywords]');
        this.contextKeywords = [];
        
        elements.forEach(el => {
            const keywords = el.getAttribute('data-keywords').split(',').map(k => k.trim());
            this.contextKeywords.push(...keywords);
        });
        
        // Extract from page content
        const title = document.title.toLowerCase();
        const headings = Array.from(document.querySelectorAll('h1, h2, h3')).map(h => h.textContent.toLowerCase());
        const metaKeywords = document.querySelector('meta[name="keywords"]');
        
        if (metaKeywords) {
            this.contextKeywords.push(...metaKeywords.content.split(',').map(k => k.trim()));
        }
        
        this.contextKeywords.push(...title.split(' '));
        headings.forEach(heading => {
            this.contextKeywords.push(...heading.split(' '));
        });
        
        // Clean up keywords
        const stopWords = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'];
        this.contextKeywords = [...new Set(this.contextKeywords)]
            .filter(word => word.length > 2 && !stopWords.includes(word.toLowerCase()));
    }
    
    setupStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .turtle {
                position: fixed;
                font-size: 30px;
                cursor: grab;
                pointer-events: auto;
                filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
                animation: turtleBob 2s ease-in-out infinite;
                transition: all 0.3s ease;
                z-index: 1000;
                user-select: none;
            }
            
            .turtle:active {
                cursor: grabbing;
            }
            
            .turtle.dragging {
                animation: none;
                transform: scale(1.2);
                filter: drop-shadow(4px 4px 8px rgba(0,0,0,0.5));
                z-index: 1002;
            }
            
            .turtle.popped {
                animation: none;
                transform: scale(1.3);
                filter: drop-shadow(4px 4px 12px rgba(255,215,0,0.6));
                z-index: 1003;
            }
            
            @keyframes turtleBob {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-5px) rotate(5deg); }
            }
            
            .sploot-popup {
                position: fixed;
                pointer-events: auto;
                cursor: pointer;
                z-index: 999;
                animation: splotBloom 0.8s ease-out;
                transform-origin: center bottom;
            }
            
            @keyframes splotBloom {
                0% { 
                    transform: scale(0) translateY(20px);
                    opacity: 0;
                }
                30% { 
                    transform: scale(1.2) translateY(-5px);
                    opacity: 0.8;
                }
                100% { 
                    transform: scale(1) translateY(0px);
                    opacity: 1;
                }
            }
            
            .sploot-backdrop {
                background: linear-gradient(135deg, rgba(0,0,0,0.85), rgba(30,30,30,0.9));
                border-radius: 15px;
                padding: 16px 20px;
                backdrop-filter: blur(8px);
                border: 2px solid rgba(255,215,0,0.4);
                box-shadow: 0 8px 32px rgba(0,0,0,0.3);
                min-width: 200px;
                max-width: 300px;
            }
            
            .sploot-content {
                text-align: center;
            }
            
            .sploot-text {
                color: #FFD700;
                font-weight: bold;
                font-size: 16px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
                margin-bottom: 8px;
                letter-spacing: 1px;
            }
            
            .sploot-description {
                color: #87CEEB;
                font-size: 13px;
                font-style: italic;
                margin-bottom: 8px;
                line-height: 1.4;
            }
            
            .sploot-details {
                color: #E0E0E0;
                font-size: 11px;
                margin-bottom: 12px;
                line-height: 1.3;
                opacity: 0.9;
            }
            
            .sploot-link {
                display: inline-block;
                background: linear-gradient(135deg, #FF69B4, #FF1493);
                color: white;
                text-decoration: none;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: bold;
                transition: all 0.3s ease;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
            }
            
            .sploot-link:hover {
                background: linear-gradient(135deg, #FF1493, #DC143C);
                transform: scale(1.05);
                box-shadow: 0 4px 12px rgba(255,20,147,0.4);
            }
            
            .sploot-close {
                position: absolute;
                top: -10px;
                right: -10px;
                background: linear-gradient(135deg, #FF4444, #CC0000);
                color: white;
                border: none;
                border-radius: 50%;
                width: 24px;
                height: 24px;
                font-size: 14px;
                font-weight: bold;
                cursor: pointer;
                line-height: 1;
                transition: all 0.3s ease;
                box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            }
            
            .sploot-close:hover {
                background: linear-gradient(135deg, #FF0000, #990000);
                transform: scale(1.1);
            }
            
            .sploot-emoji {
                position: fixed;
                font-size: 24px;
                pointer-events: none;
                z-index: 998;
                animation: emojiFloat 3s ease-out forwards;
            }
            
            @keyframes emojiFloat {
                0% { 
                    transform: scale(0) rotate(0deg);
                    opacity: 0;
                }
                20% { 
                    transform: scale(1.5) rotate(180deg);
                    opacity: 1;
                }
                80% { 
                    transform: scale(1) rotate(360deg) translateY(-20px);
                    opacity: 1;
                }
                100% { 
                    transform: scale(0.5) rotate(540deg) translateY(-40px);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    setupDragAndDrop() {
        document.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        document.addEventListener('mouseup', (e) => this.handleMouseUp(e));
    }
    
    setupScrollTracking() {
        // Track scroll velocity for bouncing turtles
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            const currentScrollY = window.scrollY;
            const deltaY = currentScrollY - this.lastScrollY;
            const now = Date.now();
            
            // Add to scroll history
            this.scrollHistory.push({ y: currentScrollY, deltaY, time: now });
            
            // Keep only recent history (last 200ms)
            this.scrollHistory = this.scrollHistory.filter(entry => now - entry.time < 200);
            
            // Calculate smoothed scroll velocity
            if (this.scrollHistory.length > 1) {
                const totalDelta = this.scrollHistory.reduce((sum, entry) => sum + entry.deltaY, 0);
                const timeSpan = now - this.scrollHistory[0].time;
                this.scrollVelocity = timeSpan > 0 ? (totalDelta / timeSpan) * 16.67 : 0; // Convert to pixels per frame
            }
            
            this.lastScrollY = currentScrollY;
            
            // Clear velocity after scroll stops
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                this.scrollVelocity = 0;
            }, 100);
        });
    }
    
    createTurtle(x, y, pattern = null) {
        const patterns = ['spiral', 'figure8', 'bounce', 'orbit', 'linear', 'zigzag'];
        const selectedPattern = pattern || patterns[Math.floor(Math.random() * patterns.length)];
        
        const turtle = {
            id: Math.random().toString(36).substr(2, 9),
            element: document.createElement('div'),
            x: x || Math.random() * (window.innerWidth - 60) + 30,
            y: y || Math.random() * (window.innerHeight - 60) + 30,
            vx: (Math.random() - 0.5) * this.config.speed,
            vy: (Math.random() - 0.5) * this.config.speed,
            angle: Math.random() * Math.PI * 2,
            pattern: selectedPattern,
            patternData: this.initializePattern(selectedPattern),
            lastSploot: 0,
            isPopped: false,
            isDragging: false,
            wasDragged: false
        };
        
        turtle.element.className = 'turtle';
        turtle.element.textContent = '🐢';
        turtle.element.style.left = turtle.x + 'px';
        turtle.element.style.top = turtle.y + 'px';
        turtle.element.style.fontSize = this.config.turtleSize + 'px';
        
        // Add drag and click handlers
        turtle.element.addEventListener('mousedown', (e) => this.handleTurtleMouseDown(e, turtle));
        turtle.element.addEventListener('click', (e) => this.handleTurtleClick(e, turtle));
        
        document.body.appendChild(turtle.element);
        this.turtles.push(turtle);
        
        return turtle;
    }
    
    initializePattern(pattern) {
        switch(pattern) {
            case 'spiral':
                return { 
                    centerX: Math.random() * window.innerWidth,
                    centerY: Math.random() * window.innerHeight,
                    radius: 30,
                    radiusGrowth: 0.3,
                    angleSpeed: 0.03
                };
            case 'figure8':
                return {
                    centerX: Math.random() * window.innerWidth,
                    centerY: Math.random() * window.innerHeight,
                    width: 80,
                    height: 40,
                    speed: 0.02
                };
            case 'zigzag':
                return {
                    amplitude: 50,
                    frequency: 0.02,
                    direction: Math.random() > 0.5 ? 1 : -1
                };
            case 'bounce':
                return {
                    gravity: 0.15,
                    bounce: 0.85,
                    friction: 0.995
                };
            case 'orbit':
                return {
                    centerX: window.innerWidth / 2,
                    centerY: window.innerHeight / 2,
                    radius: 80 + Math.random() * 150,
                    speed: 0.015 + Math.random() * 0.02
                };
            default:
                return {};
        }
    }
    
    handleTurtleMouseDown(e, turtle) {
        e.preventDefault();
        e.stopPropagation();
        
        this.draggedTurtle = turtle;
        turtle.isDragging = true;
        turtle.element.classList.add('dragging');
        
        const rect = turtle.element.getBoundingClientRect();
        this.dragOffset.x = e.clientX - rect.left;
        this.dragOffset.y = e.clientY - rect.top;
    }
    
    handleTurtleClick(e, turtle) {
        e.stopPropagation();
        
        // Only handle click if turtle wasn't dragged
        if (!turtle.wasDragged) {
            this.toggleTurtlePop(turtle);
        }
        
        turtle.wasDragged = false;
    }
    
    handleMouseMove(e) {
        if (this.draggedTurtle) {
            this.draggedTurtle.wasDragged = true;
            this.draggedTurtle.x = e.clientX - this.dragOffset.x;
            this.draggedTurtle.y = e.clientY - this.dragOffset.y;
            
            // Update visual position
            this.draggedTurtle.element.style.left = this.draggedTurtle.x + 'px';
            this.draggedTurtle.element.style.top = this.draggedTurtle.y + 'px';
        }
    }
    
    handleMouseUp(e) {
        if (this.draggedTurtle) {
            this.draggedTurtle.isDragging = false;
            this.draggedTurtle.element.classList.remove('dragging');
            
            // Reset velocity for new position
            this.draggedTurtle.vx = (Math.random() - 0.5) * this.config.speed;
            this.draggedTurtle.vy = (Math.random() - 0.5) * this.config.speed;
            
            this.draggedTurtle = null;
        }
    }
    
    toggleTurtlePop(turtle) {
        if (turtle.isPopped) {
            this.unpopTurtle(turtle);
        } else {
            this.popTurtle(turtle);
        }
    }
    
    popTurtle(turtle) {
        turtle.isPopped = true;
        turtle.element.classList.add('popped');
        
        // Create pie menu
        this.createPieMenu(turtle);
    }
    
    unpopTurtle(turtle) {
        turtle.isPopped = false;
        turtle.element.classList.remove('popped');
    }
    
    getContextualSploot(x, y) {
        if (!this.splotLibrary || !this.splotLibrary.concepts) return null;
        
        // Get context from the area where the click happened
        const element = document.elementFromPoint(x, y);
        let localKeywords = [];
        
        if (element) {
            // Walk up the DOM tree to collect keywords
            let current = element;
            while (current && current !== document.body) {
                if (current.hasAttribute && current.hasAttribute('data-keywords')) {
                    const keywords = current.getAttribute('data-keywords').split(',').map(k => k.trim());
                    localKeywords.push(...keywords);
                }
                
                // Also extract from text content
                if (current.textContent) {
                    const words = current.textContent.toLowerCase().split(/\s+/);
                    localKeywords.push(...words.filter(w => w.length > 3));
                }
                
                current = current.parentElement;
            }
        }
        
        // Combine with global context keywords
        const allKeywords = [...localKeywords, ...this.contextKeywords];
        
        // Score concepts based on keyword matches
        const scoredConcepts = this.splotLibrary.concepts.map(concept => {
            let score = 0;
            const conceptKeywords = concept.keywords || [];
            
            conceptKeywords.forEach(keyword => {
                allKeywords.forEach(contextKeyword => {
                    if (keyword.toLowerCase().includes(contextKeyword.toLowerCase()) ||
                        contextKeyword.toLowerCase().includes(keyword.toLowerCase())) {
                        score += 1;
                    }
                });
            });
            
            return { concept, score };
        });
        
        // Filter out recently used concepts
        const availableConcepts = scoredConcepts.filter(({ concept }) => {
            const lastUsed = this.recentSploots.get(concept.text);
            return !lastUsed || (Date.now() - lastUsed) > this.config.cooldownTime;
        });
        
        if (availableConcepts.length === 0) {
            // If all concepts are on cooldown, use any concept
            return scoredConcepts[Math.floor(Math.random() * scoredConcepts.length)]?.concept;
        }
        
        // Sort by score and use weighted random selection
        availableConcepts.sort((a, b) => b.score - a.score);
        
        // Use contextual concepts more often
        const shouldUseContextual = Math.random() < this.config.contextWeight;
        if (shouldUseContextual && availableConcepts[0].score > 0) {
            // Pick from top scoring concepts
            const topConcepts = availableConcepts.filter(({ score }) => score >= availableConcepts[0].score * 0.7);
            return topConcepts[Math.floor(Math.random() * topConcepts.length)].concept;
        }
        
        // Random selection from available concepts
        return availableConcepts[Math.floor(Math.random() * availableConcepts.length)].concept;
    }
    
    createSploot(x, y, type = 'concept') {
        if (type === 'concept') {
            const concept = this.getContextualSploot(x, y);
            if (!concept) return;
            
            this.recentSploots.set(concept.text, Date.now());
            this.createConceptSploot(x, y, concept);
        } else {
            this.createEmojiSploot(x, y);
        }
    }
    
    createConceptSploot(x, y, concept) {
        const sploot = {
            id: Math.random().toString(36).substr(2, 9),
            element: document.createElement('div'),
            x: x,
            y: y,
            concept: concept,
            createdAt: Date.now()
        };
        
        sploot.element.className = 'sploot-popup';
        sploot.element.style.left = (x - 150) + 'px'; // Center under turtle
        sploot.element.style.top = (y + 50) + 'px';
        
        const backdrop = document.createElement('div');
        backdrop.className = 'sploot-backdrop';
        backdrop.style.position = 'relative';
        
        const content = document.createElement('div');
        content.className = 'sploot-content';
        content.style.display = 'flex';
        content.style.flexDirection = 'column';
        content.style.alignItems = 'center';
        
        // Title (required, potentially linked)
        const title = document.createElement(concept.url ? 'a' : 'div');
        title.className = 'sploot-text';
        title.textContent = concept.title || concept.text; // Fallback to old 'text' property
        if (concept.url) {
            title.href = concept.url;
            title.target = '_blank';
            title.style.textDecoration = 'none';
            title.style.color = 'inherit';
        }
        content.appendChild(title);
        
        // Image or SVG (optional)
        if (concept.image) {
            const img = document.createElement('img');
            img.src = concept.image;
            img.style.maxWidth = '100%';
            img.style.height = 'auto';
            img.style.margin = '8px 0';
            img.style.borderRadius = '8px';
            
            // Apply dimensions if specified
            if (concept.width) {
                img.style.width = concept.width + 'px';
            }
            if (concept.height) {
                img.style.height = concept.height + 'px';
            }
            
            content.appendChild(img);
        }
        
        // Text content (optional, unformatted)
        if (concept.text && concept.title !== concept.text) {
            const textDiv = document.createElement('div');
            textDiv.className = 'sploot-description';
            textDiv.textContent = concept.text;
            content.appendChild(textDiv);
        } else if (concept.description) {
            // Fallback to old 'description' property
            const description = document.createElement('div');
            description.className = 'sploot-description';
            description.textContent = concept.description;
            content.appendChild(description);
        }
        
        // HTML content (optional, formatted)
        if (concept.html) {
            const htmlDiv = document.createElement('div');
            htmlDiv.className = 'sploot-html';
            htmlDiv.innerHTML = concept.html;
            htmlDiv.style.marginTop = '8px';
            content.appendChild(htmlDiv);
        }
        
        // Details (legacy support)
        if (concept.details && !concept.html) {
            const details = document.createElement('div');
            details.className = 'sploot-details';
            details.textContent = concept.details;
            content.appendChild(details);
        }
        
        // Explore link (if no URL in title)
        if (!concept.url && (concept.link || concept.url)) {
            const link = document.createElement('a');
            link.className = 'sploot-link';
            link.textContent = 'Explore →';
            link.href = concept.link || concept.url;
            link.target = '_blank';
            content.appendChild(link);
        }
        
        const closeBtn = document.createElement('button');
        closeBtn.className = 'sploot-close';
        closeBtn.textContent = '✕';
        closeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.removeSploot(sploot);
        });
        
        backdrop.appendChild(content);
        backdrop.appendChild(closeBtn);
        sploot.element.appendChild(backdrop);
        
        document.body.appendChild(sploot.element);
        this.sploots.push(sploot);
        
        // Auto-remove after lifetime
        setTimeout(() => {
            this.removeSploot(sploot);
        }, this.config.splotLifetime);
    }
    
    createEmojiSploot(x, y) {
        if (!this.splotLibrary || !this.splotLibrary.emojis) return;
        
        const emoji = this.splotLibrary.emojis[Math.floor(Math.random() * this.splotLibrary.emojis.length)];
        
        const sploot = {
            id: Math.random().toString(36).substr(2, 9),
            element: document.createElement('div'),
            x: x,
            y: y,
            emoji: emoji,
            createdAt: Date.now()
        };
        
        sploot.element.className = 'sploot-emoji';
        sploot.element.style.left = x + 'px';
        sploot.element.style.top = y + 'px';
        sploot.element.textContent = emoji.emoji;
        sploot.element.title = emoji.description;
        
        document.body.appendChild(sploot.element);
        this.sploots.push(sploot);
        
        // Auto-remove after animation
        setTimeout(() => {
            this.removeSploot(sploot);
        }, 3000);
    }
    
    removeSploot(sploot) {
        const index = this.sploots.indexOf(sploot);
        if (index > -1) {
            this.sploots.splice(index, 1);
            if (sploot.element.parentNode) {
                sploot.element.parentNode.removeChild(sploot.element);
            }
        }
    }
    
    updateTurtle(turtle, deltaTime) {
        if (turtle.isDragging || turtle.isPopped) return; // Don't move dragged or popped turtles
        
        const now = Date.now();
        
        // Update position based on pattern
        switch(turtle.pattern) {
            case 'spiral':
                this.updateSpiral(turtle, deltaTime);
                break;
            case 'figure8':
                this.updateFigure8(turtle, deltaTime);
                break;
            case 'zigzag':
                this.updateZigzag(turtle, deltaTime);
                break;
            case 'bounce':
                this.updateBounce(turtle, deltaTime);
                break;
            case 'orbit':
                this.updateOrbit(turtle, deltaTime);
                break;
            default:
                this.updateLinear(turtle, deltaTime);
        }
        
        // Boundary handling
        this.handleBoundaries(turtle);
        
        // Update visual position
        turtle.element.style.left = turtle.x + 'px';
        turtle.element.style.top = turtle.y + 'px';
        turtle.element.style.transform = `rotate(${turtle.angle}rad)`;
        
        // Random SPLOOT generation
        if (Math.random() < this.config.splotFrequency && 
            now - turtle.lastSploot > 2000) {
            this.createSploot(turtle.x, turtle.y);
            turtle.lastSploot = now;
        }
    }
    
    updateSpiral(turtle, deltaTime) {
        turtle.patternData.radius += turtle.patternData.radiusGrowth;
        turtle.angle += turtle.patternData.angleSpeed;
        
        turtle.x = turtle.patternData.centerX + 
                  Math.cos(turtle.angle) * turtle.patternData.radius;
        turtle.y = turtle.patternData.centerY + 
                  Math.sin(turtle.angle) * turtle.patternData.radius;
        
        if (turtle.patternData.radius > 200) {
            turtle.patternData.radius = 30;
            turtle.patternData.centerX = Math.random() * window.innerWidth;
            turtle.patternData.centerY = Math.random() * window.innerHeight;
        }
    }
    
    updateFigure8(turtle, deltaTime) {
        turtle.angle += turtle.patternData.speed;
        
        turtle.x = turtle.patternData.centerX + 
                  Math.sin(turtle.angle) * turtle.patternData.width;
        turtle.y = turtle.patternData.centerY + 
                  Math.sin(turtle.angle * 2) * turtle.patternData.height;
    }
    
    updateZigzag(turtle, deltaTime) {
        turtle.x += turtle.vx;
        turtle.y += turtle.vy + Math.sin(turtle.angle) * turtle.patternData.amplitude * turtle.patternData.frequency;
        turtle.angle += turtle.patternData.frequency * turtle.patternData.direction;
    }
    
    updateBounce(turtle, deltaTime) {
        // Apply gravity
        turtle.vy += turtle.patternData.gravity;
        
        // For bouncing turtles, add scroll velocity influence
        if (Math.abs(this.scrollVelocity) > 0.1) {
            // Add scroll velocity to turtle's movement (dampened)
            turtle.vy += this.scrollVelocity * 0.3;
            
            // Limit maximum velocity to keep it fun but not crazy
            const maxVel = 15;
            turtle.vy = Math.max(-maxVel, Math.min(maxVel, turtle.vy));
        }
        
        // Update position
        turtle.x += turtle.vx;
        turtle.y += turtle.vy;
        
        // Apply friction
        turtle.vx *= turtle.patternData.friction;
        turtle.vy *= turtle.patternData.friction;
        
        // Screen-relative bouncing (not content-relative)
        const screenTop = window.scrollY;
        const screenBottom = window.scrollY + window.innerHeight;
        const screenLeft = 0;
        const screenRight = window.innerWidth;
        const margin = this.config.turtleSize;
        
        // Bounce off screen edges with scroll awareness
        if (turtle.x < screenLeft + margin || turtle.x > screenRight - margin) {
            turtle.vx *= -turtle.patternData.bounce;
            turtle.x = Math.max(screenLeft + margin, Math.min(screenRight - margin, turtle.x));
            
            // Add some scroll velocity to the bounce for extra fun
            if (Math.abs(this.scrollVelocity) > 0.1) {
                turtle.vy += this.scrollVelocity * 0.2;
            }
        }
        
        if (turtle.y < screenTop + margin || turtle.y > screenBottom - margin) {
            turtle.vy *= -turtle.patternData.bounce;
            turtle.y = Math.max(screenTop + margin, Math.min(screenBottom - margin, turtle.y));
            
            // Extra bounce when hitting top/bottom during scroll
            if (Math.abs(this.scrollVelocity) > 0.1) {
                turtle.vy += this.scrollVelocity * 0.4;
                turtle.vx += (Math.random() - 0.5) * 2; // Add some horizontal randomness
            }
        }
    }
    
    updateOrbit(turtle, deltaTime) {
        turtle.angle += turtle.patternData.speed;
        
        turtle.x = turtle.patternData.centerX + 
                  Math.cos(turtle.angle) * turtle.patternData.radius;
        turtle.y = turtle.patternData.centerY + 
                  Math.sin(turtle.angle) * turtle.patternData.radius;
    }
    
    updateLinear(turtle, deltaTime) {
        turtle.x += turtle.vx;
        turtle.y += turtle.vy;
        turtle.angle += 0.01;
    }
    
    handleBoundaries(turtle) {
        const margin = this.config.turtleSize;
        
        if (turtle.x < margin || turtle.x > window.innerWidth - margin) {
            turtle.vx *= -1;
            turtle.x = Math.max(margin, Math.min(window.innerWidth - margin, turtle.x));
        }
        
        if (turtle.y < margin || turtle.y > window.innerHeight - margin) {
            turtle.vy *= -1;
            turtle.y = Math.max(margin, Math.min(window.innerHeight - margin, turtle.y));
        }
    }
    
    handleBackgroundClick(e) {
        // Only create turtle if clicking on background (not on other elements)
        if (e.target === document.body || 
            e.target.classList.contains('container') ||
            e.target.tagName === 'MAIN' ||
            e.target.tagName === 'SECTION') {
            
            const turtle = this.createTurtle(e.clientX, e.clientY);
            
            // Make turtle POPPED and create SPLOOT immediately
            turtle.isPopped = true;
            turtle.element.classList.add('popped');
            
            setTimeout(() => {
                this.createSploot(turtle.x, turtle.y, 'concept');
            }, 200);
        }
    }
    
    animate() {
        if (!this.isRunning) return;
        
        const now = Date.now();
        const deltaTime = now - (this.lastFrame || now);
        this.lastFrame = now;
        
        // Update all turtles
        this.turtles.forEach(turtle => {
            this.updateTurtle(turtle, deltaTime);
        });
        
        // Clean up old SPLOOTs
        this.sploots = this.sploots.filter(sploot => {
            const age = now - sploot.createdAt;
            const maxAge = sploot.concept ? this.config.splotLifetime : 3000;
            
            if (age > maxAge) {
                if (sploot.element.parentNode) {
                    sploot.element.parentNode.removeChild(sploot.element);
                }
                return false;
            }
            return true;
        });
        
        this.animationFrame = requestAnimationFrame(() => this.animate());
    }
    
    start() {
        if (this.isRunning) return;
        
        this.isRunning = true;
        
        // Create initial turtles
        for (let i = 0; i < Math.min(this.config.maxTurtles, 3); i++) {
            this.createTurtle();
        }
        
        // Add background click handler
        document.addEventListener('click', (e) => this.handleBackgroundClick(e));
        
        this.animate();
    }
    
    stop() {
        this.isRunning = false;
        if (this.animationFrame) {
            cancelAnimationFrame(this.animationFrame);
        }
        
        // Clean up
        this.turtles.forEach(turtle => {
            if (turtle.element.parentNode) {
                turtle.element.parentNode.removeChild(turtle.element);
            }
        });
        this.turtles = [];
        
        this.sploots.forEach(sploot => {
            if (sploot.element.parentNode) {
                sploot.element.parentNode.removeChild(sploot.element);
            }
        });
        this.sploots = [];
    }
    
    createPieMenu(turtle) {
        // Remove any existing pie menu
        this.removePieMenu();
        
        const pieMenu = document.createElement('div');
        pieMenu.className = 'turtle-pie-menu';
        pieMenu.style.position = 'fixed';
        pieMenu.style.left = (turtle.x + 40) + 'px';
        pieMenu.style.top = (turtle.y - 20) + 'px';
        pieMenu.style.zIndex = '1004';
        
        const menuItems = [
            { text: '✨ SPLOOT', action: () => this.createSploot(turtle.x, turtle.y, 'concept') },
            { text: '🎨 EMOJI', action: () => this.createSploot(turtle.x, turtle.y, 'emoji') },
            { text: '📖 ABOUT', action: () => window.open('turtle-sploot-guide.html', '_blank') },
            { text: '❌ CLOSE', action: () => this.unpopTurtle(turtle) }
        ];
        
        menuItems.forEach((item, index) => {
            const menuItem = document.createElement('div');
            menuItem.className = 'pie-menu-item';
            menuItem.textContent = item.text;
            menuItem.style.cssText = `
                background: linear-gradient(135deg, rgba(0,0,0,0.9), rgba(30,30,30,0.95));
                color: #FFD700;
                padding: 8px 12px;
                margin: 2px 0;
                border-radius: 15px;
                cursor: pointer;
                font-size: 14px;
                font-weight: bold;
                border: 1px solid rgba(255,215,0,0.3);
                transition: all 0.3s ease;
                backdrop-filter: blur(8px);
                text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
                animation: pieItemSlide 0.3s ease-out ${index * 0.1}s both;
            `;
            
            menuItem.addEventListener('mouseenter', () => {
                menuItem.style.background = 'linear-gradient(135deg, #FF69B4, #FF1493)';
                menuItem.style.transform = 'scale(1.05)';
                menuItem.style.boxShadow = '0 4px 12px rgba(255,105,180,0.4)';
            });
            
            menuItem.addEventListener('mouseleave', () => {
                menuItem.style.background = 'linear-gradient(135deg, rgba(0,0,0,0.9), rgba(30,30,30,0.95))';
                menuItem.style.transform = 'scale(1)';
                menuItem.style.boxShadow = 'none';
            });
            
            menuItem.addEventListener('click', (e) => {
                e.stopPropagation();
                item.action();
                this.removePieMenu();
            });
            
            pieMenu.appendChild(menuItem);
        });
        
        // Add pie menu styles if not already added
        if (!document.querySelector('#pie-menu-styles')) {
            const style = document.createElement('style');
            style.id = 'pie-menu-styles';
            style.textContent = `
                @keyframes pieItemSlide {
                    0% {
                        transform: translateX(-20px);
                        opacity: 0;
                    }
                    100% {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
                
                .turtle-pie-menu {
                    pointer-events: auto;
                }
            `;
            document.head.appendChild(style);
        }
        
        document.body.appendChild(pieMenu);
        this.currentPieMenu = pieMenu;
        
        // Close pie menu when clicking elsewhere
        setTimeout(() => {
            document.addEventListener('click', this.handlePieMenuClose.bind(this), { once: true });
        }, 100);
    }
    
    removePieMenu() {
        if (this.currentPieMenu) {
            this.currentPieMenu.remove();
            this.currentPieMenu = null;
        }
    }
    
    handlePieMenuClose(e) {
        if (this.currentPieMenu && !this.currentPieMenu.contains(e.target)) {
            this.removePieMenu();
            // Unpop all turtles
            this.turtles.forEach(turtle => this.unpopTurtle(turtle));
        }
    }
}

// Global instance
window.TurtleSplootEngine = TurtleSplootEngine;

// Auto-start when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    if (!window.opener && !document.querySelector('.demo-popup')) {
        window.turtleEngine = new TurtleSplootEngine();
        
        setTimeout(() => {
            window.turtleEngine.start();
        }, 1000);
        
        // Debug controls (hidden by default)
        const controls = document.createElement('div');
        controls.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 10000;
            display: none;
            background: rgba(0,0,0,0.8);
            padding: 10px;
            border-radius: 8px;
        `;
        controls.innerHTML = `
            <button onclick="window.turtleEngine.stop()" style="margin: 5px; padding: 8px; background: #FF4444; color: white; border: none; border-radius: 4px;">Stop</button>
            <button onclick="window.turtleEngine.start()" style="margin: 5px; padding: 8px; background: #44FF44; color: white; border: none; border-radius: 4px;">Start</button>
        `;
        document.body.appendChild(controls);
        
        // Show controls with SPLOOT sequence
        let keySequence = [];
        document.addEventListener('keydown', (e) => {
            keySequence.push(e.key.toLowerCase());
            if (keySequence.length > 6) keySequence.shift();
            
            if (keySequence.join('') === 'sploot') {
                controls.style.display = controls.style.display === 'none' ? 'block' : 'none';
                keySequence = [];
            }
        });
    }
}); 