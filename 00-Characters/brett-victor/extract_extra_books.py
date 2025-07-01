#!/usr/bin/env python3
"""
Extract all extra books that don't belong on any shelf into extra-books.yml
"""

import yaml
import os

def load_yaml(filepath):
    """Load a YAML file and return its content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_yaml(data, filepath):
    """Save data to a YAML file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

def extract_extra_books():
    """Extract all extra books based on the reconciliation analysis."""
    
    # Define the extra books to extract (from our analysis)
    extra_books_to_remove = {
        'r2-c1': [
            {'title': 'Vehicles: Experiments in Synthetic Psychology', 'author': 'Valentino Braitenberg', 'index': 1},
            {'title': 'Thinking, Fast and Slow', 'author': 'Daniel Kahneman', 'index': 5},
            {'title': 'Gödel, Escher, Bach: An Eternal Golden Braid', 'author': 'Douglas R. Hofstadter', 'index': 6}
        ],
        'r2-c2': [
            {'title': 'The Inmates Are Running the Asylum', 'author': 'Alan Cooper', 'index': 2}
        ],
        'r2-c3': [
            {'title': 'LISP in Small Pieces', 'author': 'Christian Queinnec', 'index': 2}
        ],
        'r2-c4': [
            {'title': 'The Image: A Guide to Pseudo-events in America', 'author': 'Daniel J. Boorstin', 'index': 0},
            {'title': 'The Semiotic Engineering of Human-Computer Interaction', 'author': 'Clarisse de Souza', 'index': 1}
        ],
        'r6-c1': [
            {'title': 'The Oregon Experiment', 'author': 'Christopher Alexander, Murray Silverstein, Shlomo Angel, etc.', 'index': 1},
            {'title': 'On Growth and Form', 'author': "D'Arcy Wentworth Thompson", 'index': 3},
            {'title': 'The Natural House', 'author': 'Frank Lloyd Wright', 'index': 4},
            {'title': 'The Modular of Le Corbusier', 'author': 'Le Corbusier', 'index': 5},
            {'title': 'The City in History: Its Origins, Its Transformations, and Its Prospects', 'author': 'Lewis Mumford', 'index': 6},
            {'title': 'The Social Life of Small Urban Spaces', 'author': 'William H. Whyte', 'index': 8},
            {'title': 'An Introduction to the History of Western Architecture', 'author': 'David Watkin', 'index': 9},
            {'title': 'The New Organic Architecture: The Breaking Wave', 'author': 'David Pearson', 'index': 10},
            {'title': "An Engineer's Conception of Life", 'author': 'James T. P. Yao', 'index': 11},
            {'title': 'Architecture without Architects: A Short Introduction to Non-Pedigreed Architecture', 'author': 'Bernard Rudofsky', 'index': 12}
        ],
        'r6-c3': [
            {'title': 'Logic Synthesis and Verification Algorithms', 'author': 'Gary D. Hachtel, Fabio Somenzi', 'index': 0},
            {'title': 'The Art of Digital Design: An Introduction to Top-Down Design', 'author': 'Franklin P. Prosser, David E. Winkel', 'index': 2},
            {'title': 'Digital Design', 'author': 'M. Morris Mano', 'index': 3},
            {'title': 'The Art of Electronics', 'author': 'Paul Horowitz, Winfield Hill', 'index': 5}
        ]
    }
    
    # Collect all extra books with their full data
    extra_books_collection = {
        'description': 'Books that were incorrectly added to Brett Victor\'s bookshelf during enrichment',
        'total_count': 21,
        'shelves': {}
    }
    
    for shelf, books_to_remove in extra_books_to_remove.items():
        print(f"\nProcessing shelf {shelf}...")
        
        # Load the current shelf file
        shelf_file = f"bookshelf-{shelf}.yml"
        shelf_data = load_yaml(shelf_file)
        
        if not shelf_data or 'books' not in shelf_data:
            print(f"  Warning: No books found in {shelf_file}")
            continue
            
        # Extract the extra books
        extracted_books = []
        remaining_books = []
        
        # Sort books to remove by index in reverse order to avoid index shifting issues
        books_to_remove_sorted = sorted(books_to_remove, key=lambda x: x['index'], reverse=True)
        
        for i, book in enumerate(shelf_data['books']):
            # Check if this book should be removed
            should_remove = False
            for extra_book in books_to_remove:
                if (book.get('title') == extra_book['title'] and 
                    book.get('author') == extra_book['author'] and
                    i == extra_book['index']):
                    should_remove = True
                    extracted_books.append(book)
                    print(f"  Extracting: {book['title']} by {book['author']}")
                    break
            
            if not should_remove:
                remaining_books.append(book)
        
        # Store extracted books
        if extracted_books:
            extra_books_collection['shelves'][shelf] = {
                'extracted_count': len(extracted_books),
                'books': extracted_books
            }
        
        # Update the shelf file with remaining books
        shelf_data['books'] = remaining_books
        save_yaml(shelf_data, shelf_file)
        print(f"  Updated {shelf_file}: removed {len(extracted_books)} books, {len(remaining_books)} remain")
    
    # Save all extra books to extra-books.yml
    save_yaml(extra_books_collection, 'extra-books.yml')
    print(f"\n✅ Saved {extra_books_collection['total_count']} extra books to extra-books.yml")
    
    # Verify the counts
    actual_count = sum(shelf_info['extracted_count'] for shelf_info in extra_books_collection['shelves'].values())
    print(f"   Actual extracted: {actual_count}")

if __name__ == "__main__":
    extract_extra_books() 