# Treasure Island Game

An interactive, text-based adventure game written in Python. It challenges the player to navigate through a series of dangerous scenarios by making the correct choices to find the hidden treasure.

## Description

Classic example of control flow programming, utilizing nested conditional statements to create a branching narrative where every choice matters and is designed to demonstrate:

- User input handling (input()).

- String manipulation and normalization (.lower()).

- Nested logic structures (if, elif, else).

## Game Logic & Flow

The game operates on a "Three-Stage" survival structure. The player must pass all three stages consecutively to win. A wrong move at any stage results in an immediate "Game Over."
The Decision Tree

- Stage 1: The Crossroad

    - Input: left or right

    - Right: Game Over (Fell into a hole).

    - Left: Proceed to Stage 2 (The Lake).

- Stage 2: The Lake

    - Input: swim or wait

    - Swim: Game Over (Attacked by trout).

    - Wait: Proceed to Stage 3 (The House).

- Stage 3: The House (3 Doors)

    - Input: red, blue, or yellow

    - Red: Game Over (Burned by fire).

    - Blue: Game Over (Eaten by beasts).

    - Yellow: WIN (You found the treasure!)

    - Other: Game Over (Invalid Input).

## Prerequisites

- Python 3.x installed on your machine.

- A terminal or command-line interface.

## How to Run

- Save the file TreasureIsland.py

- Open your Terminal:

    - Windows: Search for "cmd" or "PowerShell".

    - Mac/Linux: Open "Terminal".

- Navigate to the file location: Use the cd command to go to the folder where you saved the file.
    

- Execute the script: Run one of the following commands:

    - "python TreasureIsland.py" OR "python3 TreasureIsland.py"

