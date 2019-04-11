# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        
        # odd, even = [], []
        # for item in array:
        #     if item % 2:
        #         odd.append(item)
        #     else:
        #         even.append(item)
        # return odd+even
        
        # https://docs.python.org/3.6/howto/sorting.html#key-functions
        
        return sorted(array, key=lambda item:item%2, reverse=True)
