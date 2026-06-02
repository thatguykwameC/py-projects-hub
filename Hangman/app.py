from utils import welcome_message, get_user_input, display_output, lives_lost
from config import HANGMANPICS, word, display


def main():
    """"""
    active = True
    welcome_message()

    while active:

        guess = get_user_input()

        life_count = lives_lost(guess)

    

        if life_count == 0:
            print("===== GAME OVER =====")
            active = False
        
        output_d = display_output(guess, word, display)

        if word == output_d:
            print("===== YOU WIN! =====")
            active = False



if __name__ == "__main__":
    main()