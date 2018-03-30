# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
美团笔试题：
    计算两个字符串的距离
'''
import sys
S = input()
T = input()
len_S = len(S)
len_T = len(T)
d = 0
for i in range(len_S-len_T+1):
    for j in range(len_T):
        if S[i+j] != T[j]:
            d += 1
sys.stdout.write(str(d))

