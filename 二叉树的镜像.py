# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def Mirror(self, root):
        if root == None:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        root.left = self.Mirror(root.left)
        root.right = self.Mirror(root.right)
        return root
