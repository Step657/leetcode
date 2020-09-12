"""
78. 子集(subset)
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
    输出:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
"""
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """解法一：利用数学归纳法的思想：假设我现在知道了规模更小的子问题的结果，如何推导出现在问题的结果呢？
            递归算法时间复杂度：找到递归深度，然后乘以每次递归中迭代的次数"""
        # base case：空集的子集为空集
        if len(nums) == 0:
            return [[]]
        # 拿出最后一个元素
        n = nums.pop()
        # 先递归运算前面元素的所有子集
        res = self.subsets(nums)

        for i in range(len(res)):
            res.append(res[i].copy())
            res[-1].append(n)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """解法二：回溯算法"""
        # 记录走过的路径
        track, res = [], []
        self.backtrack(nums, 0, track, res)
        return res

    def backtrack(self, nums: List[int], start, track: List[int], res):
        res.append(track.copy())

        # 注意i从start开始递增
        for i in range(start, len(nums)):
            # 做选择
            track.append(nums[i])
            # 回溯
            self.backtrack(nums, i + 1, track, res)
            # 撤销选择
            track.pop()


if __name__ == '__main__':
    nums = [0]
    s = Solution()
    res = s.subsets2(nums)
    print(res)
