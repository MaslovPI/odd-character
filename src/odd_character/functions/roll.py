import random


def roll(dimensions):
    if dimensions < 1:
        raise ValueError(f"Wrong dimensions: {dimensions}")
    return random.randint(1, dimensions)


def roll_multiple(number, dimensions):
    if number < 1:
        raise ValueError(f"Wrong number: {dimensions}")
    return sum(roll(dimensions) for _ in range(number))


def roll_dice(dice_to_roll):
    dice_info = dice_to_roll.split("d")
    if not len(dice_info) == 2:
        raise ValueError("Invalid format. Use NdM (e.g. 2d6)")

    number = int(dice_info[0]) if dice_info[0] else 1
    dimensions = int(dice_info[1])
    return roll_multiple(number, dimensions)
