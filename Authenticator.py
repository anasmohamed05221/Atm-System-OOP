# ========================= Authenticator.py =========================
class Authenticator:
    """
    Handles authentication of users via card number and PIN.
    """

    def __init__(self, bank):
        self.bank = bank

    def authenticate(self, card_number: str, pin: str):
        """
        Authenticate a card number and PIN.
        """
        for acc in self.bank.accounts.values():
            if acc.linked_card and acc.linked_card.number == card_number and acc.linked_card.pin_getter == pin:
                return acc
        return None

