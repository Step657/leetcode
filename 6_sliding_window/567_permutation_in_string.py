"""
567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
"""
import sys


class PermutationInString(object):
    def __init__(self, s1, s2):
        """
        initialize variable s1,s2
        :param s1: target string
        :param s2: source string
        """
        self.s1 = s1
        self.s2 = s2

    def solution(self):
        window = {}
        need = {k:0 for k in self.s1}
        for c in self.s1:
            need[c] += 1
        left, right = 0, 0
        valid = 0

        while right < len(self.s2):
            c = self.s2[right]
            right += 1
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1

            while right-left >= len(self.s1):
                if valid == len(need):
                    return True
                d = self.s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    example = PermutationInString(s1, s2)
    res = example.solution()
    print(res)
