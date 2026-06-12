# Hangman Game

A command-line implementation of the classic Hangman game built with Python.

Players guess letters one at a time to reveal a hidden animal name.<br>
The player has 7 lives and loses one life for each incorrect guess.<br>
The game ends when the player successfully reveals the word or runs out of lives.

---

## Features

- Random animal selection
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
Animal to guess: _ _ _ _ _

Guess a letter: a

a _ _ _ _

Guess a letter: z

'z' is not in the word.

6/7 lives left

Guess a letter: p

a p _ _ _

Guess a letter: e

a p e _ _

...
```

---

## Project Structure

```text
Hangman/
├── app.py
├── categories
│   ├── animals.txt
│   ├── countries.txt
│   └── space.txt
├── config.py
├── README.md
├── trial.py
└── utils.py
```

---

## Version History

```text
v1.0:
- Basic game loop
- Single-occurrence letter handling

v2.0:
- Multiple occurrence letter handling

v3.0:
- Game restart functionality
- Added Category Selection
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
