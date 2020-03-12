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