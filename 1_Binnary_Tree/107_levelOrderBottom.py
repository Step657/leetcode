"""
给定一个二叉树，返回其节点值自底向上的层次遍历。（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""
import queue
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """BFS："""
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.path([root], res)
        return list(reversed(res))

    def path(self, closed, res):
        """
        递归遍历
        :param closed: 存放当前扩展的结点
        :param res: 结果列表
        :return:
        """
        if len(closed) == 0:
            return
        opened = []
        temp = []
        for i in closed:
            if not i:
                continue
            opened.append(i.left)
            opened.append(i.right)
            temp.append(i.val)
            closed.remove(i)
        res.append(temp)
        self.path(opened, res)

    def levelTraverse(self, root):
        q = queue.Queue()
        q.put(root)
        cur = None
        res = []
        while q.not_empty():
            cur = q.get()
            res.append(q.get().val)

