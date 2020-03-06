# Given an array, rotate the array to the right by k steps, where k is non-negative.


def rotate_array(array, k):
    rotation = k % len(array)
    for _ in range(rotation):
        # remove from right and push to left
        num = array.pop()
        array.insert(0, num)


# (not in-place)
# modulus of rotation input to account for greater than array length
# split array by rotation point
# def rotate_array(array, k):
#     rotation = -(k % len(array))
#     return [*array[rotation:], *array[:rotation]]


def test_1():
    input_array = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(input_array, 3)
    assert (input_array == [5, 6, 7, 1, 2, 3, 4])


def test_2():
    input_array = [-1, -100, 3, 99]
    rotate_array(input_array, 2)
    assert (input_array == [3, 99, -1, -100])
