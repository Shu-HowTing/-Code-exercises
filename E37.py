# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
题意：用三种颜色的气球装饰桌子，每个桌子装饰三个气球，并且每个桌子至少要用两个颜色的气球装饰，
    问最多能装饰多少桌子

思路：很显然比较两种颜色较少的气球的和是否小于最多的气球的一半，若是小于则用最多气球中的两个,
    再加一个颜色较少的气球;否则为三种气球总数的平均数


'''
def party(num):
    num.sort()
    if num[0]+num[1]>(num[2]//2):
        count = num[0]+num[1]+num[2]
        return count//3
    else:
        return num[0]+num[1]
if __name__ == '__main__':
    Bubble = []
    k = int(input())
    for i in range(k):
        b = [int(x) for x in input().split()]
        Bubble.append(b)
    for x in Bubble:
        print(party(x))

