from classes.color import Color
from functions.equipment import generate_equipment
from functions.roll import roll, rollMultipleAccumulate


def main():
    strength = rollMultipleAccumulate(3, 6)
    dexterity = rollMultipleAccumulate(3, 6)
    willpower = rollMultipleAccumulate(3, 6)
    high = max(strength, dexterity, willpower)

    hit_protection = roll(6)
    print(
        f"{Color.CYAN.apply('Strength:')} {Color.RED.apply(strength) if strength == high else Color.CYAN.apply(strength)}"
    )
    print(
        f"{Color.CYAN.apply('Dexterity:')} {Color.RED.apply(dexterity) if dexterity == high else Color.CYAN.apply(dexterity)}"
    )
    print(
        f"{Color.CYAN.apply('Willpower:')} {Color.RED.apply(willpower) if willpower == high else Color.CYAN.apply(willpower)}"
    )
    print("")
    print(Color.BLUE.apply(f"Hit Protection: {hit_protection}"))

    starter = generate_equipment(hit_protection, high)
    if starter:
        print(Color.YELLOW.apply(f"Starting package: {starter.content}"))
        print(Color.MAGENTA.apply(f"Has arcana: {starter.arcana}"))


if __name__ == "__main__":
    main()
