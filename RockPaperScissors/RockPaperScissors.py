"""
Welcome to my Rock Paper Scissors Game!
"""

# Import Necessary Libraries
import random

# Main variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Assigning to List
rock_paper_scissors_list = [rock, paper, scissors]

# Random integer generator
random_integer = random.randint(0,2)

# Title
print("Welcome to my Rock Paper Scissors Game!")

# Output statements
draw_statement = "It's a draw"
lose_statement = "Schade :( \nYou lose"
win_statement = "Yay! \nYou Win!"
error_statement = "Was this supposed to happen???!"

# Input - Will only accept integers 0,1,2
my_selection = int(input("What do you choose?\n"
      "Type 0 for Rock, 1 for paper and 2 for scissors\n"))

# My selection - Rock
if my_selection == 0:
    print("You chose:")
    print(rock_paper_scissors_list[my_selection])
    print("Computer chose:")
    computer_selection = rock_paper_scissors_list[random_integer]
    print(computer_selection)

# My selection - Paper
elif my_selection == 1:
    print("You chose:")
    print(rock_paper_scissors_list[my_selection])
    print("Computer chose:")
    computer_selection = rock_paper_scissors_list[random_integer]
    print(computer_selection)

# My selection - Scissors
elif my_selection == 2:
    print("You chose:")
    print(rock_paper_scissors_list[my_selection])
    print("Computer chose:")
    computer_selection = rock_paper_scissors_list[random_integer]
    print(computer_selection)

# My selection - Invalid input
else:
    print("Wrong input, but that's okay we all make mistakes sometimes :)")

# -- Outcome - Draw Scenario
if random_integer == my_selection:
    print(draw_statement)

# -- Outcome - Lose Scenario
elif my_selection == 0 and random_integer == 1:
    print(lose_statement)
elif my_selection == 1 and random_integer == 2:
    print(lose_statement)
elif my_selection == 2 and random_integer == 0:
    print(lose_statement)

# -- Outcome - Win Scenario
elif my_selection == 0 and random_integer == 2:
    print(win_statement)
elif my_selection == 1 and random_integer == 0:
    print(win_statement)
elif my_selection == 2 and random_integer == 1:
    print(win_statement)

# -- Outcome - Invalid input
else:
    print("Game over")
