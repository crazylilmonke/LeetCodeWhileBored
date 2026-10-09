class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = list(s)
        i = 0
        
        for j in range(len(l)):
            l[i] = l[j]
            if i > 0 and l[i] == l[i - 1]:
                i -= 1
            else:
                i += 1
                
        return "".join(l[:i])
