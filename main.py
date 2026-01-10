from classes.colors import Colors
from functions.equipment import generate_equipment
from functions.roll import roll, rollMultipleAccumulate


def main():
    colors = Colors()
    strength = rollMultipleAccumulate(3, 6)
    dexterity = rollMultipleAccumulate(3, 6)
    willpower = rollMultipleAccumulate(3, 6)
    high = max(strength, dexterity, willpower)

    hit_protection = roll(6)
    print(
        f"Strength: {colors.colorize(strength, 'red') if strength == high else strength}"
    )
    print(
        f"Dexterity: {colors.colorize(dexterity, 'red') if dexterity == high else dexterity}"
    )
    print(
        f"Willpower: {colors.colorize(willpower, 'red') if willpower == high else willpower}"
    )
    print(f"Highest Ability Score: {high}")
    print(f"Hit Protection: {hit_protection}")

    starter = generate_equipment(hit_protection, high)
    if starter:
        print(f"Starting package: {starter.content}")
        print(f"Has arcana: {starter.arcana}")


if __name__ == "__main__":
    main()
