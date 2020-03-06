# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Naive way - iterate over array and build list of known values
# Break when existing value is found
# def contains_duplicate(array):
#     duplicates = []
#     for i in array:
#         if i in duplicates:
#             return True
#         else:
#             duplicates.append(i)
#     return False

# Sort array first - increase speed
# def contains_duplicate(array):
#     sorted_list = sorted(array)
#     print(sorted_list)
#     index = 1
#     while index < len(sorted_list):
#         if sorted_list[index] == sorted_list[index - 1]:
#             return True
#         index += 1
#     return False


# cast list to set and compare length
def contains_duplicate(array):
    no_duplicates = set(array)
    print(no_duplicates)
    return len(no_duplicates) != len(array)


def test_1():
    assert (contains_duplicate([1, 2, 3, 1]) == True)


def test_2():
    assert (contains_duplicate([1, 2, 3, 4]) == False)


def test_3():
    assert (contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)
