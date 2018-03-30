# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
基数排序
'''
class CountingSort:
    def countingSort(self, A, m):
        result = []
        A_min = min(A)
        A_max = max(A)
        buckets_len = A_max - A_min + 1
        buckets = [0] * buckets_len  # 创建桶
        # 装桶
        for n in A:
            buckets[n - A_min] += 1
        # 桶倒出
        for i in range(buckets_len):
            value = i + A_min
            n = buckets[i]
            result += [value] * n
        return result

l = [2,3,4,5,5,6]
print(CountingSort().countingSort(l, len(l)))