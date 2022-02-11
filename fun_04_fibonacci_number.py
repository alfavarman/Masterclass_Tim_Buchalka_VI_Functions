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


print(fibonacci_numbers(10))