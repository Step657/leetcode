"""
28. 实现 strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
    输入: haystack = "hello", needle = "ll"
    输出: 2

示例 2:
    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
    说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 定义dp数组，（from 状态机）
        if len(needle) == 0:
            return 0
        # res = self.search(pat=needle, txt=haystack)
        res = self.KMP(pat=needle, txt=haystack)
        return res

    def search(self, pat, txt):
        """KMP算法 利用动态规划（状态机）"""
        dp = self.create_dp(pat)
        j = 0  # 状态
        for i in range(len(txt)):
            # 当前是状态j，遇到字符txt[i]
            # pat 应该转移到哪个状态
            j = dp[j][ord(txt[i])]

            if j == len(pat):
                # j 为终止状态则说明找到了子串
                return i - len(pat)
        # txt走完还没有找到，则说明不存在子串
        return -1

    def create_dp(self, pat):
        status = len(pat)
        dp = [[0 for i in range(256)] for j in range(status)]
        dp[0][ord(pat[0])] = 1
        x = 0  # 影子状态x初始化为0
        for i in range(1, status):
            for c in range(256):
                if ord(pat[i]) == c:
                    dp[i][c] = i + 1
                else:
                    dp[i][c] = dp[x][c]
            x = dp[x][ord(pat[i])]
        return dp

    def KMP(self, pat, txt):
        next_arr = self.get_next(pat)
        i, j = 0, 0
        while i <= len(txt) and j <= len(pat):
            if j == 0 or txt[i - 1] == pat[j - 1]:
                i += 1
                j += 1
            else:
                j = next_arr[j - 1]
        if j == len(pat) + 1:
            return i - len(pat) - 1
        return -1

    def get_next(self, pat):
        next_arr = [0 for i in range(len(pat))]
        i, j = 1, 0
        while i < len(pat):
            if j == 0 or pat[i - 1] == pat[j - 1]:
                j += 1
                i += 1
                next_arr[i - 1] = j
            else:
                j = next_arr[j - 1]
        return next_arr


if __name__ == '__main__':
    s = Solution()
    res = s.strStr('a', 'a')
    print(res)
