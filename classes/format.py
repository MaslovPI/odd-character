from enum import Enum


class Format(Enum):
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSED = "\033[7m"
    RESET = "\033[0m"

    def apply(self, text) -> str:
        return f"{self.value}{text}{Format.RESET.value}"
