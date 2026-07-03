MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Dictionary for coins
coin_dict = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

# List of buttons available on machine
machine_buttons = ["espresso","latte","cappuccino","report","shutdown"]

def machine_report(resources):
    """
    Prints report of current resources inside machine
    """
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def get_user_order(machine_buttons):
    """
    Function to give machine only valid input
    """
    while (usr_input := input(f"What would you like to order?\nButtons:{machine_buttons}:").lower().strip()) not in machine_buttons:
        print("Please enter a valid input")
    return usr_input

def check_sufficient_resources():
    """
    Checks if system has sufficient resources
    """
    
    required_water = MENU[user_input]["ingredients"]["water"]
    required_milk = MENU[user_input]["ingredients"]["milk"]
    required_coffee = MENU[user_input]["ingredients"]["coffee"]

    if not (resources["water"] - required_water) < 0:
        if not resources["milk"] - required_milk < 0:
            if not resources["coffee"] - required_coffee < 0:
                return True
            else:
                print("Sorry, we do not have enough Coffee beans")
                return False
        else:
            print("Sorry, we do not have enough Milk")
            return False
    else:
        print("Sorry, we do not have enough water")
        return False

def get_valid_int(prompt):
    """
    Get valid number from user

    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def process_coins(coin_dict):
    quarters_count = get_valid_int("How many quarters?: ")
    dimes_count = get_valid_int("How many dimes?: ")
    nickles_count = get_valid_int("How many nickles?: ")
    pennies_count = get_valid_int("How many pennies?: ")

    total_sum = (
        (coin_dict["quarter"] * quarters_count) + 
        (coin_dict["dime"] * dimes_count) + 
        (coin_dict["nickel"] * nickles_count) + 
        (coin_dict["penny"] * pennies_count)
    )

    return total_sum

def output_coffee(func_input):
        check_inventory = check_sufficient_resources() # checking for enough milk, water, coffee
        
        if check_inventory:
            print(f"We have enough resources for an {func_input}")
            user_payment = process_coins(coin_dict)
        
            if (user_payment) >= (MENU[func_input]["cost"]):
                change = round((user_payment) - (MENU[func_input]["cost"]),2)

                print(f"The money is sufficient")
                print(f"Here is your change: ${change}")

                resources["money"] += MENU[func_input]["cost"]
                
                resources["water"] -= MENU[func_input]["ingredients"]["water"]
                resources["milk"] -= MENU[func_input]["ingredients"]["milk"]
                resources["coffee"] -= MENU[func_input]["ingredients"]["coffee"]

                print(f"Here is your {func_input}, Have a good day!")
            else:
                print(f"Insufficient funds for {func_input}, returning money")

while True:
    user_input = get_user_order(machine_buttons)
    # user_input = "espresso" # Remove Testing code input

    if user_input == "report":
        machine_report(resources)

    elif user_input == "espresso":
        output_coffee(user_input)

    elif user_input == "latte":
        output_coffee(user_input)
        
    elif user_input == "cappuccino":
        output_coffee(user_input)

    elif user_input == "shutdown":
        print("Thank you for using my services, Vielen Dank!")
        break
    
    else:
        print("please enter valid input")
        get_user_order(machine_buttons)
