from classes.format import Format
from functions.equipment import generate_equipment
from functions.roll import roll, roll_multiple
from functions.styling import apply_style


def main():
    strength = roll_multiple(3, 6)
    dexterity = roll_multiple(3, 6)
    willpower = roll_multiple(3, 6)
    high = max(strength, dexterity, willpower)
    hit_protection = roll(6)

    print_stats(
        strength,
        dexterity,
        willpower,
        high,
        hit_protection,
    )

    print("")
    starter = generate_equipment(hit_protection, high)
    if starter:
        print_starter(starter)


def print_stats(strength, dexterity, willpower, high, hit_protection):
    print(f"{format_headline('Strength:', Format.CYAN)} {format_stat(strength, high)}")
    print(
        f"{format_headline('Dexterity:', Format.CYAN)} {format_stat(dexterity, high)}"
    )
    print(
        f"{format_headline('Willpower:', Format.CYAN)} {format_stat(willpower, high)}"
    )
    print("")
    print(fit_to_print("Hit protection", hit_protection, Format.BLUE))


def format_stat(stat, high):
    return Format.RED.apply(stat) if stat == high else Format.CYAN.apply(stat)


def print_starter(starter):
    print(fit_to_print("Starter package", starter.content, Format.YELLOW))
    if starter.arcana:
        spell_name, spell_description = starter.arcana
        print(fit_to_print(spell_name, spell_description, Format.MAGENTA))


def fit_to_print(topic, value, color):
    return f"{format_headline(f'{topic}:', color)} {color.apply(value)}"


def format_headline(text, color):
    return apply_style(text, color, Format.BOLD, Format.UNDERLINE)


if __name__ == "__main__":
    main()
