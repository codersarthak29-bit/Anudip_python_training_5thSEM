# ==========================================================
# Contact Management System
# ==========================================================
# Load contacts from file
def load_contacts():
    contacts = []
    file = open("contacts.txt", "r")
    for line in file:
        contacts.append(line.strip().split(","))
    file.close()
    return contacts
# Save contacts back to file
def save_contacts(contacts):
    file = open("contacts.txt", "w")
    for contact in contacts:
        file.write(contact[0] + "," + contact[1] + "\n")
    file.close()
# Display all contacts
def display_contacts():
    contacts = load_contacts()
    print("\nContact List")
    print("-" * 30)
    for contact in contacts:
        print("Name   :", contact[0])
        print("Number :", contact[1])
        print("-" * 30)
# Search contact by name
def search_contact():
    name = input("Enter Name : ")
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("\nContact Found")
            print("Name   :", contact[0])
            print("Number :", contact[1])
            found = True
    if found == False:
        print("Contact not found.")
# Add new contact
def add_contact():
    name = input("Enter Name : ")
    number = input("Enter Mobile Number : ")
    contacts = load_contacts()
    contacts.append([name, number])
    save_contacts(contacts)
    print("Contact Added Successfully.")
# Update contact number
def update_contact():
    name = input("Enter Name to Update : ")
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if contact[0].lower() == name.lower():
            new_number = input("Enter New Number : ")
            contact[1] = new_number
            found = True
            print("Contact Updated Successfully.")
    if found == False:
        print("Contact not found.")
    save_contacts(contacts)
# Delete contact
def delete_contact():
    name = input("Enter Name to Delete : ")
    contacts = load_contacts()
    updated_contacts = []
    found = False
    for contact in contacts:
        if contact[0].lower() == name.lower():
            found = True
        else:
            updated_contacts.append(contact)
    if found == True:
        save_contacts(updated_contacts)
        print("Contact Deleted Successfully.")
    else:
        print("Contact not found.")
# Display names starting with vowels
def vowel_contacts():
    contacts = load_contacts()
    vowels = "AEIOUaeiou"
    print("\nContacts Starting With Vowel")
    print("-" * 35)
    found = False
    for contact in contacts:
        if contact[0][0] in vowels:
            print(contact[0], "-", contact[1])
            found = True
    if found == False:
        print("No contacts found.")
# ==========================================================
# Menu Driven Program
# ==========================================================
while True:
    print("\n")
    print("=" * 40)
    print("     CONTACT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add New Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        display_contacts()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        add_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        vowel_contacts()
    elif choice == 7:
        print("Thank You.")
        break
    else:
        print("Invalid Choice.")