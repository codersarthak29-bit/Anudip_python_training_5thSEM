'''
Problem Statement:
Library Management System using File Handling

books.txt Format:

B101,Python Basics,5
B102,Java Programming,2
B103,Data Science,0
B104,DBMS,3
B105,Machine Learning,1
B106,Operating Systems,4
B107,Networking,2
B108,Cyber Security,6
B109,Cloud Computing,0
B110,Web Development,3
'''
# ==========================================================
# Library Management System
# ==========================================================
# ----------------------------------------------------------
# Function: Load all books from file
# Purpose : Read file and store records in a list
# ----------------------------------------------------------
def load_books():
    books = []
    file = open("books.txt", "r")
    for line in file:
        data = line.strip().split(",")
        books.append(data)
    file.close()
    return books
# ----------------------------------------------------------
# Function: Save updated records to file
# Purpose : Rewrite file after issue/return operation
# ----------------------------------------------------------
def save_books(books):
    file = open("books.txt", "w")
    for book in books:
        record = book[0] + "," + book[1] + "," + str(book[2])
        file.write(record + "\n")
    file.close()
# ----------------------------------------------------------
# Function: Display all books
# ----------------------------------------------------------
def display_books():
    books = load_books()
    print("\nAvailable Books")
    print("-" * 50)
    for book in books:
        print("Book ID  :", book[0])
        print("Title    :", book[1])
        print("Quantity :", book[2])
        print("-" * 50)
# ----------------------------------------------------------
# Function: Search book using Book ID
# ----------------------------------------------------------
def search_book():
    book_id = input("Enter Book ID : ")
    books = load_books()
    found = False
    for book in books:
        if book[0] == book_id:
            print("\nBook Found")
            print("Book ID  :", book[0])
            print("Title    :", book[1])
            print("Quantity :", book[2])
            found = True
    if found == False:
        print("Book not found.")
# ----------------------------------------------------------
# Function: Issue a Book
# ----------------------------------------------------------
def issue_book():
    book_id = input("Enter Book ID to Issue : ")
    books = load_books()
    found = False
    for book in books:
        if book[0] == book_id:
            found = True
            quantity = int(book[2])
            if quantity > 0:
                quantity -= 1
                book[2] = quantity
                print("Book Issued Successfully.")
            else:
                print("Book Not Available.")
    if found == False:
        print("Book ID not found.")
    save_books(books)
# ----------------------------------------------------------
# Function: Return a Book
# ----------------------------------------------------------
def return_book():
    book_id = input("Enter Book ID to Return : ")
    books = load_books()
    found = False
    for book in books:
        if book[0] == book_id:
            found = True
            quantity = int(book[2])
            quantity += 1
            book[2] = quantity
            print("Book Returned Successfully.")
    if found == False:
        print("Book ID not found.")
    save_books(books)
# ----------------------------------------------------------
# Function: Display Unavailable Books
# ----------------------------------------------------------
def unavailable_books():
    books = load_books()
    print("\nUnavailable Books")
    print("-" * 50)
    found = False
    for book in books:
        if int(book[2]) == 0:
            print(book[0], "-", book[1])
            found = True
    if found == False:
        print("No unavailable books.")
# ----------------------------------------------------------
# Function: Display Books Requiring Restocking
# ----------------------------------------------------------
def restocking_books():
    books = load_books()
    print("\nBooks Requiring Restocking")
    print("-" * 50)
    found = False
    for book in books:
        if int(book[2]) < 2:
            print(book[0], "-", book[1], "-", book[2])
            found = True
    if found == False:
        print("No books require restocking.")
# ==========================================================
# Menu Driven Program
# ==========================================================
while True:
    print("\n")
    print("=" * 50)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")
    choice = int(input("Enter Your Choice : "))
    # ------------------------------------------------------
    # Perform operation according to user's choice
    # ------------------------------------------------------
    if choice == 1:
        display_books()
    elif choice == 2:
        search_book()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        unavailable_books()
    elif choice == 6:
        restocking_books()
    elif choice == 7:
        print("Thank You for Using Library Management System.")
        break
    else:
        print("Invalid Choice. Please Try Again.")