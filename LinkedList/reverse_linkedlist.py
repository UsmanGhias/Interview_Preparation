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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linked_list.head = prev

# Example usage:
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print("Original Linked List:")
my_linked_list.display()

reverse_linked_list(my_linked_list)

print("\nReversed Linked List:")
my_linked_list.display()
