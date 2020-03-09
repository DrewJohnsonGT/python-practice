# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit
# signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Casting to string and reversing using
# string indexing
def reverse_int(x):
    reversed_num = str(x)[::-1]
    if x < 0:
        return int('-' + reversed_num[:-1])
    else:
        return int(reversed_num)


def test_1():
    assert (reverse_int(123) == 321)


def test_2():
    assert (reverse_int(-123) == -321)


def test_3():
    assert (reverse_int(120) == 21)
