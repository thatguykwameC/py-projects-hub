from config import word, display
from utils import welcome_message, get_user_input
from utils import lives_lost, display_output
from utils import win_loose


def main():
    """the main app"""

    life_count = 7
    count = 0
    active = True

    welcome_message()

    while active:
        guess = get_user_input()

        life_count = lives_lost(guess, life_count, count)

        if life_count == 0:
            print("===== GAME OVER =====")
            active = False

        check = display_output(guess, word, display)

        if word == check:
            print("===== YOU WIN! =====")
            active = False
    

if __name__ == "__main__":
    main()