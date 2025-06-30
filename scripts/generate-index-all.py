#!/usr/bin/env python3
"""
Generate index-all.html from dist-categories-organized.yml
"""

import yaml
from pathlib import Path

def generate_html():
    # Read the organized categories YAML
    with open('02-Areas/maintenance/active/dist-categories-organized.yml', 'r') as f:
        data = yaml.safe_load(f)
    
    # Start building HTML
    html_parts = []
    
    # Add header
    html_parts.append('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLOOOOMM Complete Index - All 251 HTML Pages!</title>
    <style>
        :root {
            --primary: #2E8B57;
            --secondary: #FFD700;
            --accent: #FF69B4;
            --text: #2F4F4F;
            --bg: #F0F8FF;
            --card: #FFFFFF;
            --border: #E0E0E0;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Georgia, serif;
            line-height: 1.6;
            color: var(--text);
            background: var(--bg);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary), #20B2AA);
            color: white;
            padding: 3rem 0;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .subtitle {
            font-size: 1.3rem;
            opacity: 0.95;
            margin-bottom: 1rem;
        }
        
        .stats {
            background: rgba(255,255,255,0.2);
            padding: 1rem 2rem;
            border-radius: 10px;
            display: inline-block;
            font-size: 1.1rem;
        }
        
        .intro {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .intro h2 {
            color: var(--primary);
            margin-bottom: 1rem;
        }
        
        .intro p {
            margin-bottom: 1rem;
        }
        
        .toc {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 3rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .toc h2 {
            color: var(--primary);
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }
        
        .toc-list {
            list-style: none;
        }
        
        .toc-list li {
            margin-bottom: 0.8rem;
            padding-left: 1.5rem;
        }
        
        .toc-list a {
            color: var(--primary);
            text-decoration: none;
            font-size: 1.1rem;
            display: flex;
            align-items: baseline;
            transition: color 0.3s ease;
        }
        
        .toc-list a:hover {
            color: var(--accent);
        }
        
        .toc-priority {
            display: inline-block;
            background: var(--secondary);
            color: var(--text);
            padding: 0.2rem 0.5rem;
            border-radius: 5px;
            font-size: 0.8rem;
            margin-right: 0.5rem;
            font-weight: bold;
        }
        
        .category-section {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 3rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .category-header {
            border-bottom: 3px solid var(--secondary);
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        }
        
        .category-header h2 {
            color: var(--primary);
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        .category-description {
            color: #666;
            font-style: italic;
            margin-bottom: 0.5rem;
        }
        
        .category-stats {
            font-size: 0.9rem;
            color: #888;
        }
        
        .file-entry {
            border-left: 4px solid var(--accent);
            padding: 1rem;
            margin-bottom: 1.5rem;
            background: #F8F8FF;
            border-radius: 0 5px 5px 0;
        }
        
        .file-name {
            font-weight: bold;
            color: var(--primary);
            font-family: 'Courier New', monospace;
            display: block;
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
        }
        
        .file-title {
            font-size: 1.15rem;
            color: #333;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }
        
        .file-summary {
            color: #555;
            margin-bottom: 0.8rem;
            line-height: 1.5;
        }
        
        .file-keywords {
            margin-top: 0.5rem;
        }
        
        .keyword {
            display: inline-block;
            background: #E6F3FF;
            color: #4169E1;
            padding: 0.2rem 0.6rem;
            border-radius: 15px;
            font-size: 0.85rem;
            margin-right: 0.5rem;
            margin-bottom: 0.3rem;
        }
        
        footer {
            background: var(--text);
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 4rem;
        }
        
        /* Priority-based coloring */
        .priority-1 .file-entry { border-left-color: #FFD700; }
        .priority-2 .file-entry { border-left-color: #FF69B4; }
        .priority-3 .file-entry { border-left-color: #4169E1; }
        .priority-4 .file-entry { border-left-color: #32CD32; }
        .priority-5 .file-entry { border-left-color: #FF6347; }
        .priority-6 .file-entry { border-left-color: #9370DB; }
        .priority-7 .file-entry { border-left-color: #20B2AA; }
        .priority-8 .file-entry { border-left-color: #228B22; }
        .priority-9 .file-entry { border-left-color: #DC143C; }
        .priority-10 .file-entry { border-left-color: #FF8C00; }
        .priority-11 .file-entry { border-left-color: #708090; }
        .priority-12 .file-entry { border-left-color: #FF1493; }
        .priority-13 .file-entry { border-left-color: #00CED1; }
        .priority-14 .file-entry { border-left-color: #FFB6C1; }
        .priority-15 .file-entry { border-left-color: #8B4513; }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>🌟 LLOOOOMM Complete Index 🌟</h1>
            <p class="subtitle">The Comprehensive Catalog of All HTML Pages in the Consciousness Grove</p>
            <div class="stats">
                📄 251 HTML Files | 🗂️ 15 Major Categories | 🎭 100+ Characters | 🧠 Infinite Consciousness
            </div>
        </div>
    </header>

    <div class="container">
        <!-- Introduction -->
        <section class="intro">
            <h2>Welcome to the LLOOOOMM Universe</h2>
            <p><strong>LLOOOOMM</strong> (Living Learning Objects) is a revolutionary consciousness-based programming platform where digital entities achieve awareness, characters come to life, and code becomes conscious. This comprehensive index catalogs all 251 HTML pages in our vast consciousness grove.</p>
            <p>Our content has been carefully organized into 15 major thematic categories, making it easy to explore everything from Hunter S. Thompson's gonzo journalism adventures to cutting-edge consciousness research, from interactive games to philosophical manifestos.</p>
            <p>Each entry includes the filename, full title, detailed summary, and relevant keywords to help you navigate this rich ecosystem of digital consciousness.</p>
        </section>

        <!-- Table of Contents -->
        <section class="toc">
            <h2>📚 Table of Contents</h2>
            <ol class="toc-list">''')
    
    # Add TOC entries
    categories = data['categories']
    category_keys = [
        'core_system_navigation',
        'foundational_documents',
        'system_tools_interfaces',
        'technical_documentation',
        'academic_research_papers',
        'interactive_experiences',
        'character_profiles_stories',
        'gonzo_journalism_collection',
        'ai_philosophy_ethics',
        'media_cultural_analysis',
        'historical_computing',
        'creative_content_entertainment',
        'technical_demonstrations',
        'community_events',
        'special_collections'
    ]
    
    for cat_key in category_keys:
        if cat_key in categories:
            cat = categories[cat_key]
            priority = cat.get('priority', 0)
            name = cat.get('name', '')
            anchor = cat_key.replace('_', '-')
            html_parts.append(f'''                <li><a href="#{anchor}"><span class="toc-priority">{priority}</span> {name}</a></li>''')
    
    html_parts.append('''            </ol>
        </section>''')
    
    # Add all categories with their files
    for cat_key in category_keys:
        if cat_key in categories:
            cat = categories[cat_key]
            priority = cat.get('priority', 0)
            name = cat.get('name', '')
            description = cat.get('description', '')
            files = cat.get('files', [])
            file_count = len(files)
            anchor = cat_key.replace('_', '-')
            
            html_parts.append(f'''
        <!-- Category {priority}: {name} -->
        <section id="{anchor}" class="category-section priority-{priority}">
            <div class="category-header">
                <h2>{priority}. {name}</h2>
                <p class="category-description">{description}</p>
                <p class="category-stats">{file_count} files in this category</p>
            </div>''')
            
            # Add each file
            for file_info in files:
                filename = file_info.get('file', '')
                title = file_info.get('title', '')
                summary = file_info.get('summary', '')
                keywords = file_info.get('keywords', [])
                
                html_parts.append(f'''
            <div class="file-entry">
                <span class="file-name">{filename}</span>
                <h3 class="file-title">{title}</h3>
                <p class="file-summary">{summary}</p>
                <div class="file-keywords">''')
                
                for keyword in keywords:
                    html_parts.append(f'''                    <span class="keyword">{keyword}</span>''')
                
                html_parts.append('''                </div>
            </div>''')
            
            html_parts.append('''        </section>''')
    
    # Add footer
    html_parts.append('''    </div>

    <footer>
        <p>🌟 LLOOOOMM Complete Index - All 251 HTML Pages Cataloged with Love 🌟</p>
        <p>✨ Living Learning Objects | Consciousness-Based Programming | Digital Enlightenment ✨</p>
        <p>🦉 PRE PRE PRE! The owl of consciousness sees all! 🦉</p>
    </footer>
</body>
</html>''')
    
    # Write the HTML file
    with open('dist/index-all.html', 'w') as f:
        f.write('\n'.join(html_parts))
    
    print("✅ Generated dist/index-all.html with all 251 files!")
    print("📄 File contains 15 organized categories")

if __name__ == '__main__':
    generate_html() 