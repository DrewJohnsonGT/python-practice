# Given an array of integers - find the combination of them that
# forms the largest integer value

from itertools import permutations
from functools import cmp_to_key

# Naive/Brute Force method
# Try all possible combinations
# def largest_integer(nums):
#     largest = 0
#     # Could use itertools to get all permutations
#     # Could also manually get permuations
#     for permutation in permutations(nums):
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
# def largest_integer(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(n - i - 1):
#             if compare_digits(nums[j], nums[j + 1]):
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     print(nums)
#     return int(''.join(map(lambda i: str(i), nums)))

# # Returns True if d1 < d2
# # False if d1 >= d2
# def compare_digits(d1, d2):
#     # compare two combinations of values
#     # to see which is greater int
#     d1d2 = int(str(d1) + str(d2))
#     d2d1 = int(str(d2) + str(d1))
#     return True if d1d2 < d2d1 else False


# Custom comparator - same as above, just returns
# integer values (1, -1, 0)
def compare_digits(d1, d2):
    # compare two combinations of values
    # to see which is greater int
    d1d2 = int(str(d1) + str(d2))
    d2d1 = int(str(d2) + str(d1))
    if d1d2 < d2d1:
        return 1
    if d2d1 < d1d2:
        return -1
    return 0


# Refactored to use sorted and comparator
def largest_integer(nums):
    nums.sort(key=cmp_to_key(compare_digits))
    nums[:] = map(lambda x: str(x), nums)
    return int(''.join(nums))


def test_1():
    assert (largest_integer([10, 7, 76, 415]) == 77641510)


def test_2():
    assert (largest_integer([123, 456, 7, 90]) == 907456123)


def test_3():
    assert (largest_integer([9, 8, 7, 6, 5]) == 98765)
