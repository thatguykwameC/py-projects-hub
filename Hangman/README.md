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

You have 7 lives :)
Pick a Category Animal/Astronomy-Term/Country/Fruit/Vegetable: country
Country to guess: _ _ _ _ _ _
Guess a letter: a
_ _ _ a _ _
Guess a letter: i
Your guess 'i' is not in the word, you lose a life

  +---+
  |   |
      |
      |
      |
      |
=========
***************** 6/7 LIVES LEFT *****************
_ _ _ a _ _
Guess a letter: a
You already guessed 'a'
Guess a letter: u
_ u _ a _ u
Guess a letter: o
Your guess 'o' is not in the word, you lose a life

  +---+
  |   |
  O   |
      |
      |
      |
=========
***************** 5/7 LIVES LEFT *****************
_ u _ a _ u
Guess a letter: 

...
```

## Project Structure

```text
Hangman/
├── categories
│   ├── animals.txt
│   ├── countries.txt
│   └── space.txt
├── app.py
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
- Category selection
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
