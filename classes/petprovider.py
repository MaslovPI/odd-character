from functions.roll import roll_dice


class PetProvider:
    def __init__(self, pet_dict):
        self.pet_dict = pet_dict

    def get_pet_description(self, pet):
        description = pet
        if pet not in self.pet_dict:
            return description

        pet_item = self.pet_dict[pet]
        description += "\n"
        description += f"Cost: {pet_item['cost']}\n"
        description += f"Strength: {roll_dice(pet_item['str'])}\n"
        description += f"Attack: {pet_item['attack']}"
        return description
