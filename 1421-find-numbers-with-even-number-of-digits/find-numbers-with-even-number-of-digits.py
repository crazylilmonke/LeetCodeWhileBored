class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        j = []
        
        def Count(n: int):
            countx = 0
            while(n > 0):
                n = n // 10
                countx += 1
            return countx
        
        l = nums
        n = len(l)
        
        for i in range(n):
            if Count(l[i]) % 2 == 0:
                j.append(l[i])
                
        return len(j)
