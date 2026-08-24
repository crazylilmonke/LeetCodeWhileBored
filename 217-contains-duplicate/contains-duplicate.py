class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        t = []
        for x in nums:
            if x in myset:
                t.append(x)
            myset.add(x)
        
        return len(t) != 0