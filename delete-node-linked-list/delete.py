# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val} => {self.next}'

    def __eq__(self, other):
        _self_node = self
        _other_node = other
        if _self_node.val != _other_node.val:
            return False
        return _self_node.next == _other_node.next


# change current node value to next node value
# point to next node of next node
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


def create_linked_list(l):
    size = len(l)
    prev_node, curr_node = None, None
    for i in range(0, size):
        index = size - i - 1
        curr_node = ListNode(l[index])
        curr_node.next = prev_node
        prev_node = curr_node
    return prev_node


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
