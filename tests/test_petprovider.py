import unittest

from classes.petprovider import PetProvider


class TestConversion(unittest.TestCase):
    def test_should_return_none_when_pet_not_in_dict(self):
        pet_dict = {"Something": []}
        pet_provider = PetProvider(pet_dict)
        description = pet_provider.get_pet_description("Pet")
        self.assertIsNone(description)


if __name__ == "__main__":
    unittest.main()
