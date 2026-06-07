from config import (
    GAME_COVER,
    HANGMANPICS,
    MAX_LIVES,
    word,
    dashes,
)


def welcome_message(dashes):
    """Displays the game banner"""
    print(GAME_COVER)
    print(f"Animal to guess: {dashes}")


# Helper function that checks index
def checks_index(guess, word, display):
    """Finds all occurrences of guess and updates display accordingly"""
    for index, letter in enumerate(word):
        if letter == guess:
            display[index] = guess
    return display


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


def lives_lost(guess, life_count):
    """Handles wrong inputs"""
    if guess not in word:
        print(f"You guessed '{guess}'. That is not in the word, you lose a life")
        print(HANGMANPICS[MAX_LIVES - life_count])

        life_count -= 1

        print(
            f"*********************** {life_count}/{MAX_LIVES} LIVES LEFT ***********************"
        )
    return life_count


def display_output(guess, word, display):
    """Displays the output of the guesses"""
    if guess in word:
        display = checks_index(guess, word, display)

    check = "".join(display)
    print(check)
    return check


def game_status(life_count, word, check):
    """Checks if the game has been won or lost"""
    if life_count == 0:
        print("===== GAME OVER =====")
        return False

    if word == check:
        print("===== YOU WIN! =====")
        return False
    return True
