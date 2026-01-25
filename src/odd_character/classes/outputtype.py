from enum import Enum


class OutputType(Enum):
    CHARACTER = "character"
    PET = "pet"
    HIRE = "hire"
    ARCANA = "arcana"

    def __str__(self):
        return self.value
