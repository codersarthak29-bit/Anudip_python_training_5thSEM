'''Problem Statement: 
Create a Student class to store the student's name, roll number, and marks obtained in three subjects. 
Implement methods to: 
• Accept student details.  
• Calculate the total marks.  
• Calculate the percentage.  
• Display the complete student report. '''
# Student Class Program using List to Store Marks

class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.marks = []

    # Accept student details
    def accept_details(self):
        self.name = input("Enter Student Name: ")
        if not self.name.isalpha():
            print("Invalid Name. Please enter alphabetic characters only.")
            self.name = input("Enter Student Name: ") # Re-prompt for name
        self.roll_no = input("Enter Roll Number: ")
        if not self.roll_no.isdigit():
            print("Invalid Roll Number. Please enter digits only.")
            self.roll_no = input("Enter Roll Number: ") # Re-prompt for roll number     

        print("Enter marks of 3 subjects:")
        for i in range(3):
            mark = float(input(f"Subject {i+1}: "))
            if mark<0:
                print("Marks cannot be negative. Please enter a valid mark.")
                mark = float(input(f"Subject {i+1}: ")) # Re-prompt for mark
            elif mark > 100:
                print("Marks cannot be greater than 100. Please enter a valid mark.")
                mark = float(input(f"Subject {i+1}: ")) # Re-prompt for mark

            self.marks.append(mark)

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks)

    # Calculate percentage
    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    # Display complete student report
    def display_report(self):
        print("\n------ STUDENT REPORT ------")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

        for i in range(len(self.marks)):
            print(f"Marks in Subject {i+1}: {self.marks[i]}")

        print("Total Marks:", self.calculate_total())
        print("Percentage: {:.2f}%".format(self.calculate_percentage()))


# Main Program
student = Student()
student.accept_details()
student.display_report()