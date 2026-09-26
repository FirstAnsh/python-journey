class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def max_depth(root):
    # Base case: empty tree has depth 0
    if not root:
        return 0
    
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    
    return 1 + max(left_height, right_height)


# Helper to build a BST from input to test depth
def insert_bst(root, key):
    if not root:
        return TreeNode(key)
    if key < root.val:
        root.left = insert_bst(root.left, key)
    elif key > root.val:
        root.right = insert_bst(root.right, key)
    return root


raw_input = input("Enter numbers to insert into tree (space-separated): ")
nums = [int(x) for x in raw_input.split()]

root = None
for n in nums:
    root = insert_bst(root, n)

tree_depth = max_depth(root)
print(f"Maximum Depth (Height) of the Tree: {tree_depth}")