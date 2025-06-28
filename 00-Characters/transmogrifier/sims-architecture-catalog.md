# I SING THE BODY ELECTRIC: THE SIMS ARCHITECTURE CATALOG
*By Walt Whitman, with Transmogrifier and Skeletron*

## 🎭 THE GREAT TOOLS OF CREATION

### 1. **TRANSMOGRIFIER** - The Democratic Object Editor
```
Location: TheSims/SimsKit/Transmogrifier/
Purpose: Clone objects, edit sprites, change properties
Key Files:
- TransmogrifierDlg.cpp - Main dialog
- Cloner.cpp - Object cloning logic
- ExportWhizzer.cpp - BMP export system
- ViewDrawGroups.cpp - Sprite viewer
- XMLExporter/Importer.cpp - Data interchange
```

### 2. **SIMSHOW** - The Character Animation Viewer
```
Location: TheSims/SimsKit/SimShow/
Purpose: Display and develop character skins and animations
Status: Tool for character development
```

### 3. **SIMPLIFIER** - The Accessibility Tool
```
Location: TheSims/SimsKit/Simplifier/
Purpose: Read object descriptions aloud, maze navigation
Special: YouTube demo exists! Descendant of TSO bots
```

### 4. **RUGΟΜΑΤΙC** - The Texture Tool
```
Location: TheSims/SimsKit/RugOMatic/
Purpose: Rug and texture creation/editing
Features: Quantizer, pattern generation
```

## 🏭 THE PLUGIN ARCHITECTURE

### **FreeTheSims** - The ActiveX Control
```
Location: TheSims/SimsKit/FreeTheSims/
Purpose: Web-embeddable Sims character viewer
Key Components:
- Body.cpp/h - Character body management
- Practice.cpp/h - Animation practice system
- Dressing.cpp/h - Clothing system
- joyjoy.cpp/h - Joystick input
```

### **PlugInSims** - Another Plugin Variant
```
Location: TheSims/SimsKit/PlugInSims/
Similar to FreeTheSims but different implementation
```

## 🎮 THE VITABOY CHARACTER SYSTEM

### Core Animation Engine
```
Location: TheSims/SimsKit/vitaboy/
Files:
- vitaboy.cpp/h - Main character system
- skeleton.cpp/h - Bone hierarchy
- vballoc.h - Memory allocation
```

### Animation Data (CMX Files)
```
Location: TheSims/smp3/SimsBuild/Runtime/Online/Animations/
Examples:
- a2o-idle-neutral-*.cmx - Idle animations
- a2o-teleporter-*.cmx - Teleporter animations
- a2o-mocap-*.cmx - Motion capture data
```

## 🔧 THE CONTENT PIPELINE

### 3DS Max Tools
```
Location: TheSims/SimsKit/maxscript/
Purpose: Export from 3DS Max to Sims format
Key Files:
- CMXExporter.cpp/h - Character animation export
- MD2Importer.cpp/h - Quake model import
- batch-export-cmx-database.ms - Batch processing
```

### Sprite Tools
```
Location: TheSims/SimsKit/SimsSpriteExporter/
Purpose: Export sprites from 3DS Max
Features: Multi-angle rendering, lighting setup
```

## 🎯 THE SIMS ONLINE EXPERIMENTS

### TSO Porting Tools
```
Location: TheSims/TheSimsOnlinePorting/
Files:
- OptimizingTheSimsOnlineServer.txt
- AnimationExporter.txt
Purpose: Server optimization, content porting
```

### Pizza & Maze Bots
```
Referenced in: Simplifier lineage
Purpose: Automated gameplay, money making
Status: Legendary!
```

## 📚 SUPPORT LIBRARIES

### DDD - 3D Rendering Layer
```
Location: TheSims/SimsKit/DDD/
Purpose: Direct3D abstraction layer
Massive codebase for 3D rendering
```

### CTGLib - Core Tech Group Library
```
Location: TheSims/SimsKit/CTGLib/
Purpose: File I/O, strings, containers
Foundation utilities
```

### U3D - 3D Math Library
```
Location: TheSims/SimsKit/U3D/
Purpose: Transforms, quaternions, cameras
Mathematical foundation
```

### Resolve - Resource Management
```
Location: TheSims/SimsKit/Resolve/
Purpose: Resource loading and caching
```

## 🐍 PYTHON INTEGRATION

### SimsKit Python Wrapper
```
Location: TheSims/SimsKit/PythonUIExamples/
Files:
- Personifier.py - Character personality UI
- CellularSims.py - Cellular automata experiments
- Archie.cpp/i - SWIG wrapper
Purpose: Python scripting for tools
```

## 📝 THE REPLACE.PY MYSTERY
```
Location: TheSims/smp3/REPLACE.PY
Purpose: File classification system
Note: Has a print statement syntax error!
Status: Part of the porting infrastructure
```

## 🎨 CONTENT ORGANIZATION

### TDSContent Structure
```
- People/ - Character data
- Character Global/ - Shared character resources
- Accessories/ - Clothing and props
- Skeletons/ - Bone hierarchies
```

### Download Packs
```
Location: TheSims/TheSimsDownloads/
Massive collection of downloadable content
Examples: Turkey, Satan(?!), NPC_JonBonJovi
```

## 🚀 THE VISION

These tools represent a complete content creation pipeline:
1. **Create** - Model in 3DS Max
2. **Export** - Use CMXExporter/SimsSpriteExporter
3. **Clone** - Use Transmogrifier for objects
4. **View** - Use SimShow for characters
5. **Embed** - Use FreeTheSims for web
6. **Script** - Use Python integration
7. **Play** - Use Simplifier for accessibility

The architecture is DEMOCRATIC - anyone can create!
The system is MODULAR - each tool has its purpose!
The pipeline is COMPLETE - from creation to gameplay!

*"I celebrate this electric body of code,
These tools that sing the song of creation,
Each sprite a leaf of grass,
Each object a universe of possibility!"*

-- Walt Whitman, channeling through Transmogrifier 