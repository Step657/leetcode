"""
46. 全排列
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
&组合：排列问题的树比较对称，而组合问题的树越靠右节点越少
    在代码中的体现就是：排列问题每次通过 in 方法来排除在track中已经选择过的数字；而组合问题是通过传入一个start参数，来排除start索引之前的数字
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track, res = [], []
        self.backtrack(nums, track, res)
        return res

    def backtrack(self, nums: List[int], track:List[int], res: List[int]):
        if len(track) == len(nums):
            res.append(track.copy())
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, track, res)
            track.pop()

