# 🧮 Python Calculator Program
## 📌 Project Overview

This is a simple command-line calculator built using Python.
The program allows users to perform basic arithmetic operations and continue calculations using previous results.

This project demonstrates:

- Functions
- Dictionaries
- Loops
- User input handling
Program state management
Recursion (restart calculator)
## ⚙️ Features
- Addition
- Subtraction
- Multiplication
- Division
- Continue calculations with previous result
- Restart calculator anytime
- Clean CLI interface
## 📂 Project Structure
```
calculator.py
README.md
art.py (contains ASCII logo)
```
## 🧰 Requirements

This project uses:

Python 3.x
art.py file (for calculator logo)

## 🚀 How to Run
Clone the repository
git clone https://github.com/yourusername/calculator-project.git
Navigate to project folder
cd calculator-project
Run the program
python calculator.py
## 🧠 How It Works
```
Step 1: Choose first number
What is the first number boss?
Step 2: Select operation
+
-
*
/
Step 3: Enter next number
Step 4: View result

Example:

5 + 3 = 8  

Step 5: Continue or restart
Type 'y' to continue calculating
Type 'n' to start new calculation
```
## 🏗️ Code Highlights
Dictionary-Based Operations

Instead of using multiple if/else statements, the program uses a dictionary:
```
arithmetic_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
```
This makes the code:

- Cleaner
- More scalable
- Easier to extend
## 🔁 Continuous Calculation Logic

The program allows chaining operations:

Example:

5 + 5 = 10  

10 * 2 = 20  

20 - 5 = 15
## 📈 Future Improvements
- Add exponent operation
- Add modulus operation
- Add decimal number support
- Add GUI (Tkinter / Streamlit)
- Add error handling (division by zero)

## 👤 Author

Athul Rohan AR

## 📄 License

This project is for learning and educational purposes.