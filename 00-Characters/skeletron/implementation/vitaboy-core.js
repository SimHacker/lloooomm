/**
 * VitaBoy Core Classes for LLOOOOMM
 * Based on The Sims animation system
 * Created by Skeletron - The Typo Hero
 */

// Base Transform utilities
class Transform {
  constructor(matrix = null) {
    this.matrix = matrix || mat4.create();
  }

  static fromTranslationRotationScale(translation, rotation, scale) {
    const t = new Transform();
    mat4.fromRotationTranslationScale(t.matrix, rotation, translation, scale);
    return t;
  }

  multiply(other) {
    const result = new Transform();
    mat4.multiply(result.matrix, this.matrix, other.matrix);
    return result;
  }
}

// Quaternion for smooth rotations
class Quaternion {
  constructor(x = 0, y = 0, z = 0, w = 1) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.w = w;
  }

  static fromAxisAngle(axis, angle) {
    const halfAngle = angle * 0.5;
    const s = Math.sin(halfAngle);
    return new Quaternion(
      axis[0] * s,
      axis[1] * s,
      axis[2] * s,
      Math.cos(halfAngle)
    );
  }

  normalize() {
    const len = Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z + this.w * this.w);
    if (len > 0) {
      const invLen = 1 / len;
      this.x *= invLen;
      this.y *= invLen;
      this.z *= invLen;
      this.w *= invLen;
    }
    return this;
  }

  slerp(other, t) {
    // Spherical linear interpolation for smooth animation
    let dot = this.x * other.x + this.y * other.y + this.z * other.z + this.w * other.w;
    
    if (dot < 0) {
      other = new Quaternion(-other.x, -other.y, -other.z, -other.w);
      dot = -dot;
    }

    if (dot > 0.95) {
      // Linear interpolation for close quaternions
      return new Quaternion(
        this.x + t * (other.x - this.x),
        this.y + t * (other.y - this.y),
        this.z + t * (other.z - this.z),
        this.w + t * (other.w - this.w)
      ).normalize();
    }

    const theta = Math.acos(dot);
    const sinTheta = Math.sin(theta);
    const a = Math.sin((1 - t) * theta) / sinTheta;
    const b = Math.sin(t * theta) / sinTheta;

    return new Quaternion(
      a * this.x + b * other.x,
      a * this.y + b * other.y,
      a * this.z + b * other.z,
      a * this.w + b * other.w
    );
  }
}

// Props - key/value pairs for metadata
class Props {
  constructor() {
    this.associations = new Map();
  }

  set(key, value) {
    this.associations.set(key, value);
  }

  get(key) {
    return this.associations.get(key);
  }

  has(key) {
    return this.associations.has(key);
  }

  clear() {
    this.associations.clear();
  }
}

// TimeProps - time-based property animations
class TimeProps {
  constructor() {
    this.keyframes = [];
  }

  add(time, props) {
    this.keyframes.push({ time, props });
    this.keyframes.sort((a, b) => a.time - b.time);
  }

  get(time) {
    if (this.keyframes.length === 0) return null;
    
    // Find surrounding keyframes
    let before = null;
    let after = null;
    
    for (let i = 0; i < this.keyframes.length; i++) {
      if (this.keyframes[i].time <= time) {
        before = this.keyframes[i];
      }
      if (this.keyframes[i].time >= time && !after) {
        after = this.keyframes[i];
      }
    }

    if (!before) return after ? after.props : null;
    if (!after || before === after) return before.props;

    // TODO: Interpolate between keyframes
    return before.props;
  }
}

// Bone - skeletal hierarchy node
class Bone {
  constructor(name) {
    this.name = name;
    this.parent = null;
    this.children = [];
    this.sibling = null;
    
    // Local transform
    this.translation = vec3.create();
    this.rotation = new Quaternion();
    
    // Global transform (computed)
    this.globalTranslation = vec3.create();
    this.globalRotation = new Quaternion();
    this.transform = new Transform();
    
    // Animation properties
    this.canTranslate = true;
    this.canRotate = true;
    this.canBlend = true;
    this.canWiggle = false;
    this.wigglePower = 0.0;
    
    this.props = new Props();
  }

  addChild(bone) {
    bone.parent = this;
    if (this.children.length > 0) {
      bone.sibling = this.children[this.children.length - 1];
    }
    this.children.push(bone);
  }

  updateTransform(parentTranslation = vec3.create(), parentRotationInverse = new Quaternion()) {
    // Compute global transform from local + parent
    vec3.add(this.globalTranslation, parentTranslation, this.translation);
    
    // Apply parent rotation to translation
    const rotatedTrans = vec3.create();
    vec3.transformQuat(rotatedTrans, this.translation, parentRotationInverse);
    vec3.add(this.globalTranslation, parentTranslation, rotatedTrans);
    
    // Combine rotations
    this.globalRotation = parentRotationInverse.multiply(this.rotation);
    
    // Update transform matrix
    this.transform = Transform.fromTranslationRotationScale(
      this.globalTranslation,
      this.globalRotation,
      vec3.fromValues(1, 1, 1)
    );
    
    // Update children
    const myRotInverse = new Quaternion(-this.globalRotation.x, -this.globalRotation.y, 
                                        -this.globalRotation.z, this.globalRotation.w);
    for (const child of this.children) {
      child.updateTransform(this.globalTranslation, myRotInverse);
    }
  }

  wiggle() {
    if (!this.canWiggle || this.wigglePower === 0) return;
    
    // Add Perlin noise to rotation
    const time = performance.now() * 0.001;
    const noise = new Quaternion(
      (Math.sin(time * 2.3) * 0.5 + Math.sin(time * 5.7) * 0.5) * this.wigglePower,
      (Math.sin(time * 3.1) * 0.5 + Math.sin(time * 7.3) * 0.5) * this.wigglePower,
      (Math.sin(time * 4.7) * 0.5 + Math.sin(time * 6.1) * 0.5) * this.wigglePower,
      1.0
    ).normalize();
    
    this.rotation = this.rotation.slerp(noise, 0.1);
  }
}

// Motion - animation data for a bone
class Motion {
  constructor(boneName) {
    this.boneName = boneName;
    this.frames = 0;
    this.duration = 0;
    
    this.hasTranslation = false;
    this.hasRotation = false;
    
    this.translations = [];
    this.rotations = [];
    
    this.props = new Props();
    this.timeProps = new TimeProps();
  }

  getTranslation(frame) {
    if (!this.hasTranslation || frame >= this.translations.length) {
      return vec3.create();
    }
    return this.translations[frame];
  }

  getRotation(frame) {
    if (!this.hasRotation || frame >= this.rotations.length) {
      return new Quaternion();
    }
    return this.rotations[frame];
  }

  setTranslation(frame, translation) {
    while (this.translations.length <= frame) {
      this.translations.push(vec3.create());
    }
    this.translations[frame] = translation;
    this.hasTranslation = true;
    this.frames = Math.max(this.frames, frame + 1);
  }

  setRotation(frame, rotation) {
    while (this.rotations.length <= frame) {
      this.rotations.push(new Quaternion());
    }
    this.rotations[frame] = rotation;
    this.hasRotation = true;
    this.frames = Math.max(this.frames, frame + 1);
  }
}

// Skill - collection of motions (animation clip)
class Skill {
  constructor(name) {
    this.name = name;
    this.motions = new Map(); // boneName -> Motion
    this.duration = 0;
    this.distance = 0;
    this.isMoving = false;
    this.isTurning = false;
    this.offset = vec3.create();
    this.turn = new Quaternion();
  }

  addMotion(motion) {
    this.motions.set(motion.boneName, motion);
    this.duration = Math.max(this.duration, motion.duration);
  }

  findMotion(boneName) {
    return this.motions.get(boneName);
  }
}

// Practice - active animation instance
class Practice {
  constructor(skeleton, skill) {
    this.skeleton = skeleton;
    this.skill = skill;
    
    this.priority = 1;
    this.scale = 1.0;
    this.weight = 1.0;
    this.elapsed = 0;
    this.isOver = false;
    
    this.repeatMode = 0; // 0=once, 1=loop, 2=pingpong
    this.fadeDuration = 0;
    this.fading = 0;
    this.fadeStart = 0;
    
    this.opaque = false;
    this.interruptable = true;
    this.stopWhenFaded = true;
    
    this.anchor = null;
    this.anchored = false;
    this.mixRootTranslation = true;
    this.mixRootRotation = true;
  }

  apply(now) {
    if (this.isOver && this.repeatMode === 0) return;
    
    // Calculate frame
    const normalizedTime = (this.elapsed / this.skill.duration) % 1.0;
    const frame = Math.floor(normalizedTime * this.skill.frames);
    
    // Apply motions to bones
    for (const [boneName, motion] of this.skill.motions) {
      const bone = this.skeleton.findBone(boneName);
      if (!bone) continue;
      
      // Get animation data
      const translation = motion.getTranslation(frame);
      const rotation = motion.getRotation(frame);
      
      // Apply with weight
      if (motion.hasTranslation && bone.canTranslate) {
        vec3.lerp(bone.translation, bone.translation, translation, this.weight);
      }
      
      if (motion.hasRotation && bone.canRotate) {
        bone.rotation = bone.rotation.slerp(rotation, this.weight);
      }
    }
  }

  update(deltaTime) {
    this.elapsed += deltaTime * this.scale;
    
    if (this.elapsed >= this.skill.duration) {
      switch (this.repeatMode) {
        case 0: // Once
          this.isOver = true;
          break;
        case 1: // Loop
          this.elapsed = this.elapsed % this.skill.duration;
          break;
        case 2: // Ping-pong
          // TODO: Implement ping-pong
          break;
      }
    }
    
    // Handle fading
    if (this.fading !== 0) {
      const fadeProgress = (performance.now() - this.fadeStart) / this.fadeDuration;
      if (this.fading > 0) {
        // Fade in
        this.weight = Math.min(1.0, fadeProgress);
      } else {
        // Fade out
        this.weight = Math.max(0.0, 1.0 - fadeProgress);
        if (this.weight === 0 && this.stopWhenFaded) {
          this.isOver = true;
        }
      }
      
      if (fadeProgress >= 1.0) {
        this.fading = 0;
      }
    }
  }
}

// Skin - mesh binding to bone
class Skin {
  constructor(name, boneName) {
    this.name = name;
    this.boneName = boneName;
    this.flags = 0;
    this.props = new Props();
    this.data = null; // DeformableMesh
  }
}

// Suit - collection of skins (outfit)
class Suit {
  constructor(name) {
    this.name = name;
    this.type = 0; // 0=normal, 1=nude, etc
    this.skins = [];
    this.props = new Props();
  }

  addSkin(skin) {
    this.skins.push(skin);
  }

  findSkin(boneName) {
    return this.skins.find(skin => skin.boneName === boneName);
  }
}

// Dressing - active suit binding
class Dressing {
  constructor(skeleton, suit) {
    this.skeleton = skeleton;
    this.suit = suit;
    this.bindings = []; // bone->skin associations
  }

  bind(textureName = null, flagMask = 0xFFFF) {
    // Create bindings for each skin
    for (const skin of this.suit.skins) {
      const bone = this.skeleton.findBone(skin.boneName);
      if (bone && (skin.flags & flagMask)) {
        this.bindings.push({ bone, skin, data: null });
      }
    }
  }

  unbind() {
    // Clean up bindings
    this.bindings = [];
  }
}

// Skeleton - the bone hierarchy
class Skeleton {
  constructor(name) {
    this.name = name;
    this.bones = [];
    this.root = null;
    this.transform = new Transform();
    
    this.practices = [];
    this.dressings = [];
    
    this.data = null; // VitaBoy reference
  }

  addBone(bone) {
    this.bones.push(bone);
    return this.bones.length - 1;
  }

  addRootBone(bone) {
    this.addBone(bone);
    this.root = bone;
  }

  findBone(name) {
    return this.bones.find(bone => bone.name === name);
  }

  startPractice(skill, priority = 1, scale = 1.0, weight = 1.0) {
    const practice = new Practice(this, skill);
    practice.priority = priority;
    practice.scale = scale;
    practice.weight = weight;
    
    this.practices.push(practice);
    this.practices.sort((a, b) => b.priority - a.priority);
    
    return practice;
  }

  stopPractice(practice) {
    const index = this.practices.indexOf(practice);
    if (index >= 0) {
      this.practices.splice(index, 1);
    }
  }

  dress(suit, textureName = null) {
    const dressing = new Dressing(this, suit);
    dressing.bind(textureName);
    this.dressings.push(dressing);
    return dressing;
  }

  undress(dressing) {
    const index = this.dressings.indexOf(dressing);
    if (index >= 0) {
      dressing.unbind();
      this.dressings.splice(index, 1);
    }
  }

  updateBoneTransforms() {
    if (this.root) {
      this.root.updateTransform();
    }
  }

  applyPractices(now) {
    // Reset bone transforms
    for (const bone of this.bones) {
      bone.translation = vec3.create();
      bone.rotation = new Quaternion();
    }
    
    // Apply practices in priority order
    for (const practice of this.practices) {
      if (!practice.isOver) {
        practice.apply(now);
      }
    }
    
    // Apply wiggle
    for (const bone of this.bones) {
      bone.wiggle();
    }
    
    // Update transforms
    this.updateBoneTransforms();
  }

  update(deltaTime, now) {
    // Update practices
    for (const practice of this.practices) {
      practice.update(deltaTime);
    }
    
    // Remove finished practices
    this.practices = this.practices.filter(p => !p.isOver);
    
    // Apply animations
    this.applyPractices(now);
  }

  clone() {
    const clone = new Skeleton(this.name);
    
    // Clone bones
    const boneMap = new Map();
    for (const bone of this.bones) {
      const cloneBone = new Bone(bone.name);
      cloneBone.translation = vec3.clone(bone.translation);
      cloneBone.rotation = new Quaternion(bone.rotation.x, bone.rotation.y, 
                                         bone.rotation.z, bone.rotation.w);
      cloneBone.canTranslate = bone.canTranslate;
      cloneBone.canRotate = bone.canRotate;
      cloneBone.canBlend = bone.canBlend;
      cloneBone.canWiggle = bone.canWiggle;
      cloneBone.wigglePower = bone.wigglePower;
      
      clone.addBone(cloneBone);
      boneMap.set(bone, cloneBone);
    }
    
    // Rebuild hierarchy
    for (const bone of this.bones) {
      const cloneBone = boneMap.get(bone);
      if (bone.parent) {
        const cloneParent = boneMap.get(bone.parent);
        cloneParent.addChild(cloneBone);
      }
    }
    
    if (this.root) {
      clone.root = boneMap.get(this.root);
    }
    
    return clone;
  }
}

// Export for use
export {
  Transform,
  Quaternion,
  Props,
  TimeProps,
  Bone,
  Motion,
  Skill,
  Practice,
  Skin,
  Suit,
  Dressing,
  Skeleton
}; 