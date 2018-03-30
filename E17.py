# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
华为：
   大数相乘(含负数)
'''

def multipy(a, b, f_a, f_b):
    a.reverse()
    b.reverse()
    c = [0 for k in range(0, len(a) + len(b)+1)]
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            c[i + j] += a[i] * b[j]

    for m in range(0, len(c)-1):
        if (c[m] > 9):
            c[m + 1] += c[m] // 10
            c[m] = c[m] % 10
        c[len(c)-1] = '-' if f_a*f_b==-1 else '+'
    c.reverse()
    return c
if __name__ == '__main__':
     a = input()
     b = input()
     print(int(a)*int(b))
     f_a=f_b=1
     if int(a)<0:
         f_a=-1
         a = [int(x) for x in a[1:]]
     else:
         a = [int(x) for x in a]
     if int(b)<0:
         f_b=-1
         b = [int(x) for x in b[1:]]
     else:
         b = [int(x) for x in b]

     print(''.join(map(str,multipy(a, b,f_a,f_b))))


