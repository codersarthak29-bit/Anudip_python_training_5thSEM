''' Create a digital library management system. 
Example Structure 
library = { 
    "B101": { 
        "title": "Python Basics", 
        "author": "ABC", 
        "copies": 5 
    } 
} 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase.  
Challenge 
Generate a complete library summary report.'''
# ==========================================
# DIGITAL LIBRARY MANAGEMENT SYSTEM
# ==========================================

# Dictionary to store all book records
library = {}

# ------------------------------------------
# INPUT DETAILS OF 30 BOOKS
# ------------------------------------------

for i in range(2):

    print("\nEnter Details Of Book", i + 1)

    # ------------------------------------------
    # Book ID Validation
    # Format Example : B101
    # ------------------------------------------

    while True:

        bid = input("Enter Book ID : ").upper().strip()

        if bid in library:
            print("Book ID Already Exists")

        elif bid.startswith("B") and len(bid) == 4 and bid[1:].isdigit():
            break

        else:
            print("Invalid Book ID! Example : B101")

    # ------------------------------------------
    # Book Title Validation
    # ------------------------------------------

    while True:

        title = " ".join(input("Enter Book Title : ").split()).title()

        if title.replace(" ", "").isalnum():
            break

        print("Invalid Book Title")

    # ------------------------------------------
    # Author Name Validation
    # ------------------------------------------

    while True:

        author = " ".join(input("Enter Author Name : ").split()).title()

        if author.replace(" ", "").isalpha():
            break

        print("Author Name Should Contain Alphabets Only")

    # ------------------------------------------
    # Copies Validation
    # ------------------------------------------

    while True:

        copies = input("Enter Available Copies : ").strip()

        if not copies.isdigit():
            print("Copies Must Contain Digits Only")
            continue

        copies = int(copies)

        if copies >= 0:
            break

        print("Copies Cannot Be Negative")

    # ------------------------------------------
    # Store Record In Dictionary
    # ------------------------------------------

    library[bid] = {
        "title": title,
        "author": author,
        "copies": copies
    }

# ==========================================
# MENU DRIVEN PROGRAM
# ==========================================

while True:

    print("\n")
    print("====================================")
    print(" DIGITAL LIBRARY MANAGEMENT SYSTEM ")
    print("====================================")
    print("1. Display All Books")
    print("2. Add A Book")
    print("3. Remove A Book")
    print("4. Search Book By ID")
    print("5. Search Book By Title")
    print("6. Update Available Copies")
    print("7. Issue A Book")
    print("8. Return A Book")
    print("9. Display Books With Fewer Than 3 Copies")
    print("10. Display Unavailable Books")
    print("11. Find Most Available Book")
    print("12. Generate Restocking Report")
    print("13. Immediate Purchase Books")
    print("14. Library Summary Report")
    print("15. Exit")

    choice = int(input("\nEnter Your Choice : "))

    # ------------------------------------------
    # 1. Display All Books
    # ------------------------------------------

    if choice == 1:

        print("\n========== ALL BOOKS ==========")

        for bid, data in library.items():

            print(
                f'{bid} -> '
                f'title="{data["title"]}", '
                f'author="{data["author"]}", '
                f'copies="{data["copies"]}"'
            )

    # ------------------------------------------
    # 2. Add A Book
    # ------------------------------------------

    elif choice == 2:

        while True:

            bid = input("Enter Book ID : ").upper().strip()

            if bid in library:
                print("Book ID Already Exists")

            elif bid.startswith("B") and len(bid) == 4 and bid[1:].isdigit():
                break

            else:
                print("Invalid Book ID")

        while True:

            title = " ".join(
                input("Enter Book Title : ").split()
            ).title()

            if title.replace(" ", "").isalnum():
                break

            print("Invalid Title")

        while True:

            author = " ".join(
                input("Enter Author Name : ").split()
            ).title()

            if author.replace(" ", "").isalpha():
                break

            print("Invalid Author Name")

        while True:

            copies = input("Enter Copies : ").strip()

            if not copies.isdigit():
                print("Invalid Copies")
                continue

            copies = int(copies)

            if copies >= 0:
                break

        library[bid] = {
            "title": title,
            "author": author,
            "copies": copies
        }

        print("Book Added Successfully")

    # ------------------------------------------
    # 3. Remove A Book
    # ------------------------------------------

    elif choice == 3:

        bid = input("Enter Book ID : ").upper().strip()

        if bid in library:

            del library[bid]

            print("Book Removed Successfully")

        else:

            print("Book Not Found")

    # ------------------------------------------
    # 4. Search Book By ID
    # ------------------------------------------

    elif choice == 4:

        bid = input("Enter Book ID : ").upper().strip()

        if bid in library:

            print("\nBook Found")

            print(
                f'{bid} -> '
                f'title="{library[bid]["title"]}", '
                f'author="{library[bid]["author"]}", '
                f'copies="{library[bid]["copies"]}"'
            )

        else:

            print("Book Not Found")

    # ------------------------------------------
    # 5. Search Book By Title
    # ------------------------------------------

    elif choice == 5:

        title = input(
            "Enter Book Title : "
        ).strip().lower()

        found = False

        for bid, data in library.items():

            if data["title"].lower() == title:

                print(
                    bid,
                    "->",
                    data
                )

                found = True

        if not found:

            print("Book Not Found")

    # ------------------------------------------
    # 6. Update Available Copies
    # ------------------------------------------

    elif choice == 6:

        bid = input("Enter Book ID : ").upper().strip()

        if bid in library:

            while True:

                copies = input(
                    "Enter New Copies : "
                ).strip()

                if not copies.isdigit():
                    print("Invalid Copies")
                    continue

                copies = int(copies)

                if copies >= 0:
                    break

            library[bid]["copies"] = copies

            print("Copies Updated Successfully")

        else:

            print("Book Not Found")

    # ------------------------------------------
    # 7. Issue A Book
    # ------------------------------------------

    elif choice == 7:

        bid = input("Enter Book ID : ").upper().strip()

        if bid in library:

            if library[bid]["copies"] > 0:

                library[bid]["copies"] -= 1

                print("Book Issued Successfully")

            else:

                print("Book Unavailable")
    # ------------------------------------------
    # 8. Return A Book
    # ------------------------------------------

    elif choice == 8:

        bid = input("Enter Book ID : ").upper().strip()

        if bid in library:

            library[bid]["copies"] += 1

            print("Book Returned Successfully")

        else:

            print("Book Not Found")

    # ------------------------------------------
    # 9. Display Books With Fewer Than 3 Copies
    # ------------------------------------------

    elif choice == 9:

        print("\n========== LOW STOCK BOOKS ==========")

        found = False

        for bid, data in library.items():

            if data["copies"] < 3:

                print(
                    f'{bid} -> '
                    f'title="{data["title"]}", '
                    f'author="{data["author"]}", '
                    f'copies="{data["copies"]}"'
                )

                found = True

        if not found:

            print("No Books Found")

    # ------------------------------------------
    # 10. Display Unavailable Books
    # ------------------------------------------

    elif choice == 10:

        print("\n========== UNAVAILABLE BOOKS ==========")

        found = False

        for bid, data in library.items():

            if data["copies"] == 0:

                print(
                    f'{bid} -> '
                    f'title="{data["title"]}", '
                    f'author="{data["author"]}", '
                    f'copies="{data["copies"]}"'
                )

                found = True

        if not found:

            print("No Unavailable Books")

    # ------------------------------------------
    # 11. Find Most Available Book
    # ------------------------------------------

    elif choice == 11:

        for bid in library:

            most_available = bid
            break

        for bid in library:

            if (
                library[bid]["copies"]
                >
                library[most_available]["copies"]
            ):

                most_available = bid

        print("\n========== MOST AVAILABLE BOOK ==========")

        print(
            f'{most_available} -> '
            f'title="{library[most_available]["title"]}", '
            f'author="{library[most_available]["author"]}", '
            f'copies="{library[most_available]["copies"]}"'
        )

    # ------------------------------------------
    # 12. Generate Restocking Report
    # Books Having Less Than 3 Copies
    # ------------------------------------------

    elif choice == 12:

        print("\n========== RESTOCKING REPORT ==========")

        found = False

        for bid, data in library.items():

            if data["copies"] < 3:

                print(
                    f'{bid} -> '
                    f'title="{data["title"]}", '
                    f'copies="{data["copies"]}"'
                )

                found = True

        if not found:

            print("No Books Need Restocking")

    # ------------------------------------------
    # 13. Create Dictionary Of Books
    # Requiring Immediate Purchase
    # Copies <= 1
    # ------------------------------------------

    elif choice == 13:

        immediate_purchase = {}

        for bid, data in library.items():

            if data["copies"] <= 1:

                immediate_purchase[bid] = data

        print("\n===== IMMEDIATE PURCHASE BOOKS =====")

        if len(immediate_purchase) == 0:

            print("No Books Require Immediate Purchase")

        else:

            for bid, data in immediate_purchase.items():

                print(
                    f'{bid} -> '
                    f'title="{data["title"]}", '
                    f'author="{data["author"]}", '
                    f'copies="{data["copies"]}"'
                )

    # ------------------------------------------
    # 14. Generate Complete Library Summary Report
    # ------------------------------------------

    elif choice == 14:

        total_books = len(library)

        available_books = 0
        unavailable_books = 0
        low_stock_books = 0

        for bid, data in library.items():

            if data["copies"] > 0:

                available_books += 1

            else:

                unavailable_books += 1

            if data["copies"] < 3:

                low_stock_books += 1

        # Find Most Available Book

        for bid in library:

            most_available = bid
            break

        for bid in library:

            if (
                library[bid]["copies"]
                >
                library[most_available]["copies"]
            ):

                most_available = bid

        print("\n")
        print("========================================")
        print("         LIBRARY SUMMARY REPORT         ")
        print("========================================")

        print("Total Books               :", total_books)

        print(
            "Available Books           :",
            available_books
        )

        print(
            "Unavailable Books         :",
            unavailable_books
        )

        print(
            "Books With Low Stock      :",
            low_stock_books
        )

        print(
            "Most Available Book       :",
            library[most_available]["title"]
        )

        print(
            "Available Copies          :",
            library[most_available]["copies"]
        )

        print("========================================")
        print("          REPORT COMPLETED              ")
        print("========================================")

    # ------------------------------------------
    # 15. Exit Program
    # ------------------------------------------

    elif choice == 15:

        print("\nExiting Library Management System...")
        break

    # ------------------------------------------
    # Invalid Choice
    # ------------------------------------------

    else:

        print("Invalid Choice! Please Try Again.")
    