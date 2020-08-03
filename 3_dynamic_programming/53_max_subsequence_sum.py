"""
53. 最大子序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
    如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
import sys


class MaxSubArray(object):
    def __init__(self, nums):
        self.nums = nums

    def maxSubArray(self):
        nums = self.nums
        if len(nums) == 0:
            return 0

        dp = [num for num in nums]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        res = sys.minsize
        for i in dp:
            res = max(i, res)

        return res

    def maxSubArray(self):
        """状态压缩"""
        nums = self.nums
        if len(nums) == 0:
            return 0

        dp_0, dp_1 = nums[0], 0
        res = dp_0

        for i in range(1, len(nums)):
            dp_1 = max(nums[i], dp_0 + nums[i])
            dp_0 = dp_1
            res = max(res, dp_1)
        return res
