# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
假设这有一个各种字母组成的字符串A，和另外一个字符串B，字符串里B的字母数相对少一些。
什么方法能最快的查出所有小字符串B里的字母在大字符串A里都有？
    我们可以对短字串进行轮询（此思路的叙述可能与网上的一些叙述有出入，因为我们最好是应该把短的先存储，那样，会降低题目的时间复杂度），
    把其中的每个字母都放入一个Hashtable里(我们始终设m为短字符串的长度，那么此项操作成本是O(m))。
    然后轮询长字符串，在Hashtable里查询短字符串的每个字符，看能否找到。如果找不到，说明没有匹配成功，
'''
def compare(str1,str2):
    hash = [0 for i in range(26)]
    count = 0
    for x in str2:
        index = ord(x) - ord('A')
        if hash[index] == 0:
            hash[index] = 1
            count +=1
    for x in str1:
        index = ord(x) - ord('A')
        if hash[index] == 1:
            hash[index] = 0
            count -= 1
            if count == 0:
                break
    if count == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    str1 = "ABCDEFGHLMNOPQRS"
    str2 = "DCGSRQPOM"
    print(compare(str1, str2))

'''
素数法:
    将每个字母对应一个素数，将字符串表示成每个素数的乘积;对于短的字符串，用长字符串的乘积去求余运算(mod),如果余数不为0，则退出;
    例如：如果两个字符串的字符一样，但是顺序不一样，被认为是兄弟字符串，问如何在迅速匹配兄弟字符串（如，bad和adb就是兄弟字符串）。
    思路：判断各自素数乘积是否相等
'''