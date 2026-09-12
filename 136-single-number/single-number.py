class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for j in nums:
            if nums.count(j) == 1:
                return j