# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# sort list, find end of zero(s) index
# remove zeros and append to end
# def move_zeros(nums):
#     nums.sort()
#     zero_index = 0
#     while nums[zero_index] == 0:
#         zero_index += 1
#     del nums[:zero_index]
#     nums.extend([0] * zero_index)
#     return nums


# iterate over once
# when 0 encountered, slice off to end
def move_zeros(nums):
    i = j = 0
    while j < len(nums):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
        else:
            i += 1
        j += 1


def test_1():
    assert (move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0])


def test_2():
    assert (move_zeros([0, 0, 0, 5, 10, 0]) == [5, 10, 0, 0, 0, 0])
