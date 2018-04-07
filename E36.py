# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
 长度为N的数值，放了0~N的数(无序无重复),如何找出缺失的数值
'''
# def find_no(num):
#
L = [5,1,3,4,0]
x = 0
for i in range(len(L)+1):
    x = x^i
for j in L:
    x = x^j
print(x)
L=[2,1,5,0,4,5,3]
'''
    长度为N的数组，放了0~N-1的数(无序),如何找出重复的数值
'''
def find_duplication(L):
    for i in range(len(L)):
        while(L[i]!=i):
            if L[i]==L[L[i]]:
                return L[i]
            #注：不能使用 L[i],L[[i]] = L[L[i]],L[i]
            temp = L[i]
            L[i] = L[temp]
            L[temp] = temp
    return False
if __name__ == '__main__':
    L = [2, 1, 5, 0, 4, 5, 3]
    print(find_duplication(L))