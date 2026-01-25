import unittest

from odd_character.classes.equipmentprovider import EquipmentProvider
from odd_character.classes.hireprovider import HireProvider


class TestHireProvider(unittest.TestCase):
    def test_should_return_none_when_hire_not_in_dict(self):
        hire_dict = {"Something": []}
        equipment_dict = {"Something": []}

        equipment_provider = EquipmentProvider(equipment_dict)
        hire_provider = HireProvider(hire_dict, equipment_provider)
        description = hire_provider.get_hire_description("Hire")
        self.assertIsNone(description)

    def test_should_return_valid_hire_description(self):
        hire_dict = {
            "guy": {
                "cost_per_day": "1s",
                "hp": "d1",
                "str": "d1",
                "ability_scores": 3,
                "equipment": ["sword", "club", "lockpick"],
            }
        }
        equipment_dict = {
            "club": {
                "cost": "1s",
                "description": "d6 Damage, Bulky.",
            },
            "Thief tools": {
                "cost": "3s",
                "description": "",
                "examples": ["lockpick", "dollarbag"],
            },
        }

        equipment_provider = EquipmentProvider(equipment_dict)
        hire_provider = HireProvider(hire_dict, equipment_provider)
        description = hire_provider.get_hire_description("guy")
        print(description)
        self.assertEqual(
            """Cost (per day): 1s
Hit protection: 1
Strength: 1
Dexterity: 1
Willpower: 1
sword
club (Cost: 1s Description: d6 Damage, Bulky.)
lockpick (Cost: 3s)
""",
            description,
        )

    def test_should_generate_valid_ability_with_lower_pregen_scores(self):
        pregen_strength = 5
        available = 10
        strength, dexterity, willpower = HireProvider(
            None, None
        ).generate_hire_ability_scores(available, pregen_strength)
        self.assertEqual(pregen_strength, strength)
        self.assertEqual(available, strength + dexterity + willpower)

    def test_should_generate_valid_ability_with_higher_pregen_scores(self):
        pregen_strength = 20
        available = 10
        strength, dexterity, willpower = HireProvider(
            None, None
        ).generate_hire_ability_scores(available, pregen_strength)
        self.assertEqual(pregen_strength, strength)
        self.assertEqual(1, dexterity)
        self.assertEqual(1, willpower)

    def test_should_generate_valid_ability_with_no_pregen_scores(self):
        available = 100
        strength, dexterity, willpower = HireProvider(
            None, None
        ).generate_hire_ability_scores(available, None)
        self.assertEqual(available, strength + dexterity + willpower)

    def test_should_generate_minimal_ability_with_no_available_scores(self):
        available = 0
        strength, dexterity, willpower = HireProvider(
            None, None
        ).generate_hire_ability_scores(available, None)
        self.assertEqual(1, strength)
        self.assertEqual(1, dexterity)
        self.assertEqual(1, willpower)


if __name__ == "__main__":
    unittest.main()
