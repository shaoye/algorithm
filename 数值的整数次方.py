# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        # return base**exponent
        if base == 0 and exponent < 0:
            raise ValueError()
        if exponent == 0:
            return 1
        ans = 1
        exp = int(bin(abs(exponent))[2:])
        while exp > 0:
            exp, mod = divmod(exp, 10)
            if mod:
                ans *= base 
            base *= base
        return ans if exponent > 0 else 1/ans
