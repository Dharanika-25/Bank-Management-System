from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount


class Bank:

    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def generate_account_number(self):
        while str(self.next_account_number) in self.accounts:
            self.next_account_number += 1

        account_number = str(self.next_account_number)
        self.next_account_number += 1
        return account_number

    def create_account(self):
        print("\n========== CREATE ACCOUNT ==========")

        name = input("Enter Account Holder Name: ").strip()

        if not name:
            print("\nAccount holder name cannot be empty.")
            return

        account_number = self.generate_account_number()

        while True:
            print("\n1. Savings Account")
            print("2. Current Account")

            choice = input("Select Account Type: ")

            if choice not in ("1", "2"):
                print("\nInvalid account type. Please try again.")
                continue

            try:
                balance = float(input("Enter Initial Deposit: "))
            except ValueError:
                print("\nPlease enter a valid amount.")
                continue

            if balance < 0:
                print("\nInitial deposit cannot be negative.")
                continue

            if choice == "1" and balance < 500:
                print("\nSavings Account requires minimum balance of ₹500. Please try again.")
                continue

            if choice == "1":
                account = SavingsAccount(account_number, name, balance)
            else:
                account = CurrentAccount(account_number, name, balance)

            break

        self.accounts[account_number] = account

        print("\nAccount created successfully!")
        print("Your Account Number is:", account_number)
        print("Please save this number — you'll need it to deposit, withdraw, or check your balance.")

    def find_account(self):
        account_number = input("\nEnter Account Number: ").strip()

        if account_number in self.accounts:
            return self.accounts[account_number]

        print("\nAccount not found.")
        return None

    def deposit_money(self):
        print("\n========== DEPOSIT MONEY ==========")

        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter Deposit Amount: "))
                account.deposit(amount)
            except ValueError:
                print("\nPlease enter a valid amount.")

    def withdraw_money(self):
        print("\n========== WITHDRAW MONEY ==========")

        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter Withdrawal Amount: "))
                account.withdraw(amount)
            except ValueError:
                print("\nPlease enter a valid amount.")

    def balance_inquiry(self):
        print("\n========== BALANCE INQUIRY ==========")

        account = self.find_account()

        if account:
            account.check_balance()

    def view_transaction_history(self):
        print("\n========== TRANSACTION HISTORY ==========")

        account = self.find_account()

        if account:
            account.show_transaction_history()