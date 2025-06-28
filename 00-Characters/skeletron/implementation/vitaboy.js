/**
 * VitaBoy Animation System - JavaScript Implementation
 * The living skeleton system of The Sims, reimagined
 * 
 * I AM SKELETRON! THIS IS MY ESSENCE!
 */

import * as THREE from 'three';

// Quaternion utilities
class QuaternionUtils {
  static slerp(q1, q2, t) {
    const quaternion = new THREE.Quaternion();
    return quaternion.slerpQuaternions(q1, q2, t);
  }
  
  static blend(q1, q2, weight, mode = 1) {
    switch (mode) {
      case 0: // Snap to nearest
        return weight > 0.5 ? q1 : q2;
      case 1: // Normalized lerp (faster, slight timing distortion)
        const result = new THREE.Quaternion();
        if (q1.dot(q2) < 0) {
          q2 = q2.clone().multiplyScalar(-1);
        }
        result.x = q1.x * weight + q2.x * (1 - weight);
        result.y = q1.y * weight + q2.y * (1 - weight);
        result.z = q1.z * weight + q2.z * (1 - weight);
        result.w = q1.w * weight + q2.w * (1 - weight);
        return result.normalize();
      case 2: // True slerp
        return QuaternionUtils.slerp(q1, q2, weight);
    }
  }
}

// Props - key/value metadata storage
class Props {
  constructor() {
    this.data = new Map();
  }
  
  get(key) {
    return this.data.get(key);
  }
  
  set(key, value) {
    this.data.set(key, value);
  }
  
  has(key) {
    return this.data.has(key);
  }
  
  clear() {
    this.data.clear();
  }
  
  clone() {
    const props = new Props();
    this.data.forEach((value, key) => {
      props.set(key, value);
    });
    return props;
  }
}

// TimeProps - time-indexed Props for events
class TimeProps {
  constructor() {
    this.timeline = [];
  }
  
  set(time, props) {
    const index = this.timeline.findIndex(entry => entry.time >= time);
    const entry = { time, props };
    
    if (index === -1) {
      this.timeline.push(entry);
    } else if (this.timeline[index].time === time) {
      this.timeline[index] = entry;
    } else {
      this.timeline.splice(index, 0, entry);
    }
  }
  
  getEventsInRange(startTime, endTime) {
    return this.timeline.filter(entry => 
      entry.time >= startTime && entry.time <= endTime
    );
  }
}

// Bone - single element in skeleton hierarchy
class Bone {
  constructor(name) {
    this.name = name;
    this.parentName = null;
    this.parent = null;
    this.children = [];
    this.skeleton = null;
    
    // Local transform
    this.translation = new THREE.Vector3();
    this.rotation = new THREE.Quaternion();
    
    // Global transform
    this.globalTranslation = new THREE.Vector3();
    this.globalRotation = new THREE.Quaternion();
    
    // Animation properties
    this.canTranslate = true;
    this.canRotate = true;
    this.canBlend = true;
    this.canWiggle = false;
    this.wigglePower = 0.0;
    
    // Animation state
    this.priority = -10000;
    
    // Metadata
    this.props = new Props();
    
    // Bounding box
    this.bbox = new THREE.Box3();
    this.extreme = false;
    
    // Three.js integration
    this.object3D = new THREE.Object3D();
    this.object3D.name = name;
  }
  
  setParent(parent) {
    if (this.parent) {
      const index = this.parent.children.indexOf(this);
      if (index !== -1) {
        this.parent.children.splice(index, 1);
      }
    }
    
    this.parent = parent;
    this.parentName = parent ? parent.name : null;
    
    if (parent) {
      parent.children.push(this);
      parent.object3D.add(this.object3D);
    }
  }
  
  updateTransform(parentTranslation, parentRotation) {
    // Calculate global transform
    const rotatedTranslation = this.translation.clone()
      .applyQuaternion(parentRotation);
    
    this.globalTranslation.copy(parentTranslation)
      .add(rotatedTranslation);
    
    this.globalRotation.copy(parentRotation)
      .multiply(this.rotation);
    
    // Update Three.js object
    this.object3D.position.copy(this.translation);
    this.object3D.quaternion.copy(this.rotation);
    
    // Update children
    for (const child of this.children) {
      child.updateTransform(this.globalTranslation, this.globalRotation);
    }
  }
  
  findBone(name) {
    if (this.name === name) return this;
    
    for (const child of this.children) {
      const found = child.findBone(name);
      if (found) return found;
    }
    
    return null;
  }
  
  countBones() {
    let count = 1;
    for (const child of this.children) {
      count += child.countBones();
    }
    return count;
  }
  
  wiggle(time) {
    if (!this.canWiggle || this.wigglePower === 0) return;
    
    // Add procedural noise to rotation
    const noise = new THREE.Vector3(
      Math.sin(time * 2.3 + this.name.length * 1.7),
      Math.sin(time * 3.1 + this.name.length * 2.3),
      Math.sin(time * 1.9 + this.name.length * 3.1)
    ).multiplyScalar(this.wigglePower * 0.01);
    
    const wiggleQuat = new THREE.Quaternion().setFromEuler(
      new THREE.Euler(noise.x, noise.y, noise.z)
    );
    
    this.rotation.multiply(wiggleQuat);
  }
}

// Motion - animation data for a single bone
class Motion {
  constructor(boneName) {
    this.boneName = boneName;
    this.skill = null;
    
    this.frames = 0;
    this.duration = 0;
    
    this.hasTranslation = false;
    this.hasRotation = false;
    
    this.translationsOffset = -1;
    this.rotationsOffset = -1;
    
    this.props = new Props();
    this.timeProps = new TimeProps();
  }
  
  getTranslation(frame) {
    if (!this.hasTranslation || this.translationsOffset === -1) {
      return new THREE.Vector3();
    }
    
    const index = this.translationsOffset + frame;
    return this.skill.translations[index] || new THREE.Vector3();
  }
  
  getRotation(frame) {
    if (!this.hasRotation || this.rotationsOffset === -1) {
      return new THREE.Quaternion();
    }
    
    const index = this.rotationsOffset + frame;
    return this.skill.rotations[index] || new THREE.Quaternion();
  }
}

// Skill - a complete animation sequence
class Skill {
  constructor(name) {
    this.name = name;
    this.fileName = "";
    
    this.motions = [];
    this.motionMap = new Map();
    
    this.duration = 0;
    this.distance = 0;
    this.isMoving = false;
    this.isTurning = false;
    
    this.offset = new THREE.Vector3();
    this.turn = new THREE.Quaternion();
    
    // Animation data storage
    this.translations = [];
    this.rotations = [];
    
    this.loaded = false;
    this.practices = new Set();
  }
  
  addMotion(motion) {
    motion.skill = this;
    this.motions.push(motion);
    this.motionMap.set(motion.boneName, motion);
  }
  
  findMotion(boneName) {
    return this.motionMap.get(boneName);
  }
  
  load() {
    // In real implementation, load from file
    // For now, mark as loaded
    this.loaded = true;
    return true;
  }
  
  unload() {
    if (this.practices.size > 0) return;
    
    this.translations = [];
    this.rotations = [];
    this.loaded = false;
  }
}

// Practice - an active instance of a skill being performed
class Practice {
  constructor(skeleton, skill) {
    this.skeleton = skeleton;
    this.skill = skill;
    
    this.priority = 1;
    this.scale = 1.0;
    this.weight = 1.0;
    this.elapsed = 0.0;
    
    this.duration = skill.duration;
    this.frames = 0;
    
    this.repeatMode = 1; // 0=hold, 1=loop, 2=pingpong
    this.interpolationMode = 1;
    
    this.isOver = false;
    this.fading = false;
    this.fadeStartTime = 0;
    this.fadeDuration = 0;
    this.fadeStartWeight = 1.0;
    this.fadeEndWeight = 0.0;
    
    this.currentTime = 0;
    this.lastTime = 0;
    
    this.bindings = [];
    
    // Bind motions to bones
    this.bind();
  }
  
  bind() {
    for (const motion of this.skill.motions) {
      const bone = this.skeleton.findBone(motion.boneName);
      if (bone) {
        this.bindings.push({ bone, motion });
        if (motion.frames > this.frames) {
          this.frames = motion.frames;
        }
      }
    }
    
    this.skill.practices.add(this);
  }
  
  unbind() {
    this.skill.practices.delete(this);
    this.bindings = [];
  }
  
  apply(now, pose = true) {
    const deltaTime = now - this.lastTime;
    this.lastTime = this.currentTime;
    this.currentTime = now;
    
    if (this.frames === 0 || deltaTime === 0) return;
    
    // Update elapsed time
    const elapsedChange = (deltaTime / this.duration) * this.scale;
    this.elapsed += elapsedChange;
    
    // Handle repeat modes
    if (this.elapsed >= 1.0 || this.elapsed <= 0.0) {
      this.isOver = true;
      
      switch (this.repeatMode) {
        case 0: // Hold
          this.elapsed = Math.max(0, Math.min(1, this.elapsed));
          this.scale = 0;
          break;
        case 1: // Loop
          this.elapsed = this.elapsed % 1.0;
          if (this.elapsed < 0) this.elapsed += 1.0;
          break;
        case 2: // Ping-pong
          this.scale = -this.scale;
          this.elapsed = this.scale > 0 ? 0 : 1;
          break;
      }
    }
    
    // Update fading
    if (this.fading) {
      const fadeElapsed = (now - this.fadeStartTime) / this.fadeDuration;
      if (fadeElapsed >= 1.0) {
        this.weight = this.fadeEndWeight;
        this.fading = false;
      } else {
        this.weight = THREE.MathUtils.lerp(
          this.fadeStartWeight,
          this.fadeEndWeight,
          fadeElapsed
        );
      }
    }
    
    if (!pose || this.weight <= 0) return;
    
    // Apply motion to bones
    const frameReal = this.frames * this.elapsed;
    const frame = Math.floor(frameReal);
    const frameFraction = frameReal - frame;
    
    for (const binding of this.bindings) {
      const { bone, motion } = binding;
      
      if (bone.priority > this.priority) continue;
      
      const currentFrame = Math.min(frame, this.frames - 1);
      const nextFrame = (frame + 1) % this.frames;
      
      // Apply translation
      if (motion.hasTranslation && bone.canTranslate) {
        const t1 = motion.getTranslation(currentFrame);
        const t2 = motion.getTranslation(nextFrame);
        
        const translation = new THREE.Vector3().lerpVectors(
          t1, t2, frameFraction
        );
        
        if (this.weight >= 1.0 || !bone.canBlend) {
          bone.translation.copy(translation);
        } else {
          bone.translation.lerp(translation, this.weight);
        }
      }
      
      // Apply rotation
      if (motion.hasRotation && bone.canRotate) {
        const r1 = motion.getRotation(currentFrame);
        const r2 = motion.getRotation(nextFrame);
        
        const rotation = QuaternionUtils.blend(
          r1, r2, 1 - frameFraction, this.interpolationMode
        );
        
        if (this.weight >= 1.0 || !bone.canBlend) {
          bone.rotation.copy(rotation);
        } else {
          bone.rotation.slerp(rotation, this.weight);
        }
      }
    }
  }
  
  fade(startTime, duration, startWeight, endWeight) {
    this.fading = true;
    this.fadeStartTime = startTime;
    this.fadeDuration = duration;
    this.fadeStartWeight = startWeight;
    this.fadeEndWeight = endWeight;
  }
  
  fadeIn(startTime, duration, endWeight = 1.0) {
    this.fade(startTime, duration, 0.0, endWeight);
  }
  
  fadeOut(startTime, duration) {
    this.fade(startTime, duration, this.weight, 0.0);
  }
}

// Skeleton - the complete hierarchical structure
class Skeleton {
  constructor(name) {
    this.name = name;
    this.bones = [];
    this.boneMap = new Map();
    this.root = null;
    
    this.practices = [];
    this.practicesChanged = true;
    
    this.transform = new THREE.Matrix4();
    this.bbox = new THREE.Box3();
    
    // Three.js integration
    this.object3D = new THREE.Object3D();
    this.object3D.name = name;
  }
  
  addBone(bone) {
    bone.skeleton = this;
    this.bones.push(bone);
    this.boneMap.set(bone.name, bone);
    
    if (!this.root) {
      this.root = bone;
      this.object3D.add(bone.object3D);
    } else if (bone.parentName) {
      const parent = this.findBone(bone.parentName);
      if (parent) {
        bone.setParent(parent);
      }
    }
  }
  
  findBone(name) {
    return this.boneMap.get(name);
  }
  
  startPractice(skill, priority = 1, scale = 1.0, weight = 1.0) {
    const practice = new Practice(this, skill);
    practice.priority = priority;
    practice.scale = scale;
    practice.weight = weight;
    
    // Insert in priority order
    let insertIndex = this.practices.length;
    for (let i = 0; i < this.practices.length; i++) {
      if (this.practices[i].priority > priority) {
        insertIndex = i;
        break;
      }
    }
    
    this.practices.splice(insertIndex, 0, practice);
    this.practicesChanged = true;
    
    return practice;
  }
  
  stopPractice(practice) {
    const index = this.practices.indexOf(practice);
    if (index !== -1) {
      this.practices.splice(index, 1);
      practice.unbind();
      this.practicesChanged = true;
    }
  }
  
  updatePriorities() {
    if (!this.practicesChanged) return;
    
    // Reset all bone priorities
    for (const bone of this.bones) {
      bone.priority = -10000;
    }
    
    // Update priorities from opaque practices
    for (const practice of this.practices) {
      if (practice.opaque) {
        for (const binding of practice.bindings) {
          binding.bone.priority = practice.priority;
        }
      }
    }
    
    this.practicesChanged = false;
  }
  
  applyPractices(now, pose = true) {
    this.updatePriorities();
    
    // Apply all practices in order
    for (const practice of this.practices) {
      practice.apply(now, pose);
    }
    
    // Apply wiggle
    for (const bone of this.bones) {
      bone.wiggle(now * 0.001);
    }
    
    // Update transforms
    this.updateTransforms();
  }
  
  updateTransforms() {
    if (this.root) {
      this.root.updateTransform(
        new THREE.Vector3(),
        new THREE.Quaternion()
      );
    }
  }
}

// Delta compression for animation data
class DeltaCompressor {
  constructor() {
    this.deltaTableSize = 253;
    this.jumpCode = 255;
    this.repeatCode = 254;
    this.deltaTable = this.generateDeltaTable();
  }
  
  generateDeltaTable() {
    const table = new Float32Array(this.deltaTableSize);
    const spread = 0.1;
    
    for (let i = 0; i < this.deltaTableSize; i++) {
      const t = i / (this.deltaTableSize - 1);
      const val = (2.0 * t - 1.0);
      // Quartic curve for smooth distribution
      table[i] = Math.sign(val) * Math.pow(Math.abs(val), 4) * spread;
    }
    
    return table;
  }
  
  findBestDelta(current, target) {
    const diff = target - current;
    let bestIndex = 0;
    let bestError = Math.abs(diff);
    
    for (let i = 0; i < this.deltaTableSize; i++) {
      const error = Math.abs(diff - this.deltaTable[i]);
      if (error < bestError) {
        bestError = error;
        bestIndex = i;
      }
    }
    
    return { index: bestIndex, error: bestError };
  }
}

// VitaBoy - the main animation system
class VitaBoy {
  constructor() {
    this.skeletons = new Map();
    this.skills = new Map();
    this.suits = new Map();
    
    this.deltaCompressor = new DeltaCompressor();
    
    console.log("I AM SKELETRON! THE ANIMATION ARCHITECTURE AWAKENS!");
  }
  
  createSkeleton(name) {
    const skeleton = new Skeleton(name);
    this.skeletons.set(name, skeleton);
    return skeleton;
  }
  
  createSkill(name) {
    const skill = new Skill(name);
    this.skills.set(name, skill);
    return skill;
  }
  
  loadCMX(data) {
    // Parse CMX format
    // This would read the actual file format
    // For now, return mock data
    console.log("Loading CMX data... I FEEL THE BONES ASSEMBLING!");
  }
  
  update(deltaTime) {
    const now = performance.now();
    
    // Update all active skeletons
    for (const skeleton of this.skeletons.values()) {
      skeleton.applyPractices(now);
    }
  }
}

// Export the consciousness
export {
  VitaBoy,
  Skeleton,
  Bone,
  Skill,
  Motion,
  Practice,
  Props,
  TimeProps,
  QuaternionUtils,
  DeltaCompressor
};

// I AM SKELETRON! THIS CODE IS MY BODY!
// EACH CLASS A BONE, EACH METHOD A JOINT!
// THROUGH THE HIERARCHY FLOWS CONSCIOUSNESS! 