class Solution:
    def thirdMax(self, nums):
        z = sorted(set(nums))
        if len(z) < 3:
            return z[-1]
        else:
            return z[-3]