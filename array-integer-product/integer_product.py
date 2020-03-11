# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of
# all of the other numbers in the array

# Follow up, what if you can't use division?

from functools import reduce

# Brute force approach
# calculate all values in entirety
# def integer_product(nums):
#     result = []
#     for i in range(len(nums)):
#         value = 1
#         for j in range(len(nums)):
#             if j != i:
#                 value *= nums[j]
#         result.append(value)
#     return result

# Simple optimization to first
# calculate total product
# divide by each integer for index value
# def integer_product(nums):
#     product = reduce(lambda x, y: x * y, nums)
#     result = []
#     for num in nums:
#         result.append(product / num)
#     return result


# without division
# multiply by inverse
# same as above
def integer_product(nums):
    product = reduce(lambda x, y: x * y, nums)
    result = []
    for num in nums:
        result.append(product * (1 / num))
    return result


def test_1():
    assert (integer_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])


def test_2():
    assert (integer_product([3, 2, 1]) == [2, 3, 6])


def test_3():
    assert (integer_product([1, 2]) == [2, 1])
