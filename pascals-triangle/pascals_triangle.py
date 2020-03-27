# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


# iteratively calculate
def get_pascals(numRows):
    result = []
    if numRows > 0:
        result.append([1])
    if numRows > 1:
        result.append([1, 1])
    for i in range(2, numRows):
        row = [1]
        prev = result[i - 1]
        for j in range(0, len(prev) - 1):
            row.append(prev[j] + prev[j + 1])
        row.append(1)
        result.append(row)
    return result


def test_1():
    assert (get_pascals(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                               [1, 4, 6, 4, 1]])


def test_2():
    assert (get_pascals(1) == [[1]])
