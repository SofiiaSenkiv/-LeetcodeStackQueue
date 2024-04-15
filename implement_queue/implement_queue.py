class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    
class MyQueue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()
        self.front = None
    def push(self, x):
        if self.stack1.is_empty():
            self.front = x
        self.stack1.push(x)
    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    def peek(self):
        if not self.stack2.is_empty():
            return self.stack2.peek()
        return self.front
    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()


#Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()