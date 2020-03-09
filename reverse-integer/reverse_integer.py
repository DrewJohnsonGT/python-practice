# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit
# signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Casting to string and reversing using
# string indexing
def reverse_int(x):
    result = 0
    reversed_num = str(x)[::-1]
    result = int('-' + reversed_num[:-1]) if x < 0 else int(reversed_num)
    return 0 if abs(result) > 0x7FFFFFFF else result

# With integer math
# use modulus to repeatedly 'pop'
# integer and push in reverse to new value
# check for overflow after
# def reverse_int(x):
#     digits = []
#     if x == 0:
#         return 0
#     remains = abs(x)
#     sign = -1 if x < 0 else 1
#     while(True):
#         # remains is not zero
#         digit = remains % 10
#         remains = remains // 10
#         digits.append(digit)
#         if remains == 0:
#             break
#     ret = 0
#     for i in digits:
#         ret *= 10
#         ret += i

#     ret *= sign
#     if abs(ret) > 0x7FFFFFFF:
#         return 0
#     else:
#         return ret


def test_1():
    assert (reverse_int(123) == 321)


def test_2():
    assert (reverse_int(-123) == -321)


def test_3():
    assert (reverse_int(120) == 21)
