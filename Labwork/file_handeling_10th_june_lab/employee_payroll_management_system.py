def read_employees():
    employees = []

    file = open("employees.txt", "r")

    for line in file:
        emp_id, name, salary = line.strip().split(",")
        employees.append([emp_id, name, int(salary)])

    file.close()
    return employees


def display_all():
    employees = read_employees()

    print("\nEmployee Records")
    for emp in employees:
        print(emp[0], emp[1], emp[2])


def search_employee():
    emp_id = input("Enter Employee ID: ")

    employees = read_employees()

    for emp in employees:
        if emp[0] == emp_id:
            print("Employee Found")
            print("ID:", emp[0])
            print("Name:", emp[1])
            print("Salary:", emp[2])
            return

    print("Employee not found")


def average_salary():
    employees = read_employees()

    total = 0
    for emp in employees:
        total += emp[2]

    avg = total / len(employees)
    print("Average Salary =", avg)


def highest_lowest_salary():
    employees = read_employees()

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:
        if emp[2] > highest[2]:
            highest = emp

        if emp[2] < lowest[2]:
            lowest = emp

    print("\nHighest Paid Employee")
    print(highest[0], highest[1], highest[2])

    print("\nLowest Paid Employee")
    print(lowest[0], lowest[1], lowest[2])


def salary_above_50000():
    employees = read_employees()

    print("\nEmployees earning above ₹50,000")

    for emp in employees:
        if emp[2] > 50000:
            print(emp[0], emp[1], emp[2])


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file = open("employees.txt", "a")
    file.write("\n" + emp_id + "," + name + "," + salary)
    file.close()

    print("Employee added successfully")


def salary_categories():
    employees = read_employees()

    print("\nHIGH (₹60000 and above)")
    for emp in employees:
        if emp[2] >= 60000:
            print(emp[1], emp[2])

    print("\nMEDIUM (₹40000 to ₹59999)")
    for emp in employees:
        if 40000 <= emp[2] < 60000:
            print(emp[1], emp[2])

    print("\nLOW (Below ₹40000)")
    for emp in employees:
        if emp[2] < 40000:
            print(emp[1], emp[2])


while True:
    print("\n===== MENU =====")
    print("1. Display all employees")
    print("2. Search employee by ID")
    print("3. Average salary")
    print("4. Highest and lowest paid employee")
    print("5. Employees earning above ₹50,000")
    print("6. Add new employee")
    print("7. Salary categories")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_all()

    elif choice == "2":
        search_employee()

    elif choice == "3":
        average_salary()

    elif choice == "4":
        highest_lowest_salary()

    elif choice == "5":
        salary_above_50000()

    elif choice == "6":
        add_employee()

    elif choice == "7":
        salary_categories()

    elif choice == "8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")