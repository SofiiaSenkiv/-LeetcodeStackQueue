class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            self.size -= 1
            return item
        raise ValueError('Queue is empty.')

    def push(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    @property
    def peek(self):
        return self.head.item

class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x):
        self.queue.push(x)
        size = self.queue.size
        for _ in range(size - 1):
            self.queue.push(self.queue.pop().item)

    def pop(self):
        return self.queue.pop().item

    def top(self):
        return self.queue.peek

    def empty(self):
        return self.queue.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
