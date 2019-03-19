# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False
        return (
            self.checkHasSubtree(pRoot1, pRoot2) or
            self.checkHasSubtree(pRoot1.left, pRoot2) or
            self.checkHasSubtree(pRoot1.right, pRoot2)
        )        
   
    def checkHasSubtree(self, root1, root2):
        if root2 == None:
            return True
        if root1 == None:
            return False
        if root1.val != root2.val:
            return False
        return (
            self.checkHasSubtree(root1.left, root2.left) and
            self.checkHasSubtree(root1.right, root2.right)
        )
