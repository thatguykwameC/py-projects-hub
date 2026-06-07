## Hangman Game

A simple game of hangman:
A command line word guessing game. Players guess letters one at a time
to reveal a hidden animal name. The player has 7 lives before the game ends.

---

1. Display dashes for each letter in the word.
2. Prompt the user to guess a letter.
3. Checks if the letter is in the word
4. wrong guess means deduct a life
5. 7 lives in total
6. if the user guesses the correct letter it should replace the underscore being displayed
7. Prints a "You win", when all words are successfully guessed and "Game Over" when the user runs out of lives
8. the game ends when the user wins or loses

---

"""
Modules:
config — constants, word list and display
utils — game logic and input handling
"""

This game was built in 3 versions:
v1.o handles no occurences of substrings
v2.0 handles multiple occurences of substrings
v3.0 handles game restart
