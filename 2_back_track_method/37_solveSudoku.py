"""
37. 解数独
    编写一个程序，通过已填充的空格来解决数独问题。

    一个数独的解法需遵循如下规则：
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    空白格用 '.' 表示。
    Note:
        给定的数独序列只包含数字 1-9 和字符 '.' 。
        你可以假设给定的数独只有唯一解。
        给定数独永远是 9x9 形式的。
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 直接从（0，0）开始回溯算法
        return self._traceback(board, 0, 0)

    def _traceback(self, board, i, j):
        """回溯算法"""
        m, n = 9, 9
        if j == n:
            # 穷举到最后一列的话就换到下一行重新开始
            return self._traceback(board, i + 1, 0)
        if i == m:
            # 找到一个可行解，触发base case
            return True
        if board[i][j] != '.':
            # 如果是预设的数字，那么跳过，不用我们穷举
            return self._traceback(board, i, j + 1)

        status = [str(i) for i in range(1, 10)]
        for s in status:
            if not self._isVaild(board, i, j, s):
                continue
            else:
                board[i][j] = s
                if self._traceback(board, i, j + 1):
                    return True
                else:
                    # 撤销选择
                    board[i][j] = '.'
        return False

    def _isVaild(self, board, row, column, ch):
        """判断要填的数字是否有效"""
        for i in range(9):
            if board[i][column] == ch:
                return False
            if board[row][i] == ch:
                return False
            if board[(row // 3) * 3 + i // 3][(column // 3) * 3 + i % 3] == ch:
                return False
        return True
