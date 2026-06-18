# Hangman Game

A command-line implementation of the classic Hangman game built with Python.

Players guess letters one at a time to reveal the hidden word.<br>
The player has 7 lives and loses one life for each incorrect guess.<br>
The game ends when the player successfully reveals the word or runs out of lives.

---

## Features

- Category selection
- Random word selection
- Input validation
- Duplicate guess detection
- Multiple letter occurrence handling
- ASCII Hangman display
- Win/Loss detection
- Game restart support

---

## Installation

Clone the repository:

```bash
git clone https://github.com/thatguykwameC/py-projects-hub.git
```

Navigate to the project folder:

```bash
cd py-projects-hub/Hangman
```

Run the game:

```bash
python3 app.py
```

---

## Tab Completion

Tab autocomplete is supported for category selection.

- **Linux/macOS** — works out of the box.
- **Windows** — install `pyreadline3` to enable it:

```bash
  pip install pyreadline3
```

Without it, the game still runs normally — you just won't get Tab completion.

---

## Gameplay Flow

1. Display hidden word as underscores.
2. Prompt the player to guess a letter.
3. Check whether the letter exists in the word.
4. Correct guesses reveal all matching letters.
5. Incorrect guesses deduct a life.
6. The game ends when:
   - The word is fully revealed, or
   - The player runs out of lives.
7. Option to restart the game

---

## Example Gameplay

```text
.__
|  |__ _____    ____    ____   _____ _____    ____
|  |  \\__  \  /    \  / ___\ /     \\__  \  /    \
|   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
|___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
     \/     \/     \//_____/       \/     \/     \/

Guess the Hidden Word 🎯

Categories: (Animal/Astronomy/Country/Fruit/Vegetable)
(Press Tab to autocomplete) ⌨️
Pick a Category: country
------------------------------------------------------
                 🎮 Lives Remaining: 7
------------------------------------------------------
Country to guess: _ _ _ _ _ _ _ _ _ _ _
Guess a letter: a
❌ 'a' is not in the word.

  +---+
  |   |
      |
      |
      |
      |
=========
------------------------------------------------------
                 🎮 Lives Remaining: 6
------------------------------------------------------
_ _ _ _ _ _ _ _ _ _ _
Guess a letter: e
_ _ _ _ _ _ _ e _ _ e
Guess a letter: i
_ i _ _ _ _ _ e _ _ e
Guess a letter: a

Guessed Letters:
a, e, i
Guess a letter: l
_ i _ _ _ _ l e _ _ e
Guess a letter: v
❌ 'v' is not in the word.

  +---+
  |   |
  O   |
      |
      |
      |
=========

...
```

---

## Project Structure

```text
Hangman
├── categories
│   ├── animals.txt
│   ├── countries.txt
│   ├── fruits.txt
│   ├── space.txt
│   └── veggies.txt
├── app.py
├── config.py
├── _helpers.py
├── README.md
└── utils.py

```

---

## Concepts Practiced

- Modular programming
- Function decomposition
- Input validation
- String manipulation
- List operations
- Control flow
- Python modules and imports
- State management
- File I/O

---

## Version History

```text
v1.0:
- Implemented core Hangman game loop using Python
- Basic word guessing functionality (single letter input)
- Simple win/lose conditions based on remaining lives

v2.0:
- Improved letter handling to support multiple occurrences in a word
- Introduced tracking of guessed letters using a set to prevent duplicates
- Enhanced input validation for non-alphabetic and repeated inputs
- Added word queue system to prevent repeated words until the pool is exhausted

v3.0:
- Added full game restart functionality without restarting the program
- Implemented category selection system (Animals, Countries, Fruits, etc.)
- Improved user experience with structured prompts and cleaner game flow
- Added Tab autocompletion for Category selection
```
