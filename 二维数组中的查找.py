class Solution:
    def BinarySearch(self, array, target, left, right):
        mid = left + (right - left) // 2
        # base condition
        if left > right:
            return -1
        if array[mid] == target:
            return mid
        if array[mid] > target:
            return self.BinarySearch(array, target, left, mid - 1)
        else:
            return self.BinarySearch(array, target, mid +1, right)
        
    def Find(self, target, array):
        for a in array:
            if a == []:
                continue
            if target < a[0] or target > a[-1]:
                continue
#            if self.BinarySearch(a, target, 0, len(a)-1) != -1:
#               return True
            if self.IterativeSearch(a, target) != -1:
                return True
        return False
    
    def IterativeSearch(self, array, target):
        left = 0
        right = len(array)-1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            if array[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1
