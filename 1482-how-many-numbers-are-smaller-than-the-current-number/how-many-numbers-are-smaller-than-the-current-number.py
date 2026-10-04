class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        l = nums
        j = []
        sum = 0
        
        for i in range(len(l)):
            for v in range(len(l)):
                if l[i] > l[v]:
                    sum += 1
            j.append(sum) 
            sum = 0
        return j
