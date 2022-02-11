def fibonacci_numbers(n=100):
    """
    return fibonacci numbers for n' range.
    n must be positive int. default n is 100.
    NOTE fibonacci n = 10 is 55. N is range of indexes.
    :param n is range of fibonacci indexes
    :return: fibonacci numbers for n' range
    """
    if 0 <= n <= 1:
        return n

    n_minus1,n_minus2, = 1, 0
    fn = None
    for f in range(n -1):
        fn = n_minus1 + n_minus2
        print(fn)
        n_minus2 = n_minus1
        n_minus1 = fn

    return fn


def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although function is designed to multiply two numbers,
    can multiply a sequence. If you pass a string as `x`,
    it will be repeated `y` times, as returned value.

    :param x:
    :param y:
    :return: product of `x` and `y`.
    """

    result = x * y
    return result


def banner(text="", screen_width=80, design="*"):
    """
    Printed Banner is created around `text`, in defined `screen_width`
    `design` ed character.
    NOTE each line is separate. Can't use \"""\"""
    :param text: string to be printed, default len 76 characters
    :param screen_width: default is 80
    :param design: default is '*'
    :return:
    """
    if len(text) > screen_width - 4:
        print("Nah! max {0} char per line,\n"
              "please use big_banner(str) function".format(screen_width))
    elif text == design:
        print(design * screen_width)
    else:
        print('{0}{0}{1}{0}{0}'.format(design, text.center(screen_width - 4)))


