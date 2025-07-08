const fs = require('fs');

// Read the file
const content = fs.readFileSync('lloooommagotchi.html', 'utf8');

// Find all occurrences of "class VoiceDatabase"
const classPattern = /class VoiceDatabase \{/g;
let matches = [];
let match;

while ((match = classPattern.exec(content)) !== null) {
    matches.push(match.index);
}

console.log(`Found ${matches.length} occurrences of "class VoiceDatabase" at positions:`, matches);

if (matches.length === 2) {
    // Find the end of the duplicate class
    // Look for the closing brace followed by the comment about Voice database
    const duplicateStart = matches[1];
    const searchFrom = duplicateStart;
    
    // Find the comment that marks the end
    const endComment = "// Voice database moved to global initialization section";
    const endIndex = content.indexOf(endComment, searchFrom);
    
    if (endIndex !== -1) {
        // Remove everything from the duplicate class declaration to just before the end comment
        const beforeDuplicate = content.substring(0, duplicateStart);
        const afterDuplicate = content.substring(endIndex);
        
        // Add a clean comment where the duplicate was
        const fixed = beforeDuplicate + 
            "        // 🎤 VoiceDatabase class already defined above - duplicate removed\n\n        " + 
            afterDuplicate;
        
        // Write the fixed file
        fs.writeFileSync('lloooommagotchi-fixed.html', fixed);
        
        console.log('✅ Fixed file written to lloooommagotchi-fixed.html');
        console.log(`Removed ${endIndex - duplicateStart} characters of duplicate code`);
        
        // Show what was around the removal
        console.log('\n📍 Context around removal:');
        console.log('BEFORE:', beforeDuplicate.slice(-100));
        console.log('AFTER:', afterDuplicate.slice(0, 100));
    } else {
        console.error('❌ Could not find the end comment marker');
    }
} else {
    console.error(`❌ Expected 2 occurrences of "class VoiceDatabase", found ${matches.length}`);
} 