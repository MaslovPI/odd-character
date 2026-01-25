import random
from odd_character.functions.roll import roll_dice


class HireProvider:
    def __init__(self, hire_dict, equipment_provider):
        self.hire_dict = hire_dict
        self.equipment_provider = equipment_provider

    def get_random_hire(self):
        key = random.choice(list(self.hire_dict.keys()))
        return key, self.get_hire_description(key)

    def get_hire_description(self, hire):
        hire_item = self.hire_dict.get(hire)
        if not hire_item:
            return None

        description = f"Cost (per day): {hire_item['cost_per_day']}\n"
        description += f"Hit protection: {roll_dice(hire_item['hp'])}\n"
        available_score = hire_item["ability_scores"]
        pregen_strength = hire_item.get("str")

        strength, dexterity, willpower = self.generate_hire_ability_scores(
            available_score, roll_dice(pregen_strength) if pregen_strength else None
        )

        description += self.prepare_scores_description(strength, dexterity, willpower)

        for item in hire_item["equipment"]:
            description += (
                f"{self.equipment_provider.get_equipment_description(item)}\n"
            )
        return description

    def prepare_scores_description(self, strength, dexterity, willpower):
        description = f"Strength: {strength}\n"
        description += f"Dexterity: {dexterity}\n"
        description += f"Willpower: {willpower}\n"
        return description

    def generate_hire_ability_scores(self, available_score, pregen_strength=None):
        strength = (
            pregen_strength
            if pregen_strength
            else self.generate_score(available_score - 2)
        )

        available_score -= strength
        dexterity = self.generate_score(available_score - 1)
        available_score -= dexterity
        willpower = available_score if available_score > 0 else 1

        return strength, dexterity, willpower

    def generate_score(self, available_score):
        if available_score < 2:
            return 1
        return random.randint(1, available_score)
