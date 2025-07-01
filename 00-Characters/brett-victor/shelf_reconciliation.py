#!/usr/bin/env python3
"""
Comprehensive shelf reconciliation analysis.
Compares original bookshelf files with current versions to identify:
1. Books that were removed but should be present
2. Books that were added but don't belong
3. Books that were moved to wrong shelves
4. Books with changed order
5. Books with changed labels
"""

import yaml
import os
from collections import defaultdict, OrderedDict

def load_yaml(filepath):
    """Load a YAML file and return its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def extract_books_with_order(data):
    """Extract books preserving their order and all metadata."""
    books = []
    if data and 'books' in data:
        for idx, book in enumerate(data['books']):
            books.append({
                'index': idx,
                'title': book.get('title', 'Unknown Title'),
                'author': book.get('author', 'Unknown Author'),
                'label': book.get('label', ''),
                'summary': book.get('summary', ''),
                'full_data': book
            })
    return books

def normalize_title(title):
    """Normalize title for comparison (handle expansions)."""
    # Known title expansions that should be considered the same
    title_mappings = {
        "Mirror Worlds": "Mirror Worlds: or the Day Software Puts the Universe in a Shoebox...How It Will Happen and What It Will Mean",
        "The Art of Interactive Design": "The Art of Interactive Design: A Euphonious and Illuminating Guide to Building Successful Software",
        "The Humane Interface": "The Humane Interface: New Directions for Designing Interactive Systems",
        "Frames of Mind": "Frames of Mind: The Theory of Multiple Intelligences",
        "Origins of the Modern Mind": "Origins of the Modern Mind: Three Stages in the Evolution of Culture and Cognition",
        "A Pattern Language": "A Pattern Language: Towns, Buildings, Construction",
        "How Buildings Learn": "How Buildings Learn: What Happens After They're Built",
        "The Death and Life of Great American Cities": "The Death and Life of Great American Cities",
        "Technics and Civilization": "Technics and Civilization",
        "What Technology Wants": "What Technology Wants",
        "Computer Power and Human Reason": "Computer Power and Human Reason: From Judgment to Calculation",
        "The Nature of Code": "The Nature of Code: Simulating Natural Systems with Processing",
        "The Code Book": "The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography",
        "Engines of Logic": "Engines of Logic: Mathematicians and the Origin of the Computer",
        "Deschooling Society": "Deschooling Society",
        "The World Without Us": "The World Without Us"
    }
    
    # Check if this is a shortened version
    for short, full in title_mappings.items():
        if title == short:
            return full
        if title == full:
            return full
    
    return title

def find_book_in_all_shelves(book_title, author, all_current_books):
    """Find where a book currently exists across all shelves."""
    normalized_title = normalize_title(book_title)
    locations = []
    
    for shelf, books in all_current_books.items():
        for book in books:
            current_normalized = normalize_title(book['title'])
            # Check both title and author to handle cases where title changed
            if (current_normalized == normalized_title or 
                book['title'] == book_title or
                (book['author'] == author and 
                 (normalized_title in current_normalized or current_normalized in normalized_title))):
                locations.append({
                    'shelf': shelf,
                    'index': book['index'],
                    'title': book['title'],
                    'author': book['author'],
                    'label': book['label']
                })
    
    return locations

def analyze_shelf_changes():
    """Perform comprehensive analysis of all shelf changes."""
    
    print("="*80)
    print("COMPREHENSIVE SHELF RECONCILIATION ANALYSIS")
    print("="*80)
    
    # Load all original and current shelf data
    all_original_books = {}
    all_current_books = {}
    
    # Define all shelf files
    shelves = []
    for row in range(1, 7):
        for col in range(1, 5):
            shelves.append(f"r{row}-c{col}")
    
    # Load all data
    for shelf in shelves:
        original_path = f"../../temp/original-bookshelf-files/bookshelf-{shelf}.yml"
        current_path = f"./bookshelf-{shelf}.yml"
        
        original_data = load_yaml(original_path)
        current_data = load_yaml(current_path)
        
        if original_data:
            all_original_books[shelf] = extract_books_with_order(original_data)
        else:
            all_original_books[shelf] = []
            
        if current_data:
            all_current_books[shelf] = extract_books_with_order(current_data)
        else:
            all_current_books[shelf] = []
    
    # Analysis results
    missing_books = []  # Books that should be present but aren't
    extra_books = []    # Books that shouldn't be present
    moved_books = []    # Books in wrong shelf
    order_changes = []  # Books in different order
    label_changes = []  # Books with changed labels
    
    # Analyze each shelf
    for shelf in shelves:
        original_books = all_original_books[shelf]
        current_books = all_current_books[shelf]
        
        print(f"\n\nAnalyzing shelf {shelf}:")
        print("-" * 40)
        
        # Check each original book
        for orig_book in original_books:
            # Find this book in current shelves
            locations = find_book_in_all_shelves(orig_book['title'], orig_book['author'], all_current_books)
            
            if not locations:
                # Book is completely missing
                missing_books.append({
                    'shelf': shelf,
                    'book': orig_book,
                    'original_index': orig_book['index']
                })
                print(f"  MISSING: '{orig_book['title']}' by {orig_book['author']} (was at position {orig_book['index']})")
            else:
                # Check if it's in the right shelf
                correct_shelf = False
                for loc in locations:
                    if loc['shelf'] == shelf:
                        correct_shelf = True
                        # Check order
                        if loc['index'] != orig_book['index']:
                            order_changes.append({
                                'shelf': shelf,
                                'book': orig_book['title'],
                                'original_index': orig_book['index'],
                                'current_index': loc['index']
                            })
                            print(f"  ORDER CHANGED: '{orig_book['title']}' moved from position {orig_book['index']} to {loc['index']}")
                        
                        # Check label
                        if loc['label'] != orig_book['label']:
                            label_changes.append({
                                'shelf': shelf,
                                'book': orig_book['title'],
                                'original_label': orig_book['label'],
                                'current_label': loc['label']
                            })
                            print(f"  LABEL CHANGED: '{orig_book['title']}' from '{orig_book['label']}' to '{loc['label']}'")
                        break
                
                if not correct_shelf:
                    # Book was moved to wrong shelf
                    moved_books.append({
                        'book': orig_book,
                        'original_shelf': shelf,
                        'current_locations': locations
                    })
                    current_shelves = ', '.join([loc['shelf'] for loc in locations])
                    print(f"  MOVED TO WRONG SHELF: '{orig_book['title']}' now in {current_shelves}")
        
        # Check for extra books (in current but not in original)
        current_titles = set()
        for curr_book in current_books:
            normalized_title = normalize_title(curr_book['title'])
            
            # Check if this book belongs in this shelf
            belongs = False
            for orig_book in original_books:
                orig_normalized = normalize_title(orig_book['title'])
                if (orig_normalized == normalized_title or 
                    (curr_book['author'] == orig_book['author'] and 
                     (normalized_title in orig_normalized or orig_normalized in normalized_title))):
                    belongs = True
                    break
            
            if not belongs:
                # Check if it belongs in any other shelf
                belongs_elsewhere = None
                for other_shelf, other_books in all_original_books.items():
                    if other_shelf == shelf:
                        continue
                    for other_book in other_books:
                        other_normalized = normalize_title(other_book['title'])
                        if (other_normalized == normalized_title or
                            (curr_book['author'] == other_book['author'] and
                             (normalized_title in other_normalized or other_normalized in normalized_title))):
                            belongs_elsewhere = other_shelf
                            break
                    if belongs_elsewhere:
                        break
                
                if belongs_elsewhere:
                    # This is already tracked in moved_books
                    pass
                else:
                    # This book doesn't belong anywhere - it's extra
                    extra_books.append({
                        'shelf': shelf,
                        'book': curr_book,
                        'index': curr_book['index']
                    })
                    print(f"  EXTRA BOOK: '{curr_book['title']}' by {curr_book['author']} at position {curr_book['index']}")
    
    # Summary
    print("\n\n" + "="*80)
    print("SUMMARY OF ISSUES")
    print("="*80)
    
    print(f"\n1. MISSING BOOKS ({len(missing_books)} total):")
    for item in missing_books:
        print(f"   - {item['shelf']}: '{item['book']['title']}' by {item['book']['author']}")
    
    print(f"\n2. EXTRA BOOKS ({len(extra_books)} total):")
    for item in extra_books:
        print(f"   - {item['shelf']}: '{item['book']['title']}' by {item['book']['author']}")
    
    print(f"\n3. MOVED TO WRONG SHELF ({len(moved_books)} total):")
    for item in moved_books:
        current_locs = ', '.join([f"{loc['shelf']} (pos {loc['index']})" for loc in item['current_locations']])
        print(f"   - '{item['book']['title']}': should be in {item['original_shelf']} but is in {current_locs}")
    
    print(f"\n4. ORDER CHANGES ({len(order_changes)} total):")
    for item in order_changes:
        print(f"   - {item['shelf']}: '{item['book']}' moved from position {item['original_index']} to {item['current_index']}")
    
    print(f"\n5. LABEL CHANGES ({len(label_changes)} total):")
    for item in label_changes:
        print(f"   - {item['shelf']}: '{item['book']}' changed from '{item['original_label']}' to '{item['current_label']}'")
    
    # Save detailed results for correction script
    results = {
        'missing_books': missing_books,
        'extra_books': extra_books,
        'moved_books': moved_books,
        'order_changes': order_changes,
        'label_changes': label_changes,
        'all_original_books': all_original_books,
        'all_current_books': all_current_books
    }
    
    with open('reconciliation_results.yaml', 'w') as f:
        yaml.dump(results, f, default_flow_style=False, allow_unicode=True)
    
    print("\n\nDetailed results saved to reconciliation_results.yaml")
    
    return results

if __name__ == "__main__":
    analyze_shelf_changes() 