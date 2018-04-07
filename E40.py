# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
一个只有三个元素[0,1,2]数组，如何排序？只允许遍历一次
'''
#三个指针，p0,p1,p2, p0指向第一个不为0的数，p1指向不为1的数，p2从尾部往前，指向第一个不为2的数
def sort(L):
    i = 0
    j = len(L)-1
    k = 0
    while L[i] == 0:
        i+=1
    k = i
    while L[j] == 2:
        j-=1
    while k<=j:
        if L[k] == 1:
            k+=1
        elif L[k] == 0:
            L[k],L[i] = L[i],L[k]
            while L[i]==0:
                i+=1
        elif L[k]==2:
            L[k],L[j] = L[j],L[k]
            while L[j]==2:
                j-=1
if __name__ == '__main__':
    L=[2,0,1,2,0,2,1,2,1,1,2]

#质因数分解法
def sort2(L):
    x = 1
    for i in L:
        if i == 0:
            x *= 2
        elif i == 1:
            x *= 3
        else:
            x *= 5
    j = 0
    while x%2 == 0:
        x //= 2
        L[j] = 0
        j+=1
    while x%3 == 0:
        x //= 3
        L[j] = 1
        j += 1
    while x%5 == 0:
        x //= 5
        L[j] = 2
        j += 1
print(L)