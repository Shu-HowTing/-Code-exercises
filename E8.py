# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
经典背包问题：
    假设我们有n件物品，分别编号为1, 2...n。其中编号为i的物品价值为vi，它的重量为wi。
    为了简化问题，假定价值和重量都是整数值。现在，假设我们有一个背包，它能够承载的重量是W。
    现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？
              0                                  if i=0 or w=0
    c[i,w] =  c[i-1,w]                           if w_i>w
              max(v_i+c[i-1, w-w_i], c[i-1,w])   if i>0 and w_i<=w
'''
import numpy as np

def solve(v_list, w_list, W, n):
    #resArr[i] 表示剩余的承载重量为i时，背包已经存放的物品的最大总价值
    resArr = np.zeros((W) + 1, dtype=np.int32)
    for i in range(0, n):
        for j in range(W, 0, -1):
            if w_list[i] <= j:
                resArr[j] = max(resArr[j], resArr[j - w_list[i]] + v_list[i])
    return resArr[-1]

if __name__ == '__main__':
    v = [60, 120, 100, 140]
    w = [1, 3, 2, 2]
    weight = 5
    n = len(v)
    result = solve(v, w, weight, n)
    print(result)
