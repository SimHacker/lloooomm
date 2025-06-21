# 🚀 LLOOOOMM GitHub Pages Deployment Instructions

## Quick Start

### 1. Make scripts executable:
```bash
chmod +x scripts/*.sh
```

### 2. Rename duplicate index.html files:
```bash
./scripts/rename-html-files.sh
```

### 3. Build the dist directory:
```bash
./scripts/build-dist.sh
```

### 4. Test locally (optional):
```bash
cd dist
python3 -m http.server 8000
# Visit http://localhost:8000
```

### 5. Deploy to GitHub Pages:

#### First time setup:
1. Go to your repo Settings → Pages
2. Source: GitHub Actions
3. Save

#### Deploy:
```bash
git add .
git commit -m "🚀 Deploy LLOOOOMM to GitHub Pages"
git push
```

The GitHub Action will automatically:
- Rename duplicate HTML files
- Build the dist directory
- Deploy to GitHub Pages
- Your site will be live at: `https://[username].github.io/lloooomm/`

## Manual Deployment (Alternative)

If you prefer manual deployment:

```bash
# Build
./scripts/build-dist.sh

# Create gh-pages branch
git checkout -b gh-pages
git rm -rf .
cp -r dist/* .
git add .
git commit -m "Deploy to GitHub Pages"
git push origin gh-pages --force
git checkout main
```

## Bird Attack Mode 🐦

Once deployed, open the browser console on the Late Night show page and type:
```javascript
birdAttack()
```

## Notes

- All HTML files are flattened into the dist directory
- The main index.html comes from `02-Areas/website/index.html`
- CSS, JS, and images are copied automatically
- The Late Night show has TECHNICOLOR LOGGING in the console!

🎉 PRE PRE PRE PRE PRE!!! 🎉 