# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
在一个无序向量中，某一个数出现次数超过了一半(众数)，求这个数?

当我们遍历下一个数时，如果和之前的数字相同，则次数+1；否则次数减1；如果count=0，则需要保存下一个数，并把count设为1，
最后一个把count设为1的数一定是众数
'''
def more_than_half(nums):
    count = 0
    for x in nums:
        if count == 0:
            major = x
            count = 1
        else:
            count = count + 1 if major == x else count-1
    return major
if __name__ == '__main__':
    L= [2,3,7,3,5,3,8,3,5,3,3]
    print(more_than_half(L))