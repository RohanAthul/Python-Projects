# Number Guessing Game

A simple command-line number guessing game written in Python. The system picks a random number between 1 and 100, and the player has to guess it within a limited number of attempts based on the chosen difficulty.

**Note** - Except for debugging one function, all this code has been written without AI help.

## How It Works

1. On launch, the game displays a logo and welcome message.
2. The player selects a difficulty:
   - **Easy** — 10 attempts
   - **Hard** — 5 attempts
3. The game generates a random number between 1 and 100.
4. The player repeatedly guesses the number. After each guess, the game responds with:
   - `Too low` — if the guess is below the target number
   - `Too high` — if the guess is above the target number
   - A success message — if the guess is correct
5. The game ends when the player guesses correctly or runs out of attempts.
6. After each game, the player is asked whether they want to play again (`yes`/`no`).

## Requirements

- Python 3.x
- A local `art.py` module that defines a `logo` variable (ASCII art displayed at startup)

## File Structure

```
.
├── main.py      # Game logic (the script described in this README)
└── art.py       # Contains the `logo` ASCII art string
```

## Usage

Run the script from the terminal:

```bash
python main.py
```

Follow the on-screen prompts to choose a difficulty and enter your guesses.

## Function Reference

### `random_number()`
Generates and returns a random integer between 1 and 100 (inclusive).

### `check_guess(guess, rand_int)`
Compares the player's guess against the target number.
- Prints `Too low` and returns `False` if the guess is too low.
- Prints `Too high` and returns `False` if the guess is too high.
- Returns `True` if the guess matches the target number.

### `valid_guess()`
Prompts the user for input and ensures it is a valid whole number. Re-prompts on invalid (non-integer) input.

### `play_game()`
Runs the main game loop:
- Asks the player to choose a difficulty (`easy` or `hard`).
- Sets the number of attempts accordingly.
- Generates a random target number.
- Loops, accepting guesses and providing feedback, until the player wins or runs out of attempts.
- Prints a win or loss message at the end.

## Game Flow (Replay Loop)

After the first game finishes, the script asks the player if they'd like to play again. This loop continues, replaying the game, until the player types `no`. The program then prints a farewell message and exits.

## Notes / Potential Improvements

- Input validation for difficulty and replay prompts only accepts `easy`/`hard` and `yes`/`no` (case-insensitive, whitespace-trimmed).
- There is a minor typo in the in-game message ("Thread carefully" — likely intended to be "Tread carefully").
- The `art` module is a required dependency; the script will fail to run without it.
