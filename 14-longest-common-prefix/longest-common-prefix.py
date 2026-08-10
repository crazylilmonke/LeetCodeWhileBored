class Solution:
    def longestCommonPrefix(self, l):
        res = ''
        first = l[0]
        for i in range(len(first)):
            ch = first[i]
            ok = True
            for j in l:
                if i >= len(j):
                    ok = False
                elif j[i] != ch:
                    ok = False
            if ok == True:
                res = res + ch
            else:
                break
        return res