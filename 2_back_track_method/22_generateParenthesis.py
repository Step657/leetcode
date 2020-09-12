"""
22. 括号生成
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
    输入：n = 3
    输出：[
           "((()))",
           "(()())",
           "(())()",
           "()(())",
           "()()()"
         ]
括号问题
    - 括号的合法性判断
    - 合法括号的生成
    性质：一个合法括号的组合的左括号数量一定等于右括号数量
         对于一个合法的括号字符串组合p， 必然对于任何 0 <= i <= len(p)都有：子串p[0...i]中左括号的数量都大于或等于右括号的数量。
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        # 记录所有合法的括号组合
        res = []
        # 回溯过程中的路径
        track = ''
        self.backtrack(n, n, track, res)
        return res

    def backtrack(self, left: int, right: int, track: str, res: List[int]):
        # 若左括号剩下的多，说明不合法
        if right < left:
            return
        # 数量小于 0 肯定是不合法的
        if right < 0 or left < 0:
            return
        # 当所有括号都恰好用完时，得到一个合法的括号组合
        if left == 0 and right == 0:
            res.append(track)
            return

        # 尝试放一个左括号
        track = track + '('     # 选择
        self.backtrack(left - 1, right, track, res)
        track = track[:len(track) - 1:]     # 撤销选择

        # 尝试放一个右括号
        track = track + ')'     # 选择
        self.backtrack(left, right - 1, track, res)
        track = track[:len(track) - 1:]     # 撤销选择
