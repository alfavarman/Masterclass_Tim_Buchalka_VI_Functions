def fibbonaci_numbers(n):
    """
    function fibbonaci numbers - sequence of numbers where
    fn = fn-1 + fn-2.
    :param range_s: start of range
    :param range_e: end of range
    :return: fibbonaci numbers within user's range
    """
    if 0 <= n <= 1:
        return n

    n_minus1,n_minus2, = 1, 0

    for f in range(n -1):
        fn = n_minus1 + n_minus2
        print(fn)
        n_minus2 = n_minus1
        n_minus1 = fn

print(fibbonaci_numbers(100))