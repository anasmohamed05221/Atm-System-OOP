# ========================= CardReader.py =========================
from Authenticator import Authenticator


class CardReader:
    """
    Simulates a card reader for an ATM.
    """

    def __init__(self, atm):
        self.atm = atm
        self.authenticator = Authenticator(self.atm.bank)

    def insert_card(self, card):
        """
        Insert a card and authenticate the user.
        """
        pin = self.atm.keypad.get_input("Please enter your PIN: ")
        account = self.authenticator.authenticate(card.number, pin)
        if account:
            self.atm.display_main_menu(account)
            return account
        else:
            self.atm.screen.show_message("Invalid card or PIN.")
            return None
