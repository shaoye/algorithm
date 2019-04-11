# -*- coding:utf-8 -*-

# LeetCode - 153 & 154

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0: return 0
        if length == 1: return rotateArray[0]
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right - left) // 2
            if rotateArray[mid] < rotateArray[right]:
                right = mid
                continue
            if rotateArray[mid] > rotateArray[left]:
                left = mid + 1
                continue
            if rotateArray[mid] == rotateArray[right]:
                right -= 1
            if rotateArray[mid] == rotateArray[left]:
                left += 1
        return rotateArray[right]
