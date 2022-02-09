#Print Banner:
# define function to print banner:
# Function print text outpu in center of scr of set width with 2* on each side
# if string is '*' all line of asterix is printed
# if string is longer than scr width message is printed
# remeber to include 2 asterix on each side


def banner(text, screen_width):
    #screen_width = 80
    if len(text) > screen_width - 4:
        print("Nah! max 80 char per line,\n"
              "please use big_banner(str) function")
    elif text == '*':
        print('*' * screen_width)
    else:
        print('**{0}**'.format(text.center(screen_width - 4)))


banner('*', 80)
banner('today I learn python', 80)
banner('tomorrow I apply for job', 80)
banner('day after Yoy blowjob :D', 80)
banner('*', 80)
banner(' ', 80)
banner('Rika needs Chares', 80)
#banner('************************************************************************************')