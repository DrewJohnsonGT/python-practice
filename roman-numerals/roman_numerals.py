# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1 - mult
# V             5
# X             10 - mult
# L             50
# C             100 - mult
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However,
#  the numeral for four is not IIII. Instead, the number four is written as IV. Because
# the one is before the five we subtract it making four. The same principle applies to
# the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


def roman_to_int(roman):


def test_1():
    assert(roman_to_int('III') == 3)


def test_2():
    assert(roman_to_int('IV') == 4)


def test_3():
    assert(roman_to_int('IX') == 9)


def test_4():
    assert(roman_to_int('LVIII') == 58)


def test_5():
    assert(roman_to_int('MMMCMXCIX') == 3999)
