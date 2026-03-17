from art import logo
print(logo)

all_bidders = {}
other_bidders = True

def blind_auction_input():
    name = input("What is your name?\n")
    amount = int(input("What is your bid amount (in Euros)?\n"))
    all_bidders[name] = amount

while other_bidders:
    blind_auction_input()
    want_to_loop = input("Are there other bidders?\nIf yes type 'yes' and if no type 'no'\n").lower()

    if want_to_loop == "yes":
        print("\n" * 100)
    elif want_to_loop == "no":
        other_bidders = False
        highest_bidder = sorted(
            all_bidders,
            key = all_bidders.get,
            reverse = True
        )[0]
        print(f"The winner is {highest_bidder} with a bid of €{all_bidders[highest_bidder]}")
    else:
        other_bidders = True
        print("\n" * 100)
        print("Please type either Yes or No")
