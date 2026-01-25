class EquipmentProvider:
    def __init__(self, equipment_dict):
        self.equipment_dict = equipment_dict

    def get_equipment_description(self, name, description=""):
        equipment = self.get_equipment_by_name(name)
        if not equipment:
            equipment = self.get_equipment_by_example(name)

        if equipment:
            cost = equipment.get("cost")
            eq_description = equipment.get("description")
            return f"{name} (Cost: {cost if cost else 0}" + (
                f" Description: {eq_description})" if eq_description else ")"
            )
        if description:
            return f"{name} ({description})"

        return name

    def get_equipment_by_name(self, name):
        return self.equipment_dict.get(name)

    def get_equipment_by_example(self, example):
        return next(
            (
                item
                for item in self.equipment_dict.values()
                if example in item.get("examples", [])
            ),
            None,
        )
