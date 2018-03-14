# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
======================================================================
                       最大公共子序列(LCS)  O(m*n)
======================================================================
'''
def lcs(a, b):
    len_a = len(a)
    len_b = len(b)
    c = [[0 for i in range(len_b + 1)] for j in range(len_a + 1)]
    flag = [[0 for i in range(len_b + 1)] for j in range(len_a + 1)]
    for i in range(len_a):
        for j in range(len_b):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:

                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return c, flag


def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        print(a[i - 1], end='')
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)


a = input("A:")
b = input("B:")
c, flag = lcs(a, b)
# for i in c:
#     print(i)
# print('')
# for j in flag:
#     print(j)
# print('')
printLcs(flag, a, len(a), len(b))
print('')