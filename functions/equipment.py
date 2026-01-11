import csv
from classes.starter import Starter


def generate_equipment(hp, high):
    path = get_path_from_hp(hp)
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if high <= int(row["max"]):
                return Starter(
                    row["content"],
                    row["arcana"] == "1",
                )
        return None


def get_path_from_hp(hp):
    return "data/equipment/1.csv"
