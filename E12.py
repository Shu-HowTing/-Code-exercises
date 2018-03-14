# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
    一根长度为n的绳子，将绳子剪为m段（剪m-1次,m=1,2...,n-1），每段绳子的长度为k[0] ~ k[m]；
    要求k[0] * k[1] * k[2] * ~~k[m]的乘积为最大。n >1 且 m> 1。
'''
#动态规划
def cut_rope1(length):
    if length < 2:
        return 0 #如果给的绳子小于2，没法剪，不符合题目要求，返回0
    if length == 2:
        return 1 #如果长度是2，还必须至少剪一刀，只能是1*1 =1
    if length == 3:
        return 2 #如果长度为3，只能是2*1 = 2 > 1*1*1 =1
    products = [None] * (length+1)
    #products列表，放的是绳子长度最优的情况
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    for i in range(4,length+1): #从长度为4的绳子开始
        #求出从4到给出的绳子，每一个长度的最大乘积
        max = 0
        for j in range(1,i//2+1): #从1到i//2+1因为4*6和6*4一样，当到了中间相同的数字，乘积结束后就可以
            product = products[j] * products[i-j]
            if max < product:
                max = product
            products[i] = max
    max_product = products[length]
    return max_product
if __name__ == '__main__':
    length = int(input("length = "))
    print(cut_rope1(length))

#贪心算法
def cut_rope2(length):
    if length == 2:
        return 1
    if length == 3:
        return 2
    time, rest = divmod(length, 3)
    mod_2 = 1
    if rest == 1:
        time -= 1
        mod_2 = 2
    return 3**time*2**mod_2
if __name__ == '__main__':
    length = int(input("length = "))
    print(cut_rope2(length))