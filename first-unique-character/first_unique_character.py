# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Note: You may assume the string contain only lowercase letters.


# Check all values and maintain a map of values
# and reference to last unique
def first_unique(s):
    uniques = {}
    duplicates = {}
    for index, char in enumerate(s):
        if char not in duplicates:
            if char in uniques:
                del uniques[char]
                duplicates[char] = 1
            else:
                uniques[char] = index
    result = len(s)
    for key in uniques:
        if uniques[key] < result:
            result = uniques[key]
    return result if result != len(s) else -1


def test_1():
    assert (first_unique('leetcode') == 0)


def test_2():
    assert (first_unique('loveleetcode') == 2)


def test_3():
    assert (first_unique('eeeeeeeeee') == -1)


def test_4():
    assert (first_unique("aadadaad") == -1)


def test_5():
    assert (first_unique('dddccdbba') == 8)
