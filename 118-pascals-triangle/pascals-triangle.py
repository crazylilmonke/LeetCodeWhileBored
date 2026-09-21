class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        n = numRows
        l = []
        for i in range(n):
            j = [1]
            if i == 0:
                l.append(j)
            else:
                for k in range(1, i):
                    j.append(l[-1][k-1] + l[-1][k])
                
                j.append(1)
                l.append(j)
                
        return l

        