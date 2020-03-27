# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

# convert to string
# check characters
# def ones(n):
#     return str(bin(n)).count('1')


# use mask to check actual bits
def ones(n):
    bits = 0
    mask = 1
    for _ in range(32):
        if (n & mask) != 0:
            bits += 1
        mask <<= 1
    return bits


# cache 'chunks' of bits that we have calculated
# check cache before recalculating


def test_1():
    assert (ones(0b00000000000000000000000000001011) == 3)


def test_2():
    assert (ones(0b00000000000000000000000010000000) == 1)


def test_3():
    assert (ones(0b11111111111111111111111111111101) == 31)
