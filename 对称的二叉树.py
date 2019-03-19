# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# LeetCode - 101


class Solution:

    def isSymmetric(self, root):
        return self.isMirror(root, root)
    
    def isMirror(self, root1, root2):
        if root1 == root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        return (
            self.isMirror(root1.left, root2.right) and
            self.isMirror(root1.right, root2.left)
        )
