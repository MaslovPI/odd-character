from classes.format import Format


def apply_style(text, *args):
    format = ""
    for arg in args:
        format += arg.value

    return f"{format}{text}{Format.RESET.value}"
