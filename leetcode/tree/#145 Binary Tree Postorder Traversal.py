# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ret = []

    # Recursive Approach
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.ret.append(root.val)
        return self.ret

    # Iterative Approach - 1
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret, stack, parent = [], [], []
        self.pushLeft(root, stack)
        while stack:
            tmp = stack[-1]
            if parent and parent[-1] is tmp:
                ret.append(tmp.val)
                stack.pop()
                parent.pop()
            else:
                parent.append(tmp)
                self.pushLeft(tmp.right, stack)
        return ret

    def pushLeft(self, root: TreeNode, stack: List = None):
        while root:
            stack.append(root)
            root = root.left

    # Iterative Approach - 2
    def postorderTraversal(self, root):
        if not root:
            return []
        ret, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ret.append(node.val)
                else:
                    # post order traversal
                    # mark the root node visited
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return ret
