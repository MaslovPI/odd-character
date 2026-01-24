import unittest

from classes.equipmentprovider import EquipmentProvider
from classes.hireprovider import HireProvider


class TestHireProvider(unittest.TestCase):
    def test_should_return_none_when_pet_not_in_dict(self):
        hire_dict = {"Something": []}
        equipment_dict = {"Something": []}

        equipment_provider = EquipmentProvider(equipment_dict)
        hire_provider = HireProvider(hire_dict, equipment_provider)
        description = hire_provider.get_hire_description("Hire")
        self.assertIsNone(description)


if __name__ == "__main__":
    unittest.main()
