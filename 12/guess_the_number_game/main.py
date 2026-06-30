from art import logo
import random

print(logo)
print("Welcome to the Number guessing game!")

# Functions
def random_number():
    """
    Generates a random number between 1 and 100 (inclusive)
    """
    random_num = int(random.choice(range(1,101)))
    return random_num

def check_guess(guess,rand_int):
    """
    Checks if the number in the function is greater or less than the guess
    """
    if guess < rand_int:
        print("Too low")
        return False
    elif guess > rand_int:
        print("Too high")
        return False
    else:
        return True

def valid_guess():
    while True:
        try:
            return int(input("What is your guess?\n"))
        except ValueError:
            print("Please enter a whole number")

def play_game():
    """
    Main Game loop

    User inputs difficulty - if Easy then 10 attempts, if Hard 5 attempts
    System creates a random number from prev defined function
    System loops till user makes correct guess or number of tries is 0
    """
    # Select difficulty setting
    difficulty_options = ['easy','hard']
    while (difficulty := (input("Choose a difficulty. Type 'easy' or 'hard':\n").lower().strip())) not in difficulty_options:
        print("please enter a valid option")

    # Setting difficulty setting outcome
    if difficulty == "easy":
        number_of_tries = 10
        print(f"Your number of tries is: {number_of_tries}")
    if difficulty == "hard":
        number_of_tries = 5
        print(f"Your number of tries is: {number_of_tries}")
    
    print("\n" * 20)
    print(f"I'm thinking of a number between 1 and 100, you have {number_of_tries} attempts to guess it.")
      
    # Get random number
    rand_number = random_number()
    
    number_guess = -1
    game_over = False

    # Main game running loop
    while (game_over == False) and not (number_of_tries == 0):
        number_guess = valid_guess()
        game_over = check_guess(number_guess,rand_number)
        if not game_over:
            number_of_tries += -1
            print(f"Thread carefully, you have {number_of_tries} remaining!")
    
    if (game_over == True) and (number_of_tries > 0):
        print(f"Congrats! You guessed the correct number: {rand_number}")
    elif (game_over == False) and (number_of_tries == 0):
        print(f"Sorry, you're out of chances")
        print(f"The random number was {rand_number}")
 
# First attempt
play_game()

# Rerun of the game

while (play_game_again := input("Do you wish to play? Type 'yes' or 'no\n'").lower().strip()) not in ['yes','no']:
    print("please enter a valid option")

while play_game_again == "yes":
    play_game()
    
    while (play_game_again := input("Do you wish to play? Type 'yes' or 'no\n'").lower().strip()) not in ['yes','no']:
        print("please enter a valid option")

print("Thanks for playing!\nCiao")