from enum import Enum


class Color(Enum):
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    def apply(self, text) -> str:
        return f"{self.value}{text}{Color.RESET.value}"
