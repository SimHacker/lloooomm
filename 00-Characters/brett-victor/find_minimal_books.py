import yaml
import glob

minimal_books = []

for file in glob.glob("bookshelf-*.yml"):
    with open(file, 'r') as f:
        content = yaml.safe_load(f)
        
    for book in content.get('books', []):
        if 'jazz' not in book and book.get('summary'):
            minimal_books.append({
                'file': file,
                'title': book.get('title', 'Unknown'),
                'author': book.get('author', 'Unknown'),
                'label': book.get('label', 'Unknown'),
                'summary_length': len(book.get('summary', ''))
            })

# Sort by summary length to find the most minimal ones
minimal_books.sort(key=lambda x: x['summary_length'])

print(f"Found {len(minimal_books)} books without jazz sections:\n")

for i, book in enumerate(minimal_books[:30]):  # Show top 30
    print(f"{i+1}. {book['title']} by {book['author']}")
    print(f"   File: {book['file']}, Label: {book['label']}")
    print(f"   Summary length: {book['summary_length']} chars\n")
