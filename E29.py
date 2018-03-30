# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
网易笔试：
    x,y都是正整数，x、y<=n，且x%y>=k,求(x,y)一共有多少可能
'''
# def number(n, k):
#     count = 0
#     for x in range(1,n+1):
#         for y in range(1,n+1):
#             if x % y >= k:
#                 count += 1
#     return count
# if __name__ == '__main__':
#     n,k = [int(x) for x in input().split()]
#     print(number(n,k))

#O(n)
def numbers(n,k):
    count = 0
    if k==0:
        return n**2
    for y in range(k+1, n+1):
        a,b = divmod(n,y)
        count = count + a*(y-k)
        if b>=k:
            count = count + (b-k+1)
    return count
if __name__ == '__main__':
    n,k = [int(x)for x in input().split()]
    print(numbers(n,k))


