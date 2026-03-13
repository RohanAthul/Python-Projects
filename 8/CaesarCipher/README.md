# 🔐 Caesar Cipher CLI (Python)
This project is a simple command-line implementation of the classic Caesar Cipher cryptography technique written in Python. The program allows users to securely encode secret messages or decode them back into plain text by shifting the alphabet by a user-defined number. Visual feedback is provided using ASCII art upon launching the tool.

The tool is designed for beginners and focuses on core Python concepts such as defining functions, loops, string manipulation, modulo arithmetic, and handling user input.

## ⚙️ How the Cipher Works
- Mode Selection: The user chooses to either encode (encrypt) a new message or decode (decrypt) an existing secret.

- Text Input: The user provides the string of text they wish to process.

- Shift Amount: The user enters an integer defining how many positions each letter should shift down the alphabet.

- Character Preservation: Non-alphabetical characters (spaces, numbers, punctuation) are ignored by the cipher and kept in their original positions.

- Wrap-Around Safety: The cipher uses modulo arithmetic to seamlessly loop back to the start of the alphabet (e.g., shifting 'z' forward by 1 becomes 'a').

## 🚀 How to Run the Tool
Ensure Python 3.x is installed on your system. Make sure the following files are present in the same directory:

- main.py (or the name of your main script)

- art.py

### Linux / MacOS Execution
- Open your terminal.

- Navigate to the directory:

    - cd path/to/your/script

- Run the script:

    - python3 main.py

### Windows Execution
- Open PowerShell

- Navigate to the directory:

    - cd path\to\your\script
- Run the script:

    - python main.py  
- *💡 Follow the on-screen prompts to input your text, shift number, and mode.*

## 📂 Project Structure

```
caesar-cipher/
├── main.py            # Main cipher logic and user loop
├── art.py             # Contains the ASCII logo
└── README.md          # Project documentation
```

### 🧩 Key Modules and Files
- art.py: A custom module that contains the ASCII art logo displayed when the program boots up.

- main.py: The core script containing the alphabet list, the shift logic, and the interactive user prompts.

## 🧠 Logic Summary
- Initialization: The script loads an ASCII logo and defines a list containing the 26 lowercase letters of the alphabet.

- Core Function: The caesar() function accepts the text, shift amount, and direction. If decoding, it multiplies the shift by -1 to reverse the process.

- Index Math: It uses .index() to find a letter's current position, adds the shift, and uses the modulo operator (%) to prevent "out of range" errors if the shift exceeds 26.

- Filtering: The .isalpha() method ensures that only letters are shifted, instantly appending spaces or symbols directly to the output.

- Program Loop: A while loop keeps the application running, allowing the user to encode or decode multiple messages without restarting the script.

## 🎯 Learning Objectives
✅ Creating and calling functions with multiple parameters

✅ Modulo arithmetic for index wrapping

✅ String manipulation and character checking (.isalpha())

✅ while loops for continuous program execution

✅ Handling and standardizing user input (.lower())


Thank you for taking the time to go through my program!