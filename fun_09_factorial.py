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

