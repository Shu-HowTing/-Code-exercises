# -*- coding: utf-8 -*-
# Author: 小狼狗

def calculate(M, strs):
    L = [[0 for i in range(5)] for j in range(5)]
    for str in strs:
        for i in range(len(str) - 1):
            if str[i].isdigit():
                L[ord(str[i-1])-65][ord(str[i+1])-65] = int(str[i])
    print(L)
    for i in range(5):
        for j in range(i,5):
            if L[i][j]==L[j][i] and L[i][j]!=0:
                return -1


if __name__ == '__main__':
    strs = ['A2B3D','A4C2E','A5D','C3B']
    print(calculate(4, strs))
