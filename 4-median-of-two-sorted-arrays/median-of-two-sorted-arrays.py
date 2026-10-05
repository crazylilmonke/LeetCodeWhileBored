class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = nums1 + nums2
        l.sort()
        n = len(l)
        
        if n % 2 == 1:
            j = l[n // 2]
        else:
            j = (l[(n // 2) - 1] + l[n // 2]) / 2
            
        return j
