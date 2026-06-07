from random import choice

# ASCII art for the game's cover
GAME_COVER = r"""
.__                                                 
|  |__ _____    ____    ____   _____ _____    ____  
|  |  \\__  \  /    \  / ___\ /     \\__  \  /    \ 
|   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
|___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
     \/     \/     \//_____/       \/     \/     \/ 
"""

# A list of ASCII art for the gallows
HANGMANPICS = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

# A list of animals from which one is chosen at random
ANIMAL_POOL = [
    "ape",
    "frog",
    "hawk",
    "lion",
    "shark",
    "tiger",
    "zebra",
    "koala",
    "otter",
    "lemur",
    "badger",
    "falcon",
    "jaguar",
    "monkey",
    "rabbit",
    "walrus",
    "cheetah",
    "dolphin",
    "giraffe",
    "penguin",
    "alligator",
    "chimpanzee",
    "flamingo",
    "kangaroo",
    "wolverine",
    "chameleon",
    "rhinoceros",
    "salamander",
    "hippopotamus",
    "hummingbird",
]

# Constants
MAX_LIVES = 7

# variables
word = choice(ANIMAL_POOL)
dashes = "_" * len(word)
display = list(dashes)
