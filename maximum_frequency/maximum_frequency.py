class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self, item):
        self.head = Node(item, self.head)
    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item
    @property
    def peek(self):
        return self.head.item
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

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0
    def push(self, val):
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        frequency = self.freq[val]
        if frequency not in self.group:
            self.group[frequency] = Stack()
        self.group[frequency].push(val)
        self.max_freq = max(self.max_freq, frequency)
    def pop(self):
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if self.group[self.max_freq].is_empty():
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()