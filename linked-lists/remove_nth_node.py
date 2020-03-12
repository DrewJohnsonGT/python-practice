from singly_linked_list import ListNode
from ll_helpers import create_linked_list

# Given a linked list, remove the n-th node from the end of list and return its head.

# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.


def remove_node(n):
    pass


def test_1():
    ll = create_linked_list([1, 2, 3, 4, 5])
    expected_result = create_linked_list([1, 2, 3, 5])
    assert (remove_node(ll) == expected_result)
