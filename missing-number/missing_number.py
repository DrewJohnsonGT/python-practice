# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.


# sort in place
# compare to correct values
def get_missing(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            return nums[i - 1] + 1


def test_1():
    assert (get_missing([3, 0, 1]) == 2)


def test_2():
    assert (get_missing([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)
