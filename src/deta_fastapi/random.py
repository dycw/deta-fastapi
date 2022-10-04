from string import ascii_letters

from numpy import random


def random_letter() -> str:
    return random.choice(list(ascii_letters))
