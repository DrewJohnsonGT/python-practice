# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# sort in place
# compare to correct values
# def get_missing(nums):
#     if len(nums) == 1:
#         return 1 if nums[0] == 0 else 0
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1] + 1:
#             return nums[i - 1] + 1

# using a set
# def get_missing(nums):
#     if len(nums) == 1:
#         return 1 if nums[0] == 0 else 0
#     num_set = set(nums)
#     for i in range(len(nums) + 1):
#         if i not in num_set:
#             return i


# Guasses formula
# sum of n integers -
# n(n + 1) / 2
def get_missing(nums):
    expected_sum = (len(nums) * (len(nums) + 1)) // 2
    return expected_sum - sum(nums)


def test_1():
    assert (get_missing([3, 0, 1]) == 2)


def test_2():
    assert (get_missing([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)


def test_3():
    assert (get_missing([0]) == 1)