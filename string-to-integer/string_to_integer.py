# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the
# first non-whitespace character is found. Then, starting from this character, takes
# an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace
# characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.


# iterate accross characters
# relatively straightforward method
def string_to_int(s):
    if not s:
        return 0
    result = 0
    sign = 1
    starting_index = 0
    for char in s:
        if char.isnumeric() or char == '-' or char == '+':
            break
        if char != ' ':
            return 0
        starting_index += 1
    # if starting index is sign - adjust sign
    if starting_index != len(s) and s[starting_index] == '-':
        sign = -1
    if char == '-' or char == '+':
        starting_index += 1
    if starting_index == len(s):
        return 0
    # parse until end of number
    ending_index = starting_index
    while ending_index < len(s) and s[ending_index].isnumeric():
        ending_index += 1
    if starting_index == ending_index:
        return 0
    result = int(s[starting_index:ending_index]) * sign
    if abs(result) > 2**31 - 1:
        if sign == 1:
            result = 2**31 - 1
        else:
            result = -2**31
    return result


def test_1():
    assert(string_to_int('42') == 42)


def test_2():
    assert(string_to_int('      -42') == -42)


def test_3():
    assert(string_to_int("4193 with words") == 4193)


def test_4():
    assert(string_to_int('words and 987') == 0)


def test_5():
    assert(string_to_int('-91283472332') == -2147483648)
    assert(string_to_int('2147483648') == 2147483647)


def test_6():
    assert(string_to_int('3.14159') == 3)


def test_7():
    assert(string_to_int('+-2') == 0)


def test_8():
    assert(string_to_int('') == 0)
    assert(string_to_int(' ') == 0)
