from collections import deque


class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


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

levels = level_order_traversal(root)
print("Level Order Traversal by level:")
for i, level in enumerate(levels):
    print(f"Level {i}: {level}")