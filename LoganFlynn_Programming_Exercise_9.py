# Bank Account Class Example
# Logan Flynn
# 11/02/2025

class BankAcct:

    def __init__(self, name, acct_num, amount=0.0, interest_rate=0.02):
        self.name = name
        self.acct_num = acct_num
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount

    def adjust_interest_rate(self, new_rate):
        """Change the interest rate."""
        if new_rate >= 0:
            self.interest_rate = new_rate
        else:
            print("Interest rate must be non-negative.")

    def calculate_interest(self, days):
        """Calculate interest based on the number of days."""
        # Simple interest formula: A = P * r * (t/365)
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    def get_balance(self):
        """Return the current balance."""
        return self.amount

    def __str__(self):
        """String representation of the account."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: ${self.amount:,.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")


def test_bank_acct():
    """Test function to verify BankAcct methods."""
    # Create a bank account
    acct = BankAcct("Logan Flynn", 1001, 1500.00, 0.03)
    print("Initial Account Details:")
    print(acct, "\n")

    # Deposit money
    acct.deposit(500)
    print("After deposit of $500:")
    print(acct, "\n")

    # Withdraw money
    acct.withdraw(200)
    print("After withdrawal of $200:")
    print(acct, "\n")

    # Adjust interest rate
    acct.adjust_interest_rate(0.05)
    print("After changing interest rate to 5%:")
    print(acct, "\n")

    # Calculate interest for 30 days
    interest = acct.calculate_interest(30)
    print(f"Interest earned in 30 days: ${interest:,.2f}\n")

    # Show final balance
    print("Final Account Summary:")
    print(acct)


# Run the test when file is executed directly
if __name__ == "__main__":
    test_bank_acct()
