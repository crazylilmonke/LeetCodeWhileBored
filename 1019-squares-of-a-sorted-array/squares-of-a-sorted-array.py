class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = nums
        for j in range(0, len(l)):
            l[j] = pow(l[j], 2)
        l.sort()
        return l