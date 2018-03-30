# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
              快排(quicksort)
'''
def partition(numbers, low, high):
    pivot = numbers[low]   #轴点
    while low<high:
        while low<high and numbers[high]>pivot:
            high -= 1
        numbers[low] = numbers[high]
        while low<high and numbers[low]<=pivot:
            low+=1
        numbers[high] = numbers[low]
    numbers[low] = pivot
    return  low


def quick_sort(array, low, high):
    if low < high:
        rank = partition(array, low, high)
        quick_sort(array, low, rank)
        quick_sort(array, rank + 1, high)

if __name__ == '__main__':
    L = [6,5,8,7,4,1,2]
    quick_sort(L, 0, len(L)-1)
    print(L)