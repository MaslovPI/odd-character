from odd_character.classes.starter import Starter


class StarterProvider:
    def __init__(
        self,
        starter_dict,
        equipment_provider,
        arcana_provider,
        pet_provider,
        hire_provider,
    ):
        self.starter_dict = starter_dict
        self.equipment_provider = equipment_provider
        self.arcana_provider = arcana_provider
        self.pet_provider = pet_provider
        self.hire_provider = hire_provider

    def generate_starter(self, hp, high):
        item = self.starter_dict[hp][max(high, 9)]
        description = "\n"

        for content in item["content"]:
            description += f"{self.get_content_description(content)}\n"

        if "pet" in item:
            description += "\n"
            pet = item["pet"]
            pet_description = self.pet_provider.get_pet_description(pet)
            description += (
                f"{pet}\n{pet_description}\n" if pet_description else f"{pet}\n"
            )

        if "hire" in item:
            description += "\n"
            hire = item["hire"]
            hire_description = self.hire_provider.get_hire_description(hire)
            description += (
                f"{hire}\n{hire_description}\n" if hire_description else f"{hire}\n"
            )

        arcana = self.arcana_provider.get_random_arcana() if item["arcana"] else None
        return Starter(description, arcana)

    def get_content_description(self, content):
        name = content["name"]
        content_description = content["extra_info"]
        return self.equipment_provider.get_equipment_description(
            name, content_description
        )
