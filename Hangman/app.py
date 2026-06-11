from utils import (
    welcome_message,
    run_game,
    play_again,
)


def main():
    """The main app for the Hangman game"""
    while True:
        welcome_message()

        run_game()

        response = play_again()

        if response == "n":
            print("===== GOODBYE! =====")
            break


if __name__ == "__main__":
    main()
