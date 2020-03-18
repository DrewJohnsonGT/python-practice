from binary_tree import TreeNode
from tree_helpers import create_binary_tree

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.


# use list and string representation of list
def serialize(root):
    result = []
    # start with root node
    stack = [root]
    while stack:
        curr = stack.pop(0)
        if curr != None:
            result.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return ','.join(map(lambda x: str(x), result))


# Breadth first traversal using stack
def deserialize(list_str):
    l = list(map(lambda x: int(x), list_str.split(',')))
    if l[0] == None:
        return None
    nodes = [TreeNode(x) for x in l]
    size = len(nodes)
    for index, node in enumerate(nodes):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < size:
            node.left = nodes[left_index]
        if right_index < size:
            node.right = nodes[right_index]
    return nodes[0]


def test_1():
    tree = create_binary_tree([1, 2, 3, 4, 5, 6])
    result = serialize(tree)
    assert (deserialize(result) == tree)


def test_2():
    tree = create_binary_tree([1, 2, 3])
    result = serialize(tree)
    assert (deserialize(result) == tree)
