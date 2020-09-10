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


"""
二叉搜索数操作集锦
    - 二叉树的遍历框架
    - 二叉树算法的设计总路线：明确一个节点要做的事情，然后剩下的事抛给框架
    - BST: Binary Search Tree, 二叉搜索树，一个二叉树中，任意节点的值要大于等于左子树所有节点的值，且要小于等于右子树所有节点的值
        基础操作：判断BST的合法性、增、删、查
    BST遍历框架：
    void BST(TreeNode root, int target) {
        if (root.val == target)
            // 找到目标，做点什么
        if (root.val < target)
            BST(root.right, target);
        if (root.val > target)
            BST(root.left, target);
    }
"""


def traverse(root: TreeNode):
    # root 需要做什么？ 在这里做
    # 其他的不用 root 操心， 抛给框架
    traverse(root.left)
    traverse(root.right)


# 两个例子
def plusOne(root: TreeNode):
    """
    把二叉树的所有节点中的值都加 1
    :param root:
    :return: None
    """
    if not root:
        return
    root.val += 1
    plusOne(root.left)
    plusOne(root.right)


def isSameTree(root1: TreeNode, root2: TreeNode):
    """
    判断两棵二叉树是否相同
    :param root1:
    :param root2:
    :return: boolen
    """
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root2.val != root1.val:
        return False
    return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)


class BST:
    def isVaildBST(self, root: TreeNode) -> bool:
        return self.isVaildBST(root, None, None)

    def isVaildBST(self, root: TreeNode, min: TreeNode, max: TreeNode):
        """
        判断一个树是不是二叉搜索树
        :param root:
        :param min:
        :param max:
        :return:
        """
        if not root:
            return True
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        return self.isVaildBST(root.left, min, root) and self.isVaildBST(root.right, root, max)

    def isInBST(self, root: TreeNode, target: int) -> bool:
        """
        在BST中查找一个元素是否存在
        :param root:
        :param target:
        :return:
        """
        if root.val == target:
            return True
        if root.val < target:
            return self.isInBST(root.right, target)
        if root.val > target:
            return self.isInBST(root.left, target)

    def insertIntToBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        在BST中插入一个数
        :param val:
        :return: root
        """
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntToBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntToBST(root.left, val)
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        在BST中删除一个数，类似插入, 先找再改， 找到目标节点，如何删除这个节点，这是难点。因为删除节点的同时不能破坏BST的性质：
            - 目标节点恰好是末端节点：当场去世
            - 目标节点只有一个非空子节点：让孩子接替自己的位置
            - 目标节点有两个非空子节点：用左子树中最大的那个节点，或者右子树中最小的那个节点来代替自己。
        :param root:
        :param key:
        :return:
        """
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            minNode = self.__getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode((root.right, minNode.val))
        elif root.val < key:
            self.deleteNode(root.right, key)
        elif root.val > key:
            self.deleteNode(root.left, int)
        return root

    def __getMin(self, node: TreeNode) -> TreeNode:
        while not node.left:
            node = node.left
        return node


if __name__ == '__main__':
    solution = Solution()
