# Monthly Expense Analyzer
# Logan Flynn
# 09/27/2025

# This program asks the user for their monthly expenses.
# The user enters both the type of expense and the amount.
# Using the reduce() function, the program calculates:
#   1. The total of all expenses
#   2. The highest expense
#   3. The lowest expense

# Import reduce from functools
from functools import reduce


def main():
    # List to store expenses as (type, amount) tuples
    expenses = []

    # Ask for the user input
    print("Enter your expenses.")
    print("Type 'done' when finished.\n")

    # Input Loop
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")

        # If user types exit keyword, break out of loop.
        if expense_type.lower() == "done":
            break

        # Convert input amount to float and store as tuple.
        amount = float(input(f"Enter the amount for {expense_type}: "))
        expenses.append((expense_type, amount))

    # If no expenses entered, just exit program.
    if not expenses:
        print("No expenses entered.")
        return

    # Total expenses calculation using reduce
    total = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # Highest expense
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # Lowest expense
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    # Display results
    print("\n--- Expense Report ---")
    print(f"Total expenses: ${total:.2f}")
    print(f"Highest expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest expense: {lowest[0]} (${lowest[1]:.2f})")


# Run program
if __name__ == "__main__":
    main()
