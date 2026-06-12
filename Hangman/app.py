from utils import (
    welcome_message,
    choose_category,
    run_game,
    play_again,
)


def main():
    """The main app for the Hangman game"""
    while True:
        response = welcome_message()

        choose_category(response)

        run_game(response)

        response = play_again()

        if response == "n":
            print("===== GOODBYE! =====")
            break


if __name__ == "__main__":
    main()
