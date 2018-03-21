# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
解析：
    一条直线上有n座房子，每座房子里都有一定的现金（用nums[i]表示），不能同时抢劫相邻的两座房子，问最多能抢劫多少钱？这是一道典型的动态规划，
    用money[i]表示从第1座房子到第i座房子能抢到的最多的钱，那么money[i] = max(money[i - 2] + nums[i], money[i - 1])。
'''
# 空间复杂度O(n)
def search(i, nums):
    if i < 0: # 没有商家了，我们要开始销赃
        return 0
    return max(search(i - 1, nums), nums[i] + search(i - 2, nums))
def rob1(num):
    return search(len(num) - 1, num)

if __name__ == '__main__':
    num = [6, 7, 8, 9, 9, 4, 3, 38]
    print(rob1(num))

# 空间复杂度O(1)
def rob2( nums):
    """
    :type nums: List[int]
    """
    if len(nums) == 0:
        return 0
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    if len(nums) == 1:
        return dp[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    return dp[-1]
num = [6, 7, 8, 9, 9, 4, 3, 38]
print(rob2(num))

#   变形：
#   一个圆上有n座房子，其它条件都一样，只是第1座房子和第n座房子变成相邻的了，也就是说不能同时抢了，
#   那么最优解就变成 第1座房子到第n-1座房子能抢的最多的钱 或者 第2座房子到第n座房子能抢的钱了。
def rob_circle(nums):
    if len(nums) == 0:
        return  0
    if len(nums) == 1:
        return nums[0]
    dp_1 = [0 for i in range(len(nums)-1)]
    dp_1[0] = nums[0]
    dp_1[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)-1):
        dp_1[i] = max(dp_1[i - 1], nums[i] + dp_1[i - 2])
        Max = dp_1[-1]
    dp_2 = [0 for i in range(len(nums)-1)]
    dp_2[0] = nums[1]
    dp_2[1] = max(nums[1], nums[2])
    for i in range(2, len(nums)-1):
        dp_2[i] = max(dp_2[i - 1], nums[i+1] + dp_2[i - 2])
    return max(dp_1[-1],dp_2[-1])
num = [6, 7, 8, 9, 9, 4, 3, 38]
print(rob_circle(num))



















