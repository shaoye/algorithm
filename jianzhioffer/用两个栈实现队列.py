# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        # add the new item into stack1
        # [newest, newer, .., new]
        self.stack1.append(node)
        
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            # reverse stack1, literally
            # [new, newer, .., newest]
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None
