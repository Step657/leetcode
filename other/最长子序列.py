def max(a,b):
    return a if a>b else b


def lengthOfLIS(nums):
    # dp 数组初始化为1
    dp = [1 for i in range(len(nums))]

    for i in range(len(nums)):
        for j in range(i):
            if (nums[i] > nums[j]):
                dp[i] = max(dp[i], dp[j] + 1)
    
    res = 0
    for i in range(len(dp)):
        res = max(res, dp[i])
    
    return res


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = lengthOfLIS(nums)
    print(res)