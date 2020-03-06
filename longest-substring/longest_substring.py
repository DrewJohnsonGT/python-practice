# Given a string, find the length of the longest substring without repeating characters.


def longest_substring(string):
    # Attempt optimizing sliding window approach
    longest_substring_length = 0
    first_index, second_index = 0, 0
    character_map = {}
    # Iterate through characters, mapping latest (rightmost) character
    # location. Using this to skip first index to one character after character last encountered
    for second_index, char in enumerate(string):
        if char in character_map and first_index <= character_map[char]:
            first_index = character_map[char] + 1
        else:
            longest_substring_length = max(longest_substring_length,
                                           second_index - first_index + 1)
        character_map[char] = second_index
    return longest_substring_length


def test_1():
    # 'abc'
    assert longest_substring('abcabcbb') == 3


def test_2():
    # 'b'
    assert longest_substring('bbbbb') == 1


def test_3():
    # 'wke'
    assert longest_substring('pwwkew') == 3


def test_4():
    # 'wke'
    assert longest_substring('testtestyeats') == 5


def test_5():
    #  ' '
    assert longest_substring(' ') == 1


def test_6():
    #  ''
    assert longest_substring('') == 0


# def longest_substring(string):
#     # Attempt sliding window approach
#     # Maintain references to two points
#     # Incrementally adjust and compare existing values using map (dict)
#     longest_substring_length = 0
#     first_index, second_index = 0, 0
#     character_set = set()
#     while first_index < len(string) and second_index < len(string):
#         # push second index forward if character not repeated
#         if string[second_index] not in character_set:
#             character_set.add(string[second_index])
#             second_index += 1
#             longest_substring_length = max(longest_substring_length, second_index - first_index)
#         else:
#             # increment first_index
#             character_set.remove(string[first_index])
#             first_index += 1

#     return longest_substring_length

# def longest_substring(string):
#     # brute force - loop over characters
#     # attempt to generate non-repeating string
#     # track largest and return
#     longest_substring = ''
#     for character_index in range(len(string)):
#         print(f'character_index: {character_index}')
#         current_substring = ''
#         # loop from that point in the string onwards
#         for character in string[character_index:]:
#             print(f'character{character}')
#             if character not in current_substring:
#                 current_substring += character
#             else:
#                 break
#         if len(current_substring) > len(longest_substring):
#             longest_substring = current_substring

#     return len(longest_substring)