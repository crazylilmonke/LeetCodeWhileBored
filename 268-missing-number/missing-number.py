class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        
        if nums[-1] != n:
            return n
        
        for j in range(n):
            if j not in nums:
                return j