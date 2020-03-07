# Given two arrays, write a function to compute their intersection.

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?

# Make two value -> count maps for each
# Compare to find intersection/min count
# def intersection(nums1, nums2):
#     map1 = get_count_map(nums1)
#     map2 = get_count_map(nums2)
#     result = []
#     for key in map1:
#         if key in map2:
#             min_count = min(map1[key], map2[key])
#             result.extend([key] * min_count)
#     return result

# def get_count_map(nums):
#     result = {}
#     for num in nums:
#         if num not in result:
#             result[num] = 1
#         else:
#             result[num] += 1
#     return result


# If the given arrays are already sorted
def intersection(nums1, nums2):
    # single pointer iterating over both
    # compare values
    # - if same add to result list
    # - if not, increment pointer of smaller value
    result = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        else:
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
    return result


def test_1():
    sorted_result = sorted(intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    assert (sorted_result == [2, 2])


def test_2():
    sorted_result = sorted(
        intersection(nums1=[4, 9, 5, 6, 7, 9, 9, 9, 6], nums2=[9, 4, 9, 8, 4]))
    assert (sorted_result == [4, 9, 9])


def test_3():
    sorted_result = sorted(intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8,
                                                                4]))
    assert (sorted_result == [4, 9])


# Tests for sorted arrays
def test_4():
    assert (intersection([1, 1, 2, 2, 3, 4, 5],
                         [1, 1, 2, 5, 5]) == [1, 1, 2, 5])


def test_5():
    assert (intersection([1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5],
                         [1, 1, 2, 5, 5]) == [1, 1, 2, 5, 5])
