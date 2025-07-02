import yaml
import glob

books_without_jazz = []

for file in glob.glob("bookshelf-*.yml"):
    with open(file, 'r') as f:
        content = yaml.safe_load(f)
        
    for book in content.get('books', []):
        if 'jazz' not in book and book.get('summary'):
            books_without_jazz.append({
                'file': file,
                'title': book.get('title', 'Unknown'),
                'author': book.get('author', 'Unknown'),
                'id': book.get('id', 'Unknown')
            })

print(f"Found {len(books_without_jazz)} books without jazz sections:\n")

# Show a diverse selection from different files
files_seen = set()
count = 0
for book in books_without_jazz:
    if book['file'] not in files_seen or count < 20:
        print(f"{book['title']} by {book['author']}")
        print(f"  File: {book['file']}")
        print(f"  ID: {book['id']}\n")
        files_seen.add(book['file'])
        count += 1
        if count >= 20:
            break
