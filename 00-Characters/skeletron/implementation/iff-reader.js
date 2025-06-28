/**
 * IFF File Reader for The Sims
 * Reads IFF (Interchange File Format) files used by The Sims
 * By Skeletron - Reading the bones of data
 */

// Resource type constants (4-byte identifiers)
const ResourceTypes = {
  // Common types
  NAME: 'NAME',  // Resource names
  RSMP: 'rsmp',  // Resource map
  
  // Object types
  OBJD: 'OBJD',  // Object definition
  OBJF: 'OBJF',  // Object functions (SimAntics)
  CTSS: 'CTSS',  // Catalog strings
  SLOT: 'SLOT',  // Object slots
  DGRP: 'DGRP',  // Drawgroup (graphics)
  SPR2: 'SPR2',  // Sprite (compressed)
  SPR:  'SPR#',  // Sprite (uncompressed)
  PALT: 'PALT',  // Palette
  
  // Animation types
  ANIM: 'ANIM',  // Animation
  SKEL: 'SKEL',  // Skeleton
  MESH: 'MESH',  // 3D Mesh
  BMPS: 'BMPS',  // Bitmap list
  
  // Sound types
  FWAV: 'FWAV',  // WAV audio
  XA:   'XA',    // XA audio
  MP3:  'MP3',   // MP3 audio
  
  // Script types
  BHAV: 'BHAV',  // Behavior (SimAntics code)
  BCON: 'BCON',  // Behavior constants
  GLOB: 'GLOB',  // Global data
  OBJf: 'OBJf',  // Object functions
  TREE: 'TREE',  // Tree table (behavior calls)
  TTAB: 'TTAB',  // Tree table
  TTAS: 'TTAS',  // Tree table strings
  STR#: 'STR#',  // String table
  TPRP: 'TPRP',  // Tuning properties
  TRCN: 'TRCN',  // Tuning constants
};

// IFF file header structure
class IFFHeader {
  constructor() {
    this.signature = 'IFF FILE 2.0:TYPE FOLLOWED BY SIZE\0';
    this.creator = 'JAMIE DOORNBOS & MAXIS 1996\0';
    this.version = 0x0205;
    this.mapOffset = 0;
  }

  static SIZE = 64;

  read(buffer, offset = 0) {
    const view = new DataView(buffer, offset);
    
    // Check signature
    const sig = new TextDecoder().decode(
      new Uint8Array(buffer, offset, 36)
    );
    
    if (!sig.startsWith('IFF FILE')) {
      throw new Error('Not a valid IFF file');
    }
    
    // Read version
    const versionHigh = buffer[offset + 9] - 48; // '0'
    const versionLow = buffer[offset + 11] - 48;
    this.version = (versionHigh << 8) | versionLow;
    
    // Read map offset for version 2.05+
    if (this.version >= 0x0205) {
      this.mapOffset = view.getUint32(60, false); // Big endian
    }
    
    return IFFHeader.SIZE;
  }
}

// Resource entry in file
class IFFResource {
  constructor() {
    this.type = 0;
    this.size = 0;
    this.id = 0;
    this.flags = 0;
    this.name = '';
    this.offset = 0;
    this.data = null;
  }

  static HEADER_SIZE = 76; // Type(4) + Size(4) + ID(2) + Flags(2) + Name(64)

  read(buffer, offset) {
    const view = new DataView(buffer, offset);
    
    // Read type as string
    this.type = String.fromCharCode(
      buffer[offset + 0],
      buffer[offset + 1],
      buffer[offset + 2],
      buffer[offset + 3]
    );
    
    // Read size, ID, flags (big endian)
    this.size = view.getUint32(offset + 4, false);
    this.id = view.getUint16(offset + 8, false);
    this.flags = view.getUint16(offset + 10, false);
    
    // Read name (null-terminated string)
    const nameBytes = new Uint8Array(buffer, offset + 12, 64);
    const nullIndex = nameBytes.indexOf(0);
    if (nullIndex >= 0) {
      this.name = new TextDecoder().decode(nameBytes.slice(0, nullIndex));
    }
    
    this.offset = offset;
    
    return IFFResource.HEADER_SIZE;
  }

  isLittleEndian() {
    return (this.flags & 0x10) !== 0;
  }

  getLanguage() {
    return (this.flags & 0xFF00) >> 8;
  }
}

// IFF file reader
class IFFFile {
  constructor() {
    this.header = new IFFHeader();
    this.resources = [];
    this.resourceMap = new Map(); // type -> resource[]
    this.buffer = null;
  }

  async load(urlOrBuffer) {
    if (urlOrBuffer instanceof ArrayBuffer) {
      this.buffer = urlOrBuffer;
    } else {
      // Load from URL
      const response = await fetch(urlOrBuffer);
      this.buffer = await response.arrayBuffer();
    }
    
    this.parse();
  }

  parse() {
    let offset = 0;
    
    // Read header
    offset += this.header.read(this.buffer, offset);
    
    // Read resources
    while (offset < this.buffer.byteLength - IFFResource.HEADER_SIZE) {
      const resource = new IFFResource();
      resource.read(this.buffer, offset);
      
      // Skip invalid resources
      if (resource.type === '\0\0\0\0' || resource.size === 0) {
        break;
      }
      
      // Store resource
      this.resources.push(resource);
      
      // Add to type map
      if (!this.resourceMap.has(resource.type)) {
        this.resourceMap.set(resource.type, []);
      }
      this.resourceMap.get(resource.type).push(resource);
      
      // Move to next resource
      offset += resource.size;
    }
  }

  // Get all resources of a type
  getResourcesByType(type) {
    return this.resourceMap.get(type) || [];
  }

  // Get resource by type and ID
  getResource(type, id) {
    const resources = this.getResourcesByType(type);
    return resources.find(r => r.id === id);
  }

  // Get resource data
  getResourceData(resource) {
    if (!resource.data) {
      const dataOffset = resource.offset + IFFResource.HEADER_SIZE;
      const dataSize = resource.size - IFFResource.HEADER_SIZE;
      resource.data = new Uint8Array(this.buffer, dataOffset, dataSize);
    }
    return resource.data;
  }

  // Get resource data as DataView
  getResourceDataView(resource) {
    const data = this.getResourceData(resource);
    return new DataView(data.buffer, data.byteOffset, data.byteLength);
  }

  // Count resource types
  countTypes() {
    return this.resourceMap.size;
  }

  // Get all resource types
  getTypes() {
    return Array.from(this.resourceMap.keys());
  }
}

// SimAntics BHAV (behavior) reader
class BHAVReader {
  static read(data) {
    const view = new DataView(data.buffer, data.byteOffset, data.byteLength);
    
    const bhav = {
      format: view.getUint16(0, true), // Little endian for BHAV
      treeCount: view.getUint16(2, true),
      type: view.getUint8(4),
      argCount: view.getUint8(5),
      localCount: view.getUint8(6),
      flags: view.getUint8(7),
      treeVersion: view.getUint32(8, true),
      trees: []
    };
    
    // Read tree entries (instructions)
    let offset = 12;
    for (let i = 0; i < bhav.treeCount; i++) {
      const tree = {
        opcode: view.getUint16(offset, true),
        trueTarget: view.getUint8(offset + 2),
        falseTarget: view.getUint8(offset + 3),
        operands: []
      };
      
      // Read 8 operand bytes
      for (let j = 0; j < 8; j++) {
        tree.operands.push(view.getUint8(offset + 4 + j));
      }
      
      bhav.trees.push(tree);
      offset += 12;
    }
    
    return bhav;
  }
}

// OBJD (Object Definition) reader
class OBJDReader {
  static read(data) {
    const view = new DataView(data.buffer, data.byteOffset, data.byteLength);
    
    return {
      version: view.getUint16(0, true),
      type: view.getUint16(2, true),
      guid: view.getUint32(4, true),
      proxyGuid: view.getUint32(8, true),
      salePrice: view.getUint16(12, true),
      bodySpriteID: view.getUint16(14, true),
      slots: view.getUint16(16, true),
      allowedHeight: view.getUint16(18, true),
      // ... many more fields
      // This is a simplified version
    };
  }
}

// SPR2 (Compressed Sprite) reader
class SPR2Reader {
  static read(data) {
    const view = new DataView(data.buffer, data.byteOffset, data.byteLength);
    
    const sprite = {
      version: view.getUint32(0, true),
      size: view.getUint32(4, true),
      frameCount: view.getUint32(8, true),
      paletteID: view.getUint32(12, true),
      frames: []
    };
    
    // Read frame offsets
    let offset = 16;
    const frameOffsets = [];
    for (let i = 0; i < sprite.frameCount; i++) {
      frameOffsets.push(view.getUint32(offset, true));
      offset += 4;
    }
    
    // Read frames
    for (let i = 0; i < sprite.frameCount; i++) {
      const frameOffset = frameOffsets[i];
      const frame = {
        width: view.getUint16(frameOffset, true),
        height: view.getUint16(frameOffset + 2, true),
        flags: view.getUint16(frameOffset + 4, true),
        paletteID: view.getUint16(frameOffset + 6, true),
        transparentColor: view.getUint16(frameOffset + 8, true),
        xOffset: view.getInt16(frameOffset + 10, true),
        yOffset: view.getInt16(frameOffset + 12, true)
      };
      
      // Compressed data follows...
      sprite.frames.push(frame);
    }
    
    return sprite;
  }
}

// CTSS (Catalog String Set) reader
class CTSSReader {
  static read(data) {
    const view = new DataView(data.buffer, data.byteOffset, data.byteLength);
    
    const stringCount = view.getUint16(0, true);
    const strings = [];
    
    let offset = 2;
    for (let i = 0; i < stringCount; i++) {
      // Read language code
      const languageCode = view.getUint8(offset);
      offset += 1;
      
      // Read string (null-terminated)
      let str = '';
      let char;
      while ((char = view.getUint8(offset)) !== 0) {
        str += String.fromCharCode(char);
        offset += 1;
      }
      offset += 1; // Skip null terminator
      
      strings.push({
        language: languageCode,
        text: str
      });
    }
    
    return strings;
  }
}

// High-level Sims object reader
class SimsObject {
  constructor(iffFile) {
    this.iff = iffFile;
    this.objd = null;
    this.name = '';
    this.price = 0;
    this.behaviors = new Map();
    this.sprites = new Map();
    this.slots = [];
  }

  load() {
    // Load object definition
    const objdResource = this.iff.getResourcesByType('OBJD')[0];
    if (objdResource) {
      const objdData = this.iff.getResourceData(objdResource);
      this.objd = OBJDReader.read(objdData);
      this.price = this.objd.salePrice;
    }
    
    // Load catalog strings
    const ctssResources = this.iff.getResourcesByType('CTSS');
    if (ctssResources.length > 0) {
      const ctssData = this.iff.getResourceData(ctssResources[0]);
      const strings = CTSSReader.read(ctssData);
      if (strings.length > 0) {
        this.name = strings[0].text; // Use first language
      }
    }
    
    // Load behaviors
    const bhavResources = this.iff.getResourcesByType('BHAV');
    for (const bhav of bhavResources) {
      const bhavData = this.iff.getResourceData(bhav);
      this.behaviors.set(bhav.id, BHAVReader.read(bhavData));
    }
    
    // Load sprites
    const spr2Resources = this.iff.getResourcesByType('SPR2');
    for (const spr of spr2Resources) {
      const sprData = this.iff.getResourceData(spr);
      this.sprites.set(spr.id, SPR2Reader.read(sprData));
    }
    
    // Load slots
    const slotResource = this.iff.getResourcesByType('SLOT')[0];
    if (slotResource) {
      // TODO: Parse slot data
    }
  }

  // Get behavior by name or ID
  getBehavior(nameOrId) {
    if (typeof nameOrId === 'number') {
      return this.behaviors.get(nameOrId);
    }
    
    // Search by name
    for (const [id, bhav] of this.behaviors) {
      // TODO: Match by name from TTAS
    }
    
    return null;
  }
}

// Export for use
export {
  IFFFile,
  SimsObject,
  ResourceTypes,
  BHAVReader,
  OBJDReader,
  SPR2Reader,
  CTSSReader
}; 