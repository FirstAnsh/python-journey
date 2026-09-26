class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def has_cycle(self):
        slow = self.head
        fast = self.head

        # Fast moves two steps while slow moves one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they meet, a cycle exists
            if slow == fast:
                return True

        return False


# Demo execution
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.append(val)

print(f"Cycle detected initially: {ll.has_cycle()}")

# Artificially create a cycle: point tail (50) back to node with value 20
tail = ll.head
while tail.next:
    tail = tail.next

second_node = ll.head.next
tail.next = second_node

print(f"Cycle detected after connecting tail to node(20): {ll.has_cycle()}")