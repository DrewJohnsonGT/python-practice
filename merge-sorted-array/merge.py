# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6]       n = 3

# Output: [1,2,2,3,5,6]

# iterate over both arrays at same time
# comparing values and incrementing
# pointer in arr to lower value
# def merge(nums1, m, nums2, n):
#     filter(lambda x: x, nums1)
#     if m == 0 and n == 0:
#         return []
#     result = []
#     i = j = 0
#     while i < m or j < n:
#         v1 = nums1[i] if i < m else float('inf')
#         v2 = nums2[j] if j < n else float('inf')
#         if v1 <= v2:
#             result.append(v1)
#             i += 1
#         if v2 < v1:
#             result.append(v2)
#             j += 1
#     nums1[:] = result


# if you start from end of arrays
# you can modify nums1 in place
# def merge(nums1, m, nums2, n):
def merge(nums1, m, nums2, n):
    if m == 0 and n == 0:
        return []
    i, j, x = m - 1, n - 1, m + n - 1
    while x >= 0:
        v1 = nums1[i] if i >= 0 else float('-inf')
        v2 = nums2[j] if j >= 0 else float('-inf')
        if v1 >= v2:
            nums1[x] = v1
            i -= 1
        else:
            nums1[x] = v2
            j -= 1
        x -= 1


def test_1():
    list1 = [1, 2, 3, 0, 0, 0]
    merge(list1, 3, [2, 5, 6], 3)
    assert (list1 == [1, 2, 2, 3, 5, 6])
