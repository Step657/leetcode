class Solution(object):
    """
    72. 编辑距离
        给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
        你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符
        替换一个字符

    示例 1：
        输入：word1 = "horse", word2 = "ros"
        输出：3
        解释：
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')
    示例 2：
        输入：word1 = "intention", word2 = "execution"
        输出：5
        解释：
        intention -> inention (删除 't')
        inention -> enention (将 'i' 替换为 'e')
        enention -> exention (将 'n' 替换为 'x')
        exention -> exection (将 'n' 替换为 'c')
        exection -> execution (插入 'u')
    """

    def minDistance_1(self, word1, word2):
        """
        暴力解法：递归
        :param word1: string
        :param word2: string
        :return: int
        """

        def dp(i: int, j: int) -> int:
            """
            返回 word1[0..i] 和 word2[0..j] 的最小编辑距离
            :rtype: int
            """
            # base case
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(
                    dp(i, j - 1) + 1,  # 插入
                    dp(i - 1, j) + 1,  # 删除
                    dp(i - 1, j - 1) + 1)  # 替换

        # i, j初始化指向最后一个索引
        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance_2(self, word1, word2) -> int:
        """备忘录"""
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,  # 插入
                    dp(i - 1, j) + 1,  # 删除
                    dp(i - 1, j - 1) + 1)  # 替换
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance_3(self, word1, word2) -> int:
        """
        DP table:
        """
        m, n = len(word1), len(word2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        # base case
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # 自底向上求解
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        # 存储这整个word1和word2的最小编辑距离
        return dp[m][n]
