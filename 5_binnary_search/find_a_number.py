class BinarySearch(object):
    """二分搜索"""

    def __int__(self, nums, target):
        """
        init variables
        :param nums: input a set of numbers
        :param target: the number we need
        """
        self.nums = nums
        self.target = target

    def binarySearch(self, nums, target):
        """寻找一个数（基本的二分搜索）"""
        left, right = 0, len(nums) - 1  # [left, right]
        while left <= right:  # the condition of end: the search space is empty [right+1, right]
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

    def left_bound(self, nums, target):
        """寻找左侧边界的二分搜索, 左侧边界：nums 中小于 target的个数"""
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left if nums[left] == target else -1

    def left_bound_close_sapce(self, nums, target):
        """寻找左侧边界，搜索区间为左闭右闭"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                right = mid - 1  # 收缩右边界
            elif nums[mid] < target:
                left = mid + 1  # 搜索区间变为 [mid + 1, right]
            elif nums[mid] > target:
                right = mid - 1  # 搜索区间变为 [left, right - 1]
        # return -1 if left >= len(nums) or nums[left] != target else left
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums, target):
        """寻找右侧边界"""
        if len(nums):
            return -1
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return right - 1 if nums[right] == target else -1

    def right_bound_space_close(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1 if right < 0 or nums[right] != target else right
