class FullArray(object):
    def __int__(self, nums):
        self.res = [[]]
        self.nums = nums

    def permute(self, nums, res):
        """input a set of numbers, return their full array."""
        # 记录路径
        track = []
        self.backtrack(nums, track, res)
        return res

    def backtrack(self, nums, track, res):
        """
        回溯框架
        :param nums: the input set
        :param track: record the path
        :param res: the result
        :return: res
        """
        # 触发结束条件
        if len(track) == len(nums):
            res.append(track)
            return
        for i in range(len(nums)):
            # 排除不合法的选择
            if nums[i] in track:
                continue
            # 做选择
            track.append(nums[i])
            # 进入下一层决策树
            self.backtrack(nums, track, res)
            # 取消选择
            track.pop()
