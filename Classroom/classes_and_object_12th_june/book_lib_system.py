'''Problem Statement: 
Create a Book class with attributes: 
• Book ID  
• Title  
• Author  
• Availability Status  
Implement methods to: 
• Issue a book.  
• Return a book.  
• Display book details.  
Prevent issuing a book that is already issued. '''

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability_status = "available" # Initially all books are available

    def issue_book(self):
        if self.availability_status == "available":
            self.availability_status = "issued"
            print(f"Book '{self.title}' has been issued.")
        else:
            print(f"Book '{self.title}' is already {self.availability_status}.")

    def return_book(self):
        if self.availability_status == "issued":
            self.availability_status = "available"
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' is not currently issued.")

    def display_book_details(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability Status: {self.availability_status}")
#---------------------------------------------------------------------
#main program
#---------------------------------------------------------------------

book=Book("B101","The prince of persia","Thomas Elfrid")
book.display_book_details()
print("========================================================================")
book.issue_book()
print("========================================================================")
book.display_book_details()
print("========================================================================")
book.return_book()
print("========================================================================")
book.display_book_details()
print("========================================================================")
book.issue_book()
print("========================================================================")
book.display_book_details()
print("========================================================================")
book.return_book()
