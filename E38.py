# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
找出两个有序数组的中位数

其实，如果我已经确定了数组1是最短的数组，那只有两种情况了，比较好处理：
如果C1 = 0 —> 那么我们缩小L1，L1 = INT_MIN，保证判断正确。
如果C1 = n*2 —> 那么我们增大R1，R1 = INT_MAX，保证判断正确。
'''
def find_mid(num1,num2):
    n = len(num1)
    m = len(num2)
    if m<n:
        return find_mid(num2,num1)
    low = 0
    high = 2*n
    while low<=high:
        c1 = (low + high)//2
        c2 = m+n-c1
        l1 = num1[(c1-1)//2] if c1 != 0 else float("-inf")
        r1 = num1[c1//2] if c1 != 2*n else float("inf")
        l2 = num2[(c2 - 1) // 2]
        r2 = num2[c2 // 2]
        if l1 > r2:
            high = c1 - 1
        elif l2 > r1:
            low = c1 + 1
        else:
            break
    return (max(l1, l2) + min(r1, r2)) // 2

if __name__ == '__main__':
    L1 = [1,3,5,7,9,38,57]
    L2 = [10,11,15,19]
    print(find_mid(L1, L2))

def find_mid1(L1,L2):
    l = len(L1) + len(L2)
    mid,flag = divmod(l,2)
    flag = not flag
    m = n =0
    L3 = []
    for i in range(l):
        if L1[m]>L2[n]:
            n+=1
            L3.append(L2[n])
        else:
            m+=1
            L3.append(L1[m])
        if i == mid:
            break
    return (L3[mid] + L3[mid-flag])//2
if __name__ == '__main__':
    L1 = [1,3,5,7,9,38,57]
    L2 = [10,11,15,19]
    print(find_mid1(L1, L2))