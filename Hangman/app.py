from utils import (
    welcome_message,
    run_game,
    play_again,
)


def main():
    """The main app for the Hangman game"""
    guessed = []

    while True:
        welcome_message()

        run_game(guessed)

        response = play_again()

        if response == "n":
            print("===== GOODBYE! =====")
            break
        continue


if __name__ == "__main__":
    main()
