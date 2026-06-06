'''Books available in a library: 
books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
] 
Write a program to: 
• Display unavailable books.  
• Find all books with more than 2 copies.  
• Count available books.  
• Stop searching once a requested book is found.  '''
books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
] 
#Task1:Display unavailable books.
print("Unavailable books : ")
for i in books:
    if i[1]==0:
        print(i[0])
#Task2:Find all books with more than 2 copies
print("Books with more than 2 copies: ")
for i in books:
    if i[1]>2:
        print(i[0])
#Task3:Count available books.
aval_count=0
for i in books:
    if i[1]!=0:
        aval_count+=1
print("Available books: ",aval_count)
#Task4:Stop searching once a requested book is found
print("Name of the books: ")
print("1. Python Basics")
print("2. Data Science")
print("3. Java Programming")
print("4. Machine Learning")
request=input("Enter the name of the book :")
for i in books:
    if i[1]==0:
        print("Book is out of stock!!")
        break
    else:
        if i[0]==request:
            print("book found")
            break
