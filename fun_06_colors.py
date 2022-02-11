# 8 Colors
Black = '\u001b[30m'
Red = '\u001b[31m'
Green = '\u001b[32m'
Yellow = '\u001b[33m'
Blue = '\u001b[34m'
Magenta = '\u001b[35m'
Cyan = '\u001b[36m'
White = '\u001b[37m'
Bright_Black = '\u001b[30;1m'
Bright_Red = '\u001b[31;1m'
Bright_Green = '\u001b[32;1m'
Bright_Yellow = '\u001b[33;1m'
Bright_Blue = '\u001b[34;1m'
Bright_Magenta = '\u001b[35;1m'
Bright_Cyan = '\u001b[36;1m'
Bright_White = '\u001b[37;1m'
RESET = '\u001b[0m'


def print_color(text: str, effect: str) -> None:
    """
    Print text in selected ANSI effect.

    :param text: text to be printed.
    :param effect: ANSI effects
    """
    output_string = '{0}{1}{2}'.format(effect, text, RESET)
    print(output_string)


print_color("text", Green)
print_color("Blue", Blue)

