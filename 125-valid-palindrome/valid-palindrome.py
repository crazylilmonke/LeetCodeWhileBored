class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        list1 = []
        for ch in s:
            if ch.isalnum():
                list1.append(ch)

        return list1 == list1[::-1]