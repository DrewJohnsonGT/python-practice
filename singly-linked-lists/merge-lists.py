from singly_linked_list import ListNode
from ll_helpers import create_linked_list

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.


# Iterate through lists
# if one lists is at end
# add other list values
# otherwise compare and add lower value
# to maintain order
def merge(l1, l2):
    # both lists empty
    if l1 == None and l2 == None:
        return None
    result = ListNode(None)
    curr = result
    while l1 != None or l2 != None:
        if l1 == None:
            curr.next = ListNode(l2.val)
            l2 = l2.next
        elif l2 == None:
            curr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            # both lists have values
            # add the greater value
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
        curr = curr.next
    return result.next


# Recursive approach
# removes need to assess empty list
# edge case
# def merge(l1, l2):
#     if l1 is None:
#         return l2
#     elif l2 is None:
#         return l1
#     elif l1.val < l2.val:
#         l1.next = merge(l1.next, l2)
#         return l1
#     else:
#         l2.next = merge(l1, l2.next)
#         return l2


def test_1():
    ll1 = create_linked_list([1, 2, 4])
    ll2 = create_linked_list([1, 3, 4])
    expected_result = create_linked_list([1, 1, 2, 3, 4, 4])
    assert (merge(ll1, ll2) == expected_result)


def test_2():
    ll1 = create_linked_list([1, 2])
    ll2 = create_linked_list([1, 2])
    expected_result = create_linked_list([1, 1, 2, 2])
    assert (merge(ll1, ll2) == expected_result)


def test_3():
    ll1 = create_linked_list([2])
    ll2 = create_linked_list([1])
    expected_result = create_linked_list([1, 2])
    assert (merge(ll1, ll2) == expected_result)
