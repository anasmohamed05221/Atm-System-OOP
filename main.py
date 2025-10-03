from Bank import Bank
from Customer import Customer
from Account import Account
from Card import Card
from AtmInterface import AtmInterface
from CardReader import CardReader


def main():
    """
    Entry point for the ATM System demo.
    Sets up the bank, a customer, accounts, and a card,
    then runs the ATM interface (which already handles display and menu).
    """

    # Setup demo bank, customer, and accounts
    mybank = Bank("NBE", "#45455")
    customer = Customer("Anas", "Mohamed", "01213232323", "anas@example.com")

    account1 = Account("8723637")
    account2 = Account("99999")

    customer.add_account(account1)
    customer.add_account(account2)
    mybank.add_customer(customer)

    # Link a card to the first account
    card1 = Card("122345", "0000")  # card with PIN 0000
    account1.link_card(card1)

    # Setup ATM and card reader
    atm = AtmInterface(mybank, "AAST Branch ATM")
    cardreader = CardReader(atm)

    # Start ATM interaction
    print("-----Welcome to the ATM Demo-----")
    cardreader.insert_card(card1)


if __name__ == "__main__":
    main()
