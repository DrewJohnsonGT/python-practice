# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Brute force approach
# check each row/column/cell combination for validity
# def is_valid_sudoku(board):
#     # check rows
#     # keep track of columns
#     columns = [[] for i in range(9)]
#     for row in board:
#         for column_index, column in enumerate(row):
#             columns[column_index].append(column)
#         just_nums = list(filter(lambda x: x != '.', row))
#         if len(just_nums) != len(set(just_nums)):
#             return False
#     # check columns
#     print(columns)
#     for column_index, column in enumerate(columns):
#         just_nums = list(filter(lambda x: x != '.', column))
#         if len(just_nums) != len(set(just_nums)):
#             return False
#     # check 3x3 sub squares
#     row_offset = col_offset = 0
#     square = []
#     while col_offset < 9:
#         square = []
#         for i in range(row_offset, row_offset + 3):
#             for j in range(col_offset, col_offset + 3):
#                 square.append(board[i][j])
#         just_nums = list(filter(lambda x: x != '.', square))
#         if len(just_nums) != len(set(just_nums)):
#             return False
#         if row_offset == 6:
#             row_offset = 0
#             col_offset += 3
#         else:
#             row_offset += 3
#     return True


# since we know only a few value will be filled in
# make map of values to count for row/col/subsquares
def is_valid_sudoku(board):
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    squares = [{} for i in range(9)]
    for row_index in range(9):
        for column_index in range(9):
            cell = board[row_index][column_index]
            if cell != '.':
                square_index = ((row_index // 3) * 3) + (column_index // 3)
                if cell in rows[row_index] or cell in columns[
                        column_index] or cell in squares[square_index]:
                    return False
                else:
                    rows[row_index][cell] = 1
                    columns[column_index][cell] = 1
                    squares[square_index][cell] = 1
    return True


def test_1():
    assert (is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                             [".", "9", "8", ".", ".", ".", ".", "6", "."],
                             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                             [".", "6", ".", ".", ".", ".", "2", "8", "."],
                             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                             [".", ".", ".", ".", "8", ".", ".", "7",
                              "9"]]) == True)


def test_2():
    assert (is_valid_sudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                             [".", "9", "8", ".", ".", ".", ".", "6", "."],
                             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                             [".", "6", ".", ".", ".", ".", "2", "8", "."],
                             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                             [".", ".", ".", ".", "8", ".", ".", "7",
                              "9"]]) == False)


def test_3():
    assert (is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                             ["6", "8", ".", "1", "9", "5", ".", ".", "."],
                             [".", "9", "8", ".", ".", ".", ".", "6", "."],
                             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                             [".", "6", ".", ".", ".", ".", "2", "8", "."],
                             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                             [".", ".", ".", ".", "8", ".", ".", "7",
                              "9"]]) == False)
