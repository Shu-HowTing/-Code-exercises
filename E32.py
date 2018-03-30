# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
8*8的方格子，求A点到B点的最短路径有多少条？用算法实现
f[m][n] = f[m-1][n] + f[m][n-1]9
'''
def ways(N):
    r = [[0 for i in range(N+1)]for i in range(N+1)]
    for i in range(1,N+1):
        r[i][0] = 1
    for j in range(1,N+1):
        r[0][j] = 1
    for m in range(1,N+1):
        for n in range(1,N+1):
            r[m][n] = r[m-1][n] + r[m][n-1]
    return r[N][N]
if __name__ == '__main__':
    print(ways(8))