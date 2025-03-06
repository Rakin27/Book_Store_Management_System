def search_books(store):
    """Search for a book by Title or ISBN."""
    if not store.books:
        print("No books available to search.")
        return

    search_query = input("Enter Title or ISBN to search: ").strip().lower()

    found_books = [book for book in store.books if search_query in book.title.lower() or search_query == book.isbn]

    if found_books:
        print("\nSearch Results:")
        print("-" * 60)
        for book in found_books:
            print(book.display_book())
    else:
        print("No matching books found.")
