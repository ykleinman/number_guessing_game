# Step-10: Add the game art
from art import logo
print(logo)
# Step-1: Greet the user with "Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100."


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

# Step-2: Generate a random number between 1 to 100
import random
random_number = random.randint(1, 101)      # GLOBAL
# print(f"Pssst, the correct answer is {random_number}")

# Step-11: Choose a difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Invalid input. Choose between 'easy' and 'hard'")
# Step-3: Create a varible for the number of attempts


game_on = True
while game_on:
    
    # Step-4: Print the number of attempts that the user has left
    print(f"You have {attempts} attempts remaining to guess the number.")
    # Step-5: Prompt the user to guess a number
    user_guess = int(input("Make a guess: "))

    # Step-6: If the number is too high, print 'Too high. Guess again' separated by a different line
    if user_guess > random_number:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
    # Step-7: If the number is too low, print 'Too low. Guess again' separated by a different line
    elif user_guess < random_number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
    elif user_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        game_on = False

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_on = False


# Step-8: If the user loses, write "You've run out of guesses, you lose."

# Step-9: If the user wins, write "You've guessed the right number"


