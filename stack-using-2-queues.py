class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        if not self.data:
            raise IndexError("queue vazia")
        return self.data.pop(0)

    def size(self):
        return len(self.data)


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