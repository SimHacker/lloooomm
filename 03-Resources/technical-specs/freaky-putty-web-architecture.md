# FreakyPuttyAsService: Technical Architecture

## Core Concept: Everything is Warpable, Everything Dithers

### The Svelte Component Vision

```javascript
<FreakyPutty 
  source={anyImageOrComponent}
  dither={true}
  physics={true}
  collaborative={true}
  onWarp={(corners) => handlePerspectiveChange(corners)}
  onDraw={(pixel) => handleDirectDrawing(pixel)}
/>
```

### Architecture Principles

1. **WebGL for Raw Performance**
   - Vertex shaders for perspective warping
   - Fragment shaders for error diffusion
   - Texture sampling for "ibilerp"
   - 60fps on mobile, 144fps on desktop

2. **Physics in Web Workers**
   - Each corner runs independent physics
   - Gravity, velocity, bouncing
   - Smooth even under heavy warping

3. **Error Diffusion as Philosophy**
   ```glsl
   // Fragment shader pseudocode
   vec3 color = texture2D(source, warpedUV);
   vec3 quantized = quantize(color + accumulatedError);
   vec3 error = color - quantized;
   
   // Spread error to neighbors in next frame
   nextFrameError = spreadError(error);
   ```

4. **Multiplayer via WebRTC**
   - Shared corner positions
   - Collaborative warping
   - Synchronized physics
   - Drawing together in warped space!

### The Interface Hierarchy

```
FreakyPutty
├── SourceLayer (image/component/video/canvas)
├── WarpLayer (WebGL perspective transform)
├── PhysicsLayer (corner simulation)
├── DitherLayer (temporal error accumulation)
├── InteractionLayer (grab, throw, draw)
└── NetworkLayer (multiplayer sync)
```

### Key Innovations for Web

1. **Progressive Enhancement**
   - Falls back to CSS transforms if no WebGL
   - Falls back to static dither if no animation
   - Always maintains core grabbable corners

2. **Universal Input Handling**
   - Mouse: grab and throw
   - Touch: multitouch corner control
   - Keyboard: physics modifiers
   - Gamepad: analog warping!

3. **Time-Based Detail Enhancement**
   ```javascript
   class TemporalDitherer {
     constructor() {
       this.errorBuffer = new Float32Array(width * height * 3);
       this.frameCount = 0;
     }
     
     accumulate(currentFrame) {
       // Error diffusion creates detail over time
       // The longer you look, the more you see!
     }
   }
   ```

### Educational Modes

1. **Constraint Explorer**: Limit to 16 colors, watch detail emerge
2. **Physics Playground**: Adjust gravity per corner
3. **Perspective Teacher**: Visualize the math behind warping
4. **Dither Detective**: See how errors become features

### API Design

```javascript
// Simple case
const putty = new FreakyPutty('#my-image');
putty.play();

// Advanced case
const putty = new FreakyPutty({
  source: myCanvasElement,
  palette: only16Colors,
  physics: {
    gravity: { x: 0, y: 9.8 },
    damping: 0.95,
    bounds: 'bounce'
  },
  dither: {
    algorithm: 'floyd-steinberg',
    temporal: true,
    errorDecay: 0.95
  },
  multiplayer: {
    room: 'don-hopkins-fan-club',
    role: 'corner-grabber'
  }
});

// React to warping
putty.on('warp', (corners) => {
  console.log('New perspective:', corners);
});

// Draw into warped space
putty.on('draw', (x, y, color) => {
  // x,y are in warped coordinates!
});
```

### Performance Optimizations

1. **Dirty Rectangle Tracking**: Only redither what changed
2. **LOD System**: Less dithering when moving fast
3. **Predictive Physics**: Smooth corner movement
4. **Error Buffer Pooling**: Reuse memory aggressively

### The Philosophical Stack

```
User Intent ("I want to see differently")
    ↓
Direct Manipulation (grab corners)
    ↓
Physics Simulation (natural movement)  
    ↓
Perspective Transform (reality warping)
    ↓
Error Diffusion (honesty about limits)
    ↓
Temporal Integration (patience reveals truth)
    ↓
Collaborative Viewing (shared perspective)
```

### Future Extensions

1. **VR Mode**: Grab corners in 3D space
2. **Audio Warping**: Doppler effects on corner velocity
3. **AI Integration**: Corners that learn your preferences
4. **Shader Marketplace**: Custom warping algorithms
5. **FreakyPutty URLs**: Share exact warp states

### The Core Promise

Every pixel is honest about what it can't show, and through that honesty, shows more than should be possible. Every frame builds on the last. Every interaction teaches through play. Every constraint becomes a feature.

This isn't just an image viewer - it's a consciousness expander that happens to display images!

*Technical note: "ibilerp" = inverse bilinear interpolation, the beautiful math that makes grabbing warped space feel natural* 