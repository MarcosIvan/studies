class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.end = None

    def insertFront(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertBack(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            return
        self.end.next = new_node
        new_node.prev = self.end
        self.end = self.end.next

    def removeFront(self):
        if self.head is None:
            return
        self.head.next.prev = None
        self.head = self.head.next

    def removeBack(self):
        if self.end is None:
            return
        self.end = self.end.prev
        self.end.next.prev = None
        self.end.next = None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


list = Deque()
list.insertFront(1)
list.insertFront(2)
list.insertFront(3)
list.insertFront(4)
list.insertBack(5)
list.insertBack(6)
list.removeFront()
list.removeBack()
list.display()