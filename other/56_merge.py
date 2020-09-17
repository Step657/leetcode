"""
区间调度问题之区间合并：一般思路是先排序，然后观察规律
56. 合并区间
    给出一个区间的集合，请合并所有重叠的区间。
示例 1:
    输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
    输入: intervals = [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
    注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda intv: intv[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            # res 中最后一个元素的引用
            last = res[-1]
            if curr[0] <= last[1]:
                # 找到最大的end
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)
        return res
