# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        ans = [0,1,2]
        while len(ans) < number+1:
            ans.append(ans[-1]+ans[-2])
        return ans[number]
