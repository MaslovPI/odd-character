import random


class ArcanaProvider:
    def __init__(self, arcana_list):
        self.arcana_list = arcana_list

    def get_random_arcana(self):
        index = random.randint(0, len(self.arcana_list) - 1)
        item = self.arcana_list[index]
        return (item["name"], item["description"])
