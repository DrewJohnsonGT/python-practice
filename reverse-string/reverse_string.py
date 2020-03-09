# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Build in method
# def reverse_string(s):
#     s.reverse()

# Iterate over half of the array
# swapping values with value at index
# length - index
import math


def reverse_string(s):
    size = len(s) - 1
    for i in range(math.ceil(size / 2)):
        curr = s[i]
        swap = s[size - i]
        s[i] = swap
        s[size - i] = curr


# cleaner solution assigning/swapping
# iterating with two pointers
# def reverse_string(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left, right = left + 1, right - 1


def test_1():
    test_list = ["h", "e", "l", "l", "o"]
    reverse_string(test_list)
    assert (test_list == ["o", "l", "l", "e", "h"])


def test_2():
    test_list = ["H", "a", "n", "n", "a", "h"]
    reverse_string(test_list)
    assert (test_list == ["h", "a", "n", "n", "a", "H"])


def test_3():
    test_list = [
        "A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",",
        " ", "a", " ", "c", "a", "n", "a", "l", ":", " ", "P", "a", "n", "a",
        "m", "a"
    ]
    reverse_string(test_list)
    assert (test_list == [
        "a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ",
        "a", " ", ",", "n", "a", "l", "p", " ", "a", " ", ",", "n", "a", "m",
        " ", "A"
    ])
