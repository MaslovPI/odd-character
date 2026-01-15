import json
import random

from classes.starter import Starter
from functions.roll import roll_dice


def generate_equipment(hp, high):
    starter_dict = get_starter_dict()
    equipment_dict = get_equipment_dict()
    arcana_list = get_arcana_list()

    item = starter_dict[max(high, 9)]
    description = "\n"

    for content in item["content"]:
        description += f"{get_content_description(content, equipment_dict)}\n"

    if "pet" in item:
        description += "\n"
        pet = item["pet"]
        description += f"{get_pet_description(pet)}\n"

    if "hire" in item:
        description += "\n"
        hire = item["hire"]
        description += f"{get_hire_description(hire, equipment_dict)}\n"

    arcana = get_random_arcana(arcana_list) if item["arcana"] else None
    return Starter(description, arcana)


def get_content_description(content, equipment_dict):
    name = content["name"]
    content_description = content["extra_info"]
    return get_equipment_description(name, equipment_dict, content_description)


def get_equipment_description(name, equipment_dict, description=""):
    equipment = get_equipment_by_name(equipment_dict, name)
    if not equipment:
        equipment = get_equipment_by_example(equipment_dict, name)

    if equipment:
        return f"{name} (Cost: {equipment['cost']}, Description: {equipment['description']})"
    if description:
        return f"{name} ({description})"

    return name


def get_pet_description(pet):
    pet_dict = get_pet_dict()
    description = pet
    if pet not in pet_dict:
        return description

    pet_item = pet_dict[pet]
    description += "\n"
    description += f"Cost: {pet_item['cost']}\n"
    description += f"Strength: {roll_dice(pet_item['str'])}\n"
    description += f"Attack: {pet_item['attack']}"
    return description


def get_hire_description(hire, equipment_dict):
    hire_dict = get_hire_dict()
    description = hire
    if hire not in hire_dict:
        return description

    hire_item = hire_dict[hire]
    description += "\n"
    description += f"Cost (per day): {hire_item['cost_per_day']}\n"
    description += f"Hit protection: {roll_dice(hire_item['hp'])}\n"
    available_score = hire_item["ability_scores"]
    strength = 0
    if "str" in hire_item:
        strength = roll_dice(hire_item["str"])
    else:
        strength = generate_score(available_score - 2)
    available_score -= strength
    dexterity = generate_score(available_score - 1)
    available_score -= dexterity
    willpower = available_score if available_score > 0 else 1
    description += f"Strength: {strength}\n"
    description += f"Dexterity: {dexterity}\n"
    description += f"Willpower: {willpower}\n"

    for item in hire_item["equipment"]:
        description += f"{get_equipment_description(item, equipment_dict)}"
    return description


def generate_score(available_score):
    if available_score < 2:
        return 1
    return random.randint(1, available_score)


def get_equipment_by_name(equipment_dict, name):
    return equipment_dict.get(name)


def get_equipment_by_example(equipment_dict, example):
    return next(
        (
            item
            for item in equipment_dict.values()
            if example in item.get("examples", [])
        ),
        None,
    )


def get_random_arcana(arcana_list):
    index = random.randint(0, len(arcana_list) - 1)
    item = arcana_list[index]
    return (item["name"], item["description"])


def get_starter_dict():
    starters_json_data = get_list_from_json("data/starters.json")
    return {row["max"]: row for row in starters_json_data}


def get_equipment_dict():
    equipment_json_data = get_list_from_json("data/equipment.json")
    return {row["name"]: row for row in equipment_json_data}


def get_pet_dict():
    equipment_json_data = get_list_from_json("data/pets.json")
    return {row["type"]: row for row in equipment_json_data}


def get_hire_dict():
    equipment_json_data = get_list_from_json("data/hires.json")
    return {row["type"]: row for row in equipment_json_data}


def get_arcana_list():
    return get_list_from_json("data/arcana.json")


def get_list_from_json(path):
    json_data = []
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data
