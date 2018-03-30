# -*- coding: utf-8 -*-
# Author: 小狼狗


# class AntiOrder:
#     def count(self, A):
#         self.rNums = 0
#         self.mergeSort(A)
#         return self.rNums
#     def mergeSort(self, A):
#         if len(A) <= 1:
#             return A
#         m = len(A) // 2
#         a = self.mergeSort(A[:m])
#         b = self.mergeSort(A[m:])
#         return self.merge(a, b)
#     def merge(self, A, B):
#         c, i, j = [], 0, 0
#         while i < len(A) and j < len(B):
#             if A[i] <= B[j]:
#                 c.append(A[i])
#                 i += 1
#             else:
#                 c.append(B[j])
#                 j += 1
#                 self.rNums += len(A) - i #此为逆序对数
#         c += A[i:]
#         c += B[j:]
#         return c
# an = AntiOrder()
# L = [7,6,5,4]
# x = an.count(L)
# print(x)
# print(an.mergeSort(L))
count = 0
def merge_sort(data):
    if len(data)<=1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)
def merge(a,b):
    global count
    c = []
    i=j=0
    while i<len(a) and j<len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j+=1
            count += len(a) - i   #逆序对的个数
        else:
            c.append(a[i])
            i+=1
    c += b[j:]  #添加剩余的
    c += a[i:]

    return c
if __name__ == '__main__':
    L = [4,5,3,7,9,3]
    merge_sort(L)
    print(count)