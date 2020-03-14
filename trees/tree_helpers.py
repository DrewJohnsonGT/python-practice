from binary_tree import TreeNode


def create_binary_tree(l):
    # list structure: Node, Left, Right
    # Create a list of trees
    nodes = [TreeNode(x) for x in l]

    # Fix up the left and right links
    count = len(nodes)
    for index, tree in enumerate(nodes):
        left_index = 2 * index + 1
        if left_index < count:
            tree.left = nodes[left_index]

        right_index = 2 * index + 2
        if right_index < count:
            tree.right = nodes[right_index]
    return nodes[0]