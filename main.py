from add_book import add_book
from view_books import view_books
from search_book import search_books
from remove_book import remove_book
from exit import exit_program
from book_data import BookStore

def main():
    
    store = BookStore()

    bookss = store.load_books()

    if bookss:
        print('The saved books are loaded')
        for count, book in enumerate(bookss, start=1):
            print('Book Number -', count)
            
    else:
        print('Sorry, no books found in the library!')
        print('Please add books to the library -->')

    while True:
        print("-" * 60)
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_book(store)
        elif choice == "2":
            view_books(store)
        elif choice == "3":
            search_books(store)
        elif choice == "4":
            remove_book(store)
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
