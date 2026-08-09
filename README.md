# Bank Management System

A console-based Bank Management System in Python, organized by class into separate modules for clarity and maintainability.

## Project Structure
```
bank-management-system/
├── models/
│   ├── __init__.py
│   ├── bank_account.py       # BankAccount (base class)
│   ├── savings_account.py    # SavingsAccount (inherits BankAccount)
│   └── current_account.py    # CurrentAccount (inherits BankAccount)
├── bank.py                   # Bank (manages all accounts, menu actions)
├── main.py                   # Entry point — run this file
├── README.md
└── .gitignore
```

## Features
- Create Savings Account (min balance ₹500) or Current Account
- Deposit and withdraw money with validation
- Balance inquiry
- Transaction history with timestamps

## Run it
```bash
python main.py
```

## Requirements
- Python 3.x (standard library only)