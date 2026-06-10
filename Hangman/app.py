from config import MAX_LIVES
from utils import (
    welcome_message,
    word_to_be_guessed,
    get_user_input,
    lives_lost,
    display_output,
    game_status,
    play,
    play_again,
)


def main():
    """The main app for the Hangman game"""
    guessed = []

    while True:
        welcome_message()

        play(guessed)

        p_again = play_again()

        if p_again == "n":
            break
        continue


if __name__ == "__main__":
    main()
