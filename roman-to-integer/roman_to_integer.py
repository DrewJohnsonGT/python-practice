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
# the numeral for four is not IIII. Instead, the number four is written as IV. Because
# the one is before the five we subtract it making four. The same principle applies to
# the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Assign groups of numerals values
# combine them
# def roman_to_int(roman):
#     one_off_values = {
#         'CD': 400,
#         'CM': 900,
#         'XL': 40,
#         'XC': 90,
#         'IV': 4,
#         'IX': 9
#     }
#     standard_values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     result = 0
#     for one_off in one_off_values:
#         if one_off in roman:
#             result += one_off_values[one_off]
#             index = roman.find(one_off)
#             roman = roman[:index] + roman[index + len(one_off):]
#     # iterate successively - adding values
#     for value in roman:
#         result += standard_values[value]
#     return result

# cleaner solution variation
# iterate from right to left
# checking against both mappings
# def roman_to_int(roman):
#     values = {
#         'CD': 400,
#         'CM': 900,
#         'XL': 40,
#         'XC': 90,
#         'IV': 4,
#         'IX': 9,
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     result = 0
#     i = len(roman) - 1
#     while i >= 0:
#         value = 0
#         # check for two character matches
#         if i > 0:
#             chars = roman[i - 1:i + 1]
#             if chars in values:
#                 value = values[chars]
#                 i -= 2
#         if value == 0:
#             value = values[roman[i]]
#             i -= 1
#         result += value
#     return result


# subtract values in one-off cases
def roman_to_int(roman):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = values.get(roman[-1])
    for i in reversed(range(len(roman) - 1)):
        # cases where larger value comes first
        if values[roman[i]] < values[roman[i + 1]]:
            total -= values[roman[i]]
        else:
            total += values[roman[i]]
    return total


def test_1():
    assert (roman_to_int('III') == 3)


def test_2():
    assert (roman_to_int('IV') == 4)


def test_3():
    assert (roman_to_int('IX') == 9)


def test_4():
    assert (roman_to_int('LVIII') == 58)


def test_5():
    assert (roman_to_int('MMMCMXCIX') == 3999)
