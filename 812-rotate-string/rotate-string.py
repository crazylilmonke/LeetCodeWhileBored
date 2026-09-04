class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = []
        final = []
        for i in s:
            l.append(i)
        while len(final) < len(l):
            l = l + [l[0]]
            l.pop(0)
            z = "".join(l)
            final.append(z)
        return goal in final