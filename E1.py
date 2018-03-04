# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
阿里编程测验题：
    将一个圆形平均分成N等分，现有M种颜色的涂料，对每一等分进行上色，要求相邻的部分不能是同一种颜色，问一共有多少种涂法？
    思路：在不考虑第一块和最后一块颜色的情况下，保证其他N-1块的颜色满足条件： M*(M-1)^(N-1)
         再从中去掉最后一块和第一块颜色相同的情况，即为最后的答案；
         最后一块和第一块颜色相同：情况和将圆形平分成N-1等分一样即A(N-1, M)
         所以递归表达式为：A(N, M) = M*(M-1)**(N-1) - A(N-1,M)

'''
# def number(M, N):
#     if N == 1:
#         return M
#     if N == 2:
#         return M*(M-1)
#     else:
#         return M*(M-1)**(N-1)-number(M, N-1)
#
# if __name__ == '__main__':
#     [M,N]=[int(i) for i in input().split()]
#     print(number(M, N))

#=========================================================================================
'''
有个穷困的艺术家。他画了一幅超现实主义的作品《方块手拉手》。现在他已经把图画中手拉手的一排大小不一的方块都画出来了。
现在要考虑上颜色了，可惜他手中的钱并不多了。但是他是个有追求的人，他希望这幅画中每两个相邻的方块的颜色是不一样的。
你能帮他计算一下把这幅画上色后，最少需要花多少钱么。

输入:
    N个方块，K个颜色
    接下来每列是各个方块染成不同颜色的价钱
输出:
     最少花的钱
例： 4    3
    [2 3 2
     9 1 4
     7 8 1
     2 8 3]
     6
'''
def min_cost(cost, N, K):
    for i in range(N-2, -1, -1): #倒序输出 N-2, N-3, N-4, ···, 0
        for j in range(K):
            MIN = 1000000
            for r in range(K):
                if j == r:
                    continue
                else:
                    if cost[i][j] + cost[i+1][r] < MIN:
                        MIN = cost[i][j] + cost[i+1][r]
            cost[i][j] = MIN
    MIN = 100000
    for i in range(K):
        if cost[0][i] < MIN:
            MIN = cost[0][i]
    return MIN
if __name__ == '__main__':
    # cost= [[2, 3, 2],
    #        [9, 1, 4],
    #        [7, 8, 1],
    #        [2, 8, 3]]
    cost = input()     #[[2,3,2],[9,1,4],[7,8,1],[2,8,3]]
    cost = eval(cost)
    N = len(cost)
    K = len(cost[0])
    #print(N, K)
    print(min_cost(cost, N, K))