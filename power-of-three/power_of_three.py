# Given an integer, write a function to determine if it is a power of three.
# Could you do it without any loop/recursion?


# iterative division approach
# divide by 3 until equal to one (power of three)
# or less than one (not power)
# def is_power_of_3(n):
#     i = n
#     while True:
#         if i < 1:
#             return False
#         if i == 1:
#             return True
#         i /= 3

# recursive approach
# same as above
# def is_power_of_3(n):
#     if n < 1:
#         return False
#     if n == 1:
#         return True
#     return is_power_of_3(n / 3)

from math import log10


# no loops/recursion
# if we had integer cap we
# could just check if value is divisor of the max
# power of three
# otherwise ->
# n = 3^i
# i log3(n)
# i = logb(n)/logb(3)
def is_power_of_3(n):
    if n == 0:
        return False
    return (log10(n) / log10(3)) % 1 == 0


def test_1():
    assert(is_power_of_3(27) == True)


def test_2():
    assert(is_power_of_3(0) == False)


def test_3():
    assert(is_power_of_3(9) == True)


def test_4():
    assert(is_power_of_3(45) == False)
