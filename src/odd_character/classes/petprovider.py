from odd_character.functions.roll import roll_dice
import random


class PetProvider:
    def __init__(self, pet_dict):
        self.pet_dict = pet_dict

    def get_pet_description(self, pet):
        pet_item = self.pet_dict.get(pet)
        if not pet_item:
            return None
        description = f"Cost: {pet_item['cost']}\n"
        description += f"Strength: {roll_dice(pet_item['str'])}\n"
        description += f"Attack: {pet_item['attack']}"
        return description

    def get_random_pet(self):
        key = random.choice(list(self.pet_dict.keys()))
        return key, self.get_pet_description(key)
