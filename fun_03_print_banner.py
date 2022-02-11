#Print Banner:
# define function to print banner:
# Function print text outpu in center of scr of set width with 2* on each side
# if string is '*' all line of asterix is printed
# if string is longer than scr width message is printed
# remeber to include 2 asterix on each side


def banner(text: str = "", screen_width: int = 80, design: str = "*") -> None:
    """
    Printed Banner is created around `text`, in defined `screen_width`
    `design` ed character.
    NOTE each line is separate. Can't use \"""\"""
    :param text: string to be printed, default len 76 characters
    :param screen_width: int default is 80
    :param design: str default is '*'
    :return:
    """
    if len(text) > screen_width - 4:
        print("Nah! max {0} char per line,\n"
              "please use big_banner(str) function".format(screen_width))
    elif text == design:
        print(design * screen_width)
    else:
        print('{0}{0}{1}{0}{0}'.format(design, text.center(screen_width - 4)))


banner("#", 60, "#")
banner('', 60,  "#")
banner('today I learn python', 60,  "#")
banner('tomorrow I apply for job', 60,  "#")
banner('day after Yoy blowjob :D', 60,  "#")
banner('*', 60,  "#")
banner('')
banner('Rika needs Chares', 60,  "#")
banner("""
jsks
ksk
ks
""")
#banner('************************************************************************************')
