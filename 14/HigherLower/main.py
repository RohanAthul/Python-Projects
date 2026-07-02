import art
from game_data import data
import random

# print(art.logo)


# Pick random dict from data
def random_selection():
    """
    Pick random item from data list
    """
    return random.choice(data)


def print_selected_block(selected_data):
    """
    Displays selected data dict entry as a human readable sentence
    """
    return f"{selected_data['name']}, a {selected_data['description']}, from {selected_data['country']}"


def check_which_selection_greater(sel_1, sel_2):
    """
    Checks which selection is greater - outputs a str letter 'a' or 'b'
    """
    if sel_1["follower_count"] > sel_2["follower_count"]:
        return "a"
    elif sel_1["follower_count"] < sel_2["follower_count"]:
        return "b"
    
    return None


# Global vars
score = 0
selection_1 = random_selection()
selection_2 = random_selection()

while selection_2 == selection_1:
    selection_2 = random_selection()

# Game block
while True:
    # Select blocks

    greater_selection_value = check_which_selection_greater(selection_1, selection_2)

    # Print Blocks
    print(art.logo)
    print(f"Compare A: {print_selected_block(selection_1)}")
    print(art.vs)
    print(f"Compare B: {print_selected_block(selection_2)}")

    while (user_guess := input("Who has more instagram followers? 'A' or 'B':  ").lower().strip()) not in ['a', 'b']:
        print("Please enter a valid input")

    if user_guess == greater_selection_value:
        score += 1
        print("You are correct!")
        print("\n" * 20)
        selection_1 = selection_2.copy()
        selection_2 = random_selection()

    else:
        print("Sorry, game over")
        print(f"Your final score is {score}")
        break