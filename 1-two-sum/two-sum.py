class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            z = target - nums[i]
            if z in nums[i+1:]:
                j = nums.index(z, i+1)
                return [i, j]
        