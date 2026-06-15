# Helper Functions
from config import BOX_WIDTH


def _create_display(word):
    """Replaces letters in word with dashes"""
    display = []

    for char in word:
        if char == " ":
            display.append(" ")
        else:
            display.append("_")

    return display


def _format_display(display):
    """Formats the display for user output."""
    formatted = ""

    for char in display:
        if char == " ":
            formatted += "   "
        else:
            formatted += f"{char} "

    return formatted.rstrip()


def _checks_index(guess, word, display):
    """Finds all occurrences of guess and updates display accordingly"""
    for index, letter in enumerate(word):
        if letter == guess:
            display[index] = guess


def _display_remaining_lives(life_count):
    """Displays remaining lives to the user"""
    print("-" * BOX_WIDTH)
    text = f"🎮 Lives Remaining: {life_count}"
    print(f"{text:^{BOX_WIDTH}}")
    print("-" * BOX_WIDTH)
