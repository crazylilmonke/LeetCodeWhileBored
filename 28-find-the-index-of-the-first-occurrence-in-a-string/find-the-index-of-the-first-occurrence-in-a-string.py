class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):          # last valid starting position
            if haystack[i:i + m] == needle:  # compare the window
                return i
        
        return -1