# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
# You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

# Note: Each term of the sequence of integers will be represented as a string.


# Brute force approach
# start with 1 and count up to n
def count_and_say(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"
    s = "11"
    for _ in range(n - 2):
        s = get_next(s)
        print(s)
    return s


def get_next(s):
    # group/count successive values
    # generate result = count + value
    result = ''
    curr = s[0]
    count = 0
    for char in s:
        if char == curr:
            count += 1
        else:
            result += str(count) + curr
            curr = char
            count = 1
    result += str(count) + curr
    return result


def test_1():
    assert (count_and_say(1) == "1")


def test_2():
    assert (count_and_say(4) == "1211")


def test_3():
    assert (count_and_say(5) == "111221")
