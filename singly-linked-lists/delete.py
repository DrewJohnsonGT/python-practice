from singly_linked_list import ListNode
from ll_helpers import create_linked_list


# change current node value to next node value
# point to next node of next node
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


def test_1():
    l = [4, 5, 1, 9]
    ll = create_linked_list(l)
    starting_node_val = 5
    starting_node = ll
    while starting_node.val != starting_node_val:
        starting_node = starting_node.next
    new_ll = create_linked_list([4, 1, 9])
    deleteNode(starting_node)
    assert (ll == new_ll)
