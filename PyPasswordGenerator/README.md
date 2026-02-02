# PyPassword Generator
## Overview
This is a flexible command-line tool designed to generate strong, randomized passwords. This Python script creates unique passwords by combining specific quantities of letters, symbols, and digits based on user preferences.

## Description
This project demonstrates string manipulation and list operations to build a functional security tool.  
It focuses on several core programming pillars:

- **Randomization:** Utilizing the random module (specifically .choice() and .shuffle()) to ensure unpredictability.

- **List Manipulation:** Appending items to lists, concatenating multiple lists together, and converting lists back into strings.

- **Loops:** Using for loops to iterate through data structures to populate the password components.

- **User Input & Type Conversion:** Handling user input via input() and converting string inputs into integers for calculation.

## The Generation Logic
The script follows a four-step process to ensure the password is both customized and random:

- **Collection:** The user inputs the desired count for letters, symbols, and numbers.

- **Selection:** The script randomly selects the specified number of characters from predefined lists of valid characters.

- **Aggregation:** These selections are combined into a single sequence (e.g., all letters, followed by all symbols, followed by all numbers).

- **Shuffling:** The final sequence is logically shuffled to prevent predictable patterns (such as numbers always appearing at the end).

## Running the App
The script is cross-platform and will run on Windows, macOS, and Linux.

#### Linux/macOS Execution

- Open your terminal.

- Navigate to the directory: cd path/to/your/script

-  Run the script:

    - python3 PyPasswordGenerator.py

#### Windows Execution

- Open Command Prompt or PowerShell.

- Navigate to the directory: cd path\to\your\script

- Run the script:

    - python PyPasswordGenerator.py
