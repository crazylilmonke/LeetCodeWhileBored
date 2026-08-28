class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)
        l = []
        for i in n:
            l.append(i)

        if n.startswith('-'):
            l.pop(0)
            z = l[::-1]
            b = -int(''.join(z))
        else:
            a = l[::-1]
            b = int(''.join(a))

        if b > 2**31 - 1 or b < -2**31:
            return 0
        return b