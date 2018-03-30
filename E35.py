# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
def Get_ugly_number(index):
    if index <= 0:
        return 0
    U = [0 for i in range(index)]
    U[0] = 1
    i_2 = i_3 = i_5 = 0
    next_u = 1
    while(next_u<index):
        Min = min(U[i_2]*2, U[i_3]*3, U[i_5]*5)
        U[next_u] = Min
        while(U[i_2]*2 <= U[next_u]):
            i_2 += 1
        while(U[i_3]*3 <= U[next_u]):
            i_3 += 1
        while(U[i_5]*5 <= U[next_u]):
            i_5 += 1
        next_u += 1
    return U[-1]
if __name__ == '__main__':
    N = int(input())
    print(Get_ugly_number(N))