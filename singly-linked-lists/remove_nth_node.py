from singly_linked_list import ListNode
from ll_helpers import create_linked_list

# Given a linked list, remove the n-th node from the end of list and return its head.

# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# iterate once to get length
# iterate again to remove nth from end node
# def remove_node(head, n):
#     # length 1 case
#     if head.next == None:
#         return None
#     result = head
#     count = 1
#     curr = head
#     while curr.next != None:
#         curr = curr.next
#         count += 1
#     curr = head
#     # stop one node short
#     for _ in range(count - n - 1):
#         curr = curr.next
#     # head node
#     if count - n - 1 == -1:
#         curr.val = curr.next.val
#         curr.next = curr.next.next
#     else:
#         # tail node
#         if curr.next.next == None:
#             curr.next = None
#         else:
#             curr.next.val = curr.next.next.val
#             curr.next = curr.next.next
#     return result


# Update two pointers
# keep seperation of n
# when tail hit remove other pointer node
def remove_node(head, n):
    # One node
    if head.next == None:
        return None
    j = n
    count = 0
    result = head
    curr = head
    remove = head
    while curr != None:
        curr = curr.next
        count += 1
        if j < 0:
            remove = remove.next
        else:
            j -= 1
    # stopped one value before node to remove
    # head
    if count == n:
        remove.val = remove.next.val
        remove.next = remove.next.next
    else:
        remove.next = remove.next.next
    return result


def test_1():
    ll = create_linked_list([1, 2, 3, 4, 5])
    expected_result = create_linked_list([1, 2, 3, 5])
    assert (remove_node(ll, 2) == expected_result)


def test_2():
    ll = create_linked_list([1])
    expected_result = None
    assert (remove_node(ll, 1) == expected_result)


def test_3():
    ll = create_linked_list([1, 2])
    expected_result = create_linked_list([1])
    assert (remove_node(ll, 1) == expected_result)


def test_4():
    ll = create_linked_list([1, 2])
    expected_result = create_linked_list([2])
    assert (remove_node(ll, 2) == expected_result)