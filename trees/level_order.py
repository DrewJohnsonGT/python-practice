from binary_tree import TreeNode
from tree_helpers import create_binary_tree

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,None,None,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# standard level order traversal using queue
# (iterative)
# def level_order(root):
#     if root == None:
#         return []
#     levels = []
#     level = 0
#     queue = [root]
#     while len(queue) != 0:
#         levels.append([])
#         level_length = len(queue)
#         for _ in range(level_length):
#             node = queue.pop(0)
#             levels[level].append(node.val)
#             # enqueue children
#             if node.left != None:
#                 queue.append(node.left)
#             if node.right != None:
#                 queue.append(node.right)
#         level += 1
#     return levels


# recursive solution
# same as above, but track levels with
# function input
def level_order(root):
    if root == None:
        return []
    levels = []

    def traverse(node, level):
        # add list for this level if needed
        if len(levels) == level:
            levels.append([])
        # add current node to level at index
        levels[level].append(node.val)
        if node.left != None:
            traverse(node.left, level + 1)
        if node.right != None:
            traverse(node.right, level + 1)

    traverse(root, 0)
    return levels


def test_1():
    tree = create_binary_tree([3, 9, 20, None, None, 15, 7])
    assert (level_order(tree) == [[3], [9, 20], [15, 7]])


def test_2():
    tree = create_binary_tree([1, 2, 2, None, 3, None, 3])
    assert (level_order(tree) == [[1], [2, 2], [3, 3]])
