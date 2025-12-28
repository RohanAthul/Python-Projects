"""
Welcome to the Tip Calculator!
"""

print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill? €\n"))

tip = (float(input("How much tip would you like to give? 10, 12 or 15 ?\n")) / 100) + 1

split_count = int(input("How many people split the bill?\n"))

calculation_formula = total_bill * tip / split_count

amount_per_person = round(calculation_formula,2)

final_result = print(f"Each person would pay: €{amount_per_person}")
