import json
from classes.starter import Starter


def generate_equipment(hp, high):
    starter_dict = get_starter_dict()
    equipment_dict = get_equipment_dict()

    item = starter_dict[max(high, 9)]
    description = "\n"
    for content in item["content"]:
        name = content["name"]
        content_description = content["extra_info"]

        equipment = get_equipment_by_name(equipment_dict, name)
        if not equipment:
            equipment = get_equipment_by_example(equipment_dict, name)

        if equipment:
            description += f"{name} (Cost: {equipment['cost']}, Description: {equipment['description']})\n"
        elif content_description:
            description += f"{name} ({content_description})\n"
        else:
            description += f"{name}\n"

    return Starter(description, item["arcana"])


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


def get_starter_dict():
    starters_json_data = get_list_from_json("data/starters.json")
    return {row["max"]: row for row in starters_json_data}


def get_equipment_dict():
    equipment_json_data = get_list_from_json("data/equipment.json")
    return {row["name"]: row for row in equipment_json_data}


def get_list_from_json(path):
    json_data = []
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data
