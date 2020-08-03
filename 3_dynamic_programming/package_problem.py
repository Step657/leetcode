class PackageProblem(object):
    """
    背包问题
    """

    def knapsack(self, W, N, wt, val):
        """
        0-1背包问题
        描述：
            给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
            其中第 `i` 个物品的重量为 `wt[i]`，价值为 `val[i]`，现在让你用这个背包装物品，最多能装的价值是多少？

       状态和选择：**背包的容量 & 可选择的物品

       明确dp数组的定义：**对于前`i`个物品，当前背包的容量为`w`，这种情况下可以装的最大价值是`dp[i][w]`

       根据选择，思考状态转移的逻辑：
            - 没有把第i个物品装入背包：dp[i][w] =  dp[i-1][w]
            - 把第i个物品装入背包：dp[i][w] = dp[i-1][w-wt[i-1]] + val[i-1]
        :return: the most value of the bag can contain
        """
        dp = [[0 for i in range(W + 1)] for j in range(N + 1)]

        for i in range(1, N + 1):
            for w in range(1, W + 1):
                # 当容量不足时，只能选择不装入背包
                if w - wt[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
        return dp[N][W]

    def coinChange(self, amount, coins):
        """
        518. 零钱兑换 II
        给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
        示例 1:
            输入: amount = 5, coins = [1, 2, 5]
            输出: 4
            解释: 有四种方式可以凑成总金额:
            5=5
            5=2+2+1
            5=2+1+1+1
            5=1+1+1+1+1
        :param amount: int
        :param coins: List
        :return:
        """
        n = len(coins)
        dp = [[0 for i in range(amount + 1)] for j in range(n + 1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    example = PackageProblem()
    res = example.coinChange(amount, coins)
    print(res)
