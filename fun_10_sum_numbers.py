# define function: name sum_numbers,
# that sum all numbers passed as arguments
# should define single variable

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



print(sum_numbers(5, 3, 4, 4.4, 5.6, 10))
