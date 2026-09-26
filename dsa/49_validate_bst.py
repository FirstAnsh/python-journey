class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True

        # The current node's value must strictly fall within (low, high)
        if not (low < node.val < high):
            return False

        # Left subtree values must be < node.val
        # Right subtree values must be > node.val
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float("-inf"), float("inf"))


# Test Case 1: Valid BST
#      2
#     / \
#    1   3
root_valid = TreeNode(2)
root_valid.left = TreeNode(1)
root_valid.right = TreeNode(3)

# Test Case 2: Invalid BST (5 has left child 4, right child 6 which has left child 3)
#      5
#     / \
#    1   6
#       / \
#      3   7   <-- 3 is invalid because it is in the right subtree of 5!
root_invalid = TreeNode(5)
root_invalid.left = TreeNode(1)
root_invalid.right = TreeNode(6)
root_invalid.right.left = TreeNode(3)
root_invalid.right.right = TreeNode(7)

print(f"Is Tree 1 a valid BST? {is_valid_bst(root_valid)}")
print(f"Is Tree 2 a valid BST? {is_valid_bst(root_invalid)}")