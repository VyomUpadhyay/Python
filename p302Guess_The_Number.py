import random
import time

# Generate a random number between 1 and 50
target_number = random.randint(1, 50)
print("I have selected a number between 1 and 50. Try to guess it!")
print("You have 1 minute to guess the number.\n")

# Initialize variables for tracking guesses and attempts
guess = 0
attempts = 0
lower_bound = 1
upper_bound = 50

start_time = time.time()  # Start timer

# Loop until the user guesses the correct number or time runs out
while guess != target_number:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > 60:
        print("\nTime's up! You couldn't guess the number in 1 minute.")
        print(f"The correct number was: {target_number}")
        break

    print(f"Your current range is {lower_bound} to {upper_bound}")

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess > target_number:
        print("Your guess is too high! Try a lower number.")
        upper_bound = guess
    elif guess < target_number:
        print("Your guess is too low! Try a higher number.")
        lower_bound = guess
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
