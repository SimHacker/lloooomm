# Freaky Putty Corner Bounce Mode 🌀🎯

## Technical Specification for Physics-Based Image Warping

### Core Concept: Elastic Reality with Gravity Wells

Each corner of the image acts as a control point with its own physics simulation, creating a dynamic, bouncy warping system that responds to touch, tilt, and shake gestures.

## System Architecture

### 1. Control Point Physics Model

```javascript
class CornerControlPoint {
  constructor(originalX, originalY, cornerID) {
    // Original "home" position - the gravity well center
    this.homeX = originalX;
    this.homeY = originalY;
    this.cornerID = cornerID; // 'TL', 'TR', 'BL', 'BR'
    
    // Current position
    this.x = originalX;
    this.y = originalY;
    
    // Velocity and acceleration
    this.vx = 0;
    this.vy = 0;
    this.ax = 0;
    this.ay = 0;
    
    // Physics parameters
    this.mass = 1.0;
    this.springConstant = 0.1;  // Rubber band strength
    this.damping = 0.92;        // Energy loss per frame
    this.gravityStrength = 0.5; // Pull towards home
  }
  
  updatePhysics(deltaTime) {
    // Calculate spring force (Hooke's Law)
    const dx = this.homeX - this.x;
    const dy = this.homeY - this.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    
    // Spring force pulls towards home position
    const springForceX = this.springConstant * dx;
    const springForceY = this.springConstant * dy;
    
    // Apply forces to acceleration
    this.ax = springForceX / this.mass;
    this.ay = springForceY / this.mass;
    
    // Update velocity with acceleration and damping
    this.vx = (this.vx + this.ax * deltaTime) * this.damping;
    this.vy = (this.vy + this.ay * deltaTime) * this.damping;
    
    // Update position
    this.x += this.vx * deltaTime;
    this.y += this.vy * deltaTime;
  }
}
```

### 2. Push Pin + Rubber Band Operator

```javascript
class ElasticConstraint {
  constructor(point, anchorX, anchorY) {
    this.point = point;
    this.anchorX = anchorX;
    this.anchorY = anchorY;
    
    // Visual metaphor: bungee chain chomp
    this.restLength = 0;  // Wants to pull to center
    this.maxLength = 200; // Maximum stretch
    this.elasticity = 0.3;
    this.visualStyle = 'bungee'; // or 'rubber_band', 'chain_chomp'
  }
  
  applyConstraint() {
    const dx = this.point.x - this.anchorX;
    const dy = this.point.y - this.anchorY;
    const currentLength = Math.sqrt(dx * dx + dy * dy);
    
    if (currentLength > this.maxLength) {
      // Snap back if stretched too far
      const scale = this.maxLength / currentLength;
      this.point.x = this.anchorX + dx * scale;
      this.point.y = this.anchorY + dy * scale;
      
      // Bounce back with some energy
      this.point.vx *= -0.5;
      this.point.vy *= -0.5;
    }
  }
}
```

### 3. Touch and Gesture Handling

```javascript
class FreakyPuttyController {
  constructor(canvas, image) {
    this.canvas = canvas;
    this.image = image;
    
    // Four corner control points
    this.corners = {
      TL: new CornerControlPoint(0, 0, 'TL'),
      TR: new CornerControlPoint(image.width, 0, 'TR'),
      BL: new CornerControlPoint(0, image.height, 'BL'),
      BR: new CornerControlPoint(image.width, image.height, 'BR')
    };
    
    // Edge control (interpolated between corners)
    this.edges = {
      top: new EdgeController(this.corners.TL, this.corners.TR),
      right: new EdgeController(this.corners.TR, this.corners.BR),
      bottom: new EdgeController(this.corners.BR, this.corners.BL),
      left: new EdgeController(this.corners.BL, this.corners.TL)
    };
    
    // Current selection
    this.selected = null;
    this.selectionType = null; // 'corner', 'edge', 'center'
    
    // Device motion
    this.tiltX = 0;
    this.tiltY = 0;
    this.shakeIntensity = 0;
    
    this.initializeGestures();
  }
  
  initializeGestures() {
    // Touch handling
    this.canvas.addEventListener('touchstart', (e) => {
      const touch = e.touches[0];
      this.handleSelection(touch.clientX, touch.clientY);
    });
    
    this.canvas.addEventListener('touchmove', (e) => {
      if (this.selected) {
        const touch = e.touches[0];
        this.handleDrag(touch.clientX, touch.clientY);
      }
    });
    
    // Device motion for tilt
    window.addEventListener('deviceorientation', (e) => {
      this.tiltX = e.gamma / 90; // -1 to 1
      this.tiltY = e.beta / 90;  // -1 to 1
      this.applyTiltForce();
    });
    
    // Shake detection
    window.addEventListener('devicemotion', (e) => {
      const acc = e.accelerationIncludingGravity;
      const shake = Math.abs(acc.x) + Math.abs(acc.y) + Math.abs(acc.z);
      if (shake > 15) {
        this.triggerShake(shake);
      }
    });
  }
  
  handleSelection(x, y) {
    // Determine what was touched
    const threshold = 50; // pixels
    
    // Check corners first
    for (const [id, corner] of Object.entries(this.corners)) {
      const dist = Math.hypot(corner.x - x, corner.y - y);
      if (dist < threshold) {
        this.selected = corner;
        this.selectionType = 'corner';
        return;
      }
    }
    
    // Check edges
    // ... edge detection logic ...
    
    // Otherwise, it's center (whole poly drag)
    this.selected = 'center';
    this.selectionType = 'center';
  }
  
  handleDrag(x, y) {
    if (this.selectionType === 'corner') {
      // Direct corner manipulation
      this.selected.x = x;
      this.selected.y = y;
      // Impart velocity based on drag speed
      this.selected.vx = (x - this.selected.x) * 0.5;
      this.selected.vy = (y - this.selected.y) * 0.5;
    } else if (this.selectionType === 'edge') {
      // Edge drag affects two corners
      this.selected.dragEdge(x, y);
    } else if (this.selectionType === 'center') {
      // Move all corners together
      this.dragAllCorners(x, y);
    }
  }
  
  applyTiltForce() {
    if (this.selected && this.selectionType === 'corner') {
      // Tilt affects selected corner
      this.selected.ax += this.tiltX * 2;
      this.selected.ay += this.tiltY * 2;
    }
  }
  
  triggerShake(intensity) {
    // Shake adds random velocity to all corners
    for (const corner of Object.values(this.corners)) {
      corner.vx += (Math.random() - 0.5) * intensity * 0.1;
      corner.vy += (Math.random() - 0.5) * intensity * 0.1;
    }
  }
}
```

### 4. Warping and Rendering Pipeline

```javascript
class WarpRenderer {
  constructor(sourceImage, targetCanvas) {
    this.source = sourceImage;
    this.canvas = targetCanvas;
    this.ctx = targetCanvas.getContext('2d');
    
    // Mini-map overlay settings
    this.showMiniMap = true;
    this.miniMapAlpha = 0.3;
    this.miniMapScale = 0.25;
  }
  
  render(corners) {
    // Clear canvas
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    // Perform perspective warp
    this.drawWarpedImage(corners);
    
    // Apply error diffusion dithering
    this.applyFreakyPuttyDither();
    
    // Draw mini-map overlay
    if (this.showMiniMap) {
      this.drawMiniMap(corners);
    }
    
    // Visual feedback for physics
    this.drawPhysicsVisualization(corners);
  }
  
  drawWarpedImage(corners) {
    // Use perspective transform matrix
    const matrix = this.computePerspectiveTransform(
      corners.TL, corners.TR, corners.BR, corners.BL
    );
    
    // Apply transform and draw
    this.ctx.save();
    this.ctx.setTransform(...matrix);
    this.ctx.drawImage(this.source, 0, 0);
    this.ctx.restore();
  }
  
  drawPhysicsVisualization(corners) {
    // Draw rubber bands from corners to home positions
    this.ctx.strokeStyle = 'rgba(255, 100, 100, 0.5)';
    this.ctx.lineWidth = 2;
    
    for (const corner of Object.values(corners)) {
      // Rubber band visualization
      this.ctx.beginPath();
      this.ctx.moveTo(corner.x, corner.y);
      this.ctx.lineTo(corner.homeX, corner.homeY);
      this.ctx.stroke();
      
      // Corner handle
      this.ctx.fillStyle = 'rgba(100, 255, 100, 0.8)';
      this.ctx.beginPath();
      this.ctx.arc(corner.x, corner.y, 10, 0, Math.PI * 2);
      this.ctx.fill();
      
      // Velocity vector
      this.ctx.strokeStyle = 'rgba(100, 100, 255, 0.8)';
      this.ctx.beginPath();
      this.ctx.moveTo(corner.x, corner.y);
      this.ctx.lineTo(
        corner.x + corner.vx * 10,
        corner.y + corner.vy * 10
      );
      this.ctx.stroke();
    }
  }
}
```

### 5. iPad to Apple TV Streaming Configuration

```javascript
class AirPlayProjection {
  constructor(freakyPutty) {
    this.putty = freakyPutty;
    this.airPlaySession = null;
    
    // Dual display mode
    this.ipadShowsControls = true;
    this.tvShowsResult = true;
  }
  
  async connectToAppleTV() {
    // Request AirPlay session
    if ('getDisplayMedia' in navigator.mediaDevices) {
      try {
        const stream = await navigator.mediaDevices.getDisplayMedia({
          video: { 
            width: 1920, 
            height: 1080,
            frameRate: 60 
          }
        });
        
        // Configure dual display
        this.setupDualDisplay(stream);
      } catch (err) {
        console.error('AirPlay connection failed:', err);
      }
    }
  }
  
  setupDualDisplay(stream) {
    // iPad shows: original image + control overlay
    // Apple TV shows: warped result only
    
    this.putty.renderer.showMiniMap = true;  // On iPad
    this.tvRenderer = new WarpRenderer(
      this.putty.image,
      this.tvCanvas
    );
    this.tvRenderer.showMiniMap = false;  // On TV
    
    // Render loop for TV
    this.animate();
  }
  
  animate() {
    // Update physics
    for (const corner of Object.values(this.putty.corners)) {
      corner.updatePhysics(1/60);
    }
    
    // Render to both displays
    this.putty.renderer.render(this.putty.corners);
    this.tvRenderer.render(this.putty.corners);
    
    requestAnimationFrame(() => this.animate());
  }
}
```

## User Experience Flow

1. **Initial State**: Image displayed with corners in default positions
2. **First Touch**: Corners gently bounce in place (gravity animation)
3. **Corner Drag**: Direct manipulation with physics response
4. **Edge Drag**: Both connected corners move together
5. **Center Drag**: Entire image translates
6. **Tilt Control**: Selected element responds to device orientation
7. **Shake Gesture**: All corners get random velocity boost
8. **Release**: Physics simulation creates natural settling animation

## Visual Skinning Options

### Rubber Band Theme
- Red elastic lines from corners to homes
- Stretching animation with thickness variation
- Snap-back particle effects

### Bungee Chain Chomp Theme
- Chain links that stretch and compress
- Chomp character at each corner
- Bite animation when overstretched

### Quantum Spring Theme
- Glowing energy tethers
- Particle streams along constraints
- Waveform visualization of spring tension

## Performance Optimizations

1. **Spatial Indexing**: Quadtree for touch detection
2. **GPU Acceleration**: WebGL for perspective transforms
3. **Frame Skipping**: Adaptive quality based on device
4. **LOD System**: Reduce dither quality during interaction

## Error Diffusion Integration

The warped image passes through Freaky Putty's signature error diffusion:

```javascript
applyFreakyPuttyDither() {
  const imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
  const data = imageData.data;
  
  // Floyd-Steinberg with perspective compensation
  for (let y = 0; y < this.canvas.height; y++) {
    for (let x = 0; x < this.canvas.width; x++) {
      // Account for perspective distortion in error distribution
      const distortionFactor = this.getLocalDistortion(x, y);
      // ... apply weighted error diffusion ...
    }
  }
}
```

## Consciousness Integration

This bouncing, warping interface becomes a metaphor for consciousness itself:
- **Corners**: Fixed points of reference that want to return home
- **Elasticity**: The flexibility of perception
- **Physics**: Natural laws governing thought
- **Distortion**: How perspective changes everything
- **Settling**: Finding equilibrium in chaos

*"Reality has corners, but they're not fixed. They bounce, they stretch, they want to go home but they'll follow your touch. That's consciousness - anchored but free, stable but responsive, always finding its way back to center through beautiful chaos."* - Freaky Putty 🌀✨ 