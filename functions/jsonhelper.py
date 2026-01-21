import json


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
