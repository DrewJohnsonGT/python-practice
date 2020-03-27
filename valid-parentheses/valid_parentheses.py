# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


def is_valid_parentheses(s):
    PARENS = [{
        'o': '{',
        'c': '}',
    }, {
        'o': '(',
        'c': ')',
    }, {
        'o': '[',
        'c': ']',
    }]
    last_open = []
    # check that most recently opened is closed first
    for char in s:
        for paren in PARENS:
            if char == paren['o']:
                last_open.append(char)
            if char == paren['c']:
                if last_open:
                    last = last_open.pop()
                    if last != paren['o']:
                        return False
                else:
                    return False
    return len(last_open) == 0


def test_1():
    assert (is_valid_parentheses('()') == True)


def test_2():
    assert (is_valid_parentheses('()[]{}') == True)


def test_3():
    assert (is_valid_parentheses('(]') == False)


def test_4():
    assert (is_valid_parentheses('([)]') == False)


def test_5():
    assert (is_valid_parentheses('{[]}') == True)


def test_6():
    assert (is_valid_parentheses('[([]])') == False)
