"""
111. 二叉树的最小深度
"""


class TreeNode(object):
    def __int__(self, x):
        self.val = x
        self.left = None
        self.right = None


def MinDepth(root):
    """
    :param root: the binary tree's root Node
    :return: the min of the binary tree's depth
    """
    if not root:
        return 0
    q = [root]
    depth = 1

    while len(q):
        sz = len(q)
        for i in range(sz):
            cur = q.pop(0)
            if cur.left is None and cur.right is None:
                return depth
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        depth += 1
