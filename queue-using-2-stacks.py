class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data:
            raise IndexError("stack vazia")
        return self.data.pop()

    def size(self):
        return len(self.data)


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