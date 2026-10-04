class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums.count(nums[i]) == n // 2:
                j = nums[i]
        return j
