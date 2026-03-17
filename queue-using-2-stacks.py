class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("stack vazia")

        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    def size(self):
        return self._size


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, x):
        self.s1.push(x)

    def dequeue(self):
        if self.s1.size() == 0:
            raise IndexError("queue vazia")

        while self.s1.size() > 1:
            self.s2.push(self.s1.pop())

        front = self.s1.pop()

        while self.s2.size() > 0:
            self.s1.push(self.s2.pop())

        return front


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())