# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Recursive approach
# ith step is = ith step minus 1 + ith step minus 2
# def climb_stairs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return climb_stairs(n - 1) + climb_stairs(n - 2)

# recursive solution with caching of values
# def climb_stairs(n, cache={1: 1, 2: 2}):
#     if n in cache:
#         return cache[n]
#     cache[n] = climb_stairs(n - 1, cache) + climb_stairs(n - 2, cache)
#     return cache[n]

# Iterative approach - dynamic programming
# store values of n - x calculations in array
# next value == previous two values combined
# def climb_stairs(n):
#     l = [1, 2]
#     i = 2
#     while i < n:
#         l.append(l[i - 1] + l[i - 2])
#         i += 1
#     return l[n - 1]


# Iterative approach - dynamic programming
# Without using list
def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # track two previous values
    i = 3
    x = 2
    curr = prev = 3
    while i < n:
        prev = curr
        curr = prev + x
        x = prev
        i += 1
    return curr


def test_1():
    assert (climb_stairs(2) == 2)


def test_2():
    assert (climb_stairs(3) == 3)


def test_3():
    assert (climb_stairs(4) == 5)


def test_4():
    assert (climb_stairs(5) == 8)


def test_5():
    assert (climb_stairs(38) == 63245986)
