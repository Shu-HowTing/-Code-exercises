# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
输入n个数，找出其中最小的K个数
'''
def partition(L,low,high):
    pivot = L[low]
    while low < high:
        while low < high and L[high] > pivot:
            high -= 1
        L[low] = L[high]
        while low < high and L[low] < pivot:
            low += 1
        L[high] = L[low]
    L[low] = pivot
    return low
def find_top_k(L,k):
    low = 0
    high = len(L) - 1
    rank = partition(L,low,high)
    while k != rank:
        if rank < k:
            rank = partition(L, rank+1, high)
        else:
            rank = partition(L,low, rank)
    return L[:k]
if __name__ == '__main__':
    L = [4,5,1,6,2,7,3,8]
    print(find_top_k(L, 4))

#=================================================================
def find_top_k2(L,k):
    A = []
    for i in range(k):
        A.append(L[i])
    for i in range(k,len(L)-1):
        if L[i] < max(A):
            A[A.index(max(A))] = L[i]
    return A
if __name__ == '__main__':
    L = [4,5,1,6,2,7,3,8]
    print(find_top_k2(L, 4))
