def bruteFroce(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return False


def pythonList(nums, target):
    for i in nums:
        if target-i in nums:
            return [nums.index(i), nums.index(target-i)]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    res = bruteFroce(nums, 9)
    res = pythonList(nums, 9)
    print(res)