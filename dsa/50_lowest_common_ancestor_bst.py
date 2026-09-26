class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p_val, q_val):
    curr = root

    while curr:
        # If both targets are smaller than current node, LCA is in left subtree
        if p_val < curr.val and q_val < curr.val:
            curr = curr.left
        # If both targets are greater than current node, LCA is in right subtree
        elif p_val > curr.val and q_val > curr.val:
            curr = curr.right
        # The split point: one is left and one is right (or curr matches p or q)
        else:
            return curr.val

    return None


def insert_bst(root, key):
    if not root:
        return TreeNode(key)
    if key < root.val:
        root.left = insert_bst(root.left, key)
    elif key > root.val:
        root.right = insert_bst(root.right, key)
    return root


# Standard BST Setup:
#        6
#      /   \
#     2     8
#    / \   / \
#   0   4 7   9
#      / \
#     3   5
nodes = [6, 2, 8, 0, 4, 7, 9, 3, 5]
root = None
for n in nodes:
    root = insert_bst(root, n)

p = int(input("Enter first node value: "))
q = int(input("Enter second node value: "))

lca = lowest_common_ancestor(root, p, q)
print(f"Lowest Common Ancestor of {p} and {q}: {lca}")