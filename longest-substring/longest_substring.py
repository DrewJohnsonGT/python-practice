# Given a string, find the length of the longest substring without repeating characters.




def longest_substring(string):
    # Attempt sliding window approach
    # Maintain references to two points
    # Incrementally adjust and compare existing values using map (dict)
    longest_substring_length = 0
    first_index, second_index = 0, 0
    character_set = set()
    while first_index < len(string) and second_index < len(string):
        # push second index forward if character not repeated
        if string[second_index] not in character_set:
            second_index += 1
            character_set.add(string[second_index])
            longest_substring_length = max(longest_substring_length, second_index - 1 - first_index)
        else:
            # increment first_index
            first_index += 1
            character_set.remove(string[first_index])

    return longest_substring_length





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