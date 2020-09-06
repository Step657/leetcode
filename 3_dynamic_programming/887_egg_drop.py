"""
887. 鸡蛋掉落
    你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
    你的目标是确切地知道 F 的值是多少。
    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
示例 1：
    输入：K = 1, N = 2
    输出：2
    解释：
        鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
        否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
        如果它没碎，那么我们肯定知道 F = 2 。
        因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：
    输入：K = 2, N = 6
    输出：3
示例 3：
    输入：K = 3, N = 14
    输出：4
"""
class EggDrop(object):
    def __init__(self, k, n):
        self.K = k
        self.N = n

    def eggDrop(self):
        K = self.K
        N = self.N
        memo = {}

        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('INF')
            # 用二分搜索代替线性搜索
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K-1, mid - 1)
                not_broken = dp(K, N-mid)
                # res = min(max(碎，不碎)+1)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            memo[(K, N)] = res
            return res
        return dp(K, N)

    def superEggDrop(self, K, N):
        # m is not beyond N
        # base case: dp[0][...] = 0, dp[...][0] = 0
        dp = [[0 for i in range(N + 1)] for j in range(K + 1)]

        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        return m