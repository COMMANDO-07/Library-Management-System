# simple library management system using dictionary

# Database
books = {}
issued_books = {}

# add_book function
def add_book():
    name = input("Enter book name: ")
    quantity = int(input("Enter quantity: "))
    books[name] = books.get(name, 0) + quantity
    print("Book added successfully")

# show_book function
def show_book():
    if len(books) == 0:
        print("No books available")
    else:
        print("Available books:")
        for book in books:
            print(book, ":", books[book])

# issue_book function
def issue_book():
    show_book()
    print("-"*30)
    name = input("Enter book name: ")
    if name in books and books[name] > 0:
        student = input("Enter student name: ")
        days = int(input("Enter number of days: "))
        date = int(input("Enter issue date (day number): "))
        
        books[name] -= 1
        issued_books[name] = {
            "student": student,
            "days": days,
            "date": date
        }
        print("Book issued successfully")
    else:
        print("Book not available")

# return_book function
def return_book():
    name = input("Enter book name: ")
    if name in issued_books:
        return_date = int(input("Enter return date (day number): "))
        data = issued_books[name]
        
        used_days = return_date - data["date"]
        allowed_days = data["days"]
        
        fine = 0
        extra_days = used_days - allowed_days
        
        if extra_days > 0:
            if extra_days <= 7:
                fine = extra_days * 10
            elif extra_days <= 14:
                fine = extra_days * 20
            else:
                fine = extra_days * 60
        
        books[name] = books.get(name, 0) + 1
        issued_books.pop(name)
        
        print("Book returned")
        print("Days used:", used_days)
        print("Fine:", fine)
    else:
        print("Book was not issued")

# notice function
def notice():
    print("Late return charges:")
    print("1st week: 10 Rs per day per book")
    print("2nd week: 20 Rs per day per book")
    print("3rd week and more: 60 Rs per day per book")

# Library function
def library():
    notice()
    while True:
        print("-"*30)
        print("Menu")
        print("1. Add books")
        print("2. Show books")
        print("3. Issue book")
        print("4. Return book")
        print("5. Exit")
        print("-"*30)
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Program ended")
            break
        else:
            print("Invalid choice")

library()
