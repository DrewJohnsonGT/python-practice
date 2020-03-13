from singly_linked_list import ListNode
from ll_helpers import create_linked_list

# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?


# iteratively swap values
# n - index times
# def reverse(n):
#     # 0 and 1 size
#     if n == None or n.next == None:
#         return n
#     # first pass get index while swapping
#     curr = n
#     swapping = n
#     size = 1
#     while swapping.next != None:
#         next_val = swapping.next.val
#         swapping.next.val = swapping.val
#         swapping.val = next_val
#         swapping = swapping.next
#         size += 1
#     swaps = size - 1
#     # now swap the rest size - index times
#     while swaps > 0:
#         swapping = curr
#         for _ in range(swaps - 1):
#             next_val = swapping.next.val
#             swapping.next.val = swapping.val
#             swapping.val = next_val
#             swapping = swapping.next
#         swaps -= 1
#     return n

# recursive solution
def reverse(n):
    return reverse_ll(n)

# create stacks down to last node
# push current node to end
# previous stack points to current node


def reverse_ll(n):
    if n == None or n.next == None:
        return n
    rest_reversed = reverse_ll(n.next)
    n.next.next = n
    n.next = None
    return rest_reversed
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# 1 -> 2 -> 3 -> 4 -> None
#               /
#              5
# 1 -> 2 -> 3 -> None
#          /
#         4
#        /
#       5 ...


def test_1():
    ll = create_linked_list([1, 2])
    expected_result = create_linked_list([2, 1])
    assert (reverse(ll) == expected_result)


def test_2():
    ll = create_linked_list([1, 2, 3, 4, 5])
    expected_result = create_linked_list([5, 4, 3, 2, 1])
    assert (reverse(ll) == expected_result)
