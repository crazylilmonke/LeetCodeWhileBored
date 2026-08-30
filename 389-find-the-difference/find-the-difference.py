class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        for i in t:
            if i in s_list:
                s_list.remove(i)
            else:
                return i