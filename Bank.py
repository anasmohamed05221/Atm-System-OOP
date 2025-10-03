# ========================= Bank.py =========================
class Bank:
    """
    Represents a bank that manages customer accounts.
    """

    def __init__(self, name: str, swift_code: str):
        self.name = name
        self.swift_code = swift_code
        self.accounts = {}

    def add_customer(self, customer):
        """
        Add all accounts of a customer to the bank.
        """
        for acc in customer.accounts.values():
            self.accounts[acc.account_number] = acc