# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
   大数相乘
'''

def multipy(a, b):
    a.reverse()
    b.reverse()
    ccc = [0 for k in range(0, len(a) + len(b))]
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            ccc[i + j] += a[i] * b[j]

    for m in range(0, len(ccc)):
        if (ccc[m] > 9):
            ccc[m + 1] += ccc[m] // 10
            ccc[m] = ccc[m] % 10

    ccc.reverse()
    return ccc
if __name__ == '__main__':
     a = input()
     b = input()
     a = [int(x) for x in a]
     b = [int(x) for x in b]
     print(''.join(map(str,multipy(a, b))))

