from config import (
    GAME_COVER,
    HANGMANPICS,
    word,
    dashes,
)


def welcome_message():
    """Displays the game banner"""
    print(GAME_COVER)
    print(f"Animal to guess: {dashes}")


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
        print(f"You guessed '{guess}'. That is not in the word, you loose a life")
        print(HANGMANPICS[7 - life_count])

        life_count -= 1

        print(
            f"*********************** {life_count}/7 LIVES LEFT ***********************"
        )
    return life_count


def display_output(guess, word, display):
    """Displays the output of the word to be guessed"""
    if guess in word:
        check_index = word.index(guess)
        display[check_index] = guess
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
