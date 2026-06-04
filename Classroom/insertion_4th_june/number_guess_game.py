#Program to guess the number 
number=7
i=0
while i>=0:
    guess = int(input("Guess the number between 0 and 9: "))
    if guess < 0 or guess > 9:
        print("Invalid input. Please enter a number between 0 and 9.")
        continue
    if guess == number:
        print("Congratulations! You guessed the number correctly.")
        break
    else:
        print("Wrong guess. Try again.")
    i = i + 1