from string import ascii_letters

from numpy.random import choice
from numpy.random import randint


def get_random_int() -> int:
    return randint(low=0, high=10)


def get_random_letter() -> int:
    return choice(list(ascii_letters))
