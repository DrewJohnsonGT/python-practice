# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.


# Naive method - strip invalid characters
# convert to lowercase
# two pointers on either side - checking for same values
def is_valid_palindrome(s):
    pass


def test_1():
    assert (is_valid_palindrome('A man, a plan, a canal: Panama') == True)


def test_2():
    assert (is_valid_palindrome('race a car') == False)


def test_3():
    assert (is_valid_palindrome('') == True)
