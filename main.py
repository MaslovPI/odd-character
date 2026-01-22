import argparse

from classes.arcanaprovider import ArcanaProvider
from classes.equipmentprovider import EquipmentProvider
from classes.format import Format
from classes.hireprovider import HireProvider
from classes.outputtype import OutputType
from classes.petprovider import PetProvider
from classes.starterprovider import StarterProvider
from functions.jsonhelper import (
    get_arcana_list,
    get_equipment_dict,
    get_hire_dict,
    get_pet_dict,
    get_starter_dict,
)
from functions.roll import roll, roll_multiple
from functions.styling import apply_style


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
            print_pet()
        case OutputType.HIRE:
            print_hire()
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
    hire_dict = get_hire_dict()
    pet_dict = get_pet_dict()
    arcana_list = get_arcana_list()

    arcana_provider = ArcanaProvider(arcana_list)
    equipment_provider = EquipmentProvider(equipment_dict)
    pet_provider = PetProvider(pet_dict)
    hire_provider = HireProvider(hire_dict, equipment_provider)
    starter_provider = StarterProvider(
        starter_dict, equipment_provider, arcana_provider, pet_provider, hire_provider
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


def print_pet():
    pet_dict = get_pet_dict()
    pet_provider = PetProvider(pet_dict)
    pet_type, pet_description = pet_provider.get_random_pet()
    print(fit_to_print(pet_type, pet_description, Format.YELLOW))


def print_hire():
    hire_dict = get_hire_dict()
    equipment_dict = get_equipment_dict()
    equipment_provider = EquipmentProvider(equipment_dict)
    hire_provider = HireProvider(hire_dict, equipment_provider)
    hire_type, hire_description = hire_provider.get_random_hire()
    print(fit_to_print(hire_type, hire_description, Format.YELLOW))


def format_stat(stat, high):
    return Format.RED.apply(stat) if stat == high else Format.CYAN.apply(stat)


def print_starter(starter):
    print(fit_to_print("Starter package", starter.content, Format.YELLOW))
    if starter.arcana:
        spell_name, spell_description = starter.arcana
        print_arcana(spell_name, spell_description)


def fit_to_print(topic, value, color):
    return f"{format_headline(f'{topic}:', color)} {color.apply(value)}"


def format_headline(text, color):
    return apply_style(text, color, Format.BOLD, Format.UNDERLINE)


if __name__ == "__main__":
    main()
