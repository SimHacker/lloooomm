#!/bin/bash
#
# organize-stray-files.sh
#
# A script to carefully move untracked project files from the root directory
# into their correct, classified locations within the LLOOOOMM structure.
# Adheres to the "Brewster Protocol" of organization.
#
# - Moves, does not copy.
# - Preserves directory structure.
# - Will NOT overwrite existing files at the destination.
# - Is idempotent and safe to run multiple times.

# Set the project root relative to the script's location
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." &> /dev/null && pwd )"

# --- Helper Function ---
# A safe move function that checks for existence before acting.
move_safe() {
    local source_path="$1"
    local dest_dir="$2"
    
    # Ensure the source file actually exists before trying to move it
    if [ ! -f "$source_path" ]; then
        echo "INFO: Source file '$source_path' not found, skipping."
        return
    fi

    local filename=$(basename "$source_path")
    local dest_path="$dest_dir/$filename"
    
    # Ensure the destination directory exists
    mkdir -p "$dest_dir"

    # Check if a file with the same name is already at the destination
    if [ -f "$dest_path" ]; then
        echo "SKIPPING: '$filename' already exists in '$dest_dir'."
    else
        echo "MOVING: '$filename' ==> '$dest_dir'"
        mv "$source_path" "$dest_path"
    fi
}

echo "--- Starting LLOOOOMM File Organization ---"
echo "Project Root: $PROJECT_ROOT"
echo "-------------------------------------------"

# --- Define Target Directories ---
SCIFI_DIR="$PROJECT_ROOT/spacecraft-cosmic-librarian/scifi"
ARTIFACTS_DIR="$PROJECT_ROOT/03-Resources/artifacts"
DOCS_DIR="$PROJECT_ROOT/03-Resources/artifacts/documentation"

# --- 1. Move Sci-Fi Book Files ---
echo "[CLASSIFICATION: SciFi Book Collection]"
move_safe "$PROJECT_ROOT/LittleBrother.md" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/blade-runner-0000dick.yml" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/contact00saga_1.md" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/doandroidsdreamof0000dick.md" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/doandroidsdreamof0000dick.yml" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/flowersforalgern2004keye.md" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/left-hand-of-darkness-0000legu.yml" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/martian-chronicles-0000brad.yml" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/neuromancer_202209.md" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/neuromancer_202209.yml" "$SCIFI_DIR"
move_safe "$PROJECT_ROOT/stranger-strange-land-0000hein.yml" "$SCIFI_DIR"

# --- 2. Move General Artifacts ---
echo "[CLASSIFICATION: General Artifacts]"
move_safe "$PROJECT_ROOT/eval-in-other-lisp.lisp" "$ARTIFACTS_DIR"
move_safe "$PROJECT_ROOT/kmp-doctor-eliza.lisp" "$ARTIFACTS_DIR"

# --- 3. Move Documentation Artifacts ---
echo "[CLASSIFICATION: Documentation Artifacts]"
move_safe "$PROJECT_ROOT/leela-sveltekit-interface-design.html" "$DOCS_DIR"

echo "-------------------------------------------"
echo "File organization script complete."
echo "Review the output and run 'git status' to see the results." 