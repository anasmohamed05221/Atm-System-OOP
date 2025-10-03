# ========================= AtmInterface.py =========================
from Handlers import *
from Keypad import Keypad
from Screen import Screen


class AtmInterface:
    """
    Represents an ATM interface that allows a user to interact
    with different banking operations.
    """

    def __init__(self, bank, atm_location: str):
        self.bank = bank
        self.atm_location = atm_location
        self.keypad = Keypad()
        self.screen = Screen()
        self.withdraw_handler = WithdrawHandler(self.keypad, self.screen)
        self.deposit_handler = DepositHandler(self.keypad, self.screen)
        self.balance_inquiry_handler = BalanceInquiryHandler()
        self.transaction_history_handler = TransactionHistoryHandler()
        self.pin_change_handler = PinChangeHandler(self.keypad, self.screen)
        self.transfer_handler = TransferHandler(self.keypad, self.screen, bank)

    def display_main_menu(self, account):
        """
        Display the main menu for ATM operations.
        """
        message = """
        1. Withdraw
        2. Deposit
        3. Balance Inquiry
        4. View Transactions
        5. Change PIN
        6. Transfer
        7. Exit
        Choose an option: """
        while True:
            choice = self.keypad.get_input(message)
            try:
                match choice:
                    case "1":
                        self.withdraw_handler.handle(account)
                    case "2":
                        self.deposit_handler.handle(account)
                    case "3":
                        self.balance_inquiry_handler.handle(account)
                    case "4":
                        self.transaction_history_handler.handle(account)
                    case "5":
                        self.pin_change_handler.handle(account)
                    case "6":
                        self.transfer_handler.handle(account)
                    case "7":
                        break
                    case _:
                        self.screen.show_message("Invalid choice.")
                self.keypad.get_input("\nPress Enter to continue...")
                self.screen.clear_screen()
            except ValueError:
                print("Invalid amount. Please try again.")

