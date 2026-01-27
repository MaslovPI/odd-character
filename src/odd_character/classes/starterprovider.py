from odd_character.classes.starter import Starter


class StarterProvider:
    def __init__(
        self,
        starter_dict,
        equipment_provider,
        arcana_provider,
    ):
        self.starter_dict = starter_dict
        self.equipment_provider = equipment_provider
        self.arcana_provider = arcana_provider

    def generate_starter(self, hp, high):
        item = self.starter_dict[hp][max(high, 9)]
        description = "\n"

        for content in item["content"]:
            description += f"{self.get_content_description(content)}\n"

        arcana = self.arcana_provider.get_random_arcana() if item["arcana"] else None
        return Starter(description, arcana, item.get("pet"), item.get("hire"))

    def get_content_description(self, content):
        name = content["name"]
        content_description = content["extra_info"]
        return self.equipment_provider.get_equipment_description(
            name, content_description
        )
