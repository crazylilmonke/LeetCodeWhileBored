class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            a = 0
            for j in range(len(nums)):
                if nums[j] < target:
                    a = j + 1
            return a