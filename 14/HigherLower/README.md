# Higher Lower Game

A command-line "Higher or Lower" comparison game written in Python. The game presents two random items (e.g., social media accounts) from a dataset and asks the player to guess which one has more Instagram followers. The player's streak continues until they guess incorrectly.

## How It Works

1. On launch, the game selects two different random entries from the dataset.
2. The game displays a logo, then shows both selections as human-readable descriptions (name, description, and country) labeled "Compare A" and "Compare B", separated by a "vs" graphic.
3. The player guesses which entry (`A` or `B`) has more Instagram followers.
4. The game checks the guess against the actual follower counts:
   - **Correct guess** — Score increases by 1, the screen "clears" (via blank lines), Selection B becomes the new Selection A, and a new random Selection B is picked.
   - **Incorrect guess** — The game ends, and the final score is displayed.
5. The loop repeats until the player guesses incorrectly.

## Requirements

- Python 3.8+ (uses the walrus operator `:=`)
- A local `art.py` module that defines `logo` and `vs` variables (ASCII art)
- A local `game_data.py` module that defines a `data` list of dictionaries

## File Structure

```
.
├── main.py        # Game logic (the script described in this README)
├── art.py         # Contains the `logo` and `vs` ASCII art strings
└── game_data.py    # Contains the `data` list of comparison items
```

## Data Format

Each item in `game_data.data` is expected to be a dictionary with at least the following keys:

```python
{
    "name": "Example Account",
    "description": "short description of the account",
    "country": "Country Name",
    "follower_count": 1000000
}
```

## Usage

Run the script from the terminal:

```bash
python main.py
```

Follow the on-screen prompts and enter `A` or `B` to make your guess.

## Function Reference

### `random_selection()`
Picks and returns a single random item (dictionary) from `game_data.data`.

### `print_selected_block(selected_data)`
Formats a selected data dictionary into a human-readable sentence in the form:
`"{name}, a {description}, from {country}"`.

### `check_which_selection_greater(sel_1, sel_2)`
Compares the `follower_count` of two selections.
- Returns `"a"` if `sel_1` has more followers.
- Returns `"b"` if `sel_2` has more followers.
- Returns `None` if the counts are equal.

## Game Flow (Main Loop)

- Two distinct random selections are picked before the loop starts (a `while` loop re-rolls Selection B until it differs from Selection A).
- On each iteration, the correct answer is computed *before* being revealed, the logo and both selections are printed, and the player is prompted for a guess.
- Input is validated in a loop, only accepting `'a'` or `'b'` (case-insensitive, whitespace-trimmed); any other input re-prompts with an error message.
- On a correct guess, the game "shifts" — the previously unknown item (Selection B) becomes the new known item (Selection A) — mimicking the classic Higher/Lower game format, and a fresh Selection B is drawn.
- On an incorrect guess, the loop breaks and the final score is printed.

## Notes / Potential Improvements

- If `check_which_selection_greater` returns `None` (a tie in `follower_count`), no user input will ever match it, so the player will always lose on a tie — this edge case isn't explicitly handled or communicated to the player.
- The screen "clear" between rounds is simulated with 20 newline characters (`print("\n" * 20)`) rather than a true terminal clear.
- `selection_1 = selection_2.copy()` assumes `selection_2` is a `dict` (or another object supporting `.copy()`); this works with the expected data format but isn't defensively checked.
- The `art` and `game_data` modules are required dependencies; the script will fail to run without them.
- There is no replay loop — once the game ends, the script simply exits (unlike games that ask "play again?").
