# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
最大间隙问题(maximum gap):桶排序
    计算一个未排序数组中排序后相邻元素的最大差值。
    给定一个整数数组A和数组的大小n，请返回最大差值。
'''
import math
def maximum_gap(L):
    lo = min(L)
    hi = max(L)
    MAX = 0
    t_max = []
    t_min = []
    a = [[] for i in range(len(L))]
    for x in L:
        a[math.floor((len(L)-1)*(x-lo)/(hi-lo))].append(x)
    i = 0
    for i in range(len(L)):
        if a[i]!=[]:
            t_max.append(max(a[i]))
            t_min.append(min(a[i]))
    for i in range(len(t_max)-1):
        gap = t_min[i+1] - t_max[i]
        if gap>MAX:
            MAX = gap
    return MAX
if __name__ == '__main__':
    L = [2.5,9.4,4.1,10.3,1.2,5.8,19.9]
    print(maximum_gap(L))
