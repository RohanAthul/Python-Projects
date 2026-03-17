# 🕵️ Blind Auction, Python program

This project is a simple command-line implementation of a Blind Auction system written in Python. The program allows multiple participants to submit their bids privately, and once all bidders have entered their offers, the program determines and announces the highest bidder.

The project focuses on practicing fundamental Python concepts such as functions, dictionaries, loops, sorting, and user input handling. To improve the user experience, an ASCII art logo is displayed when the program starts.

## ⚙️ How the Auction Works

- Bidder Registration: Each participant enters their name and bid amount.

- Private Bidding: After a bid is entered, the screen is cleared to hide previous bids from the next participant.

- Multiple Participants: The program continues accepting bids as long as there are more bidders.

- Bid Storage: All bids are stored in a Python dictionary where the bidder’s name is the key and their bid amount is the value.

- Winner Determination: When bidding ends, the program sorts the bids and identifies the participant with the highest offer.

## 🚀 How to Run the Tool

Ensure Python 3.x is installed on your system. Make sure the following files are present in the same directory:

- main.py (or your main script file)

- art.py

### Linux / MacOS Execution

- Open your terminal.

- Navigate to the directory:

    - cd path/to/your/script

- Run the script:

    - python3 main.py

### Windows Execution

- Open PowerShell.

- Navigate to the directory:

    - cd path\to\your\script

- Run the script:

    - python main.py

💡 Follow the on-screen prompts to enter bidder names and their bid amounts.

## 📂 Project Structure
```
blind-auction/
├── main.py            # Main auction logic and bidding loop
├── art.py             # Contains the ASCII logo displayed at startup
└── README.md          # Project documentation
```
## 🧩 Key Modules and Files

- art.py:
Contains the ASCII art logo that is printed when the program starts, providing a visual introduction to the application.

- main.py:
The core script responsible for collecting bids, storing bidder data in a dictionary, and determining the winner once all participants have submitted their bids.

## 🧠 Logic Summary

- Initialization:
The program begins by displaying an ASCII logo and initializing an empty dictionary (all_bidders) to store bidder names and their corresponding bid amounts.

- Bid Collection Function:
The blind_auction_input() function collects the bidder's name and bid amount from user input and stores it inside the dictionary.

- Bidding Loop:
A while loop keeps the auction active as long as there are additional bidders. After each bid, the program asks whether another participant would like to place a bid.

- Screen Clearing:
If another bidder is present, the program prints multiple blank lines to hide the previous bid information.

- Winner Calculation:
Once bidding ends, the dictionary is sorted using the bid amounts as the sorting key. The first element of the sorted list represents the highest bidder.

- Result Announcement:
The program prints the winner’s name along with their winning bid amount.

## 🎯 Learning Objectives

✅ Creating and calling functions to organize code  

✅ Using Python dictionaries to store structured data  

✅ Implementing while loops for repeated program execution  

✅ Sorting dictionary data using sorted() and custom keys  

✅ Handling and standardizing user input  

✅ Basic command-line interface (CLI) interaction  
