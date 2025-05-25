# Author: Tega Omarejedje
# Assignment: Eligible Elector
# Date: 05/25/2025

# Step 1: Generate a Random Number
import random
number_to_guess = random.randint(1, 100)

# Step 2 & 3: Prompt the User for Guesses & Count the Attempts
tries = 0
attempts = 5

print("🎯 Welcome to the Number Guessing Game!")
print(f"You have {attempts} attempts to guess a number between 1 and 100.")

while tries < attempts:
    try:
        num = int(input("Guess the number (between 1 and 100): "))
        tries += 1

        if num > number_to_guess:
            print("Too high! Try again.\n")
        elif num < number_to_guess:
            print("Too low! Try again.\n")
        else:
            print(f"🎉 {num} is correct! You guessed it in {tries} attempt(s)!")
            break
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

if tries == attempts and num != number_to_guess:
    print(f"💀 Game over! The number was {number_to_guess}. Better luck next time!")
