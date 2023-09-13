# Define a room - Description of the game
description = "Hi and welcome to my guessing game! Let's begin. First, enter the range you want to guess in:"

# Welcome screen
print(description)
print()

import random
import math

# Get the range/input from the user
lower_bound = int(input("Enter the smallest number in the range: "))
upper_bound = int(input("Enter the largest number in the range: "))

# Pick a random number within the given range
random_number = random.randint(lower_bound, upper_bound)

# Calculate the maximum number of attempts based on the range
max_attempts = math.log(upper_bound - lower_bound + 1, 2)
print(f"\nYou have {round(max_attempts)} chances to guess the number!\n")

# Initialize the number of tries
guess_count = 0

# Start the guessing loop
while guess_count < max_attempts:
    guess_count += 1
    
    # Take a guess from the user
    user_guess = int(input("Take a guess: "))

    # Check if the guess is correct
    if user_guess == random_number:
        print(f"Awesome! You guessed it in {guess_count} tries.")
        break
    elif user_guess < random_number:
        print("Your guess is too low. Try a higher number.")
    else:
        print("Your guess is too high. Try a smaller number.")

# If you used all your tries, reveal the random number
if guess_count >= max_attempts:
    print(f"\nThe number was {random_number}")
    print("Keep practicing! You'll get it next time!")