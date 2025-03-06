import json
import os

class Book:
    def __init__(self, title, author, isbn, genre, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.price = price
        self.quantity = quantity

    # def __str__(self):
    #     return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nPrice:{self.price} Taka\nIn Stock: {self.quantity} Copies"

    def display_book(self):
        """Returns book details in a formatted string."""
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
                f"Genre: {self.genre}\n"
                f"Price: ${self.price}\n"
                f"Stock: {self.quantity} copies\n"
                )
    
# book1 = Book('It starts with us', 'Colleen Hoover', 1001, 'Romance Novel', 1300, 15)
# # print(book1)
# display = book1.display_book()
# print(display)

BOOKS_FILE = "books_file.json"

class BookStore:
    """Manages book data: loading and saving."""

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        #Load books from a JSON file. If the file doesn't exist or is empty, prompt user to create one.
        if  os.path.getsize(BOOKS_FILE) == 0:
            print("No existing book data found.")
            # choice = input("Would you like to create a new book file or start fresh? (create/start fresh)").strip().lower()
            # if choice == "create":
            #     print("Please create a new book file using add book")
            # elif choice == "start fresh":
            #     print("Starting fresh with an empty book list.")
            #     return []
            # else:
            #     print("Invalid choice. Starting with an empty list.")
        with open(BOOKS_FILE, "r") as file:
            try:
                books_data = json.load(file)
                return [Book(**book) for book in books_data]  # Convert dicts to Book objects
                print("All previous saved books are loaded")
            except (json.JSONDecodeError, TypeError):
                print("Error reading the book file.")
                return []

    def save_books(self):
        #Save books to the JSON file.
        with open(BOOKS_FILE, "w") as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)