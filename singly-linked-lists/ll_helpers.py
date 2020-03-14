from singly_linked_list import ListNode


def create_linked_list(l):
    size = len(l)
    prev_node, curr_node = None, None
    for i in range(0, size):
        index = size - i - 1
        curr_node = ListNode(l[index])
        curr_node.next = prev_node
        prev_node = curr_node
    return prev_node


def create_cyclic_linked_list(l, cycle_val):
    size = len(l)
    prev_node, curr_node, cyclic_node, tail = None, None, None, None
    for i in range(0, size):
        index = size - i - 1
        curr_node = ListNode(l[index])
        if i == 0:
            tail = curr_node
        curr_node.next = prev_node
        prev_node = curr_node
        if l[index] == cycle_val:
            cyclic_node = curr_node
    if tail != None and cyclic_node != None:
        tail.next = cyclic_node
    return prev_node