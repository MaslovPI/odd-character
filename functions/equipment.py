import json
from classes.starter import Starter
from functools import reduce


def generate_equipment(hp, high):
    json_data = []
    with open("data/starters.json") as json_file:
        json_data = json.load(json_file)

    by_max = {row["max"]: row for row in json_data}
    item = by_max[max(high, 9)]
    return Starter(
        ", ".join(map(lambda cont: cont["name"], item["content"])), item["arcana"]
    )
