class Solution:
    def moveZeroes(self, l: list[int]) -> None:
        """
        Do not return anything, modify l in-place instead.
        """
        j = []
        count = l.count(0)
        for a in l:
            if a != 0:
                j.append(a)
        while len(j) < len(l):
            j.append(0)
        l[:] = j