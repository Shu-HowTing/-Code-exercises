# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
华为：
    找出字符串中最长的数字串，长度相同输出最后一串
'''
#方案1：将所有的字母字符变为'a'，然后以'a'做分割，split(),取最长的一个
def long_number_string(s):
    L = list(s)
    for i in range(len(L)):
        if not L[i].isnumeric():
            L[i] ='a'
    l = ''.join(L).split('a')
    l.sort(key=lambda x:len(x))
    print(l[-1]+','+str(len(l[-1])))

if __name__ == '__main__':
    s = input()
    long_number_string(s)


#方法二:
a = input()
maxLen=0
maxStrs=[]
curLen=0
curStr = ""
for i, v in enumerate(a):
    if v.isnumeric():
        curLen += 1
        curStr += v
        if curLen >= maxLen:
            maxLen = curLen
            maxStrs = [curStr]
    else:
        curLen = 0
        curStr = ""
print("".join(maxStrs) + "," + str(maxLen))
