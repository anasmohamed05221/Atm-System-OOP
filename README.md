# ATM System (OOP in Python)

## 📖 Overview
This project simulates an **ATM system** using Object-Oriented Programming in Python.  
It includes features such as:
- Withdraw
- Deposit
- Balance Inquiry
- View Transactions
- Change PIN
- Transfer Between Accounts

The project is modular with classes like `Bank`, `Customer`, `Account`, `Card`, `AtmInterface`, and handler classes for transactions.  
Unit tests are written using **pytest** to ensure correctness.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AtmSystemOOP.git
   cd AtmSystemOOP
   
2. Run the ATM program:
    python main.py

---

## 🧪 Running Tests

We use pytest for testing. 
To run tests write this in terminal:
    pytest

Expected output:
    collected 13 items
    .............   [100%]

---


## 📂 Project Structure
    
    AtmSystemOOP/
    ├── Account.py
    ├── AtmInterface.py
    ├── Authenticator.py
    ├── Bank.py
    ├── Card.py
    ├── CardReader.py
    ├── Customer.py
    ├── Handlers.py
    ├── Keypad.py
    ├── Screen.py
    ├── Transactions.py
    ├── main.py
    ├── test_all.py
    ├── README.md
    └── requirements.txt

---

## ⚙️ Requirements
    Python 3.10+

    pytest (for running tests)
    
    Install dependencies:
        pip install -r requirements.txt

---

## ✨ Example Workflow

    1. Insert card
    2. Enter PIN
    
    3. Choose from ATM menu:
        -Withdraw money
        -Deposit money
        -View balance
        -Transfer funds
        -Change PIN
        -Exit

---

## 👨‍💻 Author

Developed by Anas Mohamed
Computer Science student @ AAST (Arab Academy for Science, Technology & Maritime Transport).

