from typing import List


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __int__(self):
        """init Solution, init a list for the result."""
        self.res = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """先序遍历"""
        res = self.res
        if root:
            if root.val:
                res.append(root.val)
            if root.left:
                self.preorderTraversal(root.left)
            if root.right:
                self.preorderTraversal(root.right)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """中序遍历"""
        res = self.res
        if root:
            if root.left:
                self.inorderTraversal(root.left)
            if root.val:
                res.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """后序遍历"""
        res = self.res
        if root:
            if root.left:
                self.postorderTraversal(root.left)
            if root.right:
                self.postorderTraversal(root.right)
            if root.val:
                res.append(root.val)
        return res


if __name__ == '__main__':
    solution = Solution()
