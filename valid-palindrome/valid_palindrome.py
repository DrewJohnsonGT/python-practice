# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

import re
import math
# Naive method - strip invalid characters
# convert to lowercase
# two pointers on either side - checking for same values


# def is_valid_palindrome(s):
#     # two methods to remove invalid characters
#     # regular expression
#     # regex = re.compile('[^\w]')
#     # alphanumeric_string = regex.sub('', s)

#     # filter using isalnum string method
#     alphanumeric_filter = filter(str.isalnum, s)
#     alphanumeric_string = ''.join(alphanumeric_filter).lower()
#     size = len(alphanumeric_string)
#     i, j = 0, size - 1
#     while i < math.ceil(size / 2):
#         if alphanumeric_string[i] != alphanumeric_string[j]:
#             return False
#         i += 1
#         j -= 1
#     return True

# save some cost on invalid cases
# by performing ad hoc alphanumeric filter
# ad hoc
def is_valid_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def test_1():
    assert (is_valid_palindrome('A man, a plan, a canal: Panama') == True)


def test_2():
    assert (is_valid_palindrome('race a car') == False)


def test_3():
    assert (is_valid_palindrome('') == True)


def test_4():
    assert (is_valid_palindrome('a') == True)
