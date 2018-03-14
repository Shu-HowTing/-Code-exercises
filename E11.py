# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
def jumpFloorI(number):
    w = [0 for i in range(number + 1)]
    w[1] = 1
    w[2] = 2
    for i in range(3, number + 1):
        w[i] = w[i-1] + w[i-2]
    return w[number]
if __name__ == '__main__':
    print(jumpFloorI(5))



'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
def jumpFloorII(number):
    w = [0 for i in range(number + 1)]
    w[0] = 1
    w[1] = 1
    w[2] = 2
    for i in range(3, number + 1):
        w[i] = 2*w[i-1]
    return w[number]

print(jumpFloorII(5))