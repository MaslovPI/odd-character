import json
import random


def get_random_arcana():
    json_data = []
    with open("data/arcana.json") as json_file:
        json_data = json.load(json_file)

    index = random.randint(0, len(json_data) - 1)
    item = json_data[index]
    return (item["name"], item["description"])
