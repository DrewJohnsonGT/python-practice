# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


# brute force approach
# for each value
# check for all divisors
# extremely inefficient
# def count_primes(n):
#     num_primes = 0
#     for i in range(2, n):
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             num_primes += 1
#     return num_primes

from math import sqrt, ceil


# better iterative approach
# only need to check up to square root of n
# for divisors and mark multiples less than n
# as not prime if
def count_primes(n):
    primes = [False, False] + [True] * (n - 2)
    root = ceil(sqrt(n))
    for i in range(2, root):
        if primes[i] == True:
            for j in range(i * i, n, i):
                primes[j] = False
    return primes.count(True)


def test_1():
    assert(count_primes(10) == 4)


def test_2():
    assert(count_primes(12) == 5)


def test_3():
    assert(count_primes(36) == 11)
