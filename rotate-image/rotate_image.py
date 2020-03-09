# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).

# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Confused with getting transpose, but leaving in
# Naive way - rotate items accross diagonal
# iterate over values, if x index != y index swap with
# value of switched cordinates (x = y, y = x)
# def rotate_image(matrix):
#     for y in range(len(matrix)):
#         for x in range(len(matrix)):
#             if x < y:
#                 current_cell = matrix[x][y]
#                 matrix[x][y] = matrix[y][x]
#                 matrix[y][x] = current_cell
#     return matrix


# Naive way - rotate all values
# (after drawing it out)
# Take values above/right of diagonal
# determine all rotated values location
# v1 = x, y
# v2 = size - y, x
# v3 = y, x
# v4 = y, size - x
def rotate_image(matrix):
    # relative to 0 based index
    size = len(matrix)
    # only for one quadrant
    for x in range(size // 2 + size % 2):
        for y in range(size // 2):
            v1 = matrix[x][y]
            v2 = matrix[size - 1 - y][x]
            v3 = matrix[size - 1 - x][size - 1 - y]
            v4 = matrix[y][size - 1 - x]
            matrix[x][y] = v2
            matrix[size - 1 - y][x] = v3
            matrix[size - 1 - x][size - 1 - y] = v4
            matrix[y][size - 1 - x] = v1
    return matrix


def test_1():
    assert (rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1],
                                                                [8, 5, 2],
                                                                [9, 6, 3]])


def test_2():
    assert (rotate_image([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7],
                          [15, 14, 12, 16]]) == [[15, 13, 2, 5], [14, 3, 4, 1],
                                                 [12, 6, 8, 9],
                                                 [16, 7, 10, 11]])
