# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Two pointer approach 
# since array is sorted, move second pointer until next number encountered
# Add new value to first pointer index and increment
def remove_duplicates(array):
    if len(array) == 0: return 0
    i, j = 0, 1
    while j < len(array):
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]
        j += 1
    return i + 1



def test_1():
    array = [1, 1, 2]
    result = remove_duplicates(array)
    assert result == 2
    assert array[:result] == [1, 2]
def test_2():
    array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = remove_duplicates(array)
    assert result == 5
    assert array[:result] == [0, 1, 2, 3, 4]