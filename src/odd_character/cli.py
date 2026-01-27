import argparse

from odd_character.classes.arcanaprovider import ArcanaProvider
from odd_character.classes.equipmentprovider import EquipmentProvider
from odd_character.classes.format import Format
from odd_character.classes.hireprovider import HireProvider
from odd_character.classes.outputtype import OutputType
from odd_character.classes.petprovider import PetProvider
from odd_character.classes.starterprovider import StarterProvider
from odd_character.functions.jsonhelper import (
    get_arcana_list,
    get_equipment_dict,
    get_hire_dict,
    get_pet_dict,
    get_starter_dict,
)
from odd_character.functions.roll import roll, roll_multiple
from odd_character.functions.styling import apply_style


def main():
    parser = argparse.ArgumentParser(
        description="Character (and more) generator for Into the Odd TTRPG"
    )
    parser.add_argument(
        "type",
        nargs="?",
        default=OutputType.CHARACTER,
        help="What do you want to generate",
        type=OutputType,
        choices=list(OutputType),
    )

    args = parser.parse_args()

    match args.type:
        case OutputType.CHARACTER:
            print_character()
        case OutputType.PET:
            print_random_pet()
        case OutputType.HIRE:
            print_random_hire()
        case OutputType.ARCANA:
            print_random_arcana()


def print_character():
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
    starter = generate_starter(hit_protection, high)
    if starter:
        print_starter(starter)


def generate_starter(hit_protection, high):
    starter_dict = get_starter_dict()
    equipment_dict = get_equipment_dict()
    arcana_list = get_arcana_list()

    arcana_provider = ArcanaProvider(arcana_list)
    equipment_provider = EquipmentProvider(equipment_dict)
    starter_provider = StarterProvider(
        starter_dict,
        equipment_provider,
        arcana_provider,
    )

    return starter_provider.generate_starter(hit_protection, high)


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


def print_random_arcana():
    arcana_list = get_arcana_list()
    arcana_provider = ArcanaProvider(arcana_list)
    spell_name, spell_description = arcana_provider.get_random_arcana()
    print_arcana(spell_name, spell_description)


def print_arcana(spell_name, spell_description):
    print(fit_to_print(spell_name, spell_description, Format.MAGENTA))


def print_random_pet():
    pet_dict = get_pet_dict()
    pet_provider = PetProvider(pet_dict)
    pet_type, pet_description = pet_provider.get_random_pet()
    print(fit_to_print(pet_type, pet_description, Format.YELLOW))


def print_pet(pet):
    pet_dict = get_pet_dict()
    pet_provider = PetProvider(pet_dict)
    pet_description = pet_provider.get_pet_description(pet)
    print(fit_to_print(pet, pet_description if pet_description else "", Format.YELLOW))


def print_random_hire():
    hire_dict = get_hire_dict()
    equipment_dict = get_equipment_dict()
    equipment_provider = EquipmentProvider(equipment_dict)
    hire_provider = HireProvider(hire_dict, equipment_provider)
    hire_type, hire_description = hire_provider.get_random_hire()
    print(fit_to_print(hire_type, hire_description, Format.YELLOW))


def print_hire(hire):
    hire_dict = get_hire_dict()
    equipment_dict = get_equipment_dict()
    equipment_provider = EquipmentProvider(equipment_dict)
    hire_provider = HireProvider(hire_dict, equipment_provider)
    hire_description = hire_provider.get_hire_description(hire)
    print(
        fit_to_print(hire, hire_description if hire_description else "", Format.YELLOW)
    )


def format_stat(stat, high):
    return Format.RED.apply(stat) if stat == high else Format.CYAN.apply(stat)


def print_starter(starter):
    print(fit_to_print("Starter package", starter.content, Format.YELLOW))
    if starter.pet:
        print_pet(starter.pet)
        print()

    if starter.hire:
        print_hire(starter.hire)
        print()

    if starter.arcana:
        spell_name, spell_description = starter.arcana
        print_arcana(spell_name, spell_description)
        print()


def fit_to_print(topic, value, color):
    return f"{format_headline(f'{topic}:', color)} {color.apply(value)}"


def format_headline(text, color):
    return apply_style(text, color, Format.BOLD, Format.UNDERLINE)


if __name__ == "__main__":
    main()
