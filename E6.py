# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
输入描述:
    每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，表示学生的个数，接下来的一行，包含 n 个整数，
    按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。

输出描述:
    输出一行表示最大的乘积。

输入例子:
    3
    7 4 7
    2 50

输出例子:
    49
'''

def computeMaxProduct(array, n, k, d):
    #  状态转移方程是:
    #  dpMax[i][j] = dpMax[i - x][j - 1] * A[i]
    dpMax = [[0 for i in range(n)] for i in range(n)]
    #  dpMax[i][j] 表示以数组元素A[i]作结尾时， 序列长度为j的最大乘积结果
    for i in range(n):
        dpMax[i][1] = array[i]
        dpMax[i][0] = array[0]
    Max_sofar = 0
    for j in range(2, k+1):
        for i in range(j-1, n):
            dpMax[i][j] = Max_sofar
            for x in range(1, d+1):
                if i-x >= j-2:
                    resMax = dpMax[i-x][j-1] * array[i]
                    if resMax > dpMax[i][j]:
                        dpMax[i][j] = resMax
    for i in range(k-1, n):
        if dpMax[i][k] > Max_sofar:
            Max_sofar = dpMax[i][k]
    print(dpMax)
    return Max_sofar

n = int(input())
array = eval(input())  # [7, 4, 7]
k, d = map(int, input().split())
print(computeMaxProduct(array, n, k, d))