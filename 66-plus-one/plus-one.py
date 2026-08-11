class Solution:
    def plusOne(self, digits):
        n = ''.join(str(x) for x in digits)
        k = int(n) + 1
        j = str(k)
        l = []
        for i in j:
            l.append(int(i))
        return l