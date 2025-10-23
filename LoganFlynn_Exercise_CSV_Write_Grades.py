# Write Grades Program For CSV Exercise
# Logan Flynn
# 10/23/2025

import csv

def write_grades_to_csv():
    """Prompt user for student data and write it to grades.csv."""
    filename = 'grades.csv'

    # Open file using context manager (as recommended by Overland)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Get the number of students
        num_students = int(input("Enter the number of students: "))

        # Loop through and gather data
        for i in range(num_students):
            print(f"\n--- Student {i + 1} ---")
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the student record
            writer.writerow([first, last, exam1, exam2, exam3])

    print(f"\nAll records saved successfully in {filename}.")

# Main section — Overland stresses clean main function use
if __name__ == "__main__":
    write_grades_to_csv()
