from singly_linked_list import ListNode
from ll_helpers import create_linked_list

# Given a singly linked list, determine if it is a palindrome.


# iterate over list
# create python list
# iterate and check values
def is_palindrome(n):
    l = []
    while n != None:
        l.append(n.val)
        n = n.next
    for i in range(len(l) // 2):
        if l[i] != l[len(l) - i - 1]:
            return False
    return True


def test_1():
    l = create_linked_list([1, 2])
    assert (is_palindrome(l) == False)


def test_2():
    l = create_linked_list([1, 2, 2, 1])
    assert (is_palindrome(l) == True)
