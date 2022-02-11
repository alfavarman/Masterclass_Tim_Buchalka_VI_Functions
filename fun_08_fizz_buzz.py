# def f named fizz_buzz to return string:
# fizz for number divisible by 3
# buzz for number divisible by 5
# fizz buzz for number divisible by 3 and 5
# number for number not divisible by either
# annotate and Docstring
# include for loop to check in range 1 to 100


# def f named fizz_buzz to return string:
def fizz_buzz(number: int) -> str:
    """
    fizz buzz recognize numbers divisive by 3 - result fizz
    divisive by 5 - result buzz, divisive by both - result in fizz buzz
    and in neither result in number itself as a str.
    :param number: int
    :return: string: fizz for %3, buzz for %5, fizz buzz for %3 & %5, and number for either.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return str(number)


for i in range(1, 100):
    print(fizz_buzz(i))

# buzz for number divisible by 5
# fizz buzz for number divisible by 3 and 5
# number for number not divisible by either
# annotate and Docstring
# include for loop to check in range 1 to 100


