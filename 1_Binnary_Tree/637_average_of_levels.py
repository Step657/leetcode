"""
637. 二叉树的层平均值
    给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
示例 1：
    输入：
        3
       / \
      9  20
        /  \
       15   7
    输出：[3, 14.5, 11]
    解释：
    第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        self.path([root], res)
        return res

    def path(self, closed, res):
        if len(closed) == 0:
            return res
        opened = []
        temp = []
        for node in closed:
            if not node:
                continue
            opened.append(node.left)
            opened.append(node.right)
            temp.append(node.val)
        res.append(sum(temp) / len(temp))
        self.path(opened, res)
