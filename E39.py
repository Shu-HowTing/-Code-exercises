# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
    连续子数组最大和
'''
#时间O(n) 空间O(1)
def max_sum(L):
    Max = L[0]
    pre = 0
    for i in range(len(L)):
        pre = max(pre + L[i], L[i])
        if pre > Max:
            Max = pre
    return Max
if __name__ == '__main__':
    # L = [2,5,3,-5,4,-8,6,7]
    L = [-3,-5,-5,-7]
    print(max_sum(L))

