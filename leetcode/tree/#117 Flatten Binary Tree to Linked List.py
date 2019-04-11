# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return None
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right
        root.right = root.left
        root.left = None
        
        tail = root
        while tail.right:
            tail = tail.right
        tail.right = tmp
