# ========================= Handlers.py =========================
from Transactions import WithdrawTransaction, DepositTransaction, BalanceInquiry, Transfer
from Account import Account
from Bank import Bank
from Keypad import Keypad
from Screen import Screen


class WithdrawHandler:
    """Handles withdrawal transactions."""

    def __init__(self, keypad: Keypad, screen: Screen) -> None:
        self.keypad = keypad
        self.screen = screen

    def handle(self, account: Account) -> None:
        """Process a withdrawal request."""
        while True:
            amount = self.keypad.get_input("Enter amount to withdraw: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.show_message("Invalid amount, please enter a positive value")
                    continue
                transaction = WithdrawTransaction(amount)
                transaction.execute(account)
                break
            except ValueError:
                self.screen.show_message("Invalid input.")


class DepositHandler:
    """Handles deposit transactions."""

    def __init__(self, keypad: Keypad, screen: Screen) -> None:
        self.keypad = keypad
        self.screen = screen

    def handle(self, account: Account) -> None:
        """Process a deposit request."""
        while True:
            amount = self.keypad.get_input("Enter deposit amount: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.show_message("Invalid amount, please enter a positive value")
                    continue
                transaction = DepositTransaction(amount)
                transaction.execute(account)
                break
            except ValueError:
                self.screen.show_message("Invalid input.")


class BalanceInquiryHandler:
    """Handles balance inquiry requests."""

    def handle(self, account: Account) -> None:
        """Process balance inquiry."""
        transaction = BalanceInquiry()
        transaction.execute(account)


class TransactionHistoryHandler:
    """Handles displaying transaction history."""

    def handle(self, account: Account) -> None:
        """Show account transaction history."""
        account.display_transactions()


class PinChangeHandler:
    """Handles PIN change requests."""

    def __init__(self, keypad: Keypad, screen: Screen) -> None:
        self.keypad = keypad
        self.screen = screen

    def handle(self, account: Account) -> None:
        """Process PIN change request."""
        old_pin = self.keypad.get_input("Enter your old PIN: ")
        new_pin = self.keypad.get_input("Enter new PIN: ")
        confirm_pin = self.keypad.get_input("Confirm new PIN: ")
        if new_pin != confirm_pin:
            self.screen.show_message("Pins do not match, please try again.")
            return
        if account.linked_card and account.linked_card.pin_setter(old_pin, new_pin):
            self.screen.show_message("PIN changed successfully.")
        else:
            self.screen.show_message("Incorrect old PIN, PIN changing failed.")


class TransferHandler:
    """Handles money transfer requests."""

    def __init__(self, keypad: Keypad, screen: Screen, bank: Bank) -> None:
        self.keypad = keypad
        self.screen = screen
        self.bank = bank

    def handle(self, account: Account) -> None:
        """Process transfer request."""
        while True:
            dest_num = self.keypad.get_input("Enter destination account number: ")
            amount = self.keypad.get_input("Enter amount to transfer: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.show_message("Invalid amount.")
                    continue
                transaction = Transfer(amount, dest_num)
                transaction.execute(account, self.bank)
                break
            except ValueError:
                self.screen.show_message("Invalid input.")
