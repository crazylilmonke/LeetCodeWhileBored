class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        b = []
        for a in set(nums1):
            if a in set(nums2):
                b.append(a)
        return b