class Queue:
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def is_empty(self):
        return len(self.items) == 0
class MyStack:
    def __init__(self):
        self.queue = Queue()
    def push(self, x):
        self.queue.push(x)
        size = len(self.queue.items)
        for _ in range(size - 1):
            self.queue.push(self.queue.pop())
    def pop(self):
        return self.queue.pop()
    def top(self):
        return self.queue.peek()
    def empty(self):
        return self.queue.is_empty()