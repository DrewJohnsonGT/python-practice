from binary_tree import TreeNode
from tree_helpers import create_binary_tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

# iteratively compare both sides of
# root at same time - one left first
# and other right first to mirror
# return if mismatch
# def is_symmetric(root):
#     if root == None:
#         return True
#     left_stack = [root.left]
#     right_stack = [root.right]
#     while len(left_stack) != 0 and len(right_stack) != 0:
#         left_node = left_stack.pop()
#         right_node = right_stack.pop()
#         if (left_node == None
#                 and right_node != None) or (right_node == None
#                                             and left_node != None):
#             return False
#         if left_node != None and right_node != None and left_node.val != right_node.val:
#             return False
#         # left tree add left node first
#         if left_node != None:
#             left_stack.append(left_node.left)
#             left_stack.append(left_node.right)
#         # right tree add right node first
#         if right_node != None:
#             right_stack.append(right_node.right)
#             right_stack.append(right_node.left)
#     return True


# recursive solution
# handles two trees at same time
def is_symmetric(root):
    if root == None:
        return True
    return two_trees_symmetric(root.left, root.right)


# call recursively and compare
# left first for n1
# right first for n2
def two_trees_symmetric(n1, n2):
    # if one node is None and the other isn't - false
    if n1 == None and n2 == None:
        return True
    if n1 == None or n2 == None:
        return False
    return n1.val == n2.val and two_trees_symmetric(
        n1.left, n2.right) and two_trees_symmetric(n1.right, n2.left)


def test_1():
    tree = create_binary_tree([1, 2, 2, 3, 4, 4, 3])
    assert (is_symmetric(tree) == True)


def test_2():
    tree = create_binary_tree([1, 2, 2, None, 3, None, 3])
    assert (is_symmetric(tree) == False)
