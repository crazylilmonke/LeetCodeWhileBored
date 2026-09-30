class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        flag = 0
        l = heights
        z = l.copy()
        l.sort()
        for i in range(len(l)):
            if z[i] != l[i]:
                flag += 1
        return flag