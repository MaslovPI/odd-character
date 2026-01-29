import unittest
from odd_character.classes.equipmentprovider import EquipmentProvider
from odd_character.classes.starterprovider import StarterProvider


class TestStarterProvider(unittest.TestCase):
    def test_should_generate_starter_no_extra(self):
        starter_dict_1 = {
            9: {
                "arcana": 0,
                "content": [
                    {"name": "club", "extra_info": "d6"},
                    {"name": "lockpick", "extra_info": "d6"},
                ],
            }
        }
        starter_dict = {1: starter_dict_1}
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
        starter_provider = StarterProvider(
            starter_dict,
            equipment_provider,
        )

        starter = starter_provider.generate_starter(1, 1)
        self.assertEqual(0, starter.arcana)
        self.assertIsNone(starter.hire)
        self.assertIsNone(starter.pet)
        self.assertEqual(
            "\nclub (Cost: 1s Description: d6 Damage, Bulky.)\nlockpick (Cost: 3s)\n",
            starter.content,
        )

    def test_should_generate_starter_with_extra(self):
        starter_dict_1 = {
            15: {
                "arcana": 1,
                "content": [
                    {"name": "club", "extra_info": "d6"},
                ],
                "hire": "man",
                "pet": "dog",
            }
        }
        starter_dict = {5: starter_dict_1}
        equipment_dict = {}

        equipment_provider = EquipmentProvider(equipment_dict)
        starter_provider = StarterProvider(
            starter_dict,
            equipment_provider,
        )

        starter = starter_provider.generate_starter(5, 15)
        self.assertEqual(1, starter.arcana)
        self.assertEqual("man", starter.hire)
        self.assertEqual("dog", starter.pet)
        self.assertEqual(
            "\nclub (d6)\n",
            starter.content,
        )

    def test_should_generate_starter_with_no_content(self):
        starter_dict_1 = {14: {}}
        starter_dict = {5: starter_dict_1}
        equipment_dict = {}

        equipment_provider = EquipmentProvider(equipment_dict)
        starter_provider = StarterProvider(
            starter_dict,
            equipment_provider,
        )

        starter = starter_provider.generate_starter(5, 14)
        self.assertEqual(0, starter.arcana)
        self.assertIsNone(starter.hire)
        self.assertIsNone(starter.pet)
        self.assertEqual(
            "\n",
            starter.content,
        )


if __name__ == "__main__":
    unittest.main()
