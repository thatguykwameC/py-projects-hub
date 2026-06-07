## Hangman Game

A simple game of hangman:<br>
A command-line word-guessing game. Players guess letters one at a time
to reveal a hidden animal name. The player has 7 lives before the game ends.

---

### Flow

1. Display dashes for each letter in the word.
2. Prompt the user to guess a letter.
3. Checks if the letter is in the word
4. A wrong guess means deducting a life
5. 7 lives in total
6. If the user guesses the correct letter, it should replace the underscore being displayed
7. Prints a "You win" when all words are successfully guessed and "Game Over" when the user runs out of lives
8. The game ends when the user wins or loses

---

### Modules

- config: constants, word list, and display
- utils: game logic and input handling
- app: main app

---

### Versions

This game was built in 3 versions:

- v1.0 handles no occurrences of substrings
- v2.0 handles multiple occurrences of substrings
- v3.0 handles game restart

---

### Concepts learned

- Loops
- Lists
- Functions
- Strings
- Modules
