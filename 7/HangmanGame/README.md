# Hangman Game (Python)

This project is a simple command-line implementation of the classic Hangman game written in Python. The program randomly selects a word from a predefined word list, and the player must guess the word one letter at a time before running out of lives. Visual feedback is provided using ASCII art to represent the hangman’s state as the player makes incorrect guesses.

The game is designed for beginners and focuses on core Python concepts such as loops, conditionals, lists, string manipulation, and module imports.

## How the Game Works

- The player starts with 6 lives and a random word is selected from a predefined word list

- A placeholder is generated with underscores (_) for unguessed letters.

- The player guesses one letter at a time; correct guesses reveal the letter(s) in the word.

- Incorrect guesses reduce the number of lives.

#### The game ends when:

- The player correctly guesses all letters (win), or

- The player runs out of lives (loss).

## How to Run the Game

Ensure Python 3.x is installed on your system.

#### Make sure the following files are present in the same directory:

- app.py

- hangman_words.py

- hangman_art.py

#### Linux/macOS Execution
- Open your terminal.

- Navigate to the directory: cd path/to/your/script

- Run the script:

    - python3 app.py
#### Windows Execution
- Open Command Prompt or PowerShell.

- Navigate to the directory: cd path\to\your\script

- Run the script:

    - python app.py

Follow the on-screen instructions to guess letters.

## Project Structure:
hangman-game

- main.py              **# Main game logic**
- hangman_words.py     **# Contains the word list**
- hangman_art.py       **# Contains ASCII art and logo**
- README.md            **# Project documentation**

## Key Modules and Files

- random
    - Used to randomly select a word from the word list.

- hangman_words.py
    - Contains a list of possible words for the game.

- hangman_art.py
    - Contains the game logo and hangman stages displayed after each guess.

## Game Logic Summary

- The game initializes with a randomly chosen word and a placeholder of underscores.

- A while loop keeps the game running until the player wins or loses.

- Correct guesses are stored and reused to update the displayed word.

- Repeated guesses are detected and reported to the player.

- Lives are reduced for incorrect guesses, and the hangman graphic updates accordingly.

## Learning Objectives

- Use of loops and conditional logic

- List and string manipulation

- Modular Python programming

- User input handling

- Basic game state management