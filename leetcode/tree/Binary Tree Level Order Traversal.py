# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level if node])
            level = [child for node in level for child in (node.left, node.right) if child]
            # temp = []
            # for node in level:
            #     temp += [node.left, node.right]
            # level = [child for child in temp if child]
        return ans
