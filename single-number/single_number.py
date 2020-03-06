# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Naive approach - using extra memory and O(2n) worst case
# Track existing value count with map
# def single_number(nums):
#     duplicates = {}
#     for num in nums:
#         if num in duplicates:
#             duplicates[num] += 1
#         else:
#             duplicates[num] = 1
#     for key in duplicates:
#         if duplicates[key] == 1:
#             return key

# Every element but one should occur twice
# sum(set(nums)) - sum(nums) would be all except single occurance num
# def single_number(nums):
#     return 2 * sum(set(nums)) - sum(nums)


# Use bitwise XOR (exclusive OR) on successive numbers
# two XOR operations on same number and 0 will cancel out
# remainder is the single occurance
def single_number(nums):
    value = 0
    for i in nums:
        value ^= i
    return value


def test_1():
    assert (single_number([2, 2, 1]) == 1)


def test_2():
    assert (single_number([4, 1, 2, 1, 2]) == 4)
