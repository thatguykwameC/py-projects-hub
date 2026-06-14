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
ASTRONOMY = BASE_DIR / "categories" / "space.txt"
FRUITS = BASE_DIR / "categories" / "fruits.txt"
VEGGIES = BASE_DIR / "categories" / "veggies.txt"


WORD_POOL = {
    "animal": ANIMALS.read_text().splitlines(),
    "astronomy": ASTRONOMY.read_text().splitlines(),
    "country": COUNTRIES.read_text().splitlines(),
    "fruit": FRUITS.read_text().splitlines(),
    "vegetable": VEGGIES.read_text().splitlines(),
}


CATEGORY_LABEL = {
    "animal": "Animal",
    "astronomy": "Astronomy-Term",
    "country": "Country",
    "fruit": "Fruit",
    "vegetable": "Vegetable",
}


MAX_LIVES = len(HANGMANPICS)

VALID_RESPONSES = {"y", "n"}
