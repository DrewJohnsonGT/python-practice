from singly_linked_list import ListNode
from ll_helpers import create_linked_list, create_cyclic_linked_list

# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an
# integer pos which represents the position (0-indexed)
# in the linked list where tail connects to. If pos is -1,
# then there is no cycle in the linked list.

# use map to track nodes/index
# if node has been seen return index
# def has_cycle(n):
#     if n == None:
#         return False
#     nodes = {}
#     index = 0
#     while n.next != None:
#         if n in nodes:
#             # return nodes[n]
#             return True
#         nodes[n] = index
#         n = n.next
#         index += 1
#     return False


# two pointer iteration
# fast/slow - detect overlap
def has_cycle(n):
    if n == None or n.next == None:
        return False
    slow = n
    fast = n.next
    while slow is not fast:
        # end of list
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


def test_1():
    l = create_cyclic_linked_list([1, 2, 3, 4], 2)
    assert (has_cycle(l) == True)


def test_2():
    l = create_linked_list([1])
    assert (has_cycle(l) == False)


def test_3():
    l = create_cyclic_linked_list([1, 2], 1)
    assert (has_cycle(l) == True)
