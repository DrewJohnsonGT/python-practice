# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# sort by length reversed
# iteratively compare prefix overlap
# doesn't work if order matters
# def longest(strs):
#     if len(strs) == 0:
#         return ""
#     if len(strs) == 1:
#         return strs[0]
#     strs.sort(key=lambda x: len(x))
#     prefix = strs[0]
#     for i in range(0, len(strs)):
#         curr = strs[i]
#         if prefix not in curr:
#             # iterate accross current string
#             # comparing to prefix
#             j = 0
#             while curr[j] == prefix[j]:
#                 j += 1
#             if j == 0:
#                 return ''
#             prefix = curr[0:j]
#     return prefix


# iteratively compare prefix overlap
def longest(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    prefix = strs[0]
    for i in range(1, len(strs)):
        curr = strs[i]
        # iterate accross current string
        # comparing to prefix
        j = 0
        while j < len(curr) and j < len(prefix) and curr[j] == prefix[j]:
            j += 1
        if j == 0:
            return ''
        prefix = curr[0:j]
    return prefix


def test_1():
    assert (longest(["flower", "flow", "flight"]) == "fl")


def test_2():
    assert (longest(["dog", "racecar", "car"]) == "")


def test_3():
    assert (longest(["dog", "dogtest", "dog", "dogtest"]) == "dog")


def test_4():
    assert (longest(["", "dog", "dogtest", "dog", "dogtest"]) == "")


def test_5():
    assert (longest(["c", "acc", "ccc"]) == "")
