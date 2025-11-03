class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def revert(self):
        current = self.head
        next = None
        previous = None
        while current:
            next = current.next
            if current.next == None:
                self.head = current
                current.next = previous
            elif current == self.head:
                current.next = None
            current.next = previous
            previous = current
            current = next


list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.display()
list.revert()
list.display()