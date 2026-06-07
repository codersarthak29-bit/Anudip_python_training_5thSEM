'''contacts = { 
    "Amit": "9876543210", 
    "Priya": "9876543211", 
    "Rohan": "9876543212", 
    "Neha": "9876543213", 
    "Anjali": "9876543214", 
    "Karan": "9876543215", 
    "Pooja": "9876543216", 
    "Arjun": "9876543217", 
    "Sneha": "9876543218", 
    "Rahul": "9876543219" 
} 
Tasks 
• Display all contact names in alphabetical order.  
• Count the total number of contacts.  
• Search for a given contact name.  
• Create a list of contacts whose names start with a vowel.  
• Stop the search using break once the required contact is found. '''
# Program to perform various operations on contact records

# Dictionary containing contact names as keys and phone numbers as values
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# --------------------------------------------------
# Task 1: Display all contact names in alphabetical order
# --------------------------------------------------
print("Contact Names in Alphabetical Order:")

# Sorting and displaying contact names
# sorted() sorts the dictionary keys (contact names) alphabetically
# and returns them as a list
for name in sorted(contacts):
    print(name)

# --------------------------------------------------
# Task 2: Count the total number of contacts
# --------------------------------------------------

# Counting the total number of contacts
total_contacts = len(contacts)

print("\nTotal Number of Contacts:", total_contacts)

# --------------------------------------------------
# Task 3: Search for a given contact name
# --------------------------------------------------

# Taking contact name as input from the user
search_name = input("\nEnter contact name to search: ")

# --------------------------------------------------
# Task 4: Create a list of contacts whose names
# start with a vowel
# --------------------------------------------------
vowel_contacts = []

# Checking each contact name
for name in contacts:

    # Checking if the first letter is a vowel
    if name[0].lower() in "aeiou":
        vowel_contacts.append(name)

print("\nContacts Starting with a Vowel:")
print(vowel_contacts)

# --------------------------------------------------
# Task 5: Stop the search using break once the
# required contact is found
# --------------------------------------------------
found = False

# Traversing the dictionary
for name, number in contacts.items():

    # Checking if the contact exists
    if name.lower() == search_name.lower():
        print("\nContact Found:")
        print("Name:", name)
        print("Phone Number:", number)

        found = True

        # Exiting the loop as soon as the contact is found
        break

# Displaying message if contact is not found
if not found:
    print("\nContact Not Found")