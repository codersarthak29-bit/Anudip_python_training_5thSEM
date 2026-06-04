#Program to verify the PIN entered by the user
CORRECT_PIN = 1234
while True:
    entered_pin = int(input("Please enter your PIN: "))
    if entered_pin == CORRECT_PIN:
        print("PIN verified successfully. Access granted.")
        break
    else:
        print("Incorrect PIN. Please try again.")