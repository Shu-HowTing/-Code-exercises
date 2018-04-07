# -*- coding: utf-8 -*-
# Author: 小狼狗
import collections
def first_char(str):
    dict = collections.OrderedDict()
    count = 0
    for x in str:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x]+=1
    for x in dict:
        if dict[x] == 1:
            return x,str.index(x)

if __name__ == '__main__':
    str = "abaccdeff"
    print(first_char(str))
