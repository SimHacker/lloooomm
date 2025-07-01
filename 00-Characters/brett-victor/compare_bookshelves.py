#!/usr/bin/env python3
"""
Compare original bookshelf files with enriched versions to analyze differences.
"""

import yaml
import os
from collections import defaultdict

def load_yaml(filepath):
    """Load a YAML file and return its content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_book_titles(data):
    """Extract book titles from the YAML data."""
    books = []
    if data and 'books' in data:
        for book in data['books']:
            title = book.get('title', 'Unknown Title')
            author = book.get('author', 'Unknown Author')
            books.append((title, author))
    return books

def compare_shelves():
    """Compare original and current bookshelf files."""
    original_dir = "../../temp/original-bookshelf-files"
    current_dir = "."
    
    results = {
        'added_books': defaultdict(list),
        'removed_books': defaultdict(list),
        'enriched_books': defaultdict(list),
        'unchanged_books': defaultdict(list)
    }
    
    # Process all bookshelf files
    for row in range(1, 7):
        for col in range(1, 5):
            filename = f"bookshelf-r{row}-c{col}.yml"
            original_path = os.path.join(original_dir, filename)
            current_path = os.path.join(current_dir, filename)
            
            if not os.path.exists(original_path) or not os.path.exists(current_path):
                continue
                
            print(f"\nAnalyzing {filename}...")
            
            # Load data
            original_data = load_yaml(original_path)
            current_data = load_yaml(current_path)
            
            # Extract books
            original_books = set(extract_book_titles(original_data))
            current_books = set(extract_book_titles(current_data))
            
            # Find differences
            added = current_books - original_books
            removed = original_books - current_books
            
            # Check for enrichment (books with jazz sections)
            if current_data and 'books' in current_data:
                for book in current_data['books']:
                    title = book.get('title', 'Unknown Title')
                    author = book.get('author', 'Unknown Author')
                    book_tuple = (title, author)
                    
                    if book_tuple in original_books:
                        if 'jazz' in book or 'cosmic_significance' in book or 'key_concepts' in book:
                            results['enriched_books'][filename].append(book_tuple)
                        else:
                            results['unchanged_books'][filename].append(book_tuple)
            
            # Store results
            results['added_books'][filename] = list(added)
            results['removed_books'][filename] = list(removed)
    
    return results

def print_summary(results):
    """Print a summary of the comparison results."""
    print("\n" + "="*80)
    print("BOOKSHELF COMPARISON SUMMARY")
    print("="*80)
    
    # Count totals
    total_added = sum(len(books) for books in results['added_books'].values())
    total_removed = sum(len(books) for books in results['removed_books'].values())
    total_enriched = sum(len(books) for books in results['enriched_books'].values())
    total_unchanged = sum(len(books) for books in results['unchanged_books'].values())
    
    print(f"\nOVERALL STATISTICS:")
    print(f"  Books added: {total_added}")
    print(f"  Books removed: {total_removed}")
    print(f"  Books enriched with metadata: {total_enriched}")
    print(f"  Books unchanged: {total_unchanged}")
    
    # Detailed breakdown
    if total_removed > 0:
        print(f"\n{'='*40}")
        print("BOOKS REMOVED (POTENTIAL DATA LOSS!):")
        print(f"{'='*40}")
        for shelf, books in results['removed_books'].items():
            if books:
                print(f"\n{shelf}:")
                for title, author in books:
                    print(f"  - {title} by {author}")
    
    if total_added > 0:
        print(f"\n{'='*40}")
        print("BOOKS ADDED:")
        print(f"{'='*40}")
        for shelf, books in results['added_books'].items():
            if books:
                print(f"\n{shelf}:")
                for title, author in books:
                    print(f"  + {title} by {author}")
    
    print(f"\n{'='*40}")
    print("ENRICHMENT BY SHELF:")
    print(f"{'='*40}")
    for shelf in sorted(results['enriched_books'].keys()):
        enriched_count = len(results['enriched_books'][shelf])
        unchanged_count = len(results['unchanged_books'][shelf])
        total_count = enriched_count + unchanged_count
        
        if total_count > 0:
            percentage = (enriched_count / total_count) * 100
            print(f"{shelf}: {enriched_count}/{total_count} books enriched ({percentage:.1f}%)")

if __name__ == "__main__":
    results = compare_shelves()
    print_summary(results) 