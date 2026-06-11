'''Problem Statement 
A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt. '''
#-----------------------------------------------------------------
#Program to make  Hospital Patient Record Management System
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#TASK1: Display all patients record( using function: def display_records)
#-----------------------------------------------------------------
def display_records():
    with open("patients.txt", 'r') as file:
        print("===================All Patient Records======================")
        for line in file:
            print(line.strip())

#----------------------------------------------------------------
#TASK2: Display critical patients
#----------------------------------------------------------------
def display_critical_patients():
    with open("patients.txt", 'r') as file:
        print("===================Critical Patient Records======================")
        for line in file:
            if "Critical" in line:
                print(line.strip())
#----------------------------------------------------------------
#TASK3: Count patients under each status
#----------------------------------------------------------------
def count_patients_by_status():
    status_counts = {"Normal": 0, "Critical": 0, "Stable": 0}
    with open("patients.txt", 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                status = parts[2]
                if status in status_counts:
                    status_counts[status] += 1
    print("===================Patient Counts by Status======================")
    for status, count in status_counts.items():
        print(f"{status}: {count}")
#----------------------------------------------------------------
#TASK4: search patient details using patient ID 
#----------------------------------------------------------------
def search():

    patient_id = input("Enter patient ID to search: ")  

    found = False
    with open("patients.txt", 'r') as file:
        for line in file:
            if patient_id in line:
                print("===================Patient Details======================") # This line was already present
                print(line.strip()) # Add this line to print the found patient's details
                found = True
    if not found:

        print(f"Patient with ID {patient_id} not found.")
#----------------------------------------------------------------
#TASK5: Save critical patient records to critical_patients.txt
#----------------------------------------------------------------
def save_critical_patients():
    with open("patients.txt", 'r') as infile, open("critical_patients.txt", 'w') as outfile:
        for line in infile:
            if "Critical" in line:
                outfile.write(line)
#----------------------------------------------------------------
#TASK6: Main menu for the Hospital Patient Record Management System
#----------------------------------------------------------------

while True:
    print("\n===================Hospital Patient Record Management System======================")
    print("1. Display All Patient Records")
    print("2. Display Critical Patients")
    print("3. Count Patients by Status")
    print("4. Search Patient by ID")
    print("5. Save Critical Patient Records")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
         display_records()
    elif choice == '2':
        display_critical_patients()
    elif choice == '3':
        count_patients_by_status()
    elif choice == '4':
        search()
    elif choice == '5':
        save_critical_patients()
        print("The records of critical patients stotred.")
    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
