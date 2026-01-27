from dataclasses import dataclass


@dataclass
class Starter:
    def __init__(self, content, arcana, pet, hire):
        self.content = content
        self.arcana = arcana
        self.pet = pet
        self.hire = hire
