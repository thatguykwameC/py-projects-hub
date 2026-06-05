from config import GAME_COVER, HANGMANPICS
from config import word, dashes


def welcome_message():
    """Displays the game banner"""
    print(GAME_COVER)
    print(f"Animal to guess: {dashes}")


def get_user_input():
    """Handles user input"""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Invalid input")
            continue

        if not guess.isalpha():
            print("Enter a valid letter")
            continue
        return guess
    

def lives_lost(guess, life_count, count):
    """Handles wrong inputs"""
    if guess not in word:
        print(f"You guessed '{guess}'. That is not in the word, you loose a life")
        print(HANGMANPICS[count])
        count += 1
        life_count -= 1
        print(
            f"*********************** {life_count}/7 LIVES LEFT ***********************"
            )
    return life_count
    

def display_output(guess, word, display):
    """Displays the output of the word to be guessed"""
    check = ""
  
    if guess in word:

        check_index = word.index(guess)
        display[check_index] = guess 
        
        for letter in display:
            check += letter
        print(check)
        return check
    

# def win_loose(word, life_count, check):
#     """"""
#     if life_count == 0:
#         print("===== GAME OVER =====")
#         active = False

#     if word == check:
#         print("===== YOU WIN! =====")
#         active = False
