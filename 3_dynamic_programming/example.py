class Fib(object):
    """斐波那契数列"""

    def __int__(self, N):
        self.N = N

    def brust_fib(self, N):
        """暴力递归
        :param N:input"""
        if N == 1 or N == 2:
            return 1
        return self.brust_fib(N - 1) + self.brust_fib(N - 2)

    def memo_fib(self, N):
        """带备忘录的递归解法
        :param N:input
        memo:record the value of F(i)"""
        if N < 1:
            return 0
        memo = [0 for i in range(N)]
        return self.helper(self, memo, N)

    def helper(self, memo, n):
        """带备忘录的递归解法
        :param n:input
        :param memo:record the value of F(i)"""
        # base case
        if n == 1 or n == 2:
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.helper(memo, n - 1) + self.helper(memo, n - 2)
        return memo[n]

    def dp_fib(self, N):
        """dp数组迭代解法，在dp表上完成自底向上的推算
        :param N:input"""
        dp = [0 for i in range(N + 1)]  # 不用dp[0]
        # base case
        dp[1] = dp[2] = 1
        if N > 2:
            for i in range(3, N + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[N]

    def space_compression_dp_fib(self, N):
        """状态压缩，如果我们发现每次状态转移只需要DP table中的一部分，
        那么可以尝试用状态压缩来缩小DP table，只记录必要的数据
        :type N: int
        :param N:input"""
        if N == 2 or N == 1:
            return 1
        prev, curr = 1, 1
        for i in range(3, N + 1):
            trans = prev + curr
            prev = curr
            curr = trans
        return curr


class CombineCoins(object):
    """332. 凑零钱：给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，
    再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，"""

    def __int__(self, coins, amount):
        """
        :type coins: list
        :param coins:the value of k kinds of coins
        :type amount: int
        :param amount: the amount value
        """
        self.coins = coins
        self.amount = amount

    def brust(self, coins, amount):

        def dp(n):
            # base case
            if n == 0:
                return 0
            if n < 0:
                return -1
            # 求最小值，所以初始化为正无穷
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)

            return res if res != float('INF') else -1

        return dp(amount)

    def memo(self, coins, amount):
        # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)

    def dp_table(self, coins, amount):
        # 数据大小为amount+1，初试值也为amount+1
        dp = [amount + 1 for i in range(amount + 1)]
        # base case
        dp[0] = 0
        # 外层for循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层for循环在求所有选择的最小值
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == amount + 1 else dp[amount]
