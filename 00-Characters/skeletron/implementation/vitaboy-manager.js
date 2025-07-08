/**
 * VitaBoy Animation Manager
 * Higher-level animation coordination and timeline tools
 * By Skeletron - The Animation Conductor
 */

import {
  Skeleton,
  Skill,
  Suit,
  Bone,
  Motion,
  Skin,
  Transform,
  Quaternion
} from './vitaboy-core.js';

// Animation Timeline - coordinates multiple animations
class AnimationTimeline {
  constructor(name) {
    this.name = name;
    this.tracks = new Map(); // skeleton -> Track[]
    this.duration = 0;
    this.currentTime = 0;
    this.playing = false;
    this.loop = false;
    this.speed = 1.0;
    
    this.events = []; // { time, callback }
  }

  addTrack(skeleton, skill, startTime = 0, options = {}) {
    if (!this.tracks.has(skeleton)) {
      this.tracks.set(skeleton, []);
    }
    
    const track = {
      skill,
      startTime,
      endTime: startTime + skill.duration,
      fadeIn: options.fadeIn || 0,
      fadeOut: options.fadeOut || 0,
      priority: options.priority || 1,
      scale: options.scale || 1.0,
      weight: options.weight || 1.0,
      practice: null
    };
    
    this.tracks.get(skeleton).push(track);
    this.duration = Math.max(this.duration, track.endTime);
    
    return track;
  }

  addEvent(time, callback) {
    this.events.push({ time, callback, triggered: false });
    this.events.sort((a, b) => a.time - b.time);
  }

  play() {
    this.playing = true;
    this.lastUpdateTime = performance.now();
    
    // Start initial practices
    this.updatePractices();
  }

  pause() {
    this.playing = false;
  }

  stop() {
    this.playing = false;
    this.currentTime = 0;
    
    // Stop all practices
    for (const [skeleton, tracks] of this.tracks) {
      for (const track of tracks) {
        if (track.practice) {
          skeleton.stopPractice(track.practice);
          track.practice = null;
        }
      }
    }
    
    // Reset events
    for (const event of this.events) {
      event.triggered = false;
    }
  }

  seek(time) {
    this.currentTime = Math.max(0, Math.min(time, this.duration));
    this.updatePractices();
    this.checkEvents();
  }

  update() {
    if (!this.playing) return;
    
    const now = performance.now();
    const deltaTime = (now - this.lastUpdateTime) * 0.001 * this.speed;
    this.lastUpdateTime = now;
    
    this.currentTime += deltaTime;
    
    if (this.currentTime >= this.duration) {
      if (this.loop) {
        this.currentTime = this.currentTime % this.duration;
        // Reset events
        for (const event of this.events) {
          event.triggered = false;
        }
      } else {
        this.currentTime = this.duration;
        this.playing = false;
      }
    }
    
    this.updatePractices();
    this.checkEvents();
  }

  updatePractices() {
    for (const [skeleton, tracks] of this.tracks) {
      for (const track of tracks) {
        const active = this.currentTime >= track.startTime && 
                      this.currentTime <= track.endTime;
        
        if (active && !track.practice) {
          // Start practice
          track.practice = skeleton.startPractice(
            track.skill,
            track.priority,
            track.scale,
            track.weight
          );
          
          // Set elapsed time
          track.practice.elapsed = (this.currentTime - track.startTime) * track.scale;
          
          // Handle fade in
          if (track.fadeIn > 0) {
            track.practice.fadeIn(performance.now(), track.fadeIn);
          }
        } else if (!active && track.practice) {
          // Stop practice
          skeleton.stopPractice(track.practice);
          track.practice = null;
        } else if (track.practice) {
          // Update elapsed time
          track.practice.elapsed = (this.currentTime - track.startTime) * track.scale;
          
          // Handle fade out
          if (track.fadeOut > 0 && 
              this.currentTime >= track.endTime - track.fadeOut) {
            if (track.practice.fading === 0) {
              track.practice.fadeOut(performance.now(), track.fadeOut);
            }
          }
        }
      }
    }
  }

  checkEvents() {
    for (const event of this.events) {
      if (!event.triggered && this.currentTime >= event.time) {
        event.triggered = true;
        event.callback(this.currentTime);
      }
    }
  }
}

// Animation Blender - smooth transitions between animations
class AnimationBlender {
  constructor(skeleton) {
    this.skeleton = skeleton;
    this.layers = [];
  }

  addLayer(skill, options = {}) {
    const layer = {
      skill,
      weight: options.weight || 1.0,
      blendMode: options.blendMode || 'normal', // normal, additive, override
      mask: options.mask || null, // bone name array
      practice: this.skeleton.startPractice(skill)
    };
    
    this.layers.push(layer);
    return layer;
  }

  removeLayer(layer) {
    const index = this.layers.indexOf(layer);
    if (index >= 0) {
      this.skeleton.stopPractice(layer.practice);
      this.layers.splice(index, 1);
    }
  }

  crossfade(fromSkill, toSkill, duration = 1.0) {
    // Find from layer
    const fromLayer = this.layers.find(l => l.skill === fromSkill);
    if (!fromLayer) return;
    
    // Add to layer
    const toLayer = this.addLayer(toSkill, { weight: 0 });
    
    // Animate weights
    const startTime = performance.now();
    const animate = () => {
      const elapsed = (performance.now() - startTime) * 0.001;
      const t = Math.min(elapsed / duration, 1.0);
      
      fromLayer.weight = 1.0 - t;
      toLayer.weight = t;
      
      if (t < 1.0) {
        requestAnimationFrame(animate);
      } else {
        this.removeLayer(fromLayer);
      }
    };
    
    requestAnimationFrame(animate);
  }
}

// VBAnimMgr - manages all animation resources
class VBAnimMgr {
  constructor() {
    this.skeletons = new Map();
    this.skills = new Map();
    this.suits = new Map();
    
    this.meshCache = new Map();
    this.textureCache = new Map();
  }

  // Resource loading
  async loadSkeleton(name, data) {
    const skeleton = new Skeleton(name);
    
    // Parse bone hierarchy
    for (const boneData of data.bones) {
      const bone = new Bone(boneData.name);
      bone.translation = vec3.fromValues(
        boneData.translation[0],
        boneData.translation[1],
        boneData.translation[2]
      );
      bone.rotation = new Quaternion(
        boneData.rotation[0],
        boneData.rotation[1],
        boneData.rotation[2],
        boneData.rotation[3]
      );
      
      // Set properties
      bone.canTranslate = boneData.canTranslate !== false;
      bone.canRotate = boneData.canRotate !== false;
      bone.canBlend = boneData.canBlend !== false;
      bone.canWiggle = boneData.canWiggle || false;
      bone.wigglePower = boneData.wigglePower || 0;
      
      skeleton.addBone(bone);
    }
    
    // Build hierarchy
    for (let i = 0; i < data.bones.length; i++) {
      const boneData = data.bones[i];
      const bone = skeleton.bones[i];
      
      if (boneData.parent) {
        const parent = skeleton.findBone(boneData.parent);
        if (parent) {
          parent.addChild(bone);
        }
      } else {
        skeleton.root = bone;
      }
    }
    
    this.skeletons.set(name, skeleton);
    return skeleton;
  }

  async loadSkill(name, data) {
    const skill = new Skill(name);
    
    skill.duration = data.duration;
    skill.distance = data.distance || 0;
    skill.isMoving = data.isMoving || false;
    skill.isTurning = data.isTurning || false;
    
    // Load motions
    for (const motionData of data.motions) {
      const motion = new Motion(motionData.boneName);
      motion.frames = motionData.frames;
      motion.duration = motionData.duration;
      
      // Load keyframes
      if (motionData.translations) {
        motion.hasTranslation = true;
        for (let i = 0; i < motionData.translations.length; i++) {
          const t = motionData.translations[i];
          motion.setTranslation(i, vec3.fromValues(t[0], t[1], t[2]));
        }
      }
      
      if (motionData.rotations) {
        motion.hasRotation = true;
        for (let i = 0; i < motionData.rotations.length; i++) {
          const r = motionData.rotations[i];
          motion.setRotation(i, new Quaternion(r[0], r[1], r[2], r[3]));
        }
      }
      
      skill.addMotion(motion);
    }
    
    this.skills.set(name, skill);
    return skill;
  }

  async loadSuit(name, data) {
    const suit = new Suit(name);
    
    suit.type = data.type || 0;
    
    // Load skins
    for (const skinData of data.skins) {
      const skin = new Skin(skinData.name, skinData.boneName);
      skin.flags = skinData.flags || 0;
      
      // Load mesh if specified
      if (skinData.meshUrl) {
        skin.data = await this.loadMesh(skinData.meshUrl);
      }
      
      suit.addSkin(skin);
    }
    
    this.suits.set(name, suit);
    return suit;
  }

  async loadMesh(url) {
    if (this.meshCache.has(url)) {
      return this.meshCache.get(url);
    }
    
    // TODO: Implement actual mesh loading
    const mesh = { url, vertices: [], faces: [] };
    this.meshCache.set(url, mesh);
    return mesh;
  }

  // Resource access
  findSkeleton(name) {
    return this.skeletons.get(name);
  }

  findSkill(name) {
    return this.skills.get(name);
  }

  findSuit(name) {
    return this.suits.get(name);
  }

  // Utility methods
  cloneSkeleton(name) {
    const original = this.findSkeleton(name);
    return original ? original.clone() : null;
  }

  countSkeletons() {
    return this.skeletons.size;
  }

  countSkills() {
    return this.skills.size;
  }

  countSuits() {
    return this.suits.size;
  }
}

// VitaBoy - main character controller
class VitaBoy {
  constructor(animMgr, skeletonName) {
    this.animMgr = animMgr;
    this.skeleton = animMgr.cloneSkeleton(skeletonName);
    
    if (!this.skeleton) {
      throw new Error(`Skeleton '${skeletonName}' not found`);
    }
    
    this.scale = vec3.fromValues(1, 1, 1);
    this.ghost = false;
    this.realTime = true;
    
    // Rendering
    this.renderGroup = [];
  }

  setScale(x, y, z) {
    this.scale = vec3.fromValues(x, y, z);
  }

  startPractice(skillName, priority = 1, scale = 1.0, weight = 1.0) {
    const skill = this.animMgr.findSkill(skillName);
    if (!skill) {
      console.warn(`Skill '${skillName}' not found`);
      return null;
    }
    
    return this.skeleton.startPractice(skill, priority, scale, weight);
  }

  stopPractice(practice) {
    this.skeleton.stopPractice(practice);
  }

  dress(suitName, textureName = null) {
    const suit = this.animMgr.findSuit(suitName);
    if (!suit) {
      console.warn(`Suit '${suitName}' not found`);
      return null;
    }
    
    return this.skeleton.dress(suit, textureName);
  }

  undress(dressing) {
    this.skeleton.undress(dressing);
  }

  update(deltaTime) {
    const now = performance.now();
    this.skeleton.update(deltaTime, now);
  }

  render(renderer) {
    // TODO: Implement rendering
    // This would integrate with Three.js or other WebGL renderer
  }
}

// Animation State Machine
class AnimationStateMachine {
  constructor(vitaBoy) {
    this.vitaBoy = vitaBoy;
    this.states = new Map();
    this.transitions = new Map();
    this.currentState = null;
    this.parameters = new Map();
  }

  addState(name, skill, options = {}) {
    this.states.set(name, {
      name,
      skill,
      loop: options.loop !== false,
      speed: options.speed || 1.0,
      events: options.events || []
    });
  }

  addTransition(from, to, condition) {
    const key = `${from}->${to}`;
    this.transitions.set(key, {
      from,
      to,
      condition,
      duration: 0.3
    });
  }

  setParameter(name, value) {
    this.parameters.set(name, value);
    this.checkTransitions();
  }

  setState(stateName) {
    const state = this.states.get(stateName);
    if (!state) return;
    
    // Stop current
    if (this.currentState && this.currentPractice) {
      this.vitaBoy.stopPractice(this.currentPractice);
    }
    
    // Start new
    this.currentState = state;
    this.currentPractice = this.vitaBoy.startPractice(
      state.skill.name,
      1,
      state.speed
    );
    
    if (state.loop) {
      this.currentPractice.repeatMode = 1;
    }
  }

  checkTransitions() {
    if (!this.currentState) return;
    
    for (const [key, transition] of this.transitions) {
      if (transition.from === this.currentState.name) {
        if (transition.condition(this.parameters)) {
          this.setState(transition.to);
          break;
        }
      }
    }
  }

  update(deltaTime) {
    if (this.currentPractice && this.currentPractice.isOver) {
      // Check for state events
      if (this.currentState.events.onEnd) {
        this.currentState.events.onEnd();
      }
    }
    
    this.checkTransitions();
  }
}

// Export everything
export {
  AnimationTimeline,
  AnimationBlender,
  VBAnimMgr,
  VitaBoy,
  AnimationStateMachine
}; 