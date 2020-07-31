"""
76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""
import sys


class MinimumWindowSubstring(object):
    def __int__(self, s, T):
        """
        init the variable
        :param s: source string
        :param T: target string
        :return: "" or the identity answer
        """
        self.s = s
        self.T = T

    def burst(self, s, T):
        res = ''
        target = set([c for c in T])
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                cur = set(s[i:j])
                if target.issubset(cur):
                    if res:
                        if len(res) > j - i:
                            res = s[i:j]
                    else:
                        res = s[i:j]
        return res

    def slidingwindow(self, s, T):
        # 初始化window 和 need 这两个字典
        window = {}
        need = {k: 0 for k in T}
        for c in T:
            need[c] += 1
        # initialize left, right
        left, right = 0, 0
        valid = 0  # 窗口中满足need条件的字符个数
        start, length = 0, sys.maxsize

        while right < len(s):
            c = s[right]  # c 将要移入窗口的字符
            right += 1  # 右移窗口
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    start, length = left, right - left

                d = s[left]  # d是将要移出窗口的字符
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return '' if length == sys.maxsize else s[start: start + length]
