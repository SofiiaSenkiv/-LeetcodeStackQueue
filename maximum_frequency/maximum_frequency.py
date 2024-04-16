from collections import defaultdict
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
class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(Stack)
        self.max_freq = 0
    def push(self, val):
        self.freq[val] += 1
        frequency = self.freq[val]
        self.group[frequency].push(val)
        self.max_freq = max(self.max_freq, frequency)
    def pop(self):
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if self.group[self.max_freq].is_empty():
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val

# Приклад використання:
# freqStack = FreqStack()
# freqStack.push(1)
# freqStack.push(2)
# freqStack.pop()
    