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

    def find_middle(self):
        slow = self.head
        fast = self.head

        # When fast reaches the end, slow is at the midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None


ll = LinkedList()
values = input("Enter values to append to list (space-separated): ").split()
for val in values:
    ll.append(val)

middle_value = ll.find_middle()
print(f"Middle element: {middle_value}")