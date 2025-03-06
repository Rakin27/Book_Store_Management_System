def view_books(store):
    """Display all books in the store."""
    if not store.books:
        print("No books available in the store.")
        return

    print("\nList of Books:")
    print("-" * 60)
    for book in store.books:
        print(book.display_book())
