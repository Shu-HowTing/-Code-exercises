# -*- coding: utf-8 -*-
# Author: 小狼狗
# 希尔排序
def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

import math
import random


#随机生成0~100之间的数值
def get_randomNumber(num):
    lists=[]
    i=0
    while i<num:
        lists.append(random.randint(0,1000))
        i+=1
    return lists

#基数排序
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))   #位数
    bucket = [[] for i in range(radix)]
    for i in range(k):
        S = [ [] for _ in range(10)]
        for j in lists:
            S[j // (10 ** i) % 10].append(j)     #入桶
        lists = [a for b in S for a in b]        #出桶
    return lists
if __name__ == '__main__':
    L = get_randomNumber(12)
    print(radix_sort(L))