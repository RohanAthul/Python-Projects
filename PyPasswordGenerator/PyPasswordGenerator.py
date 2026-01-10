"""
Welcome to my PyPassword Generator program!
"""
# Import necessary libraries
import random

# Core lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Title and Input section
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Empty lists
letters_list = []
symbols_list = []
numbers_list = []
password_list = []

# Selecting some random variables from the original list based on the input by the User
## Letters
for letter in letters:
    if len(letters_list) +1 <= nr_letters:
        letters_list.append(random.choice(letters))
## Symbols
for symbol in symbols:
    if len(symbols_list) +1 <= nr_symbols:
        symbols_list.append(random.choice(symbols))
## Numbers
for number in numbers:
    if len(numbers_list) +1 <= nr_numbers:
        numbers_list.append(random.choice(numbers))

# Creating password list
password_list = letters_list + symbols_list + numbers_list

# Password
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your random password is: \n{password}")
