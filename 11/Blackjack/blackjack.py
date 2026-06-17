import random
import art
import copy
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Welcome message
print(art.logo)

deck = copy.copy(cards) * 4
random.shuffle(deck)

# Functions
def deal_card():
    return deck.pop()

game_running = input("Play a game of Blackjack? Y or N?").lower()

while game_running == "y":
    # Initial lists
    user_cards = []
    dealer_cards = []

    # Initial deal
    while len(user_cards) < 2:
        user_cards.append(deal_card())
    while len(dealer_cards) < 2:
        dealer_cards.append(deal_card())

    print(f"Your cards are {user_cards}")
    print(f"Dealer's first card is {dealer_cards[0]}")

    # Sum cards
    sum_user, sum_dealer = sum(user_cards), sum(dealer_cards)
    # print(sum_user)
    # print(sum_dealer)

    # Natural Blackjack test
    if (sum_dealer == 21 or sum_user == 21) and len(user_cards) == 2:
        print(f"Your cards: {user_cards}\nDealer's cards: {dealer_cards}")
        if sum_dealer == 21 and sum_user == 21:
            print("Draw, Both of you have a Blackjack!")

        elif sum_dealer == 21:
            print("The dealer has a Blackjack!")
            
        elif sum_user == 21:
            print("You have a Blackjack!")

        game_running = input("Do you wish to play again? Y or N?").lower()
        continue

    # Player's turn check
    player_turn = True
    while player_turn:
        sum_user = sum(user_cards)

        while sum_user > 21 and 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
            sum_user = sum(user_cards)

        if sum_user >= 21:
            player_turn = False # Forcing system to end if sum over 21
        else:
            one_more_card = input("Do you want another card? Y or N?").lower()
            if one_more_card == "y":
                user_cards.append(deal_card())
                print(f"Your cards: {user_cards}")
            else:
                player_turn = False
    
    # Running sum again
    sum_user = sum(user_cards)
    sum_dealer = sum(dealer_cards)

    if sum_user > 21:
        print("You went over 21, Bust! Dealer wins.")
    else:
        while sum_dealer < 17:
            dealer_cards.append(deal_card())
            while sum_dealer > 21 and 11 in dealer_cards:
                dealer_cards.remove(11)
                dealer_cards.append(1)
            sum_dealer = sum(dealer_cards)
            
            print(f"Dealer current cards {dealer_cards}")
        
        # Checking
        if sum_dealer > 21:
            print("Dealer busted! You win!")
        elif sum_user > sum_dealer:
            print("You win!")
        elif sum_dealer > sum_user:
            print("Dealer wins!")
        else:
            print("It's a push!")


    # Play again message at the end of the game
    game_running = input("Do you wish to play again? Y or N?").lower()

