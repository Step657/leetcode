"""
单调队列：队列中的元素单调递增（或递减）
239. 滑动窗口最大值
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。
进阶：
    你能在线性时间复杂度内解决此题吗？
        【在一堆数字中，已知最值，如果给这堆数添加一个数， 那么比较一下就可以很快算出最值；但是如果减少一个数，就不一定能很快得到最值了，而要遍历所有数重新找最值。
        每个窗口前进的时候，要添加一个数的同时减少一个数，所以想在O(1)的时间得到最新的最值，就需要 单调队列 这种特殊的数据结构来辅助了】
示例:

    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    解释:

      滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

提示：
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""
from typing import List


# class my_Queue:
#     """普通队列，至少包含以下两个方法"""
#
#     def push(self, n):
#         # 或 enqueue， 在队尾加入元素
#         pass
#
#     def pop(self):
#         # 或 dequeue， 删除队头元素
#         pass


class my_deque:
    """双端队列"""
    data = []

    def push_front(self, n: int):
        """在队头插入元素 n"""
        self.data.insert(0, n)

    def push_back(self, n: int):
        """在队尾插入元素"""
        self.data.append(n)

    def pop_front(self):
        """在队头删除元素"""
        self.data.pop(0)

    def pop_back(self):
        """在队尾删除元素"""
        self.data.pop()

    def front(self) -> int:
        """返回队头元素"""
        return self.data[0]

    def back(self):
        """返回队尾元素"""
        return self.data[-1]

    def __len__(self):
        return len(self.data)


class MonotonicQueue:
    data = my_deque()

    def push(self, n: int):
        """在队头添加元素 n"""
        while not len(self.data) == 0 and self.data.back() < n:
            self.data.pop_back()
        self.data.push_back(n)

    def queue_max(self) -> int:
        """返回当前队列中的最大值"""
        return self.data.front()

    def pop(self, n: int):
        """队头元素如果是n，删除它"""
        if not len(self.data) == 0 and self.data.front() == n:
            self.data.pop_front()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = MonotonicQueue()

        for i in range(len(nums)):
            if i < k - 1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.queue_max())
                window.pop(nums[i - k + 1])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    k = 1
    res = s.maxSlidingWindow(nums, k)
    print(res)
