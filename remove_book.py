def remove_book(store):
    """Remove a book by its ISBN."""
    if not store.books:
        print("No books available to remove.")
        return

    isbn_to_remove = input("Enter ISBN of the book to remove: ").strip()

    for book in store.books:
        if book.isbn == isbn_to_remove:
            store.books.remove(book)
            store.save_books()
            print("Book removed successfully!")
            return

    print("Book not found!")
