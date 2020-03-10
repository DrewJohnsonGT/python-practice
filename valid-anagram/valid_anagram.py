# Given two strings s and t , write a function to determine if t is an anagram of s.

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
# Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the
# entire range of unicode characters, which could go up to more than 1 million. A hash table is a
# more generic solution and could adapt to any range of characters.

# Strings must be same length
# create maps of characters
# def is_valid_anagram(s, t):
#     if len(s) != len(t):
#         return False
#     s_map = {}
#     t_map = {}
#     for i in range(len(s)):
#         s_char = s[i]
#         t_char = t[i]
#         if s_char in s_map:
#             s_map[s_char] += 1
#         else:
#             s_map[s_char] = 1
#         if t_char in t_map:
#             t_map[t_char] += 1
#         else:
#             t_map[t_char] = 1
#     for char in s_map:
#         if char not in t_map:
#             return False
#         if t_map[char] != s_map[char]:
#             return False
#     return True


# Sort both strings
# compare values
def is_valid_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def test_1():
    assert (is_valid_anagram('anagram', 'nagaram') == True)


def test_2():
    assert (is_valid_anagram('rat', 'car') == False)


def test_3():
    assert (is_valid_anagram('a', 'b') == False)