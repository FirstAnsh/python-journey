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

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next  # 1. Save next node
            curr.next = prev       # 2. Reverse current pointer
            prev = curr            # 3. Move prev forward
            curr = next_node       # 4. Move curr forward
        self.head = prev           # 5. Reset head to new front

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "Empty List")


ll = LinkedList()
values = input("Enter values to append to list (space-separated): ").split()
for val in values:
    ll.append(val)

print("Original Linked List:")
ll.display()

ll.reverse()

print("Reversed Linked List:")
ll.display()