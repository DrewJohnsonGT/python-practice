# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Empty string return 0

# Built in find operator
# def strStr(haystack, needle):
#     return haystack.find(needle)

# Naive approach
# simple iteration and string slicing
# def strStr(haystack, needle):
#     # Edge cases
#     if not needle:
#         return 0
#     if len(needle) > len(haystack):
#         return -1
#     i = 0
#     # string slicing is costly
#     while i < len(haystack) - len(needle) + 1:
#         if haystack[i:i + len(needle)] == needle:
#             return i
#         i += 1
#     return -1


# building match string
# two pointers
def strStr(haystack, needle):
    # Edge cases
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1
    i = 0

    while i < len(haystack) - len(needle) + 1:
        if haystack[i] == needle[0]:
            # use j to check for reset of needle
            n, j = '', 0
            while j < len(needle) and haystack[i + j] == needle[j]:
                n += haystack[i + j]
                j += 1
            if n == needle:
                return i
        i += 1
    return -1


def test_1():
    assert (strStr(haystack="hello", needle="ll") == 2)


def test_2():
    assert (strStr(haystack="aaaaa", needle="bba") == -1)


def test_3():
    assert (strStr(haystack="testingthis", needle="this") == 7)
