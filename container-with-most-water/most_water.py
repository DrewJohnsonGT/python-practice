# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# brute force
# check all possible combinations
# def max_area(heights):
#     curr_max = 0
#     for i in range(len(heights)):
#         for j in range(i + 1, len(heights)):
#             curr_area = min(heights[i], heights[j]) * (j - i)
#             curr_max = max(curr_max, curr_area)
#     return curr_max


# sliding window approach
# two pointers starting at opposite ends
def max_area(heights):
    low, high = 0, len(heights) - 1
    result = 0
    while low < high:
        low_value = heights[low]
        high_value = heights[high]
        curr_max = min(low_value, high_value) * (high - low)
        result = max(result, curr_max)
        if low_value >= high_value:
            high -= 1
        else:
            low += 1
    return result


def test_1():
    assert (max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
