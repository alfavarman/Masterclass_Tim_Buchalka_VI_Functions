def fibonacci_numbers(n: int) -> int:
    """
    return fibonacci numbers for n' range.
    n must be positive int. default n is 100.
    NOTE fibonacci n = 10 is 55. N is range of indexes.

    :param n: int is range for which fibonacci numbers are calculated
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


def banner(text: str = "", screen_width: int = 80, design: str = "*") -> None:
    """
    Printed Banner is created around `text`, in defined `screen_width`
    `design` ed character.
    NOTE each line is separate. Can't use \"""\"""

    :param text: string to be printed, default len 76 characters
    :param screen_width: int default is 80
    :param design: str default is '*'
    raises ValueError: if string longer than screen_with -4
    """
    if len(text) > screen_width - 4:
        raise ValueError("String: {0} is longer than specified width".format(screen_width))
    elif text == design:
        print(design * screen_width)
    else:
        print('{0}{0}{1}{0}{0}'.format(design, text.center(screen_width - 4)))


def is_palindrome(string: str) -> bool:
    """
    Validate the string to be palindrome.
    ignores lower upper case

    :param string: str of characters
    :return: bool value True for str is palindrome
    """
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(string: str) -> bool:
    """
    Validate sentence to be a palindrome.
    ignores lower upper case, punctuation, whitespaces,
    and nums

    :param string: any string at any length
    :return: bool value of True for palindrome
    """
    sent = ''
    for char in string:
        if char.isalnum():
            sent += char
    return sent[::-1].casefold() == sent.casefold()


def factorial(number: int) -> int:
    """
    Factorial is multiply of next number up to argument number

    :param number: int
    :return: int factorial for argument
    """
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number+1):
            result = result +(result * i)
        return result


def sum_numbers(*numbers: float) -> float:
    """
    Calculate sum of numbers
    :param numbers: int or float
    :return: sum result as float
    """
    # return sum(numbers) # ver 1
    # or
    result = 0              # ver 2
    for n in numbers:
        result += n
    return result


