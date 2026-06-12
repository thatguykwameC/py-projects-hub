from pathlib import Path

BASE_DIR = Path(__file__).parent


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


# Pool of words
ANIMALS = BASE_DIR / "categories" / "animals.txt"
COUNTRIES = BASE_DIR / "categories" / "countries.txt"
SPACE = BASE_DIR / "categories" / "space.txt"


WORD_POOL = {
    "animal": ANIMALS.read_text().splitlines(),
    "country": COUNTRIES.read_text().splitlines(),
    "space-term": SPACE.read_text().splitlines(),
}


MAX_LIVES = len(HANGMANPICS)

VALID_RESPONSES = {"y", "n"}
