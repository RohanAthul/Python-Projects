print(
    "Welcome to Treasure Island.\n"
    "Your mission is to find the treasure.\n"
    "You're at a cross road. Where do you want to go?"
)

#Step 1
step_1 = input(
"Type \"left\" or \"right\"`?\n"
).lower() # Main input of Step 1

print(step_1)

if step_1 == "left":
    print(
        "You've come to a lake. There is an island in the middle of the lake."
    )
    # Step 2
    step_2 = input(
        "Type \"wait\" to wait for a boat or \"swim\" to swim across\n"
    ).lower()  # Main input of Step 2

    if step_2 == "wait":
        print("A mysterious boat arrives and it magically ferries you to the other side")

        # Step 3
        step_3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors.\n"
            "One \"red\", one \"yellow\" and one \"blue\".\n"
            "Which colour do you choose?\n"
        ).lower()
        if step_3 == "yellow":
            print("You Win the treasure!")
        elif step_3 == "red":
            print("Burned by fire\nGame Over")
        elif step_3 == "blue":
            print("Eaten by beasts\nGame Over")
        else:
            print("Invalid input\nGame Over")

    elif step_2 == "swim":
        print("Attacked by trout.\nGame Over")

    else:
        print("Invalid input.\nGame Over")

elif step_1 == "right":
    print("You fell into a hole\nGame Over")
else:
    print("Invalid input\nGame Over")
