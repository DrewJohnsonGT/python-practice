# Shuffle a set of numbers without duplicates.

import random


# using auxillary array
class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.shuffled = list(nums)
        self.is_shuffled = False

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        _new_shuffled = []
        _old_nums = list(self.nums)
        for _ in range(len(self.nums)):
            index = random.randrange(len(_old_nums))
            _new_shuffled.append(_old_nums.pop(index))
        self.is_shuffled = True
        self.shuffled = _new_shuffled
        return _new_shuffled


# swapping elements in place
class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.shuffled = list(nums)
        self.is_shuffled = False

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.is_shuffled = False
        self.shuffled = list(self.nums)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums
        size = len(nums)
        for i in range(size):
            # swap value with any of remaining values (including self)
            index = random.randrange(i, size)
            nums[i], nums[index] = nums[index], nums[i]
        self.shuffle = nums
        self.is_shuffled = True
        return nums
