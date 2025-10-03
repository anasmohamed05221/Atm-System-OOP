# ========================= Transactions.py =========================
from abc import ABC, abstractmethod
import datetime
import uuid
from enum import Enum
from Bank import Bank


class TransactionType(Enum):
    """Enumeration of transaction types."""
    WITHDRAW = "Withdraw"
    DEPOSIT = "Deposit"
    BALANCE_INQUIRY = "Balance Inquiry"
    TRANSFER = "Transfer"


class Transaction(ABC):
    """Abstract base class for transactions."""

    def __init__(self, transaction_type: TransactionType, amount: float | None = None) -> None:
        self.id = uuid.uuid4()
        self.timestamp = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount

    @abstractmethod
    def execute(self, account) -> None:
        pass


class WithdrawTransaction(Transaction):
    """Represents a withdrawal transaction."""

    def __init__(self, amount: float) -> None:
        super().__init__(TransactionType.WITHDRAW, amount)

    def execute(self, account) -> None:
        if self.amount is None or self.amount <= 0:
            raise ValueError("Invalid withdrawal amount.")
        if self.amount <= account.balance:
            account.balance -= self.amount
            account.add_transaction(self)
            print(f"Withdrawal Successful! Current Balance: ${account.balance}")
        else:
            print("Insufficient funds.")


class DepositTransaction(Transaction):
    """Represents a deposit transaction."""

    def __init__(self, amount: float) -> None:
        super().__init__(TransactionType.DEPOSIT, amount)

    def execute(self, account) -> None:
        if self.amount is None or self.amount <= 0:
            raise ValueError("Invalid deposit amount.")
        account.balance += self.amount
        account.add_transaction(self)
        print(f"Deposit Successful! Current Balance: ${account.balance}")


class BalanceInquiry(Transaction):
    """Represents a balance inquiry transaction."""

    def __init__(self) -> None:
        super().__init__(TransactionType.BALANCE_INQUIRY, amount=0)

    def execute(self, account) -> None:
        self.amount = account.balance
        account.add_transaction(self)
        print(f"Your balance is ${account.balance}")


class Transfer(Transaction):
    """Represents a transfer transaction between accounts."""

    def __init__(self, amount: float, destination_account_number: str) -> None:
        super().__init__(TransactionType.TRANSFER, amount)
        self.destination_account_number = destination_account_number

    def execute(self, account, bank: Bank) -> None:
        if self.amount is None or self.amount <= 0:
            raise ValueError("Invalid transfer amount.")
        if account.balance >= self.amount:
            destination_account = bank.accounts.get(self.destination_account_number)
            if destination_account:
                account.balance -= self.amount
                destination_account.balance += self.amount
                print(f"Transfer Successful! New balance: {account.balance}")
                account.add_transaction(self)
                destination_account.add_transaction(self)
            else:
                print("Invalid destination account.")
        else:
            print("Insufficient funds.")