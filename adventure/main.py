import random

# Function to generate a random number between 1 and 10
def generate_random_number():
    return random.randint(1, 10)

# List to store previous guesses
previous_guesses = []

# Generate a random number
random_number = generate_random_number()

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 10. Can you guess what it is?")

# Main game loop
while True:
    try:
        guess = int(input("Your guess: "))

        # Add the guess to the list of previous guesses
        previous_guesses.append(guess)

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number ({random_number})!")
            break  # Exit the game

        # Show previous guesses
        print("Previous guesses:", previous_guesses)

    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 10.")

print("Thank you for playing!")