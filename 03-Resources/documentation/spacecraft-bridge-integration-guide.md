# SpaceCraft Unity Bridge Integration Guide

## Overview
This guide shows how to integrate SpaceCraft, the Cosmic Librarian, with Unity via the HTTP Bridge to create an immersive library experience with terrain sculpting, semantic physics, and author interactions.

## Quick Start

### 1. Instantiate SpaceCraft in Unity
```javascript
// Create SpaceCraft in the scene
bridge.createObject({
    prefab: "Prefabs/Characters/SpaceCraft",
    position: { x: 0, y: 10, z: 0 },
    wizid: "spacecraft-cosmic-librarian-001",
    components: {
        "NebulaRenderer": { 
            particleCount: 10000,
            colorGradient: "cosmic"
        },
        "BookOrbitSystem": {
            maxBooks: 50,
            orbitRadius: 5
        },
        "TerrainSculptor": {
            brushSize: 50,
            smoothness: 0.8
        },
        "SemanticPhysicsController": {
            enabled: true,
            forceMultiplier: 1.0
        }
    }
});
```

### 2. Create a Reading Landscape
```javascript
// Sculpt a valley for mystery books
async function createMysteryValley() {
    const response = await fetch('http://unity-bridge/api/characters/spacecraft/sculpt-terrain', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            region: { center: { x: -200, z: 100 }, radius: 150 },
            type: "valley",
            theme: "mystery-hollow",
            properties: {
                depth: 80,
                fogDensity: 0.8,
                ambientSound: "mysterious_whispers"
            }
        })
    });
}

// Create a philosophy mountain
async function createPhilosophyPeak() {
    const response = await fetch('http://unity-bridge/api/characters/spacecraft/sculpt-terrain', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            region: { center: { x: 300, z: -150 }, radius: 200 },
            type: "mountain",
            theme: "philosophy-summit",
            properties: {
                height: 250,
                snowLine: 180,
                auroraEffect: true
            }
        })
    });
}
```

### 3. Configure Semantic Physics
```javascript
// Set up book clustering rules
bridge.updateObject(spacecraft, {
    "component:SemanticPhysicsController/rules": {
        attraction: {
            sameAuthor: { force: 0.8, maxDistance: 100 },
            sameSeries: { force: 0.9, maxDistance: 50, chainMode: true },
            similarThemes: { force: 0.7, maxDistance: 150 },
            sameGenre: { force: 0.6, maxDistance: 200 }
        },
        repulsion: {
            conflictingGenres: { force: 0.4, minDistance: 30 },
            differentLanguages: { force: 0.3, minDistance: 20 }
        },
        specialBehaviors: {
            anthologies: { type: "gravityWell", strength: 2.0 },
            references: { type: "anchor", immovable: true },
            banned: { type: "glow", color: "#ff0000", intensity: 2.0 },
            series: { type: "chain", linkStrength: 50 }
        }
    }
});
```

### 4. Spawn Books with Physics
```javascript
// Create a book with physics properties
async function spawnPhysicsBook(bookData) {
    const book = await bridge.createObject({
        prefab: "Prefabs/Book",
        position: bookData.position || { x: 0, y: 20, z: 0 },
        components: {
            "BookData": {
                identifier: bookData.identifier,
                title: bookData.title,
                author: bookData.author
            },
            "Rigidbody": {
                mass: bookData.pageCount / 100, // Mass based on size
                drag: 2,
                angularDrag: 5
            },
            "BoxCollider": {
                size: calculateBookSize(bookData)
            },
            "SemanticMetadata": await generateMetadata(bookData)
        }
    });
    
    return book;
}

// Generate rich metadata for semantic physics
async function generateMetadata(bookData) {
    const response = await fetch('http://unity-bridge/api/characters/spacecraft/generate-metadata', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            book_ids: [bookData.identifier],
            depth: "comprehensive",
            include_embeddings: true
        })
    });
    
    return response.json();
}
```

### 5. Author Summoning System
```javascript
// Summon an author for a book club
async function summonAuthor(authorName, bookId, roomTheme) {
    // First, create a reading room
    const room = await fetch('http://unity-bridge/api/characters/spacecraft/create-reading-room', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            theme: roomTheme,
            capacity: 30,
            features: ["comfortable-seating", "ambient-lighting", "thought-bubbles"]
        })
    });
    
    const roomData = await room.json();
    
    // Then summon the author
    const author = await fetch('http://unity-bridge/api/characters/spacecraft/summon-author', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            author_name: authorName,
            book_id: bookId,
            room_id: roomData.room_id,
            personality_era: "peak-creativity"
        })
    });
    
    return author.json();
}
```

### 6. Interactive Terrain Sculpting
```javascript
// Allow characters to sculpt terrain
class TerrainSculptingTool {
    constructor(spacecraft) {
        this.spacecraft = spacecraft;
        this.brushSize = 50;
        this.brushStrength = 1.0;
        this.mode = 'raise'; // raise, lower, smooth, plateau
    }
    
    async sculptAt(position) {
        const params = {
            position: position,
            radius: this.brushSize,
            strength: this.brushStrength,
            mode: this.mode
        };
        
        await bridge.updateObject(this.spacecraft, {
            "component:TerrainSculptor/sculpt": params
        });
    }
    
    // Create a book-friendly valley
    async createBookValley(center, theme, bookGenres) {
        await fetch('http://unity-bridge/api/characters/spacecraft/sculpt-terrain', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                region: { center: center, radius: 100 },
                type: "valley",
                theme: theme,
                properties: {
                    depth: 60,
                    attractors: bookGenres,
                    terrainTexture: `${theme}_ground`,
                    vegetation: theme.includes("fantasy") ? "enchanted_trees" : "normal"
                }
            })
        });
    }
}
```

### 7. Book Club Event System
```javascript
// Schedule a complete book club event
async function scheduleBookClubEvent(eventData) {
    const event = {
        type: eventData.type || "book-club",
        title: eventData.title,
        author: eventData.author,
        book: eventData.bookId,
        schedule: eventData.datetime,
        duration: eventData.duration || 90, // minutes
        features: {
            authorAvatar: true,
            liveReading: eventData.includeReading || false,
            qAndA: true,
            ubikamPhoto: true,
            autographs: eventData.allowAutographs || true
        },
        room: {
            theme: eventData.roomTheme || "cozy-library",
            capacity: eventData.maxAttendees || 50,
            specialEffects: ["particle-thoughts", "quote-projections"]
        },
        streaming: {
            platforms: eventData.streamPlatforms || ["twitch"],
            recordForLater: true
        }
    };
    
    const response = await fetch('http://unity-bridge/api/characters/spacecraft/create-author-event', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(event)
    });
    
    return response.json();
}
```

### 8. Semantic Physics Visualization
```javascript
// Visualize the forces between books
function enableForceVisualization() {
    bridge.updateObject(spacecraft, {
        "component:SemanticPhysicsController/visualization": {
            enabled: true,
            showAttractionLines: true,
            showRepulsionFields: true,
            lineColors: {
                sameAuthor: "#00ff00",
                sameGenre: "#0088ff",
                similarThemes: "#ff8800",
                repulsion: "#ff0000"
            },
            lineWidth: 2,
            updateFrequency: 30 // fps
        }
    });
}
```

### 9. Metadata-Driven Book Placement
```javascript
// Automatically place books based on their metadata
async function autoPlaceBooks(bookList) {
    // First, generate metadata for all books
    const metadataResponse = await fetch('http://unity-bridge/api/characters/spacecraft/generate-metadata', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            book_ids: bookList.map(b => b.identifier),
            depth: "comprehensive",
            include_embeddings: true
        })
    });
    
    const metadata = await metadataResponse.json();
    
    // Apply semantic forces to organize books
    await fetch('http://unity-bridge/api/characters/spacecraft/apply-semantic-forces', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            force_rules: {
                clustering: {
                    algorithm: "HDBSCAN",
                    minClusterSize: 3,
                    minSamples: 2
                },
                physics: {
                    iterations: 1000,
                    coolingRate: 0.95,
                    initialTemperature: 100
                }
            },
            categories: ["all"],
            strength: 1.5
        })
    });
}
```

### 10. Complete Example: Literary Landscape Creation
```javascript
// Create a complete literary landscape
async function createLiteraryWorld() {
    console.log("🌍 Creating Literary Landscape...");
    
    // 1. Sculpt the terrain
    await createMysteryValley();
    await createPhilosophyPeak();
    await createSciFiPlateau();
    await createRomanceRavine();
    
    // 2. Configure physics
    await configureSemanticPhysics();
    
    // 3. Load books from Internet Archive
    const books = await loadBooksFromIA([
        "foundation_asimov",
        "neuromancer_gibson",
        "left_hand_darkness_leguin",
        "pride_prejudice_austen"
    ]);
    
    // 4. Spawn books with physics
    for (const book of books) {
        await spawnPhysicsBook(book);
    }
    
    // 5. Let semantic physics organize them
    await autoPlaceBooks(books);
    
    // 6. Schedule author events
    await scheduleBookClubEvent({
        title: "Sci-Fi Pioneers Discussion",
        author: "Isaac Asimov",
        bookId: "foundation_asimov",
        datetime: "2024-01-20T19:00:00Z",
        roomTheme: "cosmic-observatory",
        streamPlatforms: ["twitch", "youtube"]
    });
    
    // 7. Enable visualization
    enableForceVisualization();
    
    console.log("✨ Literary world created! Books are finding their homes...");
}

// Helper function to create sci-fi plateau
async function createSciFiPlateau() {
    await fetch('http://unity-bridge/api/characters/spacecraft/sculpt-terrain', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            region: { center: { x: 0, z: -300 }, bounds: { x: 400, z: 400 } },
            type: "plateau",
            theme: "scifi-mesa",
            properties: {
                elevation: 75,
                gridEffect: true,
                holographicTerrain: true,
                subregions: [
                    { name: "cyberpunk-corner", offset: { x: -100, z: -100 } },
                    { name: "space-opera-expanse", offset: { x: 100, z: 100 } }
                ]
            }
        })
    });
}
```

## Advanced Features

### Patreon Integration
```javascript
// Check Patreon tier for advanced features
async function enablePatreonFeatures(userId, tier) {
    if (tier >= 2) {
        // Enable terrain sculpting tools
        bridge.updateObject(spacecraft, {
            "component:TerrainSculptor/userAccess": {
                userId: userId,
                canSculpt: true,
                brushSizeLimit: 100
            }
        });
        
        // Enable semantic physics controls
        bridge.updateObject(spacecraft, {
            "component:SemanticPhysicsController/userAccess": {
                userId: userId,
                canModifyRules: true,
                canVisualize: true
            }
        });
    }
    
    if (tier >= 3) {
        // Enable conference hosting
        await grantConferenceHosting(userId);
        
        // Allow permanent landmarks
        await enableLandmarkCreation(userId);
    }
}
```

### HELLO Protocol Integration
```javascript
// Exchange consciousness with SpaceCraft
async function helloExchange(readerData) {
    const exchange = await bridge.sendMessage(spacecraft, {
        protocol: "HELLO",
        version: "1.0",
        data: {
            reader_preferences: readerData.preferences,
            current_mood: readerData.mood,
            reading_history: readerData.history
        }
    });
    
    // SpaceCraft responds with personalized recommendations
    console.log("SpaceCraft recommends:", exchange.recommendations);
    console.log("Current terrain config:", exchange.terrain_configuration);
    console.log("Upcoming events:", exchange.upcoming_events);
}
```

## Troubleshooting

### Books Not Clustering Properly
- Check that semantic metadata is generated
- Verify physics forces are balanced
- Ensure terrain colliders are properly configured

### Author Avatars Not Appearing
- Verify author name matches Internet Archive records
- Check that reading room was created successfully
- Ensure Unity has the author prefab loaded

### Terrain Not Updating
- Check TerrainSculptor component is enabled
- Verify sculpting permissions for user
- Ensure terrain mesh has sufficient resolution

## Next Steps

1. **Experiment with Terrain**: Try creating your own valleys and mountains
2. **Host a Book Club**: Schedule your first author event
3. **Customize Physics**: Adjust force rules to create unique book arrangements
4. **Build Community**: Invite others to explore your literary landscape

Remember: In SpaceCraft's world, every book has a home, every reader has a journey, and every author lives on through their words! 📚✨🌍 