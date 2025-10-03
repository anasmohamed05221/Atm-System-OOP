# ========================= Account.py =========================
from Transactions import Transaction
from Card import Card


class Account:
    """
    Represents a bank account with balance, linked card, and transaction history.
    """

    def __init__(self, account_number: str):
        """
        Initialize a new account.

        Args:
            account_number (str): Unique identifier for the account.
        """
        self.account_number = account_number
        self.balance = 0.0
        self.linked_card = None
        self.transaction_history = []

    def add_transaction(self, transaction: Transaction):
        """
        Add a transaction record to the account history.
        """
        self.transaction_history.append(transaction)

    def link_card(self, card: Card):
        """
        Link a card to this account.
        """
        self.linked_card = card

    def display_transactions(self):
        """
        Display all transactions linked to this account.
        """
        if not self.transaction_history:
            print("No transactions available")
            return
        print("Transaction History:\n")
        for transaction in self.transaction_history:
            print(f"{transaction.id} | {transaction.transaction_type.value} "
                  f"| ${transaction.amount} | {transaction.timestamp}")


