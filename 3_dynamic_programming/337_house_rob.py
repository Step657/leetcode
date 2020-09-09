"""
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
示例 1:
    输入: [3,2,3,null,3,null,1]
         3
        / \
       2   3
        \   \
         3   1
    输出: 7
    解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
    输入: [3,4,5,1,3,null,1]

         3
        / \
       4   5
      / \   \
     1   3   1
    输出: 9
    解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    memo = {}

    def rob(self, root: TreeNode) -> int:
        # base case
        if not root:
            return 0

        if root in self.memo.keys():
            return self.memo[root]

        do_it = root.val + (0 if not root.left else self.rob(root.left.left) + self.rob(root.left.right)) \
                + (0 if not root.right else self.rob(root.right.left) + self.rob(root.right.right))

        not_do = self.rob(root.left) + self.rob(root.right)

        res = max(do_it, not_do)
        self.memo[root] = res
        return res

    def rob1(self, root: TreeNode) -> int:
        def dp(root: TreeNode):
            if not root:
                return [0, 0]
            left = dp(root.left)
            right = dp(root.right)
            # 抢， 下家就不能抢了
            rob = root.val + left[0] + right[0]
            # 不抢， 下家可抢可不抢，取决与收益大小
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            return [not_rob, rob]

        res = dp(root)
        return max(res)
