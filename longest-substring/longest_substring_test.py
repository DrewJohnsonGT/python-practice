from longest_substring import *

def test_1():
    # 'abc'
    assert longest_substring('abcabcbb') == 3
def test_2():
    # 'b'
    assert longest_substring('bbbbb') == 1
def test_3():
    # 'wke'
    assert longest_substring('pwwkew') == 3
def test_4():
    #  ' '
    assert longest_substring(' ') == 1
def test_5():
    #  ''
    assert longest_substring('') == 0