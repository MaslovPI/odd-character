import unittest
from odd_character.classes.equipmentprovider import EquipmentProvider
from odd_character.classes.starterprovider import StarterProvider


class TestStarterProvider(unittest.TestCase):
    def test_should_geerate_starter_no_extra(self):
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


if __name__ == "__main__":
    unittest.main()
