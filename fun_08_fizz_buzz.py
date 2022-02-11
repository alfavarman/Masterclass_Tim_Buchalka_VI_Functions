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


#       Computer Asks Player Fizz Buzz etc
# for i in range(1, 100):
#     answer = input("For {} fizz, buzz, fizz buzz or {}?: "
#                    .format(i, i))
#     if answer != fizz_buzz(i):
#         print("Wrong! For {} correct is {}"
#               .format(i, fizz_buzz(i)))
#         break
#     else:
#         print("Congrats! Try Again:")



#       Computer Guess with Player
guess = 0
while guess < 101:
    guess += 1
    print(fizz_buzz(guess))
    guess += 1
    correct_answer = fizz_buzz(guess)
    player_guess = input("fizz, buzz, fizz buzz, or number: ")
    if player_guess != fizz_buzz(guess):
        print("Wrong!! it should be {}".format(fizz_buzz(guess)))
        break
else:
    print("Congrats! You are sharp!")
