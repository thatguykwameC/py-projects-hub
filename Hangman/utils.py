from random import choice

from config import (
    GAME_COVER,
    HANGMANPICS,
    ANIMAL_POOL,
    MAX_LIVES,
    VALID_RESPONSES,
)


def welcome_message():
    """Displays the game banner"""
    print(GAME_COVER)


# Helper function that checks index
def _checks_index(guess, word, display):
    """Finds all occurrences of guess and updates display accordingly"""
    for index, letter in enumerate(word):
        if letter == guess:
            display[index] = guess
    return display


def play_again():
    """Asks if the user wants to play again"""
    while True:
        again = input("Do you wish to play again? (Y/N) ").strip().lower()
        if again in VALID_RESPONSES:
            return again
        print("Invalid Input, choose (Y/N)")


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
            guessed.append(guess)
        else:
            print(f"You already guessed {guess}")
            continue
        return guess


def lives_lost(guess, life_count, word):
    """Handles wrong inputs"""
    if guess not in word:
        print(f"Your guess '{guess}' is not in the word, you lose a life")
        print(HANGMANPICS[MAX_LIVES - life_count])

        life_count -= 1

        print(
            f"***************** {life_count}/{MAX_LIVES} LIVES LEFT *****************"
        )
    return life_count


def display_output(guess, word, display):
    """Displays the output of the guesses"""
    if guess in word:
        display = _checks_index(guess, word, display)

    check = "".join(display)
    print(check)
    return check


def game_status(life_count, word, check):
    """Checks if the game has been won or lost"""
    if life_count == 0:
        print("===== GAME OVER =====")
        print(f"The animal is {word}")
        return False

    if word == check:
        print("===== YOU WIN! =====")
        return False

    return True


def run_game():
    """Runs a single game session"""
    guessed = []
    word = choice(ANIMAL_POOL)
    dashes = "_" * len(word)
    print(f"Animal to guess: {dashes}")
    display = list(dashes)
    life_count = MAX_LIVES

    while True:
        guess = get_user_input(guessed)

        life_count = lives_lost(guess, life_count, word)

        check = display_output(guess, word, display)

        if not game_status(life_count, word, check):
            break
