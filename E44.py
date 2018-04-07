# -*- coding: utf-8 -*-
# Author: 小狼狗

import operator
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        #py3不支持cmp函数
        lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        array = sorted(numbers, cmp=lmb)
        return ''.join([str(i) for i in array])

if __name__ == '__main__':
    L = [5,3,32]
    s = Solution()
    print(s.PrintMinNumber(L))
    L = [["a",3],["b",4],["v",1]]
