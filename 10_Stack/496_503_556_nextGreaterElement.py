"""
    Monotonic stack
    单调栈：栈，利用了一些巧妙的逻辑，使得每次新元素入栈后，栈内的元素都保持有序（单调递增或单调递减）
    单调栈的用途不太广泛，只处理一种典型的问题，叫做    Next Greater Element
"""
from typing import List


def nextGreaterElement(nums: List[int]) -> List[int]:
    """
    给你一个数组，返回一个等长的数组，对应索引存储着下一个更大元素，如果没有更大的元素，就存-1。
    如一个数组[2,1,1,4,3], 你返回数组[4,2,4,-1,-1]
    :param nums:
    :return:
    """
    res = [0 for i in range(len(nums))]

    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while not len(stack) == 0 and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums[i])
    return res


class Solution1:
    """
    496. 下一个更大元素 I
        给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
        nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
    示例 1:
        输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
        输出: [-1,3,-1]
        解释:
            对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
            对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
            对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
    示例 2:
        输入: nums1 = [2,4], nums2 = [1,2,3,4].
        输出: [3,-1]
        解释:
            对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
            对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
    """

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while not len(stack) == 0 and stack[-1] <= nums2[i]:
                stack.pop()
            temp[nums2[i]] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums2[i])
        res = []
        for i in nums1:
            res.append(temp[i])
        return res


class Solution2:
    """
    503. 下一个更大元素 II
        给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
        这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
    示例 1:
        输入: [1,2,1]
        输出: [2,-1,2]
        解释: 第一个 1 的下一个更大的数是 2；
        数字 2 找不到下一个更大的数；
        第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

    """

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        增加了环形属性，问题的难点在于：这个Next的意义不仅仅是当前元素的右边，有可能出现在当前元素的左边。
        计算机的存储都是线性的，没有真正意义上的环形数组，但是我们可以模拟出环形数组的效果，一般是通过 % 运算符求模（余数）
        :param nums:
        :return:
        """
        n = len(nums)
        stack = []
        res = [0 for i in range(n)]
        for i in range(2 * n - 1, -1, -1):
            while not len(stack) == 0 and stack[-1] <= nums[i % n]:
                stack.pop()
            res[i % n] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[i % n])
        return res

if __name__ == '__main__':
    nums = [1, 2, 1]
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    s = Solution2()
    res = s.nextGreaterElements(nums)
    print(res)
