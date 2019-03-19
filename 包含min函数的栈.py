class Solution:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if not self.minStack:
            self.minStack.append(node)
        if node <= self.minStack[-1]:
            self.minStack.append(node)

    def pop(self):
        if not self.stack:
            return None
        pop = self.stack.pop()
        if pop == self.minStack[-1]:
            self.minStack.pop()
        return pop

    def top(self):
        if not self.stack:
            return None
        return self.stack[0]

    def min(self):
        if not self.minStack:
            return None
        return self.minStack[-1]
