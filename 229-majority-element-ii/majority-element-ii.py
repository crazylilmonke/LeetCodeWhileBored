from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        target_limit = len(nums) // 3
        ans = []
        number_counts = Counter(nums)
        for number in number_counts:
            times = number_counts[number]
            
           
            if times > target_limit:
                ans.append(number)
                
        return ans
