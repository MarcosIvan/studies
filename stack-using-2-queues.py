class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, x):
        new_node = Node(x)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def dequeue(self):
        if self.head is None:
            raise IndexError("queue vazia")

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        return value

    def size(self):
        return self._size


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.enqueue(x)

    def pop(self):
        if self.q1.size() == 0:
            raise IndexError("stack vazia")

        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())

        top = self.q1.dequeue()

        self.q1, self.q2 = self.q2, self.q1

        return top


s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())