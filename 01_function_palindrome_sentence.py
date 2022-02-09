
def ispalindrome(string):           #Returns True for (string) if string is palindrome, regardles H/Lcase
    return string[::-1].casefold() == string.casefold()


def ispalindromesentence(string):   #Returns True for (str) cheking only alfanumerics regardless HLcase
    sent = ''
    for char in string:
        if char.isalnum():
            sent += char
    return sent[::-1].casefold() == sent.casefold()


print(ispalindromesentence('1D...o s23dsagx£$eese see God1'))
print(ispalindromesentence('1Do geese see God1'))
print(ispalindromesentence('1Do gee,.,.se see God1'))
print(ispalindromesentence('1Do geese see God1'))
print(ispalindromesentence('1Do gees    e see God1'))
print(ispalindromesentence('1Do gee#$%^&se see God1'))
print(ispalindromesentence('Do geese see God'))
print(ispalindromesentence('DoOd'))