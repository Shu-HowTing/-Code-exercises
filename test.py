# -*- coding: utf-8 -*-
# Author: 小狼狗
import numpy as np
# x = [1,2,3,5,8]
# y = [0.11,0.12,0.13,0.15,0.18]
# X = np.mean(x)
# Y = np.mean(y)
# x = x - X
# y = y - Y
# dot_product = 0
# normA = 0
# normB = 0
# for a,b in zip(x, y):
#     dot_product += a*b
#     normA += a**2
#     normB += b**2
#
# print(dot_product / ((normA*normB)**0.5))
#
# def isPal(s):
#
#     s = s.strip(" ").lower()
#     if len(s)<=1:
#         return True
#     else:
#         return s[0] == s[-1] and isPal(s[1:-1])
# if __name__=='__main__':
#     s = input()
#     print(isPal(s))

# def min_money(m):
#     n = len(m)
#     S = sum(m)
#     f = [[0 for i in range(n)]for i in range(S)]
#     f[0][1] = -m[0]
#     f[m[1]][1] = m[0]
#     for s in range(S-1 - max(m)):
#         for i in range(n-1):
#             f[s+m[i+1]][i+1] = f[s][i] + m[i+1]
#             f[s][i+1] = f[s][i] - m[i+1]
#     MIN = 100000000
#     for i in range(S):
#         if abs(f[i][n-1]) < MIN:
#             MIN = abs(f[i][n-1])
#     return MIN
# if __name__=='__main__':
#     l = [20, 30, 10, 40, 60]
#     print(min_money(l))

'''
现有100名学生的成绩，每个班级50人，要求两个班级的平均分越接近越好，如何分配两个班级？
'''

# import numpy as np
#
# # random int of 60 ~ 100, 100s
# score = np.random.randint(60, 101, 100)
#
# a = np.zeros((51, 5001), dtype=bool)
# t = np.zeros(a.shape, dtype=int) - 1
# a[0, 0] = True
#
# for idx, s in enumerate(score):
#     a[1:, s:] = a[1:, s:] | a[:-1, :-s]  #按位求或
#     t[(t < 0) & a] = idx
#
# totalScore = sum(score)
# aScore = np.max(np.argwhere(a[50, :totalScore//2 + 1]))
# print('total score:', totalScore)
# print('class A score:', aScore)
# print('class A student:')
#
# for i in range(50, 0, -1):
#     idx = t[i][aScore]
#     aScore -= score[idx]
#     print(idx)

# t = np.array([[1,2,3],
#              [2,3,4],
#              [3,4,5]])
#
# for i in range(3):
#     print(t[:-1])
# l = [1,2,3,4,5,6]
# print(l[:-1])
# import codecs
# from textrank4zh import TextRank4Keyword, TextRank4Sentence
#
# text = codecs.open('./01.txt', 'r', 'gbk').read()
# tr4w = TextRank4Keyword()
#
# tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
#
# print( '关键词：' )
# for item in tr4w.get_keywords(3, word_min_len=1):
#     print(item.word, item.weight)
#
# print()
# print( '关键短语：' )
# for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
#     print(phrase)
#
# def count_num(num, start, end):
#     count = 0
#     for i in num:
#         if i >= start and i <= end:
#             count += 1
#     return count
#
#
# def duplication(num):
#     m = len(num)
#     start = 1
#     end = m-1
#     while end > start:
#         middle = ((end - start) >> 1) + start
#         cout = count_num(num, start, middle)
#         if cout > middle - start + 1:
#             end = middle
#         else:
#             start = middle
#     print(start)
# duplication([2,3,5,4,3,1,6,7])

# a = [3,2,4,6]
# b = [1,4,5,7,8,9]
# l_a = len(a)
# l_b = len(b)
# for x in b:
#     a.append(0)
# l = len(a)
#
# for i in  range(l-1, -1, -1):
#     if a[l_a-1] >= b[l_b-1]  and l_a > 0:
#         a[i] = a[l_a-1]
#         l_a-=1
#     else:
#         a[i] = b[l_b - 1]
#         l_b -=1
# print(a)
#
#
#
# def numberOfOne(number):
#     count = 0
#     while number > 0:
#         if number & 1 :
#             count += 1
#         number = number >> 1
#     print(count)
# numberOfOne(9)
#
# print(5^6) # 异或
#
#
import sys
#a= sys.stdin.readline().split()
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0])+int(a[1]))
# line = sys.stdin.readline()
# # a, b = map(int,line.split())
# # print(a+b)
# print(line)
a = []
for line in sys.stdin:
    a.append(line)
print(a)
#
# print(int(a[0]),int(a[1]))


