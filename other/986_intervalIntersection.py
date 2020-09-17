"""
986. 区间列表的交集
    给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
    返回这两个区间列表的交集。
    （形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。
    例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）
示例：
    输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
思路：
    - 什么情况下没有交集：两种情况
    - 什么情况下有交集：四种情况，但是可以同一表示
"""
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0  # 双指针
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            # 两个区间存在交集
            if b2 >= a1 and a2 >= b1:
                # 计算出交集， 加入res
                res.append([max(a1, b1), min(a2, b2)])
            # 指针前进
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res
