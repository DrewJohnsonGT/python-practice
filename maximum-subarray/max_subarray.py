# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution
# using the divide and conquer approach, which is more subtle.

# Brute force approach
# calculate all possible contiguous subarrays
# def max_subarray(nums):
#     if len(nums) == 1:
#         return nums[0]
#     result = float('-inf')
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             result = max(result, sum(nums[i:j + 1]))
#     return result

# Iterative apprach with two pointers
# array is contiguous
# get local maximum value at each step
# results in global maximum
# def max_subarray(nums):
#     n = len(nums)
#     curr_sum = max_sum = nums[0]

#     for i in range(1, n):
#         curr_sum = max(nums[i], curr_sum + nums[i])
#         max_sum = max(max_sum, curr_sum)

#     return max_sum


# Dynamic programming
# modify array in place
# change values to local max
# track highest local maximum
def max_subarray(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        # negative values will never help
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        max_sum = max(nums[i], max_sum)
    return max_sum


def test_1():
    assert (max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)


def test_2():
    assert (max_subarray([1]) == 1)


def test_3():
    assert (max_subarray([-2, 1]) == 1)


def test_4():
    assert (max_subarray([-2, -1]) == -1)