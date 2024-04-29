"""Q1. A program that generates a random number between 1 and 100. 
The user has to guess the number, and the program provides hints 
(higher or lower) until the correct number is guessed. """

import random

# Print the program title
print("Guess a number between 1 and 100")

# Generate a random number between 1 and 100
secret = random.randint(1, 100)


# Ask the user the number repeatedly until the guess is correct
while True:
    guess = int(input("Please guess a number between 1 and 100: "))

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again")
    else:
        print("Congratulations! Your guess is correct")
        #Exit the loop
        break  
