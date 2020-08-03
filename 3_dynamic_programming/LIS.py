"""
最长递增子序列(Longest Increasing Subsequence)
题目：
    给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例：
    输入：[10, 9, 2, 5, 3, 7, 101, 18]
    输出：4
    解释：最长的上升子序列是[2, 3, 7, 101],其长度为4
说明：
    - 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可
    - 你的算法的时间复杂度应该为O(n^2)。
进阶：
    你能将算法的时间复杂度降低到O(nlongn)吗？
【子序列 & 子串：子串一定是连续的，而子序列不一定是连续的。】

总结：
    1. 明确dp数组所存数据的含义
    2. 根据dp数组的定义，运用数学归纳法的思想，假设dp[0...i-1]都已知，想办法求出dp[i]
    (若无法完成，可能就是dp数组的定义不够恰当；或者可能dp数组存储的信息还不够，不足以退出下一步的答案，
    需要把dp数组扩大成二维数组甚至三维数组。)
"""


class LIS(object):
    """
    dp[i]表示以nums[i]这个数结尾的最长递增子序列的长度。
    base case:dp[i]初始值为1，因为以nums[i]结尾的最长递增子序列起码要包含它自己。
    最终结果：应该是dp数组中的最大值。
    """

    def __init__(self, nums):
        self.nums = nums

    def lengthOfLIS_1(self):
        """动态规划"""
        nums = self.nums
        dp = [1 for i in range(len(nums))]
        res = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        for i in dp:
            res = max(res, dp[i])

        return res

    def lengthOfLIS_2(self):
        """二分查找"""
        nums = self.nums
        top = []
        piles = 0
        for poker in nums:
            # 搜索左侧边界的二分查找
            left, right = 0, piles
            while left < right:
                mid = (left + right) / 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            if left == piles:
                piles += 1
            top[left] = poker
        return piles
