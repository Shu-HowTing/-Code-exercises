# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
    调整数组的顺序，使奇数位于偶数前面,不改变元素的相对位置
'''
def Reorder(numbers):
    odd = []
    even = []
    for i in range(len(numbers)):
        if numbers[i] & 0x01 == 1:
            odd.append(numbers[i])
        else:
            even.append(numbers[i])
    numbers = odd+even
    return numbers

if __name__ == '__main__':
    L = [1,2,3,4,5,6,7,8,9]
    print(Reorder(L))

#空间复杂度更小，但不能保证相对顺序的解法：
# class Solution:
#     def reOrderArray(self, array):
#         i = 0
#         j = len(array) - 1
#         while(i<j):
#             while(i<j and array[i]&0x01 != 0):
#                 i+=1
#             while (i < j and array[j] & 0x01 == 0):
#                 j-=1
#             if i<j:
#                 array[i],array[j] = array[j],array[i]
#         return array
# s = Solution()
# L = [1,2,3,4,5]
# print(s.reOrderArray(L))