# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
=============================================================
                    网易的一道面试题
    a^b=c^d   0<= a,b,c,d<= m
=============================================================
'''
def test(m):
    a = []
    for i in range(m):
        for j in range(m):
            a.append((i+1)**(j+1))
    dict = {}
    for i in range(len(a)):
        if a[i] not in dict.keys():
            dict[a[i]] = 1
        else:
            dict[a[i]] += 1
    res = 0
    for val in dict.values():
        res += (val**2)
    return res
m = int(input("请输入一个整数:\n"))
print(test(m))