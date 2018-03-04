# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
=================================================================================
    假设有N个值都不相同的随机数，每次给你一个数进行选择，你如果选择接受，则游戏结束，如果选择不，
    则选择下一个数，直到所有的数选择完毕，你不能反悔去选择之前的数。你可以采取如下的策略：

        1.观察前k个数，记录下其中的最大值。
        2.在后续的数中只要出现比记录下的最大值更大的数，则选择它。
        3.如果到了最后一个数，仍然没有做出选择，则选择它。
    问题是当k为多大时选择出最大的数的概率最高？  k=N/e
=================================================================================
'''
import numpy as np

#np.random.seed(0)


#可能用到的函数有：numpy.maximum.accumulate()和numpy.where()。
def choices():
    """
    返回一个长度与data相同的数组，其中的每个下标index的值为
    当k=index时，所选择的数
    """
    #np.random.seed(0)

    data = np.arange(1, 101)
    np.random.shuffle(data)
    l = []
    M = np.maximum.accumulate(data)
    Max = 0
    for k in range(len(M)):
        Max = M[k]

        for i in range(k, len(M)):
            if M[i] > Max:
                Max = M[i]
                break
        else:
            Max = data[i]
        l.append(Max)
    return l

print("best choices:")
print(choices())
#
results = np.zeros((10000, 100), np.int)
# # 【你的程序】将data的顺序打乱，调用10000次choices()，并将结果保存进results
#
# # 【你的程序】计算选择最大值的概率p1和所选值的平均值p2
#
import pylab as pl
p1 = []
p2 = []
for i in range(10000):
    results[i] = choices()
for k in range(100):
    p1.append(np.sum(results[:,k] == 100))
    p2.append(np.mean(results[:,k]))
p1 = np.array(p1)/10000
pl.subplot(211)
pl.plot(p1, lw=2)
pl.ylabel(u"选择最大值的概率")
#pl.show()
pl.subplot(212)
pl.plot(p2, lw=2)
pl.ylabel(u"所选数的平均值")
pl.xlabel("k")
pl.show()
