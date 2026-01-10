from classes.format import Format
from functions.equipment import generate_equipment
from functions.roll import roll, rollMultipleAccumulate
from functions.styling import apply_style


def main():
    strength = rollMultipleAccumulate(3, 6)
    dexterity = rollMultipleAccumulate(3, 6)
    willpower = rollMultipleAccumulate(3, 6)
    high = max(strength, dexterity, willpower)

    hit_protection = roll(6)
    print(
        f"{apply_style('Strength:', Format.CYAN, Format.BOLD, Format.UNDERLINE)} {Format.RED.apply(strength) if strength == high else Format.CYAN.apply(strength)}"
    )
    print(
        f"{apply_style('Dexterity:', Format.CYAN, Format.BOLD, Format.UNDERLINE)} {Format.RED.apply(dexterity) if dexterity == high else Format.CYAN.apply(dexterity)}"
    )
    print(
        f"{apply_style('Willpower:', Format.CYAN, Format.BOLD, Format.UNDERLINE)} {Format.RED.apply(willpower) if willpower == high else Format.CYAN.apply(willpower)}"
    )
    print("")
    print(
        f"{apply_style('Hit Protection:', Format.BLUE, Format.BOLD, Format.UNDERLINE)} {Format.BLUE.apply(hit_protection)}"
    )

    starter = generate_equipment(hit_protection, high)
    if starter:
        print(
            f"{apply_style('Starter package:', Format.YELLOW, Format.BOLD, Format.UNDERLINE)} {Format.YELLOW.apply(starter.content)}"
        )
        print(
            f"{apply_style('Hit protection:', Format.MAGENTA, Format.BOLD, Format.UNDERLINE)} {Format.MAGENTA.apply(starter.arcana)}"
        )


if __name__ == "__main__":
    main()
