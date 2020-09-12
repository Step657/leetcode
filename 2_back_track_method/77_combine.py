"""
77. 组合
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
    输入: n = 4, k = 2
    输出:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        track, res = [], []
        self.backtrack(n, k, 1, track, res)
        return res

    def backtrack(self, n: int, k: int, start: int, track: List[int], res: List[int]):
        if k == len(track):
            res.append(track.copy())
            return
        for i in range(start, n + 1):
            track.append(i)
            self.backtrack(n, k, i + 1, track, res)
            track.pop()
