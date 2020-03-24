# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number
# and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


# simply map over range of n values
# def fizz_bizz(n):
#     def get_value(i):
#         if i % 3 == 0 and i >= 3:
#             if i % 5 == 0:
#                 return 'FizzBuzz'
#             else:
#                 return 'Fizz'
#         else:
#             if i % 5 == 0 and i >= 5:
#                 return 'Buzz'
#             else:
#                 return str(i)
#     return list(map(lambda x: get_value(x), range(1, n + 1)))

# Cleaner approach - concatentate strings
# use mapping of multiples
def fizz_bizz(n):
    multiples = {3: 'Fizz', 5: 'Buzz'}
    result = []
    for i in range(1, n + 1):
        res_str = ''
        for multiple in multiples:
            if i % multiple == 0:
                res_str += multiples[multiple]
        if not res_str:
            res_str = str(i)
        result.append(res_str)
    return result


def test_1():
    assert(fizz_bizz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ])
