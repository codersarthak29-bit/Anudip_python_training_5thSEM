#Program to check the password entered by the user in LOGIN page
CORRECT_PASSWORD = "admin123"
while True:
    entered_password = input("Please enter your password: ")
    if entered_password == CORRECT_PASSWORD:
        print("Login sucessful")
        break
    else:
        print("Incorrect password. ")