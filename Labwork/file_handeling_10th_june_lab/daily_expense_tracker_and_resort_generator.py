'''Daily expenses are recorded in expenses.txt. 
File Format 
Food,450 
Travel,300 
Shopping,1200 
Electricity,850 
Internet,700 
Entertainment,600 
Medicine,400 
Education,1500 
Fuel,900 
Miscellaneous,250 
Requirements 
Develop a program to: 
1. Display all expenses.  
2. Calculate total expenditure.  
3. Find the category with highest and lowest spending.  
4. Display expenses greater than ₹800.  
5. Add a new expense category.  
6. Update an existing expense amount.  
7. Generate a summary report in report.txt containing:  
o Total Expenses  
o Highest Expense Category  
o Lowest Expense Category  
o Categories spending more than ₹800 '''
# ==========================================================
# Expense Management System
# ==========================================================
# Load expenses from file
def load_expenses():
    expenses = []
    file = open("expenses.txt", "r")
    for line in file:
        expenses.append(line.strip().split(","))
    file.close()
    return expenses
# Save expenses back to file
def save_expenses(expenses):
    file = open("expenses.txt", "w")
    for expense in expenses:
        file.write(expense[0] + "," + str(expense[1]) + "\n")
    file.close()
# Display all expenses
def display_expenses():
    expenses = load_expenses()
    print("\nExpense Records")
    print("-" * 35)
    for expense in expenses:
        print(expense[0], "- ₹", expense[1])
# Calculate total expenditure
def total_expenditure():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        total += int(expense[1])
    print("\nTotal Expenditure : ₹", total)
# Find highest and lowest expense
def highest_lowest_expense():
    expenses = load_expenses()
    highest_category = expenses[0][0]
    highest_amount = int(expenses[0][1])
    lowest_category = expenses[0][0]
    lowest_amount = int(expenses[0][1])
    for expense in expenses:
        amount = int(expense[1])
        if amount > highest_amount:
            highest_amount = amount
            highest_category = expense[0]
        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = expense[0]
    print("\nHighest Expense")
    print(highest_category, "- ₹", highest_amount)
    print("\nLowest Expense")
    print(lowest_category, "- ₹", lowest_amount)
# Display expenses above ₹800
def expenses_above_800():
    expenses = load_expenses()
    print("\nExpenses Greater Than ₹800")
    print("-" * 35)
    for expense in expenses:
        if int(expense[1]) > 800:
            print(expense[0], "- ₹", expense[1])
# Add new expense category
def add_expense():
    category = input("Enter Expense Category : ")
    amount = input("Enter Amount : ")
    file = open("expenses.txt", "a")
    file.write("\n" + category + "," + amount)
    file.close()
    print("Expense Added Successfully.")
# Update expense amount
def update_expense():
    category = input("Enter Category To Update : ")
    expenses = load_expenses()
    found = False
    for expense in expenses:
        if expense[0].lower() == category.lower():
            new_amount = input("Enter New Amount : ")
            expense[1] = new_amount
            found = True
            print("Expense Updated Successfully.")
    if found == False:
        print("Category Not Found.")
    save_expenses(expenses)
# Generate summary report
def generate_report():
    expenses = load_expenses()
    total = 0
    highest_category = expenses[0][0]
    highest_amount = int(expenses[0][1])
    lowest_category = expenses[0][0]
    lowest_amount = int(expenses[0][1])
    above_800 = []
    for expense in expenses:
        amount = int(expense[1])
        total += amount
        if amount > highest_amount:
            highest_amount = amount
            highest_category = expense[0]
        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = expense[0]
        if amount > 800:
            above_800.append(expense[0])
    file = open("report.txt", "w")
    file.write("Expense Summary Report\n")
    file.write("======================\n\n")
    file.write("Total Expenses : " + str(total) + "\n")
    file.write("Highest Expense Category : " +
               highest_category + " (" +
               str(highest_amount) + ")\n")
    file.write("Lowest Expense Category : " +
               lowest_category + " (" +
               str(lowest_amount) + ")\n")
    file.write("\nCategories Spending More Than 800rs\n")
    for category in above_800:
        file.write(category + "\n")
    file.close()
    print("Report Generated Successfully in report.txt")
# ==========================================================
# Menu Driven Program
# ==========================================================
while True:
    print("\n")
    print("=" * 40)
    print("      EXPENSE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Find Highest & Lowest Expense")
    print("4. Display Expenses Greater Than ₹800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Summary Report")
    print("8. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        display_expenses()
    elif choice == 2:
        total_expenditure()
    elif choice == 3:
        highest_lowest_expense()
    elif choice == 4:
        expenses_above_800()
    elif choice == 5:
        add_expense()
    elif choice == 6:
        update_expense()
    elif choice == 7:
        generate_report()
    elif choice == 8:
        print("Thank You.")
        break
    else:
        print("Invalid Choice.")