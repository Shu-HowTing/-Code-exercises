# -*- coding: utf-8 -*-
# Author: 小狼狗

#====================================全排列=============================

'''
不放回的抽取
递归全排列
    A、B、C、D）的全排列为：

    1、A后面跟（B、C、D）的全排列

    2、B后面跟（A、C、D）的全排列（A与B交换，其他次序保持不变）

    3、C后面跟（B、A、D）的全排列（A与C交换，其他次序保持不变）

    4、D后面跟（B、C、A）的全排列（A与D交换，其他次序保持不变）
    第二次交换的意义：保证都是在同一基础上交换顺序
'''
Count = 0
def per1(l, start, end):
    global Count
    if start==end:
        print(l)
        Count+=1
    else:
        for num in range(start, end):
            l[start], l[num] = l[num], l[start]
            per1(l, start+1, end)
            l[num],l[start] = l[start], l[num]
L=[0,2,4,5]
per1(L,0,4)
print(Count)


'''
    有放回的抽取
'''
count = 0
def per2(l, length, index):
    global count
    if index == length :
        print(l)
        count += 1
        return
    for x in L:
        l[index] = x
        per2(l, length, index+1)
L=[0,2,4,5]
l=[0 for i in range(len(L))]
per2(l, len(L), 0)
print(count)