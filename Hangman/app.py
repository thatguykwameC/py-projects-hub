from utils import (
    welcome_message,
    run_game,
    choose_category,
    play_again,
)


def main():
    """The main app for the Hangman game"""
    while True:
        welcome_message()

        category = choose_category()

        run_game(category)

        response = play_again()

        if response == "n":
            print("===== GOODBYE! =====")
            break


if __name__ == "__main__":
    main()
