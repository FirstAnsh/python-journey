class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def invert_tree(root):
    if not root:
        return None

    # Swap left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively invert both child subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.val)
        inorder_traversal(node.right, result)


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

before_inorder = []
inorder_traversal(root, before_inorder)
print(f"In-order before inversion: {before_inorder}")

invert_tree(root)

after_inorder = []
inorder_traversal(root, after_inorder)
print(f"In-order after inversion:  {after_inorder}")