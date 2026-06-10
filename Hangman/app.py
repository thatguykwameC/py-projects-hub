from utils import (
    welcome_message,
    play,
    play_again,
)


def main():
    """The main app for the Hangman game"""
    guessed = []

    while True:
        welcome_message()

        play(guessed)

        response = play_again()

        if response == "n":
            break
        continue


if __name__ == "__main__":
    main()
