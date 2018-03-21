# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
最小编辑距离：
    设A和B是两个字符串。我们要用最少的字符操作次数，将字符串A转换为字符串B。这里所说的字符操作共有三种：
        1. 删除一个字符；
        2. 插入一个字符；
        3. 将一个字符改为另一个字符。
        对任给的两个字符串A和B，计算出将字符串A变换为字符串B所用的最少字符操作次数。
'''
def min_acion(str1,str2,len1, len2):
    dp = [[0for i in range(len2+1)]for j in range(len1+1)]
    for i in range(len1+1):
        dp[i][0] = i
    for j in range(len2+1):
        dp[0][j] = j
    for i in range(1,i+1):
        for j in range(1, j+1):
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1,
                           dp[i-1][j-1] + (0 if str1[i-1] == str2[j-1] else 1))
    return dp[len1][len2]
if __name__ == '__main__':
    s1 = 'ab'
    s2 = 'aab'
    len1 = len(s1)
    len2 = len(s2)
    print(min_acion(s1,s2,len1,len2))









