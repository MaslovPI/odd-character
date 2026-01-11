from classes.format import Format
from functions.arcana import get_random_arcana
from functions.equipment import generate_equipment
from functions.roll import roll, roll_multiple
from functions.styling import apply_style


def main():
    strength = roll_multiple(3, 6)
    dexterity = roll_multiple(3, 6)
    willpower = roll_multiple(3, 6)
    high = max(strength, dexterity, willpower)
    hit_protection = roll(6)

    strength_headline = format_headline("Strength:", Format.CYAN)
    strength_value = (
        Format.RED.apply(strength) if strength == high else Format.CYAN.apply(strength)
    )
    print(f"{strength_headline} {strength_value}")
    print(
        f"{format_headline('Dexterity:', Format.CYAN)} {Format.RED.apply(dexterity) if dexterity == high else Format.CYAN.apply(dexterity)}"
    )
    print(
        f"{format_headline('Willpower:', Format.CYAN)} {Format.RED.apply(willpower) if willpower == high else Format.CYAN.apply(willpower)}"
    )
    print("")
    print(fit_to_print("Hit protection", hit_protection, Format.BLUE))

    starter = generate_equipment(hit_protection, high)
    if starter:
        print_starter(starter)


def print_starter(starter):
    print(fit_to_print("Starter package", starter.content, Format.YELLOW))
    if starter.arcana:
        spell_name, spell_description = get_random_arcana()
        print(fit_to_print(spell_name, spell_description, Format.MAGENTA))


def fit_to_print(topic, value, color):
    return f"{format_headline(f'{topic}:', color)} {color.apply(value)}"


def format_headline(text, color):
    return apply_style(text, color, Format.BOLD, Format.UNDERLINE)


if __name__ == "__main__":
    main()
