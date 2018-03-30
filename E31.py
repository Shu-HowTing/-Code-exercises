# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
给定一个整数数组，在该数组中，寻找三个数，分别代表三角形三条边的长度，问，可以寻找到多少组这样的三个数来组成三角形？
O(n^2)
'''
def triangleCount(L):
    count = 0
    L.sort()
    for i in range(2,len(L)):
        left = 0
        right = i-1
        while left < right:
            if L[left]+L[right]<=L[i]:
                left += 1
            else:
                count += (right - left)
                right -= 1
    return count
if __name__ == '__main__':
    L = [3,8,5,9]
    print(triangleCount(L))