from config import HANGMANPICS, word
from utils import get_user_input

def lives_lost(guess):
    """Handles wrong inputs"""
    life_count, count = 7, 0
    
    while True:
        if guess not in word:
            print(f"You guessed '{guess}'. That is not in the word, you loose a life")
            print(HANGMANPICS[count])
            count += 1
            life_count -= 1
            print(f"*********************** {life_count}/7LIVES LEFT ***********************")

        return life_count
    

guess = get_user_input()
d = lives_lost(guess)

















# words = list("akuamenuala")

# while "a" in words:
    
#     cv = words.index("a")
#     # dv = words.remove("a")
#     cv += 1
#     print(cv)


    # check = " "
    # ccc = list(word)
    # if guess in word:
    #     check_index = word.index(guess)

    #     if guess in display:
    #         ccc[check_index] = "*"
    #         cc = ccc.index(guess)
    #         print(cc)
            
    #         # display[check_index] = guess 
            

    #     else:
    #         check_index = word.index(guess)
    #         display[check_index] = guess 
        
    #     for letter in display:
    #         check += letter
    #     print(check)
