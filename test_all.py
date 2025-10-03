"""
test_all.py
Pytest test suite for ATM System OOP project.
Covers: Account, Bank, Customer, Card, Transactions, and ATM features.
"""

import pytest

from Account import Account
from Bank import Bank
from Customer import Customer
from Card import Card
from Transactions import WithdrawTransaction, DepositTransaction, BalanceInquiry, Transfer


# ==============================
# Fixtures
# ==============================

@pytest.fixture
def setup_bank():
    """Fixture that sets up a test bank with customer, accounts, and card."""
    bank = Bank("NBE", "#45455")
    customer = Customer("Anas", "Cairo", "0123456789", "anas@example.com")

    acc1 = Account("1111")
    acc2 = Account("2222")

    card1 = Card("card-123", "0000")
    acc1.link_card(card1)

    customer.add_account(acc1)
    customer.add_account(acc2)
    bank.add_customer(customer)

    return [bank, customer, acc1, acc2, card1]


# ==============================
# Account Tests
# ==============================

def test_account_initialization(setup_bank):
    """Test that an account is created with zero balance and no transactions."""
    acc1 = setup_bank[2]
    assert acc1.balance == 0.0
    assert acc1.transaction_history == []


def test_account_link_card(setup_bank):
    """Test linking a card to an account."""
    acc1 = setup_bank[2]
    card1 = setup_bank[4]
    assert acc1.linked_card == card1


# ==============================
# Bank Tests
# ==============================

def test_bank_add_customer(setup_bank):
    """Test that adding a customer stores their accounts in the bank."""
    bank = setup_bank[0]
    acc1 = setup_bank[2]
    acc2 = setup_bank[3]
    assert acc1.account_number in bank.accounts
    assert acc2.account_number in bank.accounts


# ==============================
# Customer Tests
# ==============================

def test_customer_details(setup_bank):
    """Test customer stores personal information correctly."""
    customer = setup_bank[1]
    assert customer.name == "Anas"
    assert customer.email == "anas@example.com"
    assert len(customer.accounts) == 2


# ==============================
# Card Tests
# ==============================

def test_card_pin_change_success(setup_bank):
    """Test changing card PIN with the correct old PIN."""
    card1 = setup_bank[4]
    assert card1.pin_setter("0000", "1234") is True
    assert card1.pin_getter == "1234"


def test_card_pin_change_fail(setup_bank):
    """Test that entering wrong old PIN fails to change the PIN."""
    card1 = setup_bank[4]
    assert card1.pin_setter("9999", "5678") is False
    assert card1.pin_getter != "5678"


# ==============================
# Transaction Tests
# ==============================

def test_deposit_transaction(setup_bank):
    """Test that a deposit increases account balance and adds a transaction."""
    acc1 = setup_bank[2]
    transaction = DepositTransaction(200)
    transaction.execute(acc1)
    assert acc1.balance == 200
    assert acc1.transaction_history[-1].transaction_type.value == "Deposit"


def test_withdraw_transaction(setup_bank):
    """Test withdrawing from an account with sufficient funds."""
    acc1 = setup_bank[2]
    acc1.balance = 300
    transaction = WithdrawTransaction(100)
    transaction.execute(acc1)
    assert acc1.balance == 200
    assert acc1.transaction_history[-1].transaction_type.value == "Withdraw"


def test_withdraw_insufficient_funds(setup_bank, capsys):
    """Test withdrawing with insufficient funds prints an error."""
    acc1 = setup_bank[2]
    transaction = WithdrawTransaction(500)
    transaction.execute(acc1)
    captured = capsys.readouterr()
    assert "Insufficient funds" in captured.out
    assert acc1.balance == 0


def test_balance_inquiry_transaction(setup_bank):
    """Test balance inquiry transaction records current balance."""
    acc1 = setup_bank[2]
    acc1.balance = 1000
    transaction = BalanceInquiry()
    transaction.execute(acc1)
    assert acc1.transaction_history[-1].transaction_type.value == "Balance Inquiry"
    assert acc1.transaction_history[-1].amount == 1000


def test_transfer_transaction_success(setup_bank):
    """Test successful transfer between two accounts."""
    bank = setup_bank[0]
    acc1 = setup_bank[2]
    acc2 = setup_bank[3]
    acc1.balance = 500
    transaction = Transfer(200, acc2.account_number)
    transaction.execute(acc1, bank)
    assert acc1.balance == 300
    assert acc2.balance == 200
    assert acc1.transaction_history[-1].transaction_type.value == "Transfer"
    assert acc2.transaction_history[-1].transaction_type.value == "Transfer"


def test_transfer_invalid_destination(setup_bank, capsys):
    """Test transferring to a non-existent account prints error."""
    bank = setup_bank[0]
    acc1 = setup_bank[2]
    acc1.balance = 500
    transaction = Transfer(100, "fake123")
    transaction.execute(acc1, bank)
    captured = capsys.readouterr()
    assert "Invalid destination account" in captured.out
    assert acc1.balance == 500


def test_transfer_insufficient_funds(setup_bank, capsys):
    """Test transfer with insufficient funds prints error."""
    bank = setup_bank[0]
    acc1 = setup_bank[2]
    acc2 = setup_bank[3]
    acc1.balance = 50
    transaction = Transfer(200, acc2.account_number)
    transaction.execute(acc1, bank)
    captured = capsys.readouterr()
    assert "Insufficient funds" in captured.out
    assert acc1.balance == 50
    assert acc2.balance == 0
