'''The number of available copies of books in a library is stored below. 
Sample Data 
books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
} 
Tasks 
1. Display books with fewer than 3 copies.  
2. Find the book with maximum copies.  
3. Find the book with minimum copies.  
4. Count total books available.  
5. Generate a restocking list. '''
#program to make Library Book Availability System 
#sample data:
books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
} 
#task1:Display books with fewer than 3 copies.
print("Books Requiring Attention: ") 
for book,copy in books.items():
    if copy<3:
        print(book)
#task2:Find the book with maximum copies. 
print("Book with Maximum Copies: ")
max_copy=max(books,key=books.get)
print(f"{max_copy}: {books[max_copy]} copies")
#task3:Find the book with minimum copies.
print("Book with Minimum Copies: ")
min_copy=min(books,key=books.get)
print(f"{min_copy}: {books[min_copy]} copies")
#task4:Count total books available.
print("Total Books Available: ")
total=0
for copy in books.values():
    total+=copy
print(total)
#task5:Generate a restocking list.
print("Restocking List:")
for book, copy in books.items():
    if copy < 3:
        restock_amount = 5 - copy # Example: restock to 5 copies
        print(f"{book}: Add {restock_amount} copies")   
