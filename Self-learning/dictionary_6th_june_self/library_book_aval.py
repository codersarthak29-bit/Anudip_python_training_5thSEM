'''books = { 
    "Python Basics": 5, 
    "Data Structures": 0, 
    "Machine Learning": 3, 
    "Java Programming": 2, 
    "DBMS": 0, 
    "Operating Systems": 6, 
    "Networking": 4, 
    "Cloud Computing": 1, 
    "Cyber Security": 0, 
    "Web Development": 7 
} 
Tasks 
• Display books that are currently unavailable.  
• Count the number of available books.  
• Find the book with the maximum copies.  
• Create a list of books having less than 3 copies.  
• Calculate the total number of books available.  '''
# Program to perform various operations on library books

# Dictionary containing book names as keys and available copies as values
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# --------------------------------------------------
# Task 1: Display books that are currently unavailable
# --------------------------------------------------
print("Books Currently Unavailable:")

# Traversing the dictionary
for book, copies in books.items():

    # Checking if copies are zero
    if copies == 0:
        print(book)

# --------------------------------------------------
# Task 2: Count the number of available books
# --------------------------------------------------
available_count = 0

# Checking each book
for copies in books.values():

    # Incrementing count if copies are available
    if copies > 0:
        available_count += 1

print("\nNumber of Available Books:", available_count)

# --------------------------------------------------
# Task 3: Find the book with the maximum copies
# --------------------------------------------------

# Assuming the first book has maximum copies initially
max_book = ""
max_copies = 0

# Traversing the dictionary
for book, copies in books.items():

    # Updating maximum copies and book name
    if copies > max_copies:
        max_copies = copies
        max_book = book

print("\nBook with Maximum Copies:")
print(max_book, "-", max_copies)

# --------------------------------------------------
# Task 4: Create a list of books having less than
# 3 copies
# --------------------------------------------------
low_stock_books = []

# Adding books with less than 3 copies to the list
for book, copies in books.items():

    # Checking if copies are less than 3
    if copies < 3:
        low_stock_books.append(book)

print("\nBooks Having Less Than 3 Copies:")
print(low_stock_books)

# --------------------------------------------------
# Task 5: Calculate the total number of books
# available
# --------------------------------------------------
total_books = 0

# Adding copies of all books
for copies in books.values():
    total_books += copies

print("\nTotal Number of Books Available:", total_books)
