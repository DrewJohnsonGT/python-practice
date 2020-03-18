from binary_tree import TreeNode
from tree_helpers import create_binary_tree


# Middle of array as root
# subsequent middles of sub-arrays
# are roots of subtrees
def arr_to_tree(nums):
    if len(nums) == 0:
        return None
    nodes = [TreeNode(x) for x in nums]

    def build_tree(nodes):
        size = len(nodes)
        if size == 1:
            return nodes[0]
        middle_index = size // 2
        root = nodes[middle_index]
        left = nodes[0:middle_index]
        right = nodes[middle_index + 1:size]
        if len(left) != 0:
            root.left = build_tree(left)
        if len(right) != 0:
            root.right = build_tree(right)
        return root

    return build_tree(nodes)


def test_1():
    tree = create_binary_tree([0, -3, 5, -10, None, 9])
    assert (arr_to_tree([-10, -3, 0, 5, 9]) == tree)


def test_2():
    tree = create_binary_tree([0, -10, 9, -20, -3, 5, 10])
    assert (arr_to_tree([-20, -10, -3, 0, 5, 9, 10]) == tree)
