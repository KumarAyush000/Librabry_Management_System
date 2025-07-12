# Updated crud_operations.py with JSON persistence
import json
import os

BOOKS_FILE = "books.json"

# Load books from JSON file
if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        books = json.load(f)
else:
    books = {}

# Save books to JSON file
def save_books():
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

# Add books
def add_books():
    while True:
        book_id = input("Enter Book ID (or press 'q' to Exit): ").strip()
        if book_id.lower() == "q":
            print("Exiting..\n")
            break
        if book_id in books:
            print(f"\n Book with ID: {book_id}, already registered in the system.\n")
            continue

        title = input("Enter book title: ")
        author = input("Enter Author Name: ").title()
        year = input("Enter Year of Publication: ")
        is_available_input = input("Enter Availability Status (True or False): ").strip().lower()
        is_available = is_available_input == "true"

        if any(field == "" for field in [book_id, title, author, is_available_input]):
            print("Fields cannot be empty.\n")
            continue

        books[book_id] = {
            "title": title,
            "author": author,
            "year": year,
            "available": is_available
        }

        save_books()

        print(f"\n Added: Book id: {book_id} → Title: {title}, Author: {author}, Year: {year}, Availability: {is_available}\n")

# View Books
def view_books():
    while True:
        book_no = input("Enter Book ID. ( or 'A' to show all, 'q' to quit): ").strip()
        if book_no == "":
            print("Book ID cannot be empty.")
            continue
        elif book_no.lower() == "q":
            print("Exiting..\n")
            break
        elif book_no.lower() == "a":
            print("\nAll Books Record:\n")
            for book_id, info in books.items():
                print(f"\n Book ID: {book_id} --> | Title: {info['title']} | Author: {info['author']} | Year: {info['year']} | Available: {info['available']}\n")
        elif book_no in books:
            info = books[book_no]
            print(f"\n Book ID: {book_no} --> | Title: {info['title']} | Author: {info['author']} | Year: {info['year']} | Available: {info['available']}\n")
        else:
            print(f"\n No Book with ID: {book_no} exists in the system.")

# Update Books
def update_books():
    while True:
        to_update = input("Enter Book ID to update (or 'q' to exit): ").strip()
        if to_update == "":
            print("Field cannot be empty.")
            continue
        elif to_update.lower() == "q":
            print("Exiting...\n")
            break
        elif to_update not in books:
            print(f"Book with ID: {to_update} is not registered in the system.")
            continue

        info = books[to_update]
        print(f"\n Current: Book ID {to_update} →| Title: {info['title']} | Author: {info['author']} | Year: {info['year']} | Available: {info['available']}\n")

        field = input("Update: 1-Title, 2-Author, 3-Year, 4-Available, q-exit: ").strip()
        if field.lower() == "q":
            print("Exiting.."); break
        elif field == "1":
            info["title"] = input("Enter new title: ")
        elif field == "2":
            info["author"] = input("Enter new Author: ").title()
        elif field == "3":
            info["year"] = input("Enter new Year: ")
        elif field == "4":
            is_available_input = input("Enter new Availability status (True or False): ").strip().lower()
            info["available"] = is_available_input == "true"

        save_books()

        print(f"\nUpdated: Book ID {to_update} →| Title: {info['title']} | Author: {info['author']} | Year: {info['year']} | Available: {info['available']}")

# Delete Books
def delete_books():
    while True:
        book_to_del = input("Enter Book ID to remove ( or 'q' to exit): ")
        if book_to_del.lower() == "q":
            print("Exiting the system...")
            break
        elif book_to_del in books:
            del books[book_to_del]
            save_books()
            print("Deletion complete.")
        else:
            print("Invalid Input.")
