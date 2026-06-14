from random import shuffle

from config import (
    GAME_COVER,
    HANGMANPICS,
    WORD_POOL,
    CATEGORY_LABEL,
    MAX_LIVES,
    VALID_RESPONSES,
)
from _helpers import (
    _create_display,
    _checks_index,
    _format_display,
)

WORD_QUEUE = {}

for category, words in WORD_POOL.items():
    shuffled_words = words.copy()
    shuffle(shuffled_words)
    WORD_QUEUE[category] = shuffled_words


def get_word(category_name):
    """Returns a unique word until the category is exhausted"""
    if not WORD_QUEUE[category_name]:
        words = WORD_POOL[category_name].copy()
        shuffle(words)
        WORD_QUEUE[category_name] = words

    return WORD_QUEUE[category_name].pop()


def get_user_input(guessed):
    """Handles user input"""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Invalid input")
            continue

        if not guess.isalpha():
            print("Enter a valid letter")
            continue

        if guess not in guessed:
            guessed.add(guess)
        else:
            print("\nGuessed Letters:")
            print(", ".join(sorted(guessed)))
            continue

        return guess


def lives_lost(guess, life_count, word):
    """Handles wrong guesses"""
    if guess not in word:
        print(f"❌ '{guess}' is not in the word.")
        print(HANGMANPICS[MAX_LIVES - life_count])
        life_count -= 1
        print(f"***************** Lives Remaining: {life_count} *****************")

    return life_count


def display_output(guess, word, display):
    """Displays the output of the guesses"""
    if guess in word:
        _checks_index(guess, word, display)

    check = "".join(display)
    # Display for the user
    print(_format_display(display))

    return check


def game_status(life_count, word, check, response):
    """Checks if the game has been won or lost"""
    if life_count == 0:
        print("===== GAME OVER =====")
        print(f"The {CATEGORY_LABEL[response]} is {word.title()}")
        return False

    if word == check:
        print("===== YOU WIN! =====")
        return False

    return True


def welcome_message():
    """Displays the game banner"""
    message = f"\nGuess the Hidden Word :)" f"\nYou have: {MAX_LIVES} lives"
    return GAME_COVER + message


def choose_category():
    """Asks the user to choose a category"""
    available = "/".join(CATEGORY_LABEL.keys())
    while True:
        print(f"Categories: ({available.title()})")
        response = input(f"Pick a Category: ").strip().lower()
        if response in WORD_POOL:
            return response
        print("Enter a valid category")


def run_game(response):
    """Runs a single game session"""
    guessed = set()
    life_count = MAX_LIVES
    word = get_word(response)
    display = _create_display(word)
    print(f"{CATEGORY_LABEL[response]} to guess: {' '.join(display)}")

    while True:
        guess = get_user_input(guessed)

        life_count = lives_lost(guess, life_count, word)

        check = display_output(guess, word, display)

        if not game_status(life_count, word, check, response):
            break


def play_again():
    """Asks if the user wants to play again"""
    while True:
        again = input("Do you wish to play again? (Y/N) ").strip().lower()
        if again in VALID_RESPONSES:
            return again
        print("Invalid Input, choose (Y/N)")
