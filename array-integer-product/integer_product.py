# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of
# all of the other numbers in the array

# Follow up, what if you can't use division?


def integer_product(nums):
    pass


def test_1():
    assert(integer_product([120, 60, 40, 30, 24]) == [1, 2, 3, 4, 5])


def test_2():
    assert(integer_product([3, 2, 1]) == [2, 3, 6])


def test_3():
    assert(integer_product([1, 2]) == [2, 1])
