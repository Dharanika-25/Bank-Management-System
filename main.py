from bank import Bank


def main():
    bank = Bank()

    while True:
        print("\n======================================")
        print("       BANK MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Balance Inquiry")
        print("5. Transaction History")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_money()
        elif choice == "3":
            bank.withdraw_money()
        elif choice == "4":
            bank.balance_inquiry()
        elif choice == "5":
            bank.view_transaction_history()
        elif choice == "6":
            print("\nThank you for using Bank Management System!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()