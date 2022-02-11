def is_palindrome(string: str) -> bool:           #Returns True for (string) if string is palindrome, regardles H/Lcase
    """
    Validate the string to be palindrome.
    ignores lower upper case

    :param str: string of characters
    :return: bool value True for str is palindrome
    """
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(string: str) -> bool:   #Returns True for (str) cheking only alfanumerics regardless HLcase
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


print(is_palindrome_sentence('1D...o sdsagx£$eese see God1'))
print(is_palindrome_sentence('1Do geese #*#%*$@^#(see God1'))
print(is_palindrome_sentence('1Do gee,.,.se see God1'))
print(is_palindrome_sentence('1Do geese see God1'))
print(is_palindrome_sentence('1Do gees    e see God1'))
print(is_palindrome_sentence('1Do gee#$%@%^#*@#%se see God1'))
print(is_palindrome_sentence('Do geese see God'))
print(is_palindrome_sentence('DoOd'))