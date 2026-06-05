#program to make an ATM simulator
initial_balance = 10000
while True: #infinite loop to keep the ATM running until the user decides to exit
    print("\nWelcome to the ATM Simulator!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Please select an option (1-4): ") #taking user input for the desired operation

    if choice == '1': #checking the balance and displaying it to the user
        print(f"Your current balance is: ${initial_balance}")
    
    elif choice == '2': #taking the deposit amount from the user and updating the balance accordingly
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount > 0: #validating the deposit amount to ensure it's a positive number
            initial_balance += deposit_amount
            print(f"You have deposited ${deposit_amount}. Your new balance is: ${initial_balance}")
        else: #if the deposit amount is not valid, display an error message
            print("Invalid amount. Please enter a positive number.")
    
    elif choice == '3': #taking the withdrawal amount from the user and updating the balance accordingly, while also checking for sufficient funds
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if 0 < withdraw_amount <= initial_balance: #validating the withdrawal amount to ensure it's a positive number and does not exceed the current balance
            initial_balance -= withdraw_amount
            print(f"You have withdrawn ${withdraw_amount}. Your new balance is: ${initial_balance}")
        else: #if the withdrawal amount is not valid or exceeds the current balance, display an error message
            print("Invalid amount or insufficient funds.")
    
    elif choice == '4': #exiting the ATM simulator and displaying a goodbye message to the user
        print("Thank you for using the ATM Simulator. Goodbye!")
        break #breaking the loop to exit the program
    
    else: #if the user input does not match any of the valid options, display an error message
        print("Invalid option. Please select a number between 1 and 4.")