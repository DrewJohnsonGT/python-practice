# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

# iterative approach - very innefficient
# def contains_fresh_orange(oranges):
#     for row in oranges:
#         if 1 in row:
#             return True
#     return False

# def oranges_rotting(grid):
#     height = len(grid)
#     width = len(grid[0])
#     minutes = 0
#     num_rotten = 0
#     while True:
#         prev_rotten = num_rotten
#         to_be_rotten = []
#         for i in range(height):
#             for j in range(width):
#                 if (grid[i][j] == 2):
#                     # UP/DOWN/LEFT/RIGHT
#                     if j > 0:
#                         if grid[i][j - 1] == 1:
#                             to_be_rotten.append((i, j - 1))
#                     if j < width - 1:
#                         if grid[i][j + 1] == 1:
#                             to_be_rotten.append((i, j + 1))
#                     if i > 0:
#                         if grid[i - 1][j] == 1:
#                             to_be_rotten.append((i - 1, j))
#                     if i < height - 1:
#                         if grid[i + 1][j] == 1:
#                             to_be_rotten.append((i + 1, j))
#         for i, j in to_be_rotten:
#             grid[i][j] = 2
#         num_rotten += len(to_be_rotten)
#         if prev_rotten == num_rotten:
#             break
#         minutes += 1
#     return -1 if contains_fresh_orange(grid) else minutes

import collections


# using tree representation and BFS to iteratively assign rotten status
# keep track of depth and last traversed will be minutes required
def oranges_rotting(grid):
    height = len(grid)
    width = len(grid[0])
    queue = collections.deque()
    # build queue
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == 2:
                queue.append((i, j, 0))

    minutes = 0
    while queue:
        (i, j, curr_minutes) = queue.popleft()
        for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= ni < height and 0 <= nj < width:
                if grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, curr_minutes + 1))
                    minutes = curr_minutes + 1

    return minutes if not any([1 in row for row in grid]) else -1


def test_1():
    assert (oranges_rotting(
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]) == 4)


def test_2():
    assert (oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1)


def test_3():
    assert (oranges_rotting([[0, 2]]) == 0)
