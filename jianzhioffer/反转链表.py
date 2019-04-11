# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        dummy = None
        while pHead:
            cur = pHead.next
            pHead.next = dummy
            dummy = pHead
            pHead = cur
        return dummy
