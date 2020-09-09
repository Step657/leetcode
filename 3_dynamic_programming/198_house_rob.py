"""
198. 打家劫舍
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
    如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
示例 1：
    输入：[1,2,3,1]
    输出：4
    解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：
    输入：[2,7,9,3,1]
    输出：12
    解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
         偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
from typing import List


class Solution:
    memo = []

    def rob(self, nums: List[int]) -> int:
        self.memo = [-1 for i in range(len(nums))]
        return self._dp1(nums, 0)

    def _dp1(self, nums: List[int], start: int) -> int:
        # 走完了所有房间
        if start >= len(nums):
            return 0
        # 利用备忘录剪枝
        if self.memo[start] != -1:
            return self.memo[start]

        res = max(
            self.dp(nums, start + 1),
            nums[start] + self.dp(nums, start + 2)
        )
        self.memo[start] = res
        return res

    # 自底向上
    def rob1(self, nums):
        length = len(nums)
        dp = [0 for i in range(length + 2)]
        for i in range(length - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + nums[i + 1])
        return dp[0]

    # 压缩空间,空间复杂度为O(1),当前状态只与最近两个状态有关
    def rob2(self, nums):
        dp_i_1, dp_i_2 = 0, 0
        dp_i = 0
        for i in range(len(nums) - 1, -1, -1):
            dp_i = max(dp_i_1, nums[i] + dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i

