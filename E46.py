# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
给定一个数字，按照如下规则翻译成字符串：0翻译成“a”，1翻译成“b”...25翻译成“z”。
一个数字有多种翻译可能，例如12258一共有5种，分别是bccfi，bwfi，bczi，mcfi，mzi。
实现一个函数，用来计算一个数字有多少种不同的翻译方法。
f[i] = f[i-1] + g(i,i-1)*f[i-2]
'''
def translation(num):
    L = [0 for x in range(len(num))]
    L[0] = L[-1] = 1
    for i in range(1, len(num)):
        L[i] = L[i-1]+L[i-2] if int(num[i-1:i+1])>=10 and int(num[i-1:i+1])<=25 else L[i-1]
    return L[-1]
if __name__ == '__main__':
    num = '12258'
    print(translation(num))
