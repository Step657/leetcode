"""
354. 俄罗斯套娃信封问题
    给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
    这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
    请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
说明:
不允许旋转信封。
示例:
    输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出: 3
    解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
思路：
    这道题其实是最长递增子序列（Longest Increasing Subsequence）的一个变种，因为显然，每次合法的嵌套是大的套小的，
    相当于找一个最长的递增子序列，其长度就是最多能嵌套的信封个数。
解法：
    先对宽度w进行升序排序，如果遇到w相同的情况，则按照高度h降序排序。之后把所有的h作为一个数组，在这个数组上计算LIS的长度就是答案
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (-x[0], x[1]), reverse=True)
        height = [x[1] for x in envelopes]
        return self.LengthOfLIS(height)

    def LengthOfLIS(self, nums: List[int]):
        piles, n = 0, len(nums)
        top = []
        for i in range(n):
            poker = nums[i]
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid + 1
            if left == piles:
                piles += 1
                top.append(poker)
            else:
                top[left] = poker
        return piles
