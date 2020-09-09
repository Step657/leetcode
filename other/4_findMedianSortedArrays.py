"""
4. 寻找两个正序数组的中位数
    给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
    请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
    示例 1:
        nums1 = [1, 3]
        nums2 = [2]
        则中位数是 2.0
    示例 2:
        nums1 = [1, 2]
        nums2 = [3, 4]
        则中位数是 (2 + 3)/2 = 2.5
"""
from typing import List


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if len(nums2) == 1 and len(nums1) == 1:
#             return (nums1[0] + nums2[0]) / 2
#         # flag 用来指示两个数组合起来的长度是奇数还是偶数：偶数：True,奇数：False
#         flag = (len(nums1) + len(nums2)) % 2 == 0
#         # 保证nums2 是长度较短的数组
#         if len(nums2) > len(nums1):
#             nums1, nums2 = nums2, nums1
#         if len(nums2) == 0:
#             return self._median(nums1)
#         # 偶数 & 1
#         if len(nums2) == 1 and not flag:
#             mid1, mid2 = self._median_res(nums1)
#             if mid1 > nums2[0]:
#                 return mid1
#             elif mid2 < nums2[0]:
#                 return mid2
#             else:
#                 return nums2[0]
#         if len(nums2) == 1 and flag:
#             mid1, mid, mid2 = self._median_res(nums1)
#             if mid1 > nums2[0]:
#                 return (mid1 + mid) / 2
#             elif mid2 < nums2[0]:
#                 return (mid2 + mid) / 2
#             else:
#                 return (nums2[0] + mid) / 2
#
#         if len(nums2) == 2 and not flag:
#             mid = self._median(nums1)
#             if mid < nums2[0]:
#                 return nums2[0]
#             elif mid > nums2[1]:
#                 return nums2[1]
#             else:
#                 return mid
#         if len(nums2) == 2 and flag:
#             mid1, mid2 = self._median_res(nums1)
#             nums2.append(mid1)
#             nums2.append(mid2)
#             nums2 = sorted(nums2)
#             return (nums2[1] + nums2[2]) / 2
#
#         median1 = self._median(nums1)
#         median2 = self._median(nums2)
#         edge = len(nums2) // 2
#         if median1 == median2:
#             return median1
#         if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
#             if median1 < median2:
#                 res = self.findMedianSortedArrays(nums1[edge::], nums2[:edge:])
#                 return res
#             else:
#                 res = self.findMedianSortedArrays(nums1[:edge:], nums2[edge::])
#                 return res
#         elif len(nums1) % 2 == 0:
#             if median1 < median2:
#                 res = self.findMedianSortedArrays(nums1[edge::], nums2[:edge + 1:])
#                 return res
#             else:
#                 res = self.findMedianSortedArrays(nums1[:edge:], nums2[edge::])
#                 return res
#         else:
#             if median1 < median2:
#                 res = self.findMedianSortedArrays(nums1[edge::], nums2[:edge:])
#                 return res
#             else:
#                 res = self.findMedianSortedArrays(nums1[:edge + 1:], nums2[edge::])
#                 return res
#
#     def _median(self, nums):
#         # nums含有偶数个元素，则中位数为中间两位的算术平均值
#         if len(nums) % 2 == 0:
#             tmp1 = nums[len(nums) // 2 - 1]
#             tmp2 = nums[len(nums) // 2]
#             return (tmp1 + tmp2) / 2
#         # nums含有奇数个元素，则中位数为中间位的元素
#         else:
#             return nums[len(nums) // 2]
#
#     def _median_res(self, nums):
#         # nums含有偶数个元素，则中位数为中间两位的算术平均值
#         if len(nums) % 2 == 0:
#             tmp1 = nums[len(nums) // 2 - 1]
#             tmp2 = nums[len(nums) // 2]
#             return tmp1, tmp2
#         # nums含有奇数个元素，则中位数为中间位的元素
#         else:
#             return nums[len(nums) // 2 - 1], nums[len(nums) // 2], nums[len(nums) // 2 + 1]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证nums2 是长度较短的数组
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        if len(nums2) == 0:
            return self._median(nums1)

        if len(nums2) <= 2:
            nums2.extend(nums1)
            return self._median(sorted(nums2))

        median1 = self._median(nums1)
        median2 = self._median(nums2)
        edge = len(nums2) // 2
        if len(nums2) % 2 == 0:
            edge -= 1
        if median1 == median2:
            return median1
        elif median1 < median2:
            res = self.findMedianSortedArrays(nums1[edge::], nums2[:len(nums2) - edge:])
            return res
        else:
            res = self.findMedianSortedArrays(nums1[:len(nums1) - edge:], nums2[edge::])
            return res

    def _median(self, nums):
        # nums含有偶数个元素，则中位数为中间两位的算术平均值
        if len(nums) % 2 == 0:
            tmp1 = nums[len(nums) // 2 - 1]
            tmp2 = nums[len(nums) // 2]
            return (tmp1 + tmp2) / 2
        # nums含有奇数个元素，则中位数为中间位的元素
        else:
            return nums[len(nums) // 2]

    def _median_res(self, nums):
        # nums含有偶数个元素，则中位数为中间两位的算术平均值
        if len(nums) % 2 == 0:
            tmp1 = nums[len(nums) // 2 - 1]
            tmp2 = nums[len(nums) // 2]
            return tmp1, tmp2
        # nums含有奇数个元素，则中位数为中间位的元素
        else:
            return nums[len(nums) // 2 - 1], nums[len(nums) // 2], nums[len(nums) // 2 + 1]


if __name__ == '__main__':
    nums1 = [1, 2, 6, 7]
    nums2 = [3, 4, 5, 8]
    s = Solution()
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)
