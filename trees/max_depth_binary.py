from binary_tree import TreeNode
from tree_helpers import create_binary_tree

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path
#  from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# # calculate height of tree
# def max_depth(head):
#     return height(head)

# # depth first count of height
# def height(n):
#     if n is None:
#         return 0
#     else:
#         right_node = height(n.right)
#         left_node = height(n.left)
#         if right_node > left_node:
#             return right_node + 1
#         else:
#             return left_node + 1


# iterative approach using stack
# add root to stack
# successively add children with depths
# pop values and compare
def max_depth(head):
    stack = []
    if head != None:
        stack.append((1, head))
    depth = 0
    while len(stack) != 0:
        curr_depth, node = stack.pop()
        if node != None:
            depth = max(depth, curr_depth)
            stack.append((curr_depth + 1, node.left))
            stack.append((curr_depth + 1, node.right))
    return depth


def test_1():
    tree = create_binary_tree([3, 9, 20, None, None, 15, 7])
    print(tree)
    assert (max_depth(tree) == 3)
