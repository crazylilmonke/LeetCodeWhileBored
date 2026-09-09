class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)  
        j = []
        for a in range(1, n + 1):
            if a not in num_set:
                j.append(a)
                
        return j