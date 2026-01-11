import random


def roll(dimensions):
    if dimensions < 1:
        raise ValueError(f"Wrong dimensions: {dimensions}")
    return random.randint(1, dimensions)


def roll_multiple(number, dimensions):
    if number < 1:
        raise ValueError(f"Wrong number: {dimensions}")
    return sum(roll(dimensions) for _ in range(number))
