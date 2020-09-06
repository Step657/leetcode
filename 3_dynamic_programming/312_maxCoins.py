"""
312. 戳气球
    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。
    这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
    求所能获得硬币的最大数量。

说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

示例:
    输入: [3,1,5,8]
    输出: 167
    解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
         coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
from typing import List
import sys


class Solution:
    res = sys.maxsize

    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums.insert(0, 1)
        print(nums)
        # self.backtrack(nums, 0)
        return self.dp(nums)

    def backtrack(self, nums, score):
        # stop
        if len(nums) == 2:
            self.res = max(self.res, score)
            return

        for i in range(1, len(nums) - 1):
            point = nums[i - 1] * nums[i] * nums[i + 1]
            # save old status
            temp = nums.copy()
            # del the select
            nums.pop(i)

            self.backtrack(nums, score + point)
            nums = temp

    def dp(self, nums):
        # base case: dp[i][i+1] = 0
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]

        # i from botton to top
        for i in range(len(nums) - 2, -1, -1):
            # j from left to right
            for j in range(i + 1, len(nums)):
                # k the last ball be broken,
                # enumerate all of the possible k belong to (i, j) and choose the bigest one
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k]
                    )
        return dp[0][len(nums) - 1]


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    s = Solution()
    res = s.maxCoins(nums)
    print(res)
