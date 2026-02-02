"""
Welcome to my Hangman game!
    Please go through the code and the comments and don't hesitate to tell me your thoughts
    I have tried to include comments whereever possible
"""

# Import necessary modules
import random
import hangman_words
from hangman_art import stages, logo

# Loading word list and setting lives to 6
word_list = hangman_words.word_list
lives = 6

# Loading welcome logo
print(logo)

# Choosing random word
chosen_word = random.choice(word_list)

# Showing the user the initial placeholder
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Game state and list of correct guesses made by the user
game_over = False
correct_letters = []

# Starting game session
while not game_over:

    # The number of lives the user has left and the input statement for letters
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # Checking if the user has already guessed a letter
    if guess in correct_letters:
        print(f"You've already guessed the letter {guess}")


    display = ""

    # Main loop
        # if guess is correct then use it to form a string and add it to correct letters list
        # fill in _ for the rest of the letters in the string
        # Each time the loop runs it will create a string with a correct guess,
            # correct letters in the list and fill _ for any remaining characters
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    # If user makes a wrong guess, print statement and reduce lives by 1
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True

            # End game - User lose statement
            print(f"***********************The Correct word was {chosen_word}! you lost. **********************")

    # End game - User win statement
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Printing Hangman art
    print(stages[lives])
