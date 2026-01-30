# 2: Write a Python program to implement a class named BankAccount with the following
# requirements:
# •
# •
# The class should contain two instance variables:
# ◦Name (Account holder name)
# ◦Amount (Account balance)
# The class should contain one class variable:
# ◦ ROI (Rate of Interest), initialized to 10.5
# •De ne a constructor (__init__) that accepts Name and initial Amount.
# •Implement the following instance methods:
# Display() – displays account holder name and current balance
# ◦Deposit() – accepts an amount from the user and adds it to balance
# ◦Withdraw() – accepts an amount from the user and subtracts it from balance
# (Ensure withdrawal is allowed only if suf cient balance exists)
# ◦
# •
# CalculateInterest() – calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5  # Class variable for Rate of Interest

    def __init__(self, Name, Amount):
        self.Name = Name  # Instance variable for account holder name
        self.Amount = Amount  # Instance variable for account balance

    def Display(self):
        # Display account holder name and current balance
        print(f"Account Holder: {self.Name}, Current Balance: {self.Amount}")

    def Deposit(self, amount):
        # Add the deposited amount to the balance
        self.Amount = self.Amount + amount
        print(f"Deposited: {amount}. New Balance: {self.Amount}")

    def Withdraw(self, amount):
        # Subtract the withdrawn amount from the balance if sufficient funds exist
        if amount <= self.Amount:
            self.Amount = self.Amount - amount
            print(f"Withdrew: {amount}. New Balance: {self.Amount}")
        else:
            print("Insufficient balance for withdrawal.")

    def CalculateInterest(self):
        # Calculate and return interest based on the current balance and ROI
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest
    
# Create instances of BankAccount and demonstrate all methods
account1 = BankAccount("Alice", 1000)
account1.Display()  # Output: Account Holder: Alice, Current Balance: 1000
account1.Deposit(500)  # Output: Deposited: 500. New Balance: 1500
account1.Withdraw(200)  # Output: Withdrew: 200. New Balance: 1300
print(f"Interest: {account1.CalculateInterest()}")  # Output: Interest: 136.5
account2 = BankAccount("Bob", 2000)
account2.Display()  # Output: Account Holder: Bob, Current Balance: 2000
account2.Withdraw(2500)  # Output: Insufficient balance for withdrawal.
account2.Deposit(1000)  # Output: Deposited: 1000. New Balance: 3000
print(f"Interest: {account2.CalculateInterest()}")  # Output: Interest: 315.0