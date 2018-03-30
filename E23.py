# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如:输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2
'''
def more_than_half(numbers):
    dict = {}
    for x in numbers:
        if not x in dict:
            dict[x] = 1
        else:
            dict[x] += 1
        if dict[x] > len(numbers) // 2:
            return x
    return False
if __name__ == '__main__':
    numbers = [3,3,2,3,5,6,3,7,3,3,3,8]
    print(more_than_half(numbers))

'''
第一个数字作为第一个士兵,守阵地；count = 1;
遇到相同元素，count++;遇到不相同元素,即为敌人,同归于尽,count--;
当遇到count为0的情况，又以新的i值作为守阵地的士兵,
继续下去，到最后还留在阵地上的士兵，有可能是主元素。
关于众数的另一个重要的事实：
    设P为向量A中长度为2m的前缀。若元素x在P中恰好出现m次，则A有众数，仅当A-P拥有众数，且众数相等。
'''
def more_than_half(number):
    count = 0
    time = 0
    for i in range(0,len(number)):
        if (count == 0):
            x = number[i];
            count = 1
        else:
            count = count+1  if numbers[i] == x else count-1
    #判断
    for i in range(0, len(number)):
        if x == number[i]:
            time += 1
    if time > len(number)//2:
        return x
    return False
if __name__ == '__main__':
    numbers = [3,3,2,3,5,6,3,7,3,3,3,8]
    print(more_than_half(numbers))
