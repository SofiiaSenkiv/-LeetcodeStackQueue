class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
class Queue:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    def is_empty(self):
        return len(self.items) == 0

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