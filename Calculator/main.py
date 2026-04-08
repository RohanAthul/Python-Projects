# Welcome to my Calculator program!
import art
print(art.logo)

# Functions
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Dictionary
arithmetic_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    preserve_state = True
    first_number = int(input("What is the first number boss? "))
    for key in arithmetic_operations:
        print(key)

    while preserve_state:
        operation = input("Please pick an operation: ")
        next_number = int(input("What is the next number please? "))
        result = arithmetic_operations[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        continue_status = input(
            f"Type 'y' to continue calculating with {result} \nor type 'n' to start a new calculation ").lower()

        if continue_status == "y":
            first_number = result
        else:
            preserve_state = False
            print("\n" * 35)
            calculator()


calculator()
