# Coffee Machine Simulator

A command-line coffee vending machine simulator written in Python. The program models a simple espresso machine that tracks resources (water, milk, coffee beans, and money), accepts coin-based payment, and dispenses one of three drinks based on availability and payment.

## How It Works

1. On launch, the machine enters an infinite loop, prompting the user to select one of the available buttons: `espresso`, `latte`, `cappuccino`, `report`, or `shutdown`.
2. Selecting a drink checks whether the machine has sufficient water, milk, and coffee beans for that recipe.
3. If resources are sufficient, the user is prompted to insert coins (quarters, dimes, nickels, pennies), which are summed into a total payment.
4. If payment covers the drink's cost, change is calculated and returned, resources are deducted, and money is added to the machine's till. Otherwise, the transaction is cancelled.
5. Selecting `report` prints the current resource and money levels without affecting state.
6. Selecting `shutdown` prints a farewell message and exits the loop.

## Requirements

- Python 3.12+ (uses nested double quotes inside f-strings, e.g. `f"{resources["water"]}ml"`)

## File Structure

```
.
└── main.py    # All machine logic (menu, resources, and control loop)
```

## Data Structures

### `MENU`
A dictionary mapping drink names (`espresso`, `latte`, `cappuccino`) to their required `ingredients` (water in ml, milk in ml, coffee in g) and `cost` in dollars.

### `resources`
A dictionary tracking the machine's current supply of `water`, `milk`, `coffee`, and accumulated `money`. Mutated in place as drinks are made.

### `coin_dict`
Maps coin names (`penny`, `nickel`, `dime`, `quarter`) to their dollar values, used to calculate payment totals.

### `machine_buttons`
A list of valid top-level commands the user can enter: `espresso`, `latte`, `cappuccino`, `report`, `shutdown`.

## Function Reference

### `machine_report(resources)`
Prints the current water, milk, coffee, and money levels from the `resources` dictionary.

### `get_user_order(machine_buttons)`
Prompts the user for input in a loop until a valid button name (lowercased, whitespace-trimmed) is entered, then returns it.

### `check_sufficient_resources()`
Checks the globally-scoped `user_input` against `MENU` to determine whether the machine has enough water, milk, and coffee for the requested drink. Prints a specific shortage message (water, then milk, then coffee) and returns `False` on the first insufficient resource found; returns `True` if all three are sufficient.

### `get_valid_int(prompt)`
Prompts the user for a whole number, re-prompting on `ValueError` until valid input is entered.

### `process_coins(coin_dict)`
Prompts the user for counts of quarters, dimes, nickels, and pennies, then returns the total dollar value of coins inserted.

### `output_coffee(func_input)`
Orchestrates a single drink transaction:
- Calls `check_sufficient_resources()` to confirm inventory.
- If sufficient, calls `process_coins()` to collect payment.
- If payment meets or exceeds the drink's cost, calculates and prints change, updates `resources` (adds cost to `money`, deducts ingredients), and prints a confirmation message.
- If payment is insufficient, prints a message and implicitly returns the money (no explicit refund logic needed, since nothing was deducted).

## Main Loop

- Repeatedly calls `get_user_order()` to get a valid button press.
- Dispatches to `machine_report()`, `output_coffee()` (for any of the three drinks), or breaks out on `shutdown`.
- An `else` branch for unrecognized input exists but is effectively unreachable, since `get_user_order()` already guarantees a valid button.

## Notes / Potential Improvements

- `check_sufficient_resources()` and `output_coffee()` rely on the global variable `user_input` / a passed-in `func_input` inconsistently — `check_sufficient_resources()` reads `user_input` from the enclosing scope rather than accepting it as a parameter, which makes the function harder to reuse or test in isolation.
- If resources are insufficient, `output_coffee()` prints nothing further and returns `None` implicitly — there's no explicit "returning money" message in that branch (contrast with the insufficient-funds branch, which does print one).
- Coins are collected via `process_coins()` even before confirming the payment is sufficient elsewhere in the flow, but there's no way to add more coins if the first batch falls short — the transaction simply fails and any inserted coins are not tracked as returned.
- `machine_report(resources)` uses nested double quotes inside an f-string (`f"{resources["water"]}ml"`), which requires Python 3.12+; on earlier versions this raises a `SyntaxError`.
- There's no input validation preventing negative coin counts in `get_valid_int()`, so a user could enter a negative number of coins to reduce or invalidate the total payment.
- The commented-out line `# user_input = "espresso" # Remove Testing code input` suggests leftover debug/testing code that should be removed before shipping.
- There's no persistent storage — all resource and money state resets when the script restarts.
