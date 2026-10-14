def tree_height(node):
    if node is None:
        return 0
    _, left, right = node
    return 1 + max(tree_height(left), tree_height(right))
