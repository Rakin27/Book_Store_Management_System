from book_data import Book

def add_book(store):
    """Add a new book to the store."""
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author: ").strip()
    isbn = input("Enter ISBN or Book ID: ").strip()
    genre = input("Enter Genre: ").strip()
    price = input("Enter Price: ").strip()
    quantity = input("Enter Quantity in stock: ").strip()

    # Validation
    if not title or not author or not isbn or not genre or not price or not quantity:
        print("All fields are required!")
        return
    try:
        price = float(price)
        if price <= 0:
            raise ValueError
    except ValueError:
        print("Price must be a positive number!")
        return
    try:
        quantity = int(quantity)
        if quantity < 0 & isinstance(quantity, int):
            raise ValueError
    except ValueError:
        print("Quantity must be a non-negative integer!")
        return

    # Check for duplicate ISBN
    for book in store.books:
        if book.isbn == isbn:
            print("A book with this ISBN already exists!")
            return

    new_book = Book(title, author, isbn, genre, price, quantity)
    store.books.append(new_book)
    store.save_books()
    print("Book added successfully!")
