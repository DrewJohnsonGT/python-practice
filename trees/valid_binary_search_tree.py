from binary_tree import TreeNode
from tree_helpers import create_binary_tree

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# DFS while checking for
# correct values
def is_valid_search_tree(root):
    stack = []
    if root != None:
        stack.append(root)
    while len(stack) != 0:
        parent_node = stack.pop()
        if parent_node != None:
            if parent_node.left != None:
                if parent_node.left.val >= parent_node.val:
                    return False
                else:
                    stack.append(parent_node.left)
            if parent_node.right != None:
                if parent_node.right.val < parent_node.val:
                    return False
                else:
                    stack.append(parent_node.right)
    return True


def test_1():
    tree = create_binary_tree([2, 1, 3])
    assert (is_valid_search_tree(tree) == True)


def test_2():
    tree = create_binary_tree([5, 1, 4, 3, 6])
    assert (is_valid_search_tree(tree) == False)


def test_3():
    tree = create_binary_tree([1, 1])
    assert (is_valid_search_tree(tree) == False)