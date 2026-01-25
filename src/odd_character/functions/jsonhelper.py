import json
from importlib.resources import files


def get_starter_dict():
    starters_json_data = get_list_from_json("starters.json")
    return {
        row["hp"]: {starter["max"]: starter for starter in row["starters"]}
        for row in starters_json_data
    }


def get_equipment_dict():
    equipment_json_data = get_list_from_json("equipment.json")
    return {row["name"]: row for row in equipment_json_data}


def get_pet_dict():
    equipment_json_data = get_list_from_json("pets.json")
    return {row["type"]: row for row in equipment_json_data}


def get_hire_dict():
    equipment_json_data = get_list_from_json("hires.json")
    return {row["type"]: row for row in equipment_json_data}


def get_arcana_list():
    return get_list_from_json("arcana.json")


def get_list_from_json(filename: str):
    data_path = files("odd_character.data") / filename
    with data_path.open("r", encoding="utf-8") as json_file:
        return json.load(json_file)
