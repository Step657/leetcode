"""
416. 分割等和子集
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
    每个数组中的元素不会超过 100
    数组的大小不会超过 200
示例 1:
    输入: [1, 5, 11, 5]
    输出: true
    解释: 数组可以分割成 [1, 5, 5] 和 [11].
示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
"""


class SeparationEqualSumSubset(object):
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        amount = sum(nums) // 2
        n = len(nums)
        dp = [[False for i in range(amount + 1)] for j in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(amount, 0, -1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - nums[i - 1]] or dp[i - 1][j]
        return dp[n][amount]

    def canPartition_space(self, nums):
        if sum(nums) % 2 != 0:
            return False
        amount = sum(nums) // 2
        n = len(nums)
        dp = [False for i in range(amount + 1)]

        # base case
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(amount, 0, -1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[amount]


if __name__ == '__main__':
    example = SeparationEqualSumSubset()
    nums = [1, 2, 5]
    res = example.canPartition(nums)
    res = example.canPartition_space(nums)
    print(res)
