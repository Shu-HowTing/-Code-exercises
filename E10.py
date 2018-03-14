# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''
#用数组实现一个hash表，时间复杂度O(n), 空间复杂度O(1)
import time
def duplicate(numbers):
    n = len(numbers)
    for i in range(n):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                print(numbers[i])
                break
            t = numbers[i]
            numbers[i] = numbers[t]
            numbers[t] = t

numbers = [2,3,1,0,2,5,3,5,6,9,7,4,10,4]
duplicate(numbers)


x = {}
for i in numbers:
    if numbers.count(i)>1:
        x[i] = numbers.count(i)
time3 = time.time()
print(x)

