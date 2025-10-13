# Phone Number, SSN, and Zip code validator
# Logan Flynn
# 10/12/2025

# Import the regular expressions module
import re

# Validation functions
def valid_phone(number):
    """Return True if phone number is valid."""
    pattern = r'^\d{3}-\d{3}-\d{4}$'  # Example: 123-456-7890
    return re.fullmatch(pattern, number) is not None

def valid_ssn(ssn):
    """Return True if SSN is valid."""
    pattern = r'^\d{3}-\d{2}-\d{4}$'  # Example: 123-45-6789
    return re.fullmatch(pattern, ssn) is not None

def valid_zip(zipcode):
    """Return True if ZIP code is valid."""
    pattern = r'^\d{5}(-\d{4})?$'  # Example: 12345 or 12345-6789
    return re.fullmatch(pattern, zipcode) is not None


# Main program
def main():
    """Ask the user for input and validate each field."""
    phone = input("Enter a phone number (123-456-7890): ")
    if valid_phone(phone):
        print("Phone number is valid.")
    else:
        print("Invalid phone number.")

    ssn = input("Enter a Social Security Number (123-45-6789): ")
    if valid_ssn(ssn):
        print("Social Security Number is valid.")
    else:
        print("Invalid Social Security Number.")

    zipcode = input("Enter a ZIP code (12345 or 12345-6789): ")
    if valid_zip(zipcode):
        print("ZIP code is valid.")
    else:
        print("Invalid ZIP code.")

# Program entry point
if __name__ == "__main__":
    main()

