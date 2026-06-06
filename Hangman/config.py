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

# ASCII art for the gallows
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

# Animal pool from which an animal is chosen at random
animal_pool = [
    "fox",
    "emu",
    "pig",
    "cat",
    "dog",
    "ant",
    "bat",
    "yak",
    "owl",
    "cow",
    "lion",
    "frog",
    "bear",
    "wolf",
    "hawk",
    "crab",
    "duck",
    "goat",
    "mule",
    "tiger",
    "shark",
    "whale",
    "rhino",
    "zebra",
    "chimp",
    "hyena",
    "camel",
    "leopard",
    "dolphin",
    "flamingo",
]

# Constants
MAX_LIVES = 7

# variables
word = choice(animal_pool)
dashes = "_" * len(word)
display = list(dashes)
