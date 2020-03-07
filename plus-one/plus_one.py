# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Convert array to number, add one, and convert back
# def plus_one(num_list):
#     str_list = map(lambda x: str(x), num_list)
#     num = int(''.join(str_list)) + 1
#     return [int(x) for x in str(num)]


# iterate over list backwards
# add one - carry to next significant bit if necessary (value is 9)
# otherwise break and return
def plus_one(num_list):
    i = len(num_list) - 1
    while i >= 0:
        print(num_list[i])
        if num_list[i] != 9:
            num_list[i] += 1
            return num_list
        else:
            num_list[i] = 0
            if i == 0:
                num_list.insert(0, 1)
                return num_list
            i -= 1


def test_1():
    assert (plus_one([1, 2, 3]) == [1, 2, 4])


def test_2():
    assert (plus_one([4, 3, 2, 1]) == [4, 3, 2, 2])


def test_3():
    assert (plus_one([0]) == [1])


def test_4():
    assert (plus_one([9, 9]) == [1, 0, 0])
