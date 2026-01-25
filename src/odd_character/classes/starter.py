from dataclasses import dataclass


@dataclass
class Starter:
    def __init__(self, content, arcana):
        self.content = content
        self.arcana = arcana
