# ========================= Card.py =========================
class Card:
    """
    Represents a bank card with a number and a private PIN.
    """

    def __init__(self, number: str, pin: str):
        self.number = number
        self.__pin = pin

    @property
    def pin_getter(self) -> str:
        """Return the current PIN."""
        return self.__pin

    def pin_setter(self, old_pin: str, new_pin: str) -> bool:
        """
        Change the card's PIN if old PIN matches.
        """
        if self.__pin == old_pin:
            self.__pin = new_pin
            return True
        print("Incorrect PIN.")
        return False
