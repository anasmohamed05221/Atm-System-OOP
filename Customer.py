# ========================= Customer.py =========================
class Customer:
    """
    Represents a bank customer with personal details and accounts.
    """

    def __init__(self, name: str, address: str, phone_number: str, email: str):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.accounts = {}

    def add_account(self, account):
        """
        Add an account to the customer.
        """
        self.accounts[account.account_number] = account