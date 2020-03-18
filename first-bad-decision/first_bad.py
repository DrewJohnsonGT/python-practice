# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version,
# all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the
# first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

# Example:

# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version.


# for local testing
def is_bad_version(n):
    return n >= 4


# assuming the versions are sorted
# start with middle of list
# check if value greater/less than
# successively check middle value of sub-array
# in direction based on value
# def first_bad_version(n):
#     if len(n) == 0:
#         return False
#     index = len(n) // 2
#     while True:
#         if len(n) == 1:
#             return n[index]
#         # update list to lower half
#         if is_bad_version(n[index]):
#             if not is_bad_version(n[index - 1]):
#                 return n[index]
#             n = n[0:index]
#         else:
#             n = n[index:len(n)]
#         index = len(n) // 2


# Binary search using two pointers
# check greater/lower center value
# repeat until
def first_bad_version(n):
    left = 1
    right = n
    while right > left:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left


def test_1():
    assert (first_bad_version(5) == 4)
