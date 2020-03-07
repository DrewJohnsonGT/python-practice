# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Brute force approach
# try successive combinations until target met
# def two_sum(nums, target):
#     i = j = 0
#     while i < len(nums):
#         print(f'i: {i}; j: {j}')
#         while j < len(nums):
#             if i != j:
#                 print(f'nums[i]: {nums[i]}; nums[j]: {nums[j]}')
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#             j += 1
#         j = 0
#         i += 1


# Create map of values to indices (assuming no duplicates)
# iterate once over nums, checking map for target - value
# Improvement - as we build map - check for valid results
def two_sum(nums, target):
    values = {}
    for index, num in enumerate(nums):
        if target - num in values:
            return [values[target - num], index]
        values[num] = index


def test_1():
    assert (sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1])


def test_2():
    assert (sorted(two_sum([2, 7, 11, 15], 26)) == [2, 3])
