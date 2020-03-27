# Reverse bits of a given 32 bits unsigned integer.


# take LSB off one at a time and
# build new integer
def reverse(n):
    # get LSB by AND with 1
    MASK = 1
    result = 0
    while n != 0:
        bit = n & MASK
        n >>= 1
        result |= bit
        result <<= 1
    result >>= 1
    return result


def test_1():
    assert (reverse(0b00000010100101000001111010011100) ==
            0b00111001011110000010100101000000)


def test_2():
    assert (reverse(0b11111111111111111111111111111101) ==
            0b10111111111111111111111111111111)
