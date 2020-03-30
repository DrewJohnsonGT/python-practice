# Given an integer k and a string s, find the length of the
# longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring
# with k distinct characters is "bcb".


def longest_substring(string, k):
    if len(string) == 0 or k == 0:
        return ''
    low = high = 0
    characters = {}
    longest = string[0]
    while high < len(string):
        # add next character to map
        next_char = string[high]
        characters[next_char] = high
        # if map length > k
        # move lower pointer to most
        # recent reference of end character
        if len(characters) > k:
            old_low = characters[string[low]]
            del characters[string[low]]
            low = old_low + 1
        # update longest if necessary
        if high - low > len(longest):
            longest = string[low:high + 1]
        high += 1

    return longest


def test_1():
    assert (longest_substring('abcba', 2) == 'bcb')


def test_2():
    assert (longest_substring('abcba', 3) == 'abcba')
