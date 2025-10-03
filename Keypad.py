# ========================= Keypad.py =========================
import getpass


class Keypad:
    """Simulates an ATM keypad for user input."""

    def get_secure_input(self, message: str) -> str:
        """Get input securely without displaying characters."""
        return getpass.getpass(message)

    def get_input(self, message: str, secure: bool = False) -> str:
        """Get input from the user."""
        if secure:
            return self.get_secure_input(message)
        return input(message)
