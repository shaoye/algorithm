# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # Recursive Approach:

    def __init__(self):
        self.ret = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.ret.append(root.val)
        self.inorderTraversal(root.right)
        return self.ret

    # Iterative Approach:

    def iterativeInorderTraversal(self, root: TreeNode) -> List[int]:
        ret, stack = [], []
        self.pushLeftNodes(root, stack)
        while stack:
            tmp = stack.pop()
            ret.append(tmp.val)
            self.pushLeftNodes(tmp.right, stack)
        return ret

    def pushLeftNodes(self, root: TreeNode, stack: List = None):
        while root:
            stack.append(root)
            root = root.left
