# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
#  Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However,
# the numeral for four is not IIII. Instead, the number four is written as IV. Because the
# one is before the five we subtract it making four. The same principle applies to the number
# nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.


# strip off each decimal place
# convert to roman and generate string
def int_to_roman(num):
    ROMANS = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }

    result = ''
    decimal_index = 10
    # iteratively strip each decimal place
    while num > 0:
        value = num % decimal_index
        num -= value
        curr_result = ''
        while value > 0:
            max_roman = max(x for x in ROMANS.keys() if x <= value)
            curr_result += ROMANS[max_roman]
            value -= max_roman
        decimal_index *= 10
        result = curr_result + result
    return result


def test_1():
    assert (int_to_roman(3) == 'III')


def test_2():
    assert (int_to_roman(4) == 'IV')


def test_3():
    assert (int_to_roman(58) == 'LVIII')
