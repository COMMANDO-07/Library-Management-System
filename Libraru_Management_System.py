# simple library management system

# Database
books = []
issued_books = []

# add_book function
def add_book():
    name = input("Enter the name of the book: ")
    books.append(name)
    print(f"{name} is added now added.")

# show_book function
def show_book():
    if len(books) == 0:
        print("No books available.")
    else:
        print("Available books: ")
        for book in books:
            print(book)

# issue_book function
def issue_book():
    show_book()
    print("-"*30)
    name = input("Enter book name: ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print(f"{name} is issued.")
    else:
        print(f"{name} is not available.")

# return_book function
def return_book():
    name = input("Enter book name: ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(f"{name} is returned.")
    else:
        print(f"{name} was not issued from library.")

# Library function
def library():
    while True:
        print("Menu")
        print("1. Add books")
        print("2. Show books")
        print("3. Issue book")
        print("4. Return book")
        print("5. Exit")
        print("-"*30)
        
        choice = int(input("Enter your preference: "))
        print("-"*30)

        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you.")
            break
        else:
            print("Invalid preference")

library()