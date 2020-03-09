# Given an array of integers - find the combination of them that
# forms the largest integer value

import itertools


# Naive/Brute Force method
# Try all possible combinations
# def largest_integer(nums):
#     largest = 0
#     # Could use itertools to get all permutations
#     # Could also manually get permuations
#     for permutation in itertools.permutations(nums):
#         print(permutation)
#         value = list_to_int(permutation)
#         if value > largest:
#             largest = value
#     return largest


# def list_to_int(l):
#     return int(''.join(map(lambda i: str(i), l)))

# Bubble type sort based on criteria:
# higher most significant digit
# compare successive lower order digits
# smaller digit takes precedence
def largest_integer(nums):
    pass


def compare_digits(d1, d2):
    pass


def test_1():
    assert(largest_integer([10, 7, 76, 415]) == 77641510)


def test_2():
    assert(largest_integer([123, 456, 7, 90]) == 907456123)
