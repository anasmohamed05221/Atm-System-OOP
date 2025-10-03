# ========================= Screen.py =========================
import os


class Screen:
    """Simulates the ATM screen for displaying messages."""

    def show_message(self, message: str) -> None:
        """Display a message on the screen."""
        print(message)

    def clear_screen(self) -> None:
        """Clear the console screen."""
        os.system('cls' if os.name == "nt" else 'clear')