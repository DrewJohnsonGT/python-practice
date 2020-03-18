from binary_tree import TreeNode
from tree_helpers import create_binary_tree

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Recursive approach
# maintaining min and max values for nodes and
# recursing down tree checking values
# def is_valid_search_tree(root, minimum=float('-inf'), maximum=float('inf')):
#     if root == None:
#         return True
#     curr_val = root.val
#     if curr_val <= minimum or curr_val >= maximum:
#         return False
#     if not is_valid_search_tree(root.right, curr_val, maximum):
#         return False
#     if not is_valid_search_tree(root.left, minimum, curr_val):
#         return False
#     return True

# same as recursive approach but
# iterative with DFS
# def is_valid_search_tree(root):
#     if root == None:
#         return True
#     stack = [
#         (root, float('-inf'), float('inf')),
#     ]
#     while stack:
#         root, lower, upper = stack.pop()
#         if root == None:
#             continue
#         val = root.val
#         if val <= lower or val >= upper:
#             return False
#         stack.append((root.right, val, upper))
#         stack.append((root.left, lower, val))
#     return True


# In order traversal works too
# checking nodes in an order
# that they should always be increasing
# (compared to previously checked)
def is_valid_search_tree(root):
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val)
        # If next element in inorder traversal
        # is smaller than the previous one
        # that's not BST.
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right

    return True


# def test_1():
#     tree = create_binary_tree([2, 1, 3])
#     assert (is_valid_search_tree(tree) == True)

# def test_2():
#     tree = create_binary_tree([5, 1, 4, 3, 6])
#     assert (is_valid_search_tree(tree) == False)

# def test_3():
#     tree = create_binary_tree([1, 1])
#     assert (is_valid_search_tree(tree) == False)


def test_4():
    tree = create_binary_tree([10, 5, 15, None, None, 6, 20])
    assert (is_valid_search_tree(tree) == False)