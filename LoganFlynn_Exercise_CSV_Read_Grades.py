# Read Grades Program For CSV Exercise
# Logan Flynn
# 10/23/2025

import csv

def read_grades_from_csv():
    """Read grades.csv and print data in a formatted table."""
    filename = 'grades.csv'

    # Open the file safely
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Display header
    print("\n{:<15}{:<15}{:<10}{:<10}{:<10}".format(
        "First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"))
    print("-" * 60)

    # Display each student record
    for row in rows[1:]:
        print("{:<15}{:<15}{:<10}{:<10}{:<10}".format(*row))

# Run program
if __name__ == "__main__":
    read_grades_from_csv()
