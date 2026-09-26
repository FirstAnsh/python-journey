class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.val:
            if current.left is None:
                current.left = TreeNode(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.val:
            if current.right is None:
                current.right = TreeNode(key)
            else:
                self._insert_recursive(current.right, key)
        # Duplicate values are ignored in this BST implementation

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


raw_input = input("Enter numbers to insert into BST (space-separated): ")
bst = BinarySearchTree()

for num in [int(x) for x in raw_input.split()]:
    bst.insert(num)

sorted_elements = bst.inorder_traversal()
print(f"In-Order Traversal (Sorted Output): {sorted_elements}")