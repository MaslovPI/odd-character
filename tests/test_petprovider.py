import unittest

from odd_character.classes.petprovider import PetProvider


class TestPetProvider(unittest.TestCase):
    def test_should_return_none_when_pet_not_in_dict(self):
        pet_dict = {"Something": []}
        pet_provider = PetProvider(pet_dict)
        description = pet_provider.get_pet_description("Pet")
        self.assertIsNone(description)

    def test_should_return_valid_pet_description(self):
        pet_dict = {"Valid pet": {"cost": "1s", "str": "d1", "attack": "d10"}}
        pet_provider = PetProvider(pet_dict)
        description = pet_provider.get_pet_description("Valid pet")
        self.assertEqual("Cost: 1s\nStrength: 1\nAttack: d10", description)


if __name__ == "__main__":
    unittest.main()
