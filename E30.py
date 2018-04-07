# -*- coding: utf-8 -*-
# Author: 小狼狗

#找出一个有序数组中距离给定数值最近的数
def bi_search(L,val):
    low = 0
    high = len(L)-1
    while low < high:
        mid = (low+high)//2
        if L[mid] == val:
            return L[mid]
        elif L[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return L[high] if abs(L[high] - val) <= abs(L[low] - val) else L[low]
lst = [1, 3, 5, 7, 9, 10, 13, 15]
val = 8
print(bi_search(lst, val))
