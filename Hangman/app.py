from config import MAX_LIVES, word, display
from utils import (
    welcome_message,
    get_user_input,
    lives_lost,
    display_output,
    game_status,
)


def main():
    """the main app"""

    guessed = []
    life_count = MAX_LIVES

    welcome_message()

    while True:
        guess = get_user_input(guessed)

        life_count = lives_lost(guess, life_count)

        check = display_output(guess, word, display)

        if not game_status(life_count, word, check):
            break


if __name__ == "__main__":
    main()
