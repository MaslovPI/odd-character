from odd_character.classes.starter import Starter


class StarterProvider:
    def __init__(
        self,
        starter_dict,
        equipment_provider,
    ):
        self.starter_dict = starter_dict
        self.equipment_provider = equipment_provider

    def generate_starter(self, hp, high):
        item = self.starter_dict[hp][max(high, 9)]
        description = "\n"

        content_list = item.get("content")
        if content_list:
            description += self.get_description_from_content_list(content_list)

        arcana = item.get("arcana") == 1
        return Starter(description, arcana, item.get("pet"), item.get("hire"))

    def get_description_from_content_list(self, content_list):
        description = ""
        for content in content_list:
            description += f"{self.get_content_description(content)}\n"
        return description

    def get_content_description(self, content):
        name = content["name"]
        content_description = content["extra_info"]
        return self.equipment_provider.get_equipment_description(
            name, content_description
        )
