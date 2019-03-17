# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        ans = cur = head
        for i in range(0, k):
            if not cur:
                return None
            cur = cur.next
        while cur:
            cur = cur.next
            ans = ans.next
        return ans

