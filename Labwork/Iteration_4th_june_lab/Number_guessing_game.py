#Program to make a number guessing game
import random
#Generating a random number between 1 and 50
number=random.randint(1,50)
#Initializing the number of attempts to 0
attempts=0  
print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 50. Can you guess it?")
while True:
    #Taking input from the user
    guess=int(input("Enter your guess: "))
    while guess<1 or guess>50:
        print("Please enter a number between 1 and 50.")
        guess=int(input("Enter your guess: "))
    attempts+=1
    #Checking if the guess is correct
    if guess==number:
        print("Congratulations! You guessed the number in",attempts,"attempts.")
        break
    elif guess<number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
print("Number of attempts:",attempts)
